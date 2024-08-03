import time

import appealer as appeal
import google.generativeai as genai

genai.configure(api_key='AIzaSyB1x9WpEtwau_0V0EKTl3lCc6DYcVFVcCY')
model = genai.GenerativeModel('gemini-1.5-flash')
a = appeal.Appealer()


def get_RH_credentials(cls):
    rh_list = a.fetch_mails(cls)
    return rh_list

def generate_personal_text(gender, full_name, profession):
    response = model.generate_content(
        "tu peux m'ecrire une definition personnelle  et courte, je suis " + gender + " " + full_name + " et ma profession est " + profession)
    return response.text


def generate_mail(company_name, full_name, email, personal_info):
    response = model.generate_content(
        personal_info + ", en se baseant sur ma definition tu peux me rediger un mail de postulation pour des opportunités en tech? aussi informer qu'il trouvera ci joint mon CV,"
                        " voici le contact de RH: nom entrprise: " + company_name + ", mail: " +
        email + ", nom complet: " + full_name + ", aussi essaye d'ecrire le mail en direct et ne me donne aucune chose a mentionner manuellement merci d'avance; finallement tu n'ecris pas l'objet; au premier mention du destinataire tu ecris directement Cher " + full_name + " a la fin mets mon nom est Bounou Zakaria ; aussi au place de chaque saut de ligne tu peux écrire <br>")
    print(response.text)
    time.sleep(10)
    a.send_mail(email, "", "", "Candidature aux poste de développeur full stack", response.text, "08_07_resume_fr.pdf")


if __name__ == '__main__':
    csv_file = 'rh.csv'
    rh_list = get_RH_credentials(csv_file)

    for rh in rh_list:
        print(f"Name: {rh.full_name}, Email: {rh.email}, Company: {rh.company_name}")

        personal_text = generate_personal_text("monsieur", "Bounou Zakaria",
                                               "developpeur full stack en backend (java springboot, php symfony)")
        generate_mail(rh.company_name, rh.full_name, rh.email, personal_text)
        time.sleep(5)
