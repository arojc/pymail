import json
from unittest import TestCase

from email_sender import email_sender
from common_variables import common_variables as cv


class Testemail_sender(TestCase):
    def test_get_settings(self):
        e = email_sender()
        sd = e.get_settings()

        self.assertIsNotNone(sd)
        self.assertNotEqual(len(sd), 0)


    def test_save_settings(self):
        fakeSender = 'sveti.peter@nebe.sa'

        e = email_sender()
        sd = e.get_settings()

        self.assertIsNotNone(sd)
        self.assertNotEqual(len(sd), 0)
        self.assertNotEqual(sd[cv.es_sender], fakeSender)

        tempSender = sd[cv.es_sender]
        sd[cv.es_sender] = fakeSender

        e.save_settings(sd)

        sd = e.get_settings()
        self.assertEqual(sd[cv.es_sender], fakeSender)

        sd[cv.es_sender] = tempSender
        e.save_settings(sd)



    def test_send_email(self):
        e = email_sender()
        e.send_email(['Nekaj', '-Command', 'D:\Event70.ps1', '33', '2', 'Task', 'andraz.rojc@caretronic.com'])
