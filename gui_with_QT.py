import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from common_variables import common_variables

class gui_with_QT:
    def window_number_1(self):
        app = QApplication(sys.argv)

        win = self.window_standard()
        win.setStyleSheet("background-color: dark-red")
        win.show()
        sys.exit(app.exec_())

    def window_number_2(self):
        app = QApplication(sys.argv)

        win = self.window_standard()

        lbl_name = QtWidgets.QLabel(win)
        lbl_name.setText("Vnesi ime ...")
        lbl_name.move(50, 50)

        lbl_surename = QtWidgets.QLabel(win)
        lbl_surename.setText("Vnesi priimek ...")
        lbl_surename.move(50, 90)

        txt_name = QtWidgets.QLineEdit(win)
        txt_name.move(200, 50)

        txt_surname = QtWidgets.QLineEdit(win)
        txt_surname.move(200, 90)

        def clicked(self):
            print("button_clicked")
            print("Name: " + txt_name.text())
            print("surname: " + txt_surname.text())

        btn_save = QtWidgets.QPushButton(win)
        btn_save.setText("Shrani")
        btn_save.clicked.connect(clicked)
        btn_save.move(200, 130)

        win.show()
        sys.exit(app.exec_())

    def window_standard(self):
        win = QMainWindow()
        win.setGeometry(1200,300, 700, 700)
        win.setWindowTitle(common_variables.top_left_text)
        win.setWindowIcon(QIcon("icons/caretronic_logo.jpg"))
        win.setToolTip("EventReader")
        win.setToolTipDuration(1000)

        #win.setStyleSheet("background-color: dark-red")

        return win

class my_window(QMainWindow):
    def __init__(self):
        super(my_window, self).__init__()
        self.setGeometry(1200, 300, 700, 700)
        self.setWindowTitle(common_variables.top_left_text)
        self.setToolTip("EventReader")
        self.setWindowIcon(QIcon("icons/caretronic_logo.jpg"))
        self.initUI()

    def initUI(self):
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText("Vnesi ime ...")
        self.lbl_name.move(50, 50)

        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText("Vnesi priimek ...")
        self.lbl_surname.move(50, 90)

        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(200, 50)
        self.txt_name.resize(200, 32)

        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(200, 90)
        self.txt_surname.resize(200, 32)

        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText("Shrani")
        self.btn_save.clicked.connect(self.clicked)
        self.btn_save.move(200, 130)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.setText("RESULT")
        self.lbl_result.move(200, 170)
        self.lbl_result.resize(200, 200)

    def clicked(self):
        self.lbl_result.setText('Name\t:' + self.txt_name.text() + '\nSurname\t:' + self.txt_surname.text())


class calculator(QMainWindow):
    def __init__(self):
        super(calculator, self).__init__()
        self.setGeometry(1200, 300, 700, 700)
        self.setWindowTitle(common_variables.top_left_text)
        self.setToolTip("EventReader")
        self.setWindowIcon(QIcon("icons/caretronic_logo.jpg"))
        self.initUI()

    def initUI(self):
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText("Prva številka:")
        self.lbl_name.move(50, 50)

        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText("Druga številka:")
        self.lbl_surname.move(50, 90)

        self.prva_st = QtWidgets.QLineEdit(self)
        self.prva_st.move(200, 50)
        self.prva_st.resize(200, 32)

        self.druga_st = QtWidgets.QLineEdit(self)
        self.druga_st.move(200, 90)
        self.druga_st.resize(200, 32)

        self.btn_add = QtWidgets.QPushButton(self)
        self.btn_add.setText("Seštej")
        self.btn_add.clicked.connect(self.clicked)
        self.btn_add.move(200, 130)

        self.btn_sub = QtWidgets.QPushButton(self)
        self.btn_sub.setText("Odštej")
        self.btn_sub.clicked.connect(self.clicked)
        self.btn_sub.move(200, 180)

        self.btn_mul = QtWidgets.QPushButton(self)
        self.btn_mul.setText("Množi")
        self.btn_mul.clicked.connect(self.clicked)
        self.btn_mul.move(200, 230)

        self.btn_div = QtWidgets.QPushButton(self)
        self.btn_div.setText("Deli")
        self.btn_div.clicked.connect(self.clicked)
        self.btn_div.move(200, 280)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.setText("RESULT")
        self.lbl_result.move(200, 320)
        self.lbl_result.resize(200, 200)

    def clicked(self):
        sender = self.sender()
        result = 0

        if sender.text() == "Seštej" :
            result = int(self.prva_st.text()) + int(self.druga_st.text())
        elif sender.text() == "Odštej" :
            result = int(self.prva_st.text()) - int(self.druga_st.text())
        elif sender.text() == "Množi" :
            result = int(self.prva_st.text()) * int(self.druga_st.text())
        elif sender.text() == "Deli" :
            result = int(self.prva_st.text()) / int(self.druga_st.text())

        self.lbl_result.setText('Result:\t' + str(result))







