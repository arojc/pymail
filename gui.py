import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget, QPushButton, QGridLayout, \
    QHBoxLayout, QListWidget, QListWidgetItem
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
        self.tab2 = TriggersTab(self)
        self.tabs.resize(300, 200)

        self.tabs.addTab(self.tab1, 'Settings')
        self.tabs.addTab(self.tab2, 'Triggers')

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

        #region labels
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
        #endregion labels

        #region lineedits
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
        #endregion lineedits

        #region buttons
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
        self.refresh_button.clicked.connect(self.refreshAll)
        self.layout.addWidget(self.refresh_button, 4, 2)

        self.saveall_button = QtWidgets.QPushButton(self)
        self.saveall_button.setText("Save All")
        self.saveall_button.setFixedSize(common_variables.gui_button_width, common_variables.gui_bottom_button_heigth)
        self.saveall_button.clicked.connect(self.saveAll)
        self.layout.addWidget(self.saveall_button, 4, 3)
        #endregion buttons

        self.setLayout(self.layout)

    #region functions
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
        es = email_sender()
        settings_dict = es.get_settings()

        value1 = self.sender_textbox.text()
        key1 = "Sender"

        value2 = self.receiver_textbox.text()
        key2 = "Receiver"

        value3 = self.password_textbox.text()
        key3 = "Password"

        settings_dict[key1] = value1
        settings_dict[key2] = value2
        settings_dict[key3] = value3

        es.save_settings(settings_dict)

        # self.saveOnlySender()
        # self.saveOnlyReceiver()
        # self.saveOnlyPassword()

    #endregion functions

    def saveIndividualSetting(self, key, value):
        es = email_sender()
        settings_dict = es.get_settings()
        settings_dict[key] = value
        es.save_settings(settings_dict)

    def refreshAll(self):
        es = email_sender()
        settings = es.get_settings()
        cv = common_variables()

        self.sender_textbox.setText(settings[cv.es_sender])
        self.receiver_textbox.setText(settings[cv.es_receiver])
        self.password_textbox.setText(settings[cv.es_password])



class TriggersTab(QWidget):

    def __init__(self, parent):

        super(QWidget, self).__init__(parent)

        self.layout1 = QVBoxLayout()
        self.layout2 = QHBoxLayout()


        list = QListWidget()

        self.layout4 = QHBoxLayout()

        self.first_label = QtWidgets.QLabel()
        self.first_label.setText('First item')
        self.first_label.setFixedSize(common_variables.gui_label_width, common_variables.gui_label_heigth)
        self.first_label.setAlignment(Qt.AlignCenter)
        self.layout4.addWidget(self.first_label, Qt.AlignCenter)

        self.first_button = QtWidgets.QPushButton()
        self.first_button.setText("First Button")
        #self.add_button.setFixedSize(common_variables.gui_button_width, common_variables.gui_label_heigth)
        #self.sender_button.clicked.connect(self.saveOnlySender)
        self.layout4.addWidget(self.first_button)

        x = QWidget()
        x.setLayout(self.layout4)

        item = QListWidgetItem("Prvi predmet", list)

        list.setItemWidget(item, x)

        #list.addItem(item)

        self.layout1.addWidget(list)

        self.add_button = QtWidgets.QPushButton(self)
        self.add_button.setText("Add")
        #self.add_button.setFixedSize(common_variables.gui_button_width, common_variables.gui_label_heigth)
        #self.sender_button.clicked.connect(self.saveOnlySender)
        self.layout2.addWidget(self.add_button)

        self.delete_button = QtWidgets.QPushButton(self)
        self.delete_button.setText("Delete")
        #self.delete_button.setFixedSize(common_variables.gui_button_width, common_variables.gui_label_heigth)
        # self.sender_button.clicked.connect(self.saveOnlySender)
        self.layout2.addWidget(self.delete_button)

        self.edit_button = QtWidgets.QPushButton(self)
        self.edit_button.setText("Edit")
        #self.delete_button.setFixedSize(common_variables.gui_button_width, common_variables.gui_label_heigth)
        # self.sender_button.clicked.connect(self.saveOnlySender)
        self.layout2.addWidget(self.edit_button)

        self.layout1.addLayout(self.layout2)

        self.setLayout(self.layout1)



        #self.layout = QGridLayout(self)

        #self.pushButton1 = QtWidgets.QPushButton(self)
        #self.pushButton1.setText('Knof1')
        #self.pushButton1.setFixedSize(200, 30)
        #self.layout.addWidget(self.pushButton1, 1, 1)

        #self.pushButton2 = QtWidgets.QPushButton(self)
        #self.pushButton2.setText('Knof2')
        #self.pushButton2.setFixedSize(200, 30)
        #self.layout.addWidget(self.pushButton2, 2, 2)

        #self.setLayout(self.layout)


class ListItem(QListWidgetItem):
    def __init__(self, parent):
        super(ListItem, self).__init__(parent)

        self.layout4 = QHBoxLayout()

        self.first_label = QtWidgets.QLabel()
        self.first_label.setText('Sender:')
        self.first_label.setFixedSize(common_variables.gui_label_width, common_variables.gui_label_heigth)
        self.first_label.setAlignment(Qt.AlignCenter)
        self.layout4.addWidget(self.first_label, Qt.AlignCenter)

        self.first_button = QtWidgets.QPushButton()
        self.first_button.setText("Add")
        #self.add_button.setFixedSize(common_variables.gui_button_width, common_variables.gui_label_heigth)
        #self.sender_button.clicked.connect(self.saveOnlySender)
        self.layout4.addWidget(self.first_button)










