import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget, QPushButton, QGridLayout
from PyQt5.QtGui import QIcon
from common_variables import common_variables
from email_sender import email_sender
from qtwidgets import PasswordEdit

class gui(QMainWindow):

    def __init__(self):
        super().__init__()
        # self.title = 'PyQt5 tabs - pythonspot.com'
        # self.setWindowTitle(common_variables.top_left_text)
        self.left = 0
        self.top = 0
        self.width = 700
        self.height = 700
        self.setWindowTitle(common_variables.top_left_text)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setToolTip("EventReader")
        self.setWindowIcon(QIcon("caretronic_logo.jpg"))

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        es = email_sender()
        settings = es.get_settings()
        cv = common_variables()

        self.table_widget.tab1.sender_textbox.setText(settings[cv.es_sender])
        self.table_widget.tab1.receiver_textbox.setText(settings[cv.es_receiver])
        self.table_widget.tab1.password_textbox.setText(settings[cv.es_password])

        self.show()

class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.tabs = QTabWidget()
        self.tab1 = SettingsTab(self)
        self.tab2 = TestingTab(self)
        self.tabs.resize(300, 200)

        self.tabs.addTab(self.tab1, 'Settings')
        self.tabs.addTab(self.tab2, 'Testing')

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

class SettingsTab(QWidget):

    def __init__(self, parent):

        super(QWidget, self).__init__(parent)

        self.layout = QGridLayout(self)

        self.sender_label = QtWidgets.QLabel(self)
        self.sender_label.setText('Sender:')
        self.sender_label.setFixedSize(common_variables.gui_label_width, common_variables.gui_label_heigth)
        self.sender_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.sender_label, 1, 1, Qt.AlignCenter)

        self.receiver_label = QtWidgets.QLabel(self)
        self.receiver_label.setText('Receiver:')
        self.receiver_label.setFixedSize(common_variables.gui_label_width, common_variables.gui_label_heigth)
        self.receiver_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.receiver_label, 2, 1)

        self.password_label = QtWidgets.QLabel(self)
        self.password_label.setText('Password:')
        self.password_label.setFixedSize(common_variables.gui_label_width, common_variables.gui_label_heigth)
        self.password_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.password_label, 3, 1)


        self.sender_textbox = QtWidgets.QLineEdit(self)
        self.sender_textbox.setText("textbox")
        self.sender_textbox.setFixedSize(common_variables.gui_textbox_width, common_variables.gui_label_heigth)
        self.layout.addWidget(self.sender_textbox, 1, 2)

        self.receiver_textbox = QtWidgets.QLineEdit(self)
        self.receiver_textbox.setText("textbox")
        self.receiver_textbox.setFixedSize(common_variables.gui_textbox_width, common_variables.gui_label_heigth)
        self.layout.addWidget(self.receiver_textbox, 2, 2)

        self.password_textbox = PasswordEdit(self)
        self.password_textbox.setText("textbox")
        self.password_textbox.setFixedSize(common_variables.gui_textbox_width, common_variables.gui_label_heigth)
        self.password_textbox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.layout.addWidget(self.password_textbox, 3, 2)


        self.sender_button = QtWidgets.QPushButton(self)
        self.sender_button.setText("Save Sender")
        self.sender_button.setFixedSize(common_variables.gui_button_width, common_variables.gui_label_heigth)
        self.sender_button.clicked.connect(self.saveOnlySender)
        self.layout.addWidget(self.sender_button, 1, 3)

        self.receiver_button = QtWidgets.QPushButton(self)
        self.receiver_button.setText("Save Receiver")
        self.receiver_button.setFixedSize(common_variables.gui_button_width, common_variables.gui_label_heigth)
        self.receiver_button.clicked.connect(self.saveOnlyReceiver)
        self.layout.addWidget(self.receiver_button, 2, 3)

        self.password_button = QtWidgets.QPushButton(self)
        self.password_button.setText("Save Password")
        self.password_button.setFixedSize(common_variables.gui_button_width, common_variables.gui_label_heigth)
        self.password_button.clicked.connect(self.saveOnlyPassword)
        self.layout.addWidget(self.password_button, 3, 3)


        self.refresh_button = QtWidgets.QPushButton(self)
        self.refresh_button.setText("Refresh")
        self.refresh_button.setFixedSize(common_variables.gui_button_width, common_variables.gui_bottom_button_heigth)
        self.refresh_button.clicked.connect(self.saveAll)
        self.layout.addWidget(self.refresh_button, 4, 2)

        self.saveall_button = QtWidgets.QPushButton(self)
        self.saveall_button.setText("Save All")
        self.saveall_button.setFixedSize(common_variables.gui_button_width, common_variables.gui_bottom_button_heigth)
        self.layout.addWidget(self.saveall_button, 4, 3)

        self.setLayout(self.layout)

    def saveOnlySender(self):
        value = self.sender_textbox.text()
        key = "Sender"
        self.saveIndividualSetting(key, value)

    def saveOnlyReceiver(self):
        value = self.receiver_textbox.text()
        key = "Receiver"
        self.saveIndividualSetting(key, value)

    def saveOnlyPassword(self):
        value = self.password_textbox.text()
        key = "Password"
        self.saveIndividualSetting(key, value)

    def saveAll(self):
        self.saveOnlySender()
        self.saveOnlyReceiver()
        self.saveOnlyPassword()

    def saveIndividualSetting(self, key, value):
        es = email_sender()
        settings_dict = es.get_settings()
        settings_dict[key] = value
        es.save_settings(settings_dict)

    def refreshAll(self):
        pass



class TestingTab(QWidget):

    def __init__(self, parent):

        super(QWidget, self).__init__(parent)

        self.layout = QGridLayout(self)

        self.pushButton1 = QtWidgets.QPushButton(self)
        self.pushButton1.setText('Knof1')
        self.pushButton1.setFixedSize(200, 30)
        self.layout.addWidget(self.pushButton1, 1, 1)

        self.pushButton2 = QtWidgets.QPushButton(self)
        self.pushButton2.setText('Knof2')
        self.pushButton2.setFixedSize(200, 30)
        self.layout.addWidget(self.pushButton2, 2, 2)

        self.setLayout(self.layout)







