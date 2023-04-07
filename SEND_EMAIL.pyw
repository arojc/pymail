import sys
import inspect

#from trigger import trigger
from email_sender import email_sender

def func(dict):
    pass

    # if False:
    #     t = trigger()
    #     t.logInfo(50, f"Starting function {inspect.stack()[0][3]}")

    es = email_sender()
    es.send_email(dict)

if __name__ == '__main__':
    dict = {}
    for i in range(len(sys.argv)):
        dict[i] = sys.argv[i]
    func(dict)

