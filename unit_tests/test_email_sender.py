from unittest import TestCase

from email_sender import email_sender


class Testemail_sender(TestCase):
    def test_get_settings(self):
        e = email_sender()
        sd = e.get_settings()

        self.assertIsNotNone(sd)
        self.assertNotEqual(len(sd), 0)

    def test_save_settings(self):
        self.fail()

    def test_send_email(self):
        self.fail()
