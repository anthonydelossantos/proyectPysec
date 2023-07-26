import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from cryptography.fernet import Fernet

class Mail:
    sender_email="" 
    sender_password=""
    receiver_email="testh892@gmail.com" 
    subject=""
    message="" 
    server=""
    attachf = ""
    def set_values(self,sender_email, sender_password, receiver_email, subject, message,attach=""):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.receiver_email = receiver_email
        self.subject = subject
        self.message = message
        self.attachf = attach

    def set_connection(self):
        smtp_server = "smtp-mail.outlook.com"
        smtp_port = 587 
        self.server = smtplib.SMTP(smtp_server, smtp_port)
        self.server.starttls()
        self.server.login(self.sender_email, self.sender_password)

    def send_encryptMail(self):
        key =Fernet.generate_key()
        cipher =Fernet(key)
        plaintext = bytes(self.message.encode())
        encrypted = cipher.encrypt(plaintext)
        self.message = "This is a Plain text. And here you have the key to decipher the text encrypted "+ str(key.decode('utf-8'))
        self.set_connection()
        self.send_email()
        self.message = str(encrypted)
        self.set_connection()
        self.send_email()



    def send_email(self):
        try:
            email_message = MIMEMultipart()
            email_message["From"] = self.sender_email
            email_message["To"] = self.receiver_email
            email_message["Subject"] = self.subject
            email_message.attach(MIMEText(self.message, "plain"))
            self.server.sendmail(self.sender_email, self.receiver_email, email_message.as_string())
            print("Success!")
            self.server.quit()
            return  True
        except:
            return False
    def send_mailAttach(self):
        try:
            email_message = MIMEMultipart()
            email_message["From"] = self.sender_email
            email_message["To"] = self.receiver_email
            email_message["Subject"] = self.subject
            email_message.attach(MIMEText("Report file is attached here.", 'plain'))
            with open(self.attachf, 'rb') as file:
                attach = MIMEApplication(file.read(), _subtype="octet-stream")
                attach.add_header('Content-Disposition', 'attachment', filename=file.name)
                email_message.attach(attach)
            self.server.sendmail(self.sender_email, self.receiver_email, email_message.as_string())
            self.server.quit()
            print("Success.")
            return  True
        except Exception as e :
            print(e)
            return False



