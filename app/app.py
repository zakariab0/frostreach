from flask import Flask, request, render_template, jsonify
import email_writer as ew
import os

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main page with options for email or LinkedIn."""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    """Handle form submission and generate content."""
    data = request.json  # Get JSON data from the frontend

    # Extract form data
    user_full_name = data.get('user_full_name')
    gender = data.get('gender')
    profession = data.get('profession')
    recruiter_full_name = data.get('recruiter_full_name')
    company_name = data.get('company_name')
    recruiter_email = data.get('recruiter_email', '')  # Optional for LinkedIn
    platform = data.get('platform')  # 'email' or 'linkedin'
    language = data.get('language')  # 'english', 'french', 'spanish', etc.

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
        return jsonify({"status": "error", "message": "Invalid platform selected."})
    
if __name__ == '__main__':
    app.run(debug=True)
