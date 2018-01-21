# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_bookmarks.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(675, 622)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pypordb/8027068_splash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonSpeichern = QtWidgets.QPushButton(Dialog)
        self.pushButtonSpeichern.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pypordb/media-floppy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSpeichern.setIcon(icon1)
        self.pushButtonSpeichern.setObjectName("pushButtonSpeichern")
        self.horizontalLayout.addWidget(self.pushButtonSpeichern)
        self.pushButtonAnzeigen = QtWidgets.QPushButton(Dialog)
        self.pushButtonAnzeigen.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("pypordb/appointment-recurring.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonAnzeigen.setIcon(icon2)
        self.pushButtonAnzeigen.setObjectName("pushButtonAnzeigen")
        self.horizontalLayout.addWidget(self.pushButtonAnzeigen)
        self.pushButtonLoeschen = QtWidgets.QPushButton(Dialog)
        self.pushButtonLoeschen.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("pypordb/user-trash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonLoeschen.setIcon(icon3)
        self.pushButtonLoeschen.setObjectName("pushButtonLoeschen")
        self.horizontalLayout.addWidget(self.pushButtonLoeschen)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidgetBookmarks = QtWidgets.QTableWidget(Dialog)
        self.tableWidgetBookmarks.setObjectName("tableWidgetBookmarks")
        self.tableWidgetBookmarks.setColumnCount(0)
        self.tableWidgetBookmarks.setRowCount(0)
        self.tableWidgetBookmarks.horizontalHeader().setVisible(True)
        self.verticalLayout.addWidget(self.tableWidgetBookmarks)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Bookmarks"))
        self.pushButtonSpeichern.setToolTip(_translate("Dialog", "Save actual site in bookmarks"))
        self.pushButtonAnzeigen.setToolTip(_translate("Dialog", "Show selected site"))
        self.pushButtonLoeschen.setToolTip(_translate("Dialog", "Delete site from bookmarks"))
        self.tableWidgetBookmarks.setSortingEnabled(True)

