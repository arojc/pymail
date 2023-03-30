import os
from win32com.client import Dispatch
from common_variables import common_variables as cv

class Setup:
    def setupShortcut(self):

        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        path_to_shortcut = os.path.join(desktop, cv.event_reader)
        path_to_here = os.path.abspath(".")
        target = os.path.join(path_to_here, cv.start_main_path)
        icon = os.path.join(path_to_here, cv.skull_icon_path)

        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path_to_shortcut)
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = os.path.join(path_to_here, "bat_scripts")
        shortcut.IconLocation = icon
        shortcut.save()

    def deleteShortcut(self):
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        path_to_shortcut = os.path.join(desktop, "EVENT_READER.lnk")
        os.remove(path_to_shortcut)




