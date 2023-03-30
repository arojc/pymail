from email.message import EmailMessage
import ssl
import smtplib
import json
from trigger import trigger
from common_variables import common_variables as cv
import inspect


class email_sender :
    def print_hi(self, name):

        # self.t = trigger()
        # self.t.logInfo(28, f"Starting function {inspect.stack()[0][3]}")

        print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    def get_settings(self):

        self.t = trigger()
        self.t.logInfo(29, f"Starting function {inspect.stack()[0][3]}")

        settings_dict = {}
        try :
            settings_file = open(cv.settings_path, "r")
            settings_string = settings_file.read()
            settings_string = settings_string.replace('\n', ' ')
            settings_dict = json.loads(settings_string)
        except Exception as x:
            t = trigger()
            t.logError(3, f"Error in function email_sender.get_settings() {x.args}")

        return settings_dict

    def save_settings(self, settings_dict):

        self.t = trigger()
        self.t.logInfo(30, f"Starting function {inspect.stack()[0][3]}")

        try:
            settings_file = open(cv.settings_path, "w")
            settings_str = json.dumps(settings_dict)
            settings_file.write(settings_str)
        except Exception as x:
            t = trigger()
            t.logError(4, "Error in function email_sender.save_settings()")




    def send_email(self, dict):

        self.t = trigger()
        self.t.logInfo(31, f"Starting function {inspect.stack()[0][3]}")

        #email_sender = 'andraz.rojc@caretronic.com'
        #email_password = 'eynuipkdyqxkvhni'
        #email_receiver = 'andraz.rojc@caretronic.com'

        settings = self.get_settings()

        print(settings)

        self.t.logInfo(51, f"Starting function {settings}")

        sender = settings["Sender"]
        receiver = dict[6]
        password = settings["Password"]

        body = """To elektronsko pismo je poskusne narave. Vseeno nanj lahko odgovorite, v kolikor je odgovor prijazen :-)"""

        em = EmailMessage()
        em['From'] = sender
        em['To'] = receiver
        em['Subject'] = f"Dogodek {dict[5]} {dict[3]}"
        em.set_content(body)

        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(sender, password)
                smtp.sendmail(sender, receiver, em.as_string())
        except Exception as x:
            t = trigger()
            t.logError(5, f"Error in function email_sender.send_email() {x.args}")



