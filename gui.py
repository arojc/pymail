import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot, Qt, QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget, QPushButton, QGridLayout, \
    QHBoxLayout, QListWidget, QListWidgetItem
from PyQt5.QtGui import QIcon, QPainter, QFont
from PyQt5.uic.Compiler.qtproxies import QtCore

from TriggerHandler import TriggerHandler
from common_variables import common_variables
from email_sender import email_sender
from qtwidgets import PasswordEdit

from XMLHandler import XMLHandler


class gui(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setToolTip("EventReader")
        self.setWindowIcon(QIcon("icons/caretronic_logo.jpg"))
        self.setWindowTitle(common_variables.top_left_text)

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
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

class SettingsTab(QWidget):

    def __init__(self, parent):

        super(QWidget, self).__init__(parent)

        es = email_sender()
        settings = es.get_settings()
        cv = common_variables()

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
        self.sender_textbox.setText(settings[cv.es_sender])
        self.sender_textbox.setFixedSize(common_variables.gui_textbox_width, common_variables.gui_label_heigth)
        self.layout.addWidget(self.sender_textbox, 1, 2)

        self.receiver_textbox = QtWidgets.QLineEdit(self)
        self.receiver_textbox.setText(settings[cv.es_receiver])
        self.receiver_textbox.setFixedSize(common_variables.gui_textbox_width, common_variables.gui_label_heigth)
        self.layout.addWidget(self.receiver_textbox, 2, 2)

        self.password_textbox = PasswordEdit(self)
        self.password_textbox.setText(settings[cv.es_password])
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

        self.list = QListWidget()

        #region populate
        # th = TriggerHandler()
        # ts = th.getTriggers()
        #
        # self.list = QListWidget()
        #
        # x = QWidget()
        #
        # myFont = QFont()
        # myFont.setPointSize(15)
        #
        # for i in ts:
        #     triggerName = f"Trigger: {i['EventName']} {i['EventID']}"
        #     item = QListWidgetItem(triggerName, self.list)
        #     item.setSizeHint(QSize(0, 30))
        #     item.setFont(myFont)
        #     self.list.setItemWidget(item, x)
        #endregion populate

        self.layout1 = QVBoxLayout()
        self.layout2 = QHBoxLayout()

        self.populate()
        self.list.itemClicked.connect(self.onItemClicked)

        # self.list.itemClicked.connect(self.onItemClicked)

        self.layout1.addWidget(self.list)

        #region Add button
        self.add_button = QtWidgets.QPushButton(self)
        self.add_button.setText("Add")
        self.add_button.clicked.connect(self.onAddButtonClicked)
        self.layout2.addWidget(self.add_button)
        #endregion Add button

        # #region Delete button
        # self.delete_button = QtWidgets.QPushButton(self)
        # self.delete_button.setText("Delete")
        # self.delete_button.clicked.connect(self.onItemClicked)
        # self.layout2.addWidget(self.delete_button)
        # #endregion Delete button
        #
        # #region Edit button
        # self.edit_button = QtWidgets.QPushButton(self)
        # self.edit_button.setText("Edit")
        # self.edit_button.clicked.connect(self.onItemClicked)
        # self.layout2.addWidget(self.edit_button)
        # #endregion Edit button

        self.layout1.addLayout(self.layout2)

        self.setLayout(self.layout1)

    def onItemClicked(self, item):

        RowId = self.list.currentRow()

        self.m = MyPopup(RowId, self, True)
        self.m.show()

    def onAddButtonClicked(self):

        RowId = self.list.currentRow()

        self.m = MyPopup(RowId, self, False)
        self.m.show()

    def populate(self):
        th = TriggerHandler()
        ts = th.getTriggers()

        self.list.clear()

        myFont = QFont()
        myFont.setPointSize(15)

        for i in ts:
            triggerName = f"Trigger: {i['EventName']} {i['EventID']}"
            self.list.addItem(triggerName)

        #self.list.itemClicked.connect(self.onItemClicked)


    def populate1(self, id, name):
        triggerName = f"Trigger: {id} {name}"
        self.list.addItem(triggerName)

    def populate2(self, id, name):
        selItems = self.list.selectedItems()
        for i in selItems:
            self.list.takeItem(self.list.row(i))

class MyPopup(QWidget):
    def __init__(self, rown, parentX, insertValues):
        QWidget.__init__(self)

        self.parentX = parentX

        self.setWindowTitle("Trigger")
        self.setWindowIcon(QIcon("icons/caretronic_logo.jpg"))

        self.layout = QGridLayout(self)

        #region labels
        self.eventName_label = QtWidgets.QLabel(self)
        self.eventName_label.setText('Event name:')
        self.eventName_label.setFixedSize(common_variables.gui_label_width, common_variables.gui_label_heigth)
        self.eventName_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.eventName_label, 1, 1, Qt.AlignCenter)

        self.eventID_label = QtWidgets.QLabel(self)
        self.eventID_label.setText('Event ID:')
        self.eventID_label.setFixedSize(common_variables.gui_label_width, common_variables.gui_label_heigth)
        self.eventID_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.eventID_label, 2, 1)
        #endregion labels

        #region lineedits
        self.eventName_textbox = QtWidgets.QLineEdit(self)
        self.eventName_textbox.setFixedSize(common_variables.gui_textbox_width, common_variables.gui_label_heigth)
        self.layout.addWidget(self.eventName_textbox, 1, 2)

        self.eventID_textbox = QtWidgets.QLineEdit(self)
        self.eventID_textbox.setFixedSize(common_variables.gui_textbox_width, common_variables.gui_label_heigth)
        self.layout.addWidget(self.eventID_textbox, 2, 2)
        #endregion lineedits

        self.save_button = QtWidgets.QPushButton(self)
        self.save_button.setText("Save")
        self.save_button.setFixedSize(common_variables.gui_button_width, common_variables.gui_label_heigth)
        self.save_button.clicked.connect(lambda: self.saveTrigger(self.eventID_textbox.text(), self.eventName_textbox.text()))
        self.layout.addWidget(self.save_button, 4, 1)

        self.delete_button = QtWidgets.QPushButton(self)
        self.delete_button.setText("Delete")
        self.delete_button.setFixedSize(common_variables.gui_button_width, common_variables.gui_label_heigth)
        self.delete_button.clicked.connect(lambda: self.deleteTrigger(self.eventID_textbox.text(), self.eventName_textbox.text()))
        self.layout.addWidget(self.delete_button, 4, 2)

        self.eventID = self.eventID_textbox.text()
        self.eventName = self.eventName_textbox.text()

        if insertValues:
            th = TriggerHandler()
            ts = th.getTriggers()
            t = ts[rown]
            self.eventName_textbox.setText(t["EventName"])
            self.eventID_textbox.setText(str(t["EventID"]))

    def saveTrigger(self, id, name):
        th = TriggerHandler()
        th.deleteATrigger(self.eventID, self.eventName)
        th.createATrigger(id, name)
        self.parentX.populate()
        self.close()

    def deleteTrigger(self, id, name):
        th = TriggerHandler()
        th.deleteATrigger(id, name)
        self.parentX.populate()
        self.close()










