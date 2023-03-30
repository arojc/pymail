#! py -3
import sys

from PyQt5.QtWidgets import QApplication

from gui import gui

if __name__ == '__main__':
    app = QApplication(sys.argv)
    g = gui()
    g.show()
    sys.exit(app.exec_())






