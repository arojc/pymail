#! py -3
import os
import sys

from PyQt5.QtWidgets import QApplication

from gui import gui

if __name__ == '__main__':
    app = QApplication(sys.argv)
    g = gui()
    g.show()
    sys.exit(app.exec_())

    #t = trigger()
    #t.trigger()

    #s = Setup()
    #s.setupTrigger()
    #s.deleteTrigger()

    #os.system(f"test.bat")

    # command = f"bat_scripts\\test.bat"
    # process = subprocess.Popen(command, stdout=None, stderr=None, shell=False)
    #output, error = process.communicate()
    print(os.getcwd())






