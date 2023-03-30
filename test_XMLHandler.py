from unittest import TestCase

from XMLHandler import XMLHandler


class TestXMLHandler(TestCase):

    def setUp(self):
        self.x = XMLHandler()

    def test_create_trigger_to_import_general(self):
        r = self.x.createTriggerToImport(1, 'A', 'andraz.rojc@caretronic.com')
        self.assertTrue(r)


