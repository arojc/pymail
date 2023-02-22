from email_sender import email_sender

def func():
    es = email_sender()
    es.send_email()

if __name__ == '__main__':
    func()