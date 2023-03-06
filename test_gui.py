from unittest import TestCase
from gui import gui
from gui import SettingsTab
from email_sender import email_sender


class TestSettingsTab(TestCase):
    def test_save_only_sender(self):
        self.fail()

    def test_save_only_receiver(self):
        self.fail()

    def test_save_only_password(self):
        self.fail()

    def test_save_all(self):
        self.fail()

    def test_save_individual_setting(self):
        g = gui()
        es = email_sender()
        st = SettingsTab(g)
        settings_dict = es.get_settings()
        settings_dict["Sender"] = "Pat"
        es.save_settings(settings_dict)

        st.saveIndividualSetting("Sender", "Mat")

        settings_dict_1 = es.get_settings()

        self.assertNotEqual(settings_dict_1["Sender"], "Mat")


