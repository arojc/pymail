import os, winshell
from win32com.client import Dispatch

class Setup:
    def setup(self):

        desktop = winshell.desktop()
        path_to_shortcut = os.path.join(desktop, "EVENT_READER.lnk")
        path_to_here = os.path.abspath(".")
        target = os.path.join(path_to_here, "script.py")
        icon = os.path.join(path_to_here, "icon_2.png")

        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path_to_shortcut)
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = path_to_here
        shortcut.IconLocation = icon
        shortcut.save()

        input("Press Enter to exit ...")