__app_name__ = "LocalLead AI Pro"
__author__ = "OSSIQN"
__website__ = "https://ossiqn.com.tr"
__github__ = "https://github.com/ossiqn"

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from src.config import Config

class MailAgent:
    def __init__(self):
        self.host = Config.SMTP_HOST
        self.port = Config.SMTP_PORT
        self.user = Config.SMTP_USER
        self.password = Config.SMTP_PASS

    def send_email(self, to_address, subject, body):
        if not self.user or not self.password:
            return False
            
        try:
            msg = MIMEMultipart()
            msg['From'] = self.user
            msg['To'] = to_address
            msg['Subject'] = subject
            
            msg.attach(MIMEText(body, 'html'))
            
            server = smtplib.SMTP(self.host, self.port)
            server.starttls()
            server.login(self.user, self.password)
            server.send_message(msg)
            server.quit()
            
            return True
        except Exception:
            return False