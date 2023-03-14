import xml.etree.ElementTree as ET
import re

class XMLHandler:
    def create(self, id, name):
        tree = ET.parse("trigger_temp.xml")
        root = tree.getroot()
        ns = re.match(r'{.*}', root.tag).group(0)

        eggs = []
        for value in root.iter(f'{ns}Subscription'):
            eggs.append(value.text)

        egg = eggs[0]

        tree1 = ET.ElementTree(ET.fromstring(egg))
        root1 = tree1.getroot()
        t = root1[0][0].text

        print(t)

        eid = "EventID=" + str(id)
        en = "@Name='" + name + "'"

        t = re.sub("EventID=[0-9]*", eid, t)
        t = re.sub("@Name=\'[a-zA-Z]*\'", en, t)

        root1[0][0].text = t
        

        self.rec(root1, 0)
        print(t)


        #egg1 = root.find('xmlns:Subscription', ns)

        #eid = "EventID=" + str(id)
        #en = "@Name='" + name + "'"

        #eggs = re.sub("EventID=[0-9]*", eid, eggs)
        #eggs = re.sub("@Name=\'[a-zA-Z]*\'", en, eggs)

        #print(egg)

    def rec(self, root, counter):
        for i in range(counter):
            print("\t", end='')
        print(root.tag)

        for kid in root:
            self.rec(kid, counter+1)

x = XMLHandler()
x.create(1, "X")