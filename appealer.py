import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib


# from_email = ""
# password = ""
# to_email = ""

class RH:
    def __init__(self, full_name, email, company_name):
        self.full_name = full_name
        self.email = email
        self.company_name = company_name

    def __str__(self):
        return f"Nom complet: {self.full_name}\nEmail: {self.email}\nEntreprise: {self.company_name}"


class Appealer:

    #password generator from gmail: https://support.google.com/accounts/answer/185833?visit_id=638582916114241109-3650894979&p=InvalidSecondFactor&rd=1
    @staticmethod
    def send_mail(to_email, from_email, password, subject, html, pdf_path):
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the HTML message
        msg.attach(MIMEText(html, 'html'))

        # Attach the PDF file
        try:
            with open(pdf_path, 'rb') as pdf_file:
                pdf_attachment = MIMEApplication(pdf_file.read(), _subtype='pdf')
                pdf_attachment.add_header('Content-Disposition', 'attachment', filename='CV.pdf')
                msg.attach(pdf_attachment)
        except Exception as e:
            print(f"Erreur lors de l'ajout du fichier PDF: {e}")
            return

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(from_email, password)
            server.sendmail(from_email, to_email, msg.as_string())
            server.quit()
            print("Email envoyé avec succès")
        except Exception as e:
            print(f"Erreur lors de l'envoi de l'email: {e}")

    @staticmethod
    def fetch_mails(csv1):
        list = []
        rh = RH('', '', '')
        with open(csv1, 'r') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                rh = RH(row['PERSONNE'], row['E-mail'], row['SOCIETE'])
                if rh.email != '' and rh.full_name != '' and rh.company_name != '':
                    list.append(rh)
        return list
