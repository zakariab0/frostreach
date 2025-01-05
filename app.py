# Import necessary libraries
from flask import Flask, request, render_template, jsonify, abort
from flask_cors import CORS
import email_writer as ew  # Custom module for generating email/LinkedIn content
import os
import psycopg2  # PostgreSQL database adapter
from psycopg2 import sql  # Safe SQL query construction
import json
from dotenv import load_dotenv  # Load environment variables from .env file
import logging  # Logging for debugging and monitoring
from contextlib import contextmanager  # Context manager for database connections

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing (CORS)

# Fetch database connection details from environment variables
DB_HOST = os.getenv("host")
DB_NAME = os.getenv("dbname")
DB_USER = os.getenv("user")
DB_PASSWORD = os.getenv("password")
DB_PORT = os.getenv("db_port")

@contextmanager
def get_db_connection():
    """
    Context manager for establishing and yielding a connection to the PostgreSQL database.
    Ensures the connection is properly closed even if an exception occurs.
    """
    conn = None
    try:
        # Establish a connection to the database
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        yield conn  # Yield the connection to the caller
    except Exception as e:
        # Log any errors that occur while connecting to the database
        logging.error("Error connecting to the database: %s", str(e))
        raise  # Re-raise the exception for further handling
    finally:
        # Ensure the connection is closed
        if conn:
            conn.close()

@app.route('/')
def index():
    """Render the main page with options for email or LinkedIn."""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    """
    Handle POST requests to the /generate endpoint.
    Processes form data, saves recruiter details to the database, and generates personalized content.
    """
    try:
        # Log the raw request data for debugging
        raw_data = request.data
        logging.info("Raw Request Data: %s", raw_data)

        # Decode the raw data as UTF-8, replacing invalid characters
        decoded_data = raw_data.decode('utf-8', errors='replace')
        data = json.loads(decoded_data)  # Parse the decoded data as JSON

        # Validate required fields
        required_fields = ['user_full_name', 'gender', 'profession', 'recruiter_full_name', 'company_name', 'platform', 'language']
        for field in required_fields:
            if field not in data or not data[field]:
                # Abort with a 400 error if any required field is missing or empty
                abort(400, description=f"Missing or invalid field: {field}")

        # Log the extracted data for debugging
        logging.info("Extracted Data: %s", {
            "user_full_name": data['user_full_name'],
            "gender": data['gender'],
            "profession": data['profession'],
            "recruiter_full_name": data['recruiter_full_name'],
            "company_name": data['company_name'],
            "recruiter_email": data.get('recruiter_email', ''),  # Optional field
            "platform": data['platform'],
            "language": data['language']
        })

        # Save recruiter details to the database
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                # Insert recruiter details into the 'recruiters' table
                cur.execute(
                    sql.SQL("INSERT INTO recruiters (full_name, company_name) VALUES (%s, %s)"),
                    (data['recruiter_full_name'], data['company_name'])
                )
                conn.commit()  # Commit the transaction

        # Generate personalized text using the custom email_writer module
        personal_text = ew.generate_personal_text(data['gender'], data['user_full_name'], data['profession'], data['language'])

        # Generate content based on the selected platform
        if data['platform'] == 'email':
            # Generate email content
            email_content = ew.generate_email_content(data['company_name'], data['recruiter_full_name'], data.get('recruiter_email', ''), personal_text, data['profession'], data['language'])
            return jsonify({"status": "success", "message": "Email content generated!", "content": email_content})
        elif data['platform'] == 'linkedin':
            # Generate LinkedIn message
            linkedin_message = ew.generate_linkedin_message(data['company_name'], data['recruiter_full_name'], personal_text, data['profession'], data['language'])
            return jsonify({"status": "success", "message": "LinkedIn message generated!", "content": linkedin_message})
        else:
            # Abort with a 400 error if an invalid platform is selected
            abort(400, description="Invalid platform selected")

    except Exception as e:
        # Log the full error traceback for debugging
        import traceback
        logging.error("Error Traceback: %s", traceback.format_exc())

        # Ensure the error message is properly encoded
        error_message = str(e).encode('utf-8', errors='replace').decode('utf-8')
        return jsonify({"status": "error", "message": error_message}), 500

# Run the Flask app
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use PORT provided by Vercel or default to 5000
    app.run(host='127.0.0.1', port=port)  # Run the app on localhost