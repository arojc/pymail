import datetime
from email.message import EmailMessage
import ssl
import smtplib
import json


class email_sender :
    def print_hi(self, name):
        # Use a breakpoint in the code line below to debug your script.
        print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    def get_settings(self):
        settings_file = open("settings.txt", "r")
        settings_string = settings_file.read()
        settings_string = settings_string.replace('\n', ' ')
        settings_dict = json.loads(settings_string)
        return settings_dict

    def send_email(self):
        #email_sender = 'andraz.rojc@caretronic.com'
        #email_password = 'eynuipkdyqxkvhni'
        #email_receiver = 'andraz.rojc@caretronic.com'

        settings = self.get_settings()
        sender = settings["Sender"]
        receiver = settings["Receiver"]
        password = settings["Password"]

        subject = 'Poskus ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        body = """To elektronsko pismo je poskusne narave. Vseeno nanj lahko odgovorite, v kolikor je odgovor prijazen :-)"""

        em = EmailMessage()
        em['From'] = sender
        em['To'] = receiver
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(sender, password)
            smtp.sendmail(sender, receiver, em.as_string())


