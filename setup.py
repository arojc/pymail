import os, winshell
from win32com.client import Dispatch

desktop = winshell.desktop()
path_to_shortcut = os.path.join(desktop, "setup.lnk")
path_to_here = os.path.abspath(".")
target = os.path.join(path_to_here, "main.py")
icon = os.path.join(path_to_here, "icon_2.png")

#target = r"P:\Media\Media Player Classic\mplayerc.exe"
#wDir = r"P:\Media\Media Player Classic"
#icon = r"P:\Media\Media Player Classic\mplayerc.exe"

shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path_to_shortcut)
shortcut.Targetpath = target
shortcut.WorkingDirectory = path_to_here
shortcut.IconLocation = icon
shortcut.save()