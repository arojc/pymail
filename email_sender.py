import datetime
from email.message import EmailMessage
import ssl
import smtplib
import json
from common_variables import EvtLevel, common_variables as cv


class email_sender :
    def print_hi(self, name):
        print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    def get_settings(self):
        settings_dict = {}
        try :
            settings_file = open(cv.PATH + "settings.txt", "r")
            settings_string = settings_file.read()
            # settings_string = '{"EventCode": 6969, "Sender": "andraz.rojc@caretronic.com", "Receiver": "andraz.rojc@caretronic.com", "Password": "eynuipkdyqxkvhni"}'
            settings_string = settings_string.replace('\n', ' ')
            settings_dict = json.loads(settings_string)
        except Exception as x:
            error = x.args

        return settings_dict

    def save_settings(self, settings_dict):
        settings_file = open("settings.txt", "w")
        settings_str = json.dumps(settings_dict)
        settings_file.write(settings_str)


    def send_email(self, dict):
        #email_sender = 'andraz.rojc@caretronic.com'
        #email_password = 'eynuipkdyqxkvhni'
        #email_receiver = 'andraz.rojc@caretronic.com'

        settings = self.get_settings()
        sender = settings["Sender"]
        receiver = settings["Receiver"]
        password = settings["Password"]

        #subject = 'Poskus ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        body = """To elektronsko pismo je poskusne narave. Vseeno nanj lahko odgovorite, v kolikor je odgovor prijazen :-)"""

        em = EmailMessage()
        em['From'] = sender
        em['To'] = receiver
        em['Subject'] = "Poskus"
        em.set_content(str(dict))

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(sender, password)
            smtp.sendmail(sender, receiver, em.as_string())


