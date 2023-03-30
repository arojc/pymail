import xml.etree.ElementTree as ET
import re
import os
from trigger import trigger
from common_variables import common_variables as cv
import inspect


class XMLHandler:
    def createTriggerToImport(self, id, name, receiver):

        # self.t = trigger()
        # self.t.logInfo(26, f"Starting function {inspect.stack()[0][3]}")

        try:
            tree0 = ET.parse(cv.blueprint_trigger_path)
        except Exception as x:
            t = trigger()
            t.logError(1, "Error in function XMLHandler.createTriggerToImport() - Error parsing tree")
            return False

        root0 = tree0.getroot()
        xmlns = re.match(r'{.*}', root0.tag).group(0)
        ET.register_namespace('', xmlns)

        tree = ET.parse(cv.blueprint_trigger_path)
        root = tree.getroot()

        eggs = []

        for value in root.iter(f'{xmlns}Subscription'):
            eggs.append(value.text)

        egg = eggs[0]

        tree1 = ET.ElementTree(ET.fromstring(egg))
        root1 = tree1.getroot()
        t = root1[0][0].text

        eid = "EventID=" + str(id)
        en = "@Name='" + name + "'"

        t = re.sub("EventID=[0-9]*", eid, t)
        t = re.sub("@Name=\'[a-zA-Z]*\'", en, t)

        root1[0][0].text = t
        tree1Txt = ET.tostring(root1, encoding='unicode')

        for value in root.iter(f'{xmlns}Subscription'):
            value.text = tree1Txt

        for x in root.iter(f"{xmlns}Actions"):
            exec = x[0]
            command = exec[0]
            command.text = os.path.join(os.path.abspath("."), 'SEND_EMAIL.exe')

            self.t = trigger()
            self.t.logInfo(39, f"Starting function {inspect.stack()[0][3]}")

            arguments = exec[1]
            argsText = arguments.text
            argsText = argsText + f" {receiver}"
            x[0][1].text = argsText
            pass

        try:
            tree.write(cv.temp_trigger_path, xml_declaration=True, encoding="UTF-16", method="xml")
        except Exception as x:
            self.t.logError(3, f"Starting function PATH: {cv.temp_trigger_path}, {x.args}")
            return False

        try:
            f = open(cv.temp_trigger_path, 'r', encoding='UTF-16')
            xmlTxt = f.read()
            f.close()

            open(cv.temp_trigger_path, 'w').close()

            f = open(cv.temp_trigger_path, 'w', encoding='UTF-16')
            xmlTxt = xmlTxt.replace(':ns0', '')
            xmlTxt = xmlTxt.replace('ns0:', '')
            f.write(xmlTxt)
            f.close()
        except Exception as x:
            t = trigger()
            t.logError(2, "Error in function XMLHandler.createTriggerToImport() - Error writing XML")
            return False

        return True


    def rec(self, root, counter):

        # self.t = trigger()
        # self.t.logInfo(27, f"Starting function {inspect.stack()[0][3]}")

        for i in range(counter):
            print("\t", end='')
        print(root.tag)
        for i in range(counter):
            print("\t", end='')
        print(root.text)

        for kid in root:
            self.rec(kid, counter+1)

        if counter==0:
            print('\n\n\n')
