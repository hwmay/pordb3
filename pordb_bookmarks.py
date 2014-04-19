# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_bookmarks.ui'
#
# Created: Sat Nov  2 22:04:55 2013
#      by: PyQt4 UI code generator 4.9.6
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
        Dialog.resize(675, 622)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("pypordb/8027068_splash.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonSpeichern = QtGui.QPushButton(Dialog)
        self.pushButtonSpeichern.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("pypordb/media-floppy.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSpeichern.setIcon(icon1)
        self.pushButtonSpeichern.setObjectName(_fromUtf8("pushButtonSpeichern"))
        self.horizontalLayout.addWidget(self.pushButtonSpeichern)
        self.pushButtonAnzeigen = QtGui.QPushButton(Dialog)
        self.pushButtonAnzeigen.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("pypordb/appointment-recurring.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonAnzeigen.setIcon(icon2)
        self.pushButtonAnzeigen.setObjectName(_fromUtf8("pushButtonAnzeigen"))
        self.horizontalLayout.addWidget(self.pushButtonAnzeigen)
        self.pushButtonLoeschen = QtGui.QPushButton(Dialog)
        self.pushButtonLoeschen.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("pypordb/user-trash.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonLoeschen.setIcon(icon3)
        self.pushButtonLoeschen.setObjectName(_fromUtf8("pushButtonLoeschen"))
        self.horizontalLayout.addWidget(self.pushButtonLoeschen)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidgetBookmarks = QtGui.QTableWidget(Dialog)
        self.tableWidgetBookmarks.setObjectName(_fromUtf8("tableWidgetBookmarks"))
        self.tableWidgetBookmarks.setColumnCount(0)
        self.tableWidgetBookmarks.setRowCount(0)
        self.tableWidgetBookmarks.horizontalHeader().setVisible(True)
        self.verticalLayout.addWidget(self.tableWidgetBookmarks)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Bookmarks", None))
        self.pushButtonSpeichern.setToolTip(_translate("Dialog", "Save actual site in bookmarks", None))
        self.pushButtonAnzeigen.setToolTip(_translate("Dialog", "Show selected site", None))
        self.pushButtonLoeschen.setToolTip(_translate("Dialog", "Delete site from bookmarks", None))
        self.tableWidgetBookmarks.setSortingEnabled(True)

