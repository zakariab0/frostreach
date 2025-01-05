import google.generativeai as genai
import logging
import re
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='email_writer.log'  # Log to a file
)

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # Ensure you have GEMINI_API_KEY in your .env
model = genai.GenerativeModel('gemini-1.5-flash')

# Input validation functions
def validate_email(email):
    """Validate the email format."""
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def validate_required_fields(data, required_fields):
    """Validate that all required fields are present and non-empty."""
    for field in required_fields:
        if field not in data or not data[field]:
            return False
    return True

# Content generation functions
def generate_personal_text(gender, full_name, profession, language):
    """
    Generate a short personal description in the selected language.

    Args:
        gender (str): Gender of the user.
        full_name (str): Full name of the user.
        profession (str): Profession of the user.
        language (str): Language in which the description should be generated.

    Returns:
        str: Generated personal description.
    """
    try:
        prompt = (
            f"Can you write a short and personal description for me in {language}? "
            f"I am {full_name} and my profession is {profession}."
        )
        logging.info(f"Prompt: {prompt}")

        response = model.generate_content(prompt)
        logging.info(f"Generated Content: {response.text}")

        return response.text
    except Exception as e:
        logging.error(f"Error generating personal text: {e}")
        return "An error occurred while generating the personal description. Please try again."

def generate_email_content(company_name, recruiter_full_name, recruiter_email, personal_info, profession, language, tone="polite"):
    """
    Generate an email content in the selected language.

    Args:
        company_name (str): Name of the company.
        recruiter_full_name (str): Full name of the recruiter.
        recruiter_email (str): Email address of the recruiter.
        personal_info (str): Personal description of the user.
        profession (str): Profession of the user.
        language (str): Language in which the email should be generated.
        tone (str): Tone of the email (e.g., polite, formal, casual).

    Returns:
        str: Generated email content.
    """
    try:
        # Validate recruiter email if provided
        if recruiter_email and not validate_email(recruiter_email):
            return "Invalid email address."

        prompt = (
            f"{personal_info}, based on my description, can you draft a job application email for opportunities in {profession}? "
            f"Here are the details: company: {company_name}, recruiter's name: {recruiter_full_name}. "
            f"The message should be {tone}, and mention that I am interested in opportunities in {profession}. "
            f"Do not include a subject line, and write the message as if I am sending it directly. "
            f"IMPORTANT: this mail should be in {language}."
        )
        logging.info(f"Prompt: {prompt}")

        response = model.generate_content(prompt)
        logging.info(f"Generated Content: {response.text}")

        return response.text
    except Exception as e:
        logging.error(f"Error generating email content: {e}")
        return "An error occurred while generating the email content. Please try again."

def generate_linkedin_message(company_name, recruiter_full_name, personal_info, profession, language, tone="professional"):
    """
    Generate a LinkedIn message in the selected language.

    Args:
        company_name (str): Name of the company.
        recruiter_full_name (str): Full name of the recruiter.
        personal_info (str): Personal description of the user.
        profession (str): Profession of the user.
        language (str): Language in which the message should be generated.
        tone (str): Tone of the message (e.g., professional, polite, casual).

    Returns:
        str: Generated LinkedIn message.
    """
    try:
        prompt = (
            f"{personal_info}, based on my description, can you draft a short and professional message to contact an HR recruiter on LinkedIn? "
            f"Here are the details: company: {company_name}, recruiter's name: {recruiter_full_name}. "
            f"The message should be {tone}, and mention that I am interested in opportunities in {profession}. "
            f"Do not include a subject line, and write the message as if I am sending it directly. "
            f"This message should be in {language}."
        )
        logging.info(f"Prompt: {prompt}")

        response = model.generate_content(prompt)
        logging.info(f"Generated Content: {response.text}")

        return response.text
    except Exception as e:
        logging.error(f"Error generating LinkedIn message: {e}")
        return "An error occurred while generating the LinkedIn message. Please try again."