# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_historie.ui'
#
# Created: Mon Nov  3 00:02:55 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(903, 754)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("pypordb/8027068_splash.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableWidgetHistory = QtGui.QTableWidget(Dialog)
        self.tableWidgetHistory.setObjectName(_fromUtf8("tableWidgetHistory"))
        self.tableWidgetHistory.setColumnCount(3)
        self.tableWidgetHistory.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetHistory.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetHistory.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetHistory.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.tableWidgetHistory)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEditSearch = QtGui.QLineEdit(Dialog)
        self.lineEditSearch.setMinimumSize(QtCore.QSize(500, 0))
        self.lineEditSearch.setObjectName(_fromUtf8("lineEditSearch"))
        self.horizontalLayout.addWidget(self.lineEditSearch)
        self.pushButtonSearch = QtGui.QPushButton(Dialog)
        self.pushButtonSearch.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("pypordb/suchen.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSearch.setIcon(icon1)
        self.pushButtonSearch.setAutoDefault(False)
        self.pushButtonSearch.setObjectName(_fromUtf8("pushButtonSearch"))
        self.horizontalLayout.addWidget(self.pushButtonSearch)
        spacerItem = QtGui.QSpacerItem(668, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonGo = QtGui.QPushButton(Dialog)
        self.pushButtonGo.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("pypordb/application-x-executable.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonGo.setIcon(icon2)
        self.pushButtonGo.setObjectName(_fromUtf8("pushButtonGo"))
        self.horizontalLayout.addWidget(self.pushButtonGo)
        self.pushButtonAbbrechen = QtGui.QPushButton(Dialog)
        self.pushButtonAbbrechen.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("pypordb/dialog-cancel.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonAbbrechen.setIcon(icon3)
        self.pushButtonAbbrechen.setAutoDefault(False)
        self.pushButtonAbbrechen.setObjectName(_fromUtf8("pushButtonAbbrechen"))
        self.horizontalLayout.addWidget(self.pushButtonAbbrechen)
        self.pushButtonClear = QtGui.QPushButton(Dialog)
        self.pushButtonClear.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("pypordb/user-trash.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonClear.setIcon(icon4)
        self.pushButtonClear.setObjectName(_fromUtf8("pushButtonClear"))
        self.horizontalLayout.addWidget(self.pushButtonClear)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "History", None))
        self.tableWidgetHistory.setWhatsThis(_translate("Dialog", "Here you see your last search command. You can repeat one search by marking the line and click on execute.", None))
        self.tableWidgetHistory.setSortingEnabled(True)
        item = self.tableWidgetHistory.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Select", None))
        item = self.tableWidgetHistory.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Command", None))
        item = self.tableWidgetHistory.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Timestamp", None))
        self.pushButtonSearch.setToolTip(_translate("Dialog", "Search in history, Ctrl+S", None))
        self.pushButtonSearch.setShortcut(_translate("Dialog", "Ctrl+S", None))
        self.pushButtonGo.setToolTip(_translate("Dialog", "Execute marked line", None))
        self.pushButtonAbbrechen.setToolTip(_translate("Dialog", "<html><head/><body><p>Cancel</p></body></html>", None))
        self.pushButtonClear.setToolTip(_translate("Dialog", "<html><head/><body><p>Clear history: delete all entries except for the last 50 entries, ctrl+delete</p></body></html>", None))
        self.pushButtonClear.setShortcut(_translate("Dialog", "Ctrl+Del", None))

