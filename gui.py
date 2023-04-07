import os
import sys
import inspect
import time

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot, Qt, QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget, QPushButton, QGridLayout, \
    QHBoxLayout, QListWidget, QListWidgetItem
from PyQt5.QtGui import QIcon, QPainter, QFont

from TriggerHandler import TriggerHandler
from common_variables import common_variables as cv
from email_sender import email_sender
from qtwidgets import PasswordEdit
from trigger import trigger

from XMLHandler import XMLHandler


class gui(QMainWindow):

    def __init__(self):
        super().__init__()

        # self.t = trigger()
        # self.t.logInfo(1, f"Starting function {inspect.stack()[0][3]}")

        self.setToolTip(cv.gui_tooltip)
        self.setWindowIcon(QIcon(cv.icon_path))
        self.setWindowTitle(cv.top_left_text)

        self.left = 0
        self.top = 0
        self.width = 700
        self.height = 700
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()

class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        # self.t = trigger()
        # self.t.logInfo(2, f"Starting function {inspect.stack()[0][3]}")

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

        self.tabs.setCurrentIndex(1)

    @pyqtSlot()
    def on_click(self):

        # self.t = trigger()
        # self.t.logInfo(3, f"Starting function {inspect.stack()[0][3]}")

        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

class SettingsTab(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        # self.t = trigger()
        # self.t.logInfo(4, f"Starting function {inspect.stack()[0][3]}")


        es = email_sender()
        settings = es.get_settings()

        self.layout = QGridLayout(self)

        #region labels
        self.sender_label = QtWidgets.QLabel(self)
        self.sender_label.setText('Sender:')
        self.sender_label.setFixedSize(cv.gui_label_width, cv.gui_label_heigth)
        self.sender_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.sender_label, 1, 1, Qt.AlignCenter)

        self.receiver_label = QtWidgets.QLabel(self)
        self.receiver_label.setText('Receiver:')
        self.receiver_label.setFixedSize(cv.gui_label_width, cv.gui_label_heigth)
        self.receiver_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.receiver_label, 2, 1)

        self.password_label = QtWidgets.QLabel(self)
        self.password_label.setText('Password:')
        self.password_label.setFixedSize(cv.gui_label_width, cv.gui_label_heigth)
        self.password_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.password_label, 3, 1)
        #endregion labels

        #region lineedits
        self.sender_textbox = QtWidgets.QLineEdit(self)
        self.sender_textbox.setText(settings[cv.es_sender])
        self.sender_textbox.setFixedSize(cv.gui_textbox_width, cv.gui_label_heigth)
        self.layout.addWidget(self.sender_textbox, 1, 2)

        self.receiver_textbox = QtWidgets.QLineEdit(self)
        self.receiver_textbox.setText(settings[cv.es_receiver])
        self.receiver_textbox.setFixedSize(cv.gui_textbox_width, cv.gui_label_heigth)
        self.layout.addWidget(self.receiver_textbox, 2, 2)

        self.password_textbox = PasswordEdit(self)
        self.password_textbox.setText(settings[cv.es_password])
        self.password_textbox.setFixedSize(cv.gui_textbox_width, cv.gui_label_heigth)
        self.password_textbox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.layout.addWidget(self.password_textbox, 3, 2)
        #endregion lineedits

        #region buttons
        self.sender_button = QtWidgets.QPushButton(self)
        self.sender_button.setText("Save Sender")
        self.sender_button.setFixedSize(cv.gui_button_width, cv.gui_label_heigth)
        self.sender_button.clicked.connect(self.saveOnlySender)
        self.layout.addWidget(self.sender_button, 1, 3)

        self.receiver_button = QtWidgets.QPushButton(self)
        self.receiver_button.setText("Save Receiver")
        self.receiver_button.setFixedSize(cv.gui_button_width, cv.gui_label_heigth)
        self.receiver_button.clicked.connect(self.saveOnlyReceiver)
        self.layout.addWidget(self.receiver_button, 2, 3)

        self.password_button = QtWidgets.QPushButton(self)
        self.password_button.setText("Save Password")
        self.password_button.setFixedSize(cv.gui_button_width, cv.gui_label_heigth)
        self.password_button.clicked.connect(self.saveOnlyPassword)
        self.layout.addWidget(self.password_button, 3, 3)


        self.refresh_button = QtWidgets.QPushButton(self)
        self.refresh_button.setText("Refresh")
        self.refresh_button.setFixedSize(cv.gui_button_width, cv.gui_bottom_button_heigth)
        self.refresh_button.clicked.connect(self.refreshAll)
        self.layout.addWidget(self.refresh_button, 4, 2)

        self.saveall_button = QtWidgets.QPushButton(self)
        self.saveall_button.setText("Save All")
        self.saveall_button.setFixedSize(cv.gui_button_width, cv.gui_bottom_button_heigth)
        self.saveall_button.clicked.connect(self.saveAll)
        self.layout.addWidget(self.saveall_button, 4, 3)
        #endregion buttons

        self.setLayout(self.layout)

    #region functions
    def saveOnlySender(self):

        # self.t = trigger()
        # self.t.logInfo(5, f"Starting function {inspect.stack()[0][3]}")

        value = self.sender_textbox.text()
        key = cv.es_sender
        self.saveIndividualSetting(key, value)

    def saveOnlyReceiver(self):

        # self.t = trigger()
        # self.t.logInfo(6, f"Starting function {inspect.stack()[0][3]}")

        value = self.receiver_textbox.text()
        key = cv.es_receiver
        self.saveIndividualSetting(key, value)

    def saveOnlyPassword(self):

        # self.t = trigger()
        # self.t.logInfo(7, f"Starting function {inspect.stack()[0][3]}")

        value = self.password_textbox.text()
        key = cv.es_password
        self.saveIndividualSetting(key, value)

    def saveAll(self):

        # self.t = trigger()
        # self.t.logInfo(8, f"Starting function {inspect.stack()[0][3]}")

        es = email_sender()
        settings_dict = es.get_settings()

        settings_dict[cv.es_sender] = self.sender_textbox.text()
        settings_dict[cv.es_receiver] = self.receiver_textbox.text()
        settings_dict[cv.es_password] = self.password_textbox.text()

        es.save_settings(settings_dict)

    #endregion functions

    def saveIndividualSetting(self, key, value):

        # self.t = trigger()
        # self.t.logInfo(9, f"Starting function {inspect.stack()[0][3]}")

        es = email_sender()
        settings_dict = es.get_settings()
        settings_dict[key] = value
        es.save_settings(settings_dict)

    def refreshAll(self):

        # self.t = trigger()
        # self.t.logInfo(10, f"Starting function {inspect.stack()[0][3]}")

        es = email_sender()
        settings = es.get_settings()

        self.sender_textbox.setText(settings[cv.es_sender])
        self.receiver_textbox.setText(settings[cv.es_receiver])
        self.password_textbox.setText(settings[cv.es_password])

