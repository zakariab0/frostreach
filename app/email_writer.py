import google.generativeai as genai

genai.configure(api_key='AIzaSyB1x9WpEtwau_0V0EKTl3lCc6DYcVFVcCY')
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_personal_text(gender, full_name, profession, language):
    """Generate a short personal description in the selected language."""
    prompt = (
        f"Can you write a short and personal description for me in {language}? I am {gender} {full_name} and my profession is {profession}."
    )

    response = model.generate_content(prompt)
    return response.text

def generate_email_content(company_name, recruiter_full_name, recruiter_email, personal_info, profession, language):
    """Generate an email content in the selected language."""
    prompt = (
        f"{personal_info}, based on my description, can you draft a job application email for opportunities in {profession}? "
        f"Here are the details: company: {company_name}, recruiter's name: {recruiter_full_name}. "
        "The message should be direct, polite, and mention that I am interested in opportunities in " + profession + ". "
        f"Do not include a subject line, and write the message as if I am sending it directly. IMPORTANT: this mail should be in {language} "
    )

    response = model.generate_content(prompt)
    return response.text

def generate_linkedin_message(company_name, recruiter_full_name, personal_info, profession, language):
    """Generate a LinkedIn message in the selected language."""
    prompt = (
        f"{personal_info}, based on my description, can you draft a short and professional message to contact an HR recruiter on LinkedIn? "
        f"Here are the details: company: {company_name}, recruiter's name: {recruiter_full_name}. "
        "The message should be direct, polite, and mention that I am interested in opportunities in " + profession + ". "
        f"Do not include a subject line, and write the message as if I am sending it directly. this message should be in {language} "
    )

    response = model.generate_content(prompt)
    return response.text