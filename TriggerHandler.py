import json
import os
import inspect
import subprocess
from trigger import trigger
from common_variables import common_variables as cv
from XMLHandler import XMLHandler


class TriggerHandler:

    # def __init__(self):
        # self.t = trigger()
        # self.t.logInfo(18, f"Starting function {inspect.stack()[0][3]}")


    def createATrigger(self, id, name, receiver):

        # self.t.logInfo(19, f"Starting function {inspect.stack()[0][3]}")

        x = XMLHandler()
        x.createTriggerToImport(id, name, receiver)
        triggerName = f"{cv.triggers_path}\\Trigger_{id}_{name}"
        self.importTrigger(triggerName)
        triggerList = self.getTriggers()
        triggerList.append({cv.trigger_event_id: id, cv.trigger_event_name: name, cv.trigger_receiver: receiver})
        self.save_triggers(triggerList)


    def deleteATrigger(self, id, name):

        # self.t.logInfo(20, f"Starting function {inspect.stack()[0][3]}")

        triggerName = f"{cv.triggers_path}\\Trigger_{id}_{name}"
        self.removeTrigger(triggerName)

        triggerList = self.getTriggers()
        for item in triggerList:
            xid = item[cv.trigger_event_id]
            xname = item[cv.trigger_event_name]
            if(xid == id and xname == name):
                triggerList.remove(item)
        self.save_triggers(triggerList)


    def importTrigger(self, taskName):

        # self.t.logInfo(21, f"Starting function {inspect.stack()[0][3]}")

        self.removeTrigger(taskName)
        command = f"{cv.import_task} {taskName}"
        subprocess.Popen(command, stdout=None, stderr=subprocess.PIPE, shell=False)


    def removeTrigger(self, taskName):

        # self.t.logInfo(22, f"Starting function {inspect.stack()[0][3]}")

        if(self.checkForTrigger(taskName)) :
            command = f"{cv.remove_task} {taskName}"
            subprocess.Popen(command, stdout=None, stderr=subprocess.PIPE, shell=False)

    def checkForTrigger(self, taskName):

        # self.t.logInfo(23, f"Starting function {inspect.stack()[0][3]}")

        command = f"{cv.check_task} {taskName}"
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        output, error = process.communicate()
        le = len(error)

        return le <= 0


    def save_triggers(self, triggers_list):

        # self.t.logInfo(24, f"Starting function {inspect.stack()[0][3]}")

        try:
            with open(cv.trigger_list_path, "w") as f:
                json.dump(triggers_list, f)
        except Exception as x:
            self.t.logError(6, x.args)


    def getTriggers(self):

        # self.t.logInfo(25, f"Starting function {inspect.stack()[0][3]}")

        triggers_list = []
        try :
            triggers_file = open(cv.trigger_list_path, "r")
            triggers_string = triggers_file.read()
            triggers_list = json.loads(triggers_string)
            triggers_file.close()
        except Exception as x:
            self.t.logError(7, "Error in function TriggerHandler.getTriggers()")

        return triggers_list


