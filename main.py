#! py -3
import sys

import wmi
import json

from PyQt5.QtWidgets import QApplication

#import SEND_EMAIL
from setup import Setup
import customtkinter
from gui_with_customtkinter import gui_with_customtkinter
from gui_with_QT import gui_with_QT, my_window, calculator
from gui import gui




if __name__ == '__main__':
    app = QApplication(sys.argv)
    g = gui()
    g.show()
    sys.exit(app.exec_())
