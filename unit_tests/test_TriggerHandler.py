from unittest import TestCase

from TriggerHandler import TriggerHandler
from common_variables import common_variables as cv


class TestTriggerHandler(TestCase):
    def test_create_atrigger(self):
        self.fail()

    def test_delete_atrigger(self):
        self.fail()

    def test_import_trigger(self):
        self.fail()

    def test_remove_trigger(self):
        self.fail()

    def test_check_for_trigger(self):
        self.fail()

    def test_save_triggers(self):
        newTrigger = {cv.trigger_event_id:1000, cv.trigger_event_name:"TestTrigger", cv.trigger_receiver:"andraz.rojc@caretronic.com"}
        triggerList = [newTrigger]

        t = TriggerHandler()
        t.save_triggers(triggerList)

        list = t.getTriggers()
        for item in list:
            if item[cv.trigger_event_id] == newTrigger[cv.trigger_event_id] and item[cv.trigger_event_name] == newTrigger[cv.trigger_event_name] :
                assert True
                return

        assert False

    def test_get_triggers(self):
        t = TriggerHandler()
        l = t.getTriggers()

        self.assertTrue(len(l)>0)
