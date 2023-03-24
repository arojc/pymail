import xml.etree.ElementTree as ET
import re
from common_variables import common_variables as cv


class XMLHandler:
    def createTriggetToImport(self, id, name, receiver):

        tree0 = ET.parse("xmls/Application_EventReader_71.xml")
        root0 = tree0.getroot()
        xmlns = re.match(r'{.*}', root0.tag).group(0)
        ET.register_namespace('', xmlns)

        tree = ET.parse("xmls/Application_EventReader_71.xml")
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
            a = x[0]
            b = a[1]
            c = b.text
            c = c + f" {receiver}"
            x[0][1].text = c
            pass

        tree.write(cv.temp_trigger_path, xml_declaration=True, encoding="UTF-16", method="xml")


        f = open(cv.temp_trigger_path, 'r', encoding='UTF-16')
        xmlTxt = f.read()
        f.close()

        open(cv.temp_trigger_path, 'w').close()

        f = open(cv.temp_trigger_path, 'w', encoding='UTF-16')
        xmlTxt = xmlTxt.replace(':ns0', '')
        xmlTxt = xmlTxt.replace('ns0:', '')
        f.write(xmlTxt)
        f.close()

    def rec(self, root, counter):
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

#x = XMLHandler()
#removeTrigger("TestingTasks\TaskX")