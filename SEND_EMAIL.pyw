import sys
import json

from email_sender import email_sender

def func(id, level, task, N):
    es = email_sender()
    es.send_email(id, level, task, N)

if __name__ == '__main__':
    j = json()
    func(sys.argv[0], sys.argv[1], sys.argv[2], len(sys.argv))

#func()