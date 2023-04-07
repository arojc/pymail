from unittest import TestCase

from XMLHandler import XMLHandler


class TestXMLHandler(TestCase):

    def test_create_trigger_to_import_general(self):
        x = XMLHandler()
        x.createTriggerToImport(1, 'A', 'andraz.rojc@caretronic.com')


