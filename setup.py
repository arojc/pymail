import os
from win32com.client import Dispatch
import subprocess

from email_sender import email_sender

class Setup:
    def setupShortcut(self):

        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        path_to_shortcut = os.path.join(desktop, "EVENT_READER.lnk")
        path_to_here = os.path.abspath(".")
        target = os.path.join(path_to_here, "bat_scripts/start_main.bat")
        icon = os.path.join(path_to_here, "icons/skull.ico")

        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path_to_shortcut)
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = os.path.join(path_to_here, "bat_scripts")
        shortcut.IconLocation = icon
        shortcut.save()

        input("Press Enter to exit ...")

    def deleteShortcut(self):
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        path_to_shortcut = os.path.join(desktop, "EVENT_READER.lnk")
        os.remove(path_to_shortcut)


    def setupTrigger(self):
        path_to_here = os.path.abspath(".")
        subprocess.call([rf'{path_to_here}\create_the_task.bat'])

    def deleteTrigger(self):
        path_to_here = os.path.abspath(".")
        subprocess.call([rf'{path_to_here}\delete_the_task.bat'])



