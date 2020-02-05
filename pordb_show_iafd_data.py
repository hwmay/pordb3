# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_show_iafd_data.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1160, 611)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pypordb/8027068_splash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonOK = QtWidgets.QPushButton(Dialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pypordb/add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonOK.setIcon(icon1)
        self.pushButtonOK.setDefault(True)
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.horizontalLayout.addWidget(self.pushButtonOK)
        self.pushButtonSelectAll = QtWidgets.QPushButton(Dialog)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("pypordb/select-all.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSelectAll.setIcon(icon2)
        self.pushButtonSelectAll.setObjectName("pushButtonSelectAll")
        self.horizontalLayout.addWidget(self.pushButtonSelectAll)
        self.pushButtonCancel = QtWidgets.QPushButton(Dialog)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("pypordb/cancel.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonCancel.setIcon(icon3)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Select items for adding a new scene"))
        self.graphicsView.setWhatsThis(_translate("Dialog", "<html><head/><body><p>For adding a scene mark the scene at the left of this window and the involved actors, then press the &quot;add scene&quot; button.</p></body></html>"))
        self.pushButtonOK.setText(_translate("Dialog", "Add scene, Enter"))
        self.pushButtonSelectAll.setText(_translate("Dialog", "Select all, Ctrl+A"))
        self.pushButtonSelectAll.setShortcut(_translate("Dialog", "Ctrl+A"))
        self.pushButtonCancel.setText(_translate("Dialog", "Cancel, Esc"))