class TriggersTab(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        # self.t = trigger()
        # self.t.logInfo(11, f"Starting function {inspect.stack()[0][3]}")


        self.list = QListWidget()

        self.layout1 = QVBoxLayout()
        self.layout2 = QHBoxLayout()

        self.populate()
        self.list.itemClicked.connect(self.onItemClicked)

        self.layout1.addWidget(self.list)

        #region Add button
        self.add_button = QtWidgets.QPushButton(self)
        self.add_button.setText("Add")
        self.add_button.clicked.connect(self.onAddButtonClicked)
        self.layout2.addWidget(self.add_button)
        #endregion Add button

        self.layout1.addLayout(self.layout2)

        self.setLayout(self.layout1)

    def onItemClicked(self, item):

        # self.t = trigger()
        # self.t.logInfo(12, f"Starting function {inspect.stack()[0][3]}")


        RowId = self.list.currentRow()

        self.m = MyPopup(RowId, self, True)
        self.m.show()

    def onAddButtonClicked(self):

        # self.t = trigger()
        # self.t.logInfo(13, f"Starting function {inspect.stack()[0][3]}")


        RowId = self.list.currentRow()

        self.m = MyPopup(RowId, self, False)
        self.m.show()

    def populate(self):

        # self.t = trigger()
        # self.t.logInfo(14, f"Starting function {inspect.stack()[0][3]}")

        th = TriggerHandler()
        ts = th.getItems()

        self.list.clear()

        myFont = QFont()
        myFont.setPointSize(15)

        for i in ts:
            triggerName = f"Trigger: {i[cv.trigger_event_name]} {i[cv.trigger_event_id]} {i[cv.trigger_receiver]}"
            item = QListWidgetItem(triggerName)
            item.setFont(myFont)
            self.list.addItem(item)


class MyPopup(QWidget):
    def __init__(self, rown, parentX, existingTrigger):
        QWidget.__init__(self)

        self.parentX = parentX

        self.setWindowTitle("Trigger")
        self.setWindowIcon(QIcon(cv.icon_path))

        self.layout = QGridLayout(self)

        #region labels
        self.eventName_label = QtWidgets.QLabel(self)
        self.eventName_label.setText('Event name:')
        self.eventName_label.setFixedSize(cv.gui_label_width, cv.gui_label_heigth)
        self.eventName_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.eventName_label, 1, 1, Qt.AlignCenter)

        self.eventID_label = QtWidgets.QLabel(self)
        self.eventID_label.setText('Event ID:')
        self.eventID_label.setFixedSize(cv.gui_label_width, cv.gui_label_heigth)
        self.eventID_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.eventID_label, 2, 1)

        self.receiver_label = QtWidgets.QLabel(self)
        self.receiver_label.setText('Receiver:')
        self.receiver_label.setFixedSize(cv.gui_label_width, cv.gui_label_heigth)
        self.receiver_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.receiver_label, 3, 1)
        #endregion labels

        #region lineedits
        self.eventName_textbox = QtWidgets.QLineEdit(self)
        self.eventName_textbox.setFixedSize(cv.gui_textbox_width, cv.gui_label_heigth)
        self.layout.addWidget(self.eventName_textbox, 1, 2)

        self.eventID_textbox = QtWidgets.QLineEdit(self)
        self.eventID_textbox.setFixedSize(cv.gui_textbox_width, cv.gui_label_heigth)
        self.layout.addWidget(self.eventID_textbox, 2, 2)

        self.receiver_textbox = QtWidgets.QLineEdit(self)
        self.receiver_textbox.setFixedSize(cv.gui_textbox_width, cv.gui_label_heigth)
        self.layout.addWidget(self.receiver_textbox, 3, 2)
        #endregion lineedits

        self.save_button = QtWidgets.QPushButton(self)
        self.save_button.setText("Save")
        self.save_button.setFixedSize(cv.gui_button_width, cv.gui_label_heigth)
        self.save_button.clicked.connect(lambda: self.saveTrigger(existingTrigger))
        self.layout.addWidget(self.save_button, 4, 1)

        self.delete_button = QtWidgets.QPushButton(self)
        self.delete_button.setText("Delete")
        self.delete_button.setFixedSize(cv.gui_button_width, cv.gui_label_heigth)
        self.delete_button.clicked.connect(lambda: self.deleteTrigger())
        self.layout.addWidget(self.delete_button, 4, 2)

        self.eventID = self.eventID_textbox.text()
        self.eventName = self.eventName_textbox.text()

        if existingTrigger:
            th = TriggerHandler()
            ts = th.getItems()
            t = ts[rown]
            self.eventName_textbox.setText(t[cv.trigger_event_name])
            self.eventID_textbox.setText(str(t[cv.trigger_event_id]))
            self.receiver_textbox.setText(t[cv.trigger_receiver])

            self.eventName = t[cv.trigger_event_name]
            self.eventID = t[cv.trigger_event_id]
            pass

    def saveTrigger(self, existingTrigger):
        input = self.getInput()

        if(not input[3]):
            return

        name = input[0]
        id = input[1]
        receiver = input[2]

        th = TriggerHandler()
        if existingTrigger:
            th.deleteATriggerItem(self.eventID, self.eventName)
        th.createATriggerItem(id, name, receiver)
        self.parentX.populate()
        self.close()

    def deleteTrigger(self):

        th = TriggerHandler()
        th.deleteATriggerItem(self.eventID, self.eventName)
        self.parentX.populate()
        self.close()

    def getInput(self):
        id = 0
        isValid = True

        try:
            id = int(self.eventID_textbox.text())
        except Exception as x:
            isValid = False

        name = self.eventName_textbox.text()
        if(len(name) == 0):
            isValid = False

        receiver = self.receiver_textbox.text()
        if(len(receiver) == 0):
            isValid = False

        if not isValid:
            self.blink()

        return name, id, receiver, isValid

    def blink(self):
        command1 = f"background-color: {cv.gui_color_1};"
        command2 = f"background-color: {cv.gui_color_2};"
        for x in range(3):
            self.eventID_textbox.setStyleSheet(command1)
            self.eventName_textbox.setStyleSheet(command1)
            self.receiver_textbox.setStyleSheet(command1)
            self.repaint()
            time.sleep(0.5)
            self.eventID_textbox.setStyleSheet(command2)
            self.eventName_textbox.setStyleSheet(command2)
            self.receiver_textbox.setStyleSheet(command2)
            self.repaint()
            time.sleep(0.5)










