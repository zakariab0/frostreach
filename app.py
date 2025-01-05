from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import email_writer as ew
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    """Render the main page with options for email or LinkedIn."""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"status": "error", "message": "No data provided"}), 400

        # Extract form data
        user_full_name = data.get('user_full_name')
        gender = data.get('gender')
        profession = data.get('profession')
        recruiter_full_name = data.get('recruiter_full_name')
        company_name = data.get('company_name')
        recruiter_email = data.get('recruiter_email', '')
        platform = data.get('platform')
        language = data.get('language')

        # Generate personalized text
        personal_text = ew.generate_personal_text(gender, user_full_name, profession, language)

        if platform == 'email':
            # Generate email content
            email_content = ew.generate_email_content(company_name, recruiter_full_name, recruiter_email, personal_text, profession, language)
            return jsonify({"status": "success", "message": "Email content generated!", "content": email_content})
        elif platform == 'linkedin':
            # Generate LinkedIn message
            linkedin_message = ew.generate_linkedin_message(company_name, recruiter_full_name, personal_text, profession, language)
            return jsonify({"status": "success", "message": "LinkedIn message generated!", "content": linkedin_message})
        else:
            return jsonify({"status": "error", "message": "Invalid platform selected"}), 400

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use PORT provided by Vercel
    app.run(host='0.0.0.0', port=port)