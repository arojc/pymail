import json
import os
import inspect
import subprocess
from trigger import trigger
from common_variables import common_variables as cv
from XMLHandler import XMLHandler


class TriggerHandler:


    def createATriggerItem(self, id, name, receiver):

        self.deleteATriggerItem(id, name)

        x = XMLHandler()
        x.createTriggerToImport(id, name, receiver)
        triggerName = f"{cv.triggers_path}\\Trigger_{id}_{name}"

        self.importTrigger(triggerName)
        triggerList = self.getItems()

        # trigger = next((t for t in triggerList if (t[cv.trigger_event_id] == id and t[cv.trigger_event_name] == name)), None)
        # if trigger == None:
        triggerList.append({cv.trigger_event_id: id, cv.trigger_event_name: name, cv.trigger_receiver: receiver})
        self.saveItems(triggerList)


    def deleteATriggerItem(self, id, name):

        triggerName = f"{cv.triggers_path}\\Trigger_{id}_{name}"
        self.removeTrigger(triggerName)

        itemList = self.getItems()
        for item in itemList:
            xid = item[cv.trigger_event_id]
            xname = item[cv.trigger_event_name]
            if(xid == id and xname == name):
                itemList.remove(item)
        self.saveItems(itemList)


    def importTrigger(self, taskName):

        self.removeTrigger(taskName)
        command = f"{cv.import_task} {taskName}"
        subprocess.Popen(command, stdout=None, stderr=subprocess.PIPE, shell=False)


    def removeTrigger(self, taskName):

        if(self.checkForTrigger(taskName)) :
            command = f"{cv.remove_task} {taskName}"
            subprocess.Popen(command, stdout=None, stderr=subprocess.PIPE, shell=False)

    def checkForTrigger(self, taskName):

        command = f"{cv.check_task} {taskName}"
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        output, error = process.communicate()
        le = len(error)

        return le <= 0


    def saveItems(self, triggers_list):

        try:
            with open(cv.trigger_list_path, "w") as f:
                json.dump(triggers_list, f)
        except Exception as x:
            self.t.logError(6, x.args)


    def getItems(self):

        triggers_list = []
        try :
            triggers_file = open(cv.trigger_list_path, "r")
            triggers_string = triggers_file.read()
            triggers_list = json.loads(triggers_string)
            triggers_file.close()
        except Exception as x:
            self.t.logError(7, "Error in function TriggerHandler.getTriggers()")

        return triggers_list


