import google.generativeai as genai

genai.configure(api_key='AIzaSyB1x9WpEtwau_0V0EKTl3lCc6DYcVFVcCY')
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_personal_text(gender, full_name, profession):
    response = model.generate_content(
        "Tu peux m'écrire une définition personnelle et courte. Je suis " + gender + " " + full_name + " et ma profession est " + profession
    )
    return response.text

def generate_email_content(company_name, recruiter_full_name, recruiter_email, personal_info, profession):
    response = model.generate_content(
        personal_info + ", en te basant sur ma définition, tu peux me rédiger un email de postulation au recruteur pour des opportunités en " + profession + ". "
        "Voici les détails : entreprise : " + company_name + ", nom du recruteur : " + recruiter_full_name + ", son email : " + recruiter_email + ". "
        "Le message doit être direct, poli, et mentionner que je suis intéressé par des opportunités en " + profession + ". "
        "Ne pas inclure d'objet, et écrire le message comme si je l'envoyais directement. "
    )
    return response.text

def generate_linkedin_message(company_name, recruiter_full_name, personal_info, profession):
    response = model.generate_content(
        personal_info + ", en te basant sur ma définition, tu peux me rédiger un message court et professionnel pour contacter une personne recruteur en RH sur LinkedIn. "
        "Voici les détails : entreprise : " + company_name + ", nom du recruteur : " + recruiter_full_name + ". "
        "Le message doit être direct, poli, et mentionner que je suis intéressé par des opportunités en " + profession + ". "
        "Ne pas inclure d'objet, et écrire le message comme si je l'envoyais directement. "
    )
    return response.text