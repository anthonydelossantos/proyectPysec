import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Crypto.Cipher import AES

class Mail:
    sender_email="" 
    sender_password=""
    receiver_email="" 
    subject=""
    message="" 
    server=""
    def set_values(self,sender_email, sender_password, receiver_email, subject, message):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.receiver_email = receiver_email
        self.subject = subject
        self.message = message

    def set_connection(self):
        smtp_server = "smtp-mail.outlook.com"
        smtp_port = 587 
        self.server = smtplib.SMTP(smtp_server, smtp_port)
        self.server.starttls()
        self.server.login(self.sender_email, self.sender_password)

    def send_encryptMail(self):
        key = b'Sixteen byte key'
        cipher = AES.new(key, AES.MODE_EAX)
        plaintext = bytes(self.message,encoding='utf-8')
        encrypted = cipher.encrypt(plaintext)
        self.message = "This is a Plain text. And here you have the key to decipher the text encrypted "+ str(key)
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
            self.server.quit()
            return  True
        except:
            return False


