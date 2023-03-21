import json
import os
import subprocess

from common_variables import common_variables as cv
from data_models.TriggerList import Trigger
from XMLHandler import XMLHandler


class TriggerHandler:

    def createATrigger(self, id, name):
        x = XMLHandler()
        x.createTriggetToImport(id, name)
        triggerName = f"TestingTasks\\Trigger_{id}_{name}"
        self.importTrigger(triggerName)

        triggerList = self.getTriggers()
        triggerList.append({"EventID": id, "EventName": name, "Receiver": "nekdo@pac.si"})
        self.save_triggers(triggerList)

    def deleteATrigger(self, id, name):
        triggerName = f"TestingTasks\\Trigger_{id}_{name}"
        self.removeTrigger(triggerName)

        triggerList = self.getTriggers()
        for item in triggerList:
            xid = item["EventID"]
            xname = item["EventName"]
            if(xid == id and xname == name):
                triggerList.remove(item)
        #triggerList.append({"EventID": id, "EventName": name, "Receiver": "nekdo@pac.si"})
        self.save_triggers(triggerList)


    def importTrigger(self, taskName):
        self.removeTrigger(taskName)
        command = f"bat_scripts\\import_the_task.bat {taskName}"
        subprocess.Popen(command, stdout=None, stderr=subprocess.PIPE, shell=False)


    def removeTrigger(self, taskName):
        if(self.checkForTrigger(taskName)) :
            command = f"bat_scripts\\remove_the_task.bat {taskName}"
            subprocess.Popen(command, stdout=None, stderr=subprocess.PIPE, shell=False)

    def checkForTrigger(self, taskName):
        command = f"bat_scripts\\check_the_task.bat {taskName}"
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        output, error = process.communicate()
        le = len(error)

        return le <= 0


    def save_triggers(self, triggers_list):
        with open("txts\\triggers.txt", "w") as f:
            json.dump(triggers_list, f)


    def getTriggers(self):
        triggers_list = []
        try :
            triggers_file = open("txts\\triggers.txt", "r")
            triggers_string = triggers_file.read()
            triggers_list = json.loads(triggers_string)
            triggers_file.close()
        except Exception as x:
            error = x.args

        return triggers_list


    def createTriggers(self):
        triggers_list = []
        for i in range(5):
            trigger = {}
            trigger["EventID"] = i
            trigger["EventName"] = "Event"
            trigger["Receiver"] = "nekdo@pac.si"
            triggers_list.append(trigger)

        self.save_triggers(triggers_list)

th = TriggerHandler()
th.checkForTrigger("TestingTasks\\Task71")

#pass
#l = th.getTriggers()
#l.pop(1)
#th.save_triggers(l)
#pass