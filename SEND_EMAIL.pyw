import sys
import json

from email_sender import email_sender

def func(dict):
    es = email_sender()
    es.send_email(dict)

if __name__ == '__main__':
    dict = {}
    for i in range(len(sys.argv)):
        dict[i] = sys.argv[i]
    #func(json.dumps(dict))
    func(dict)

#func()