# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_darsteller_umbenennen.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(483, 121)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pypordb/8027068_splash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditNeuerName = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditNeuerName.setObjectName("lineEditNeuerName")
        self.horizontalLayout.addWidget(self.lineEditNeuerName)
        self.verticalLayout.addWidget(self.groupBox)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.pushButtonUmbenennen = QtWidgets.QPushButton(Dialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pypordb/umbenennen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonUmbenennen.setIcon(icon1)
        self.pushButtonUmbenennen.setObjectName("pushButtonUmbenennen")
        self.hboxlayout.addWidget(self.pushButtonUmbenennen)
        self.pushButtonCancel = QtWidgets.QPushButton(Dialog)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("pypordb/dialog-cancel.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonCancel.setIcon(icon2)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.hboxlayout.addWidget(self.pushButtonCancel)
        self.verticalLayout.addLayout(self.hboxlayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Enter new name"))
        self.groupBox.setTitle(_translate("Dialog", "New name:"))
        self.pushButtonUmbenennen.setText(_translate("Dialog", "Rename"))
        self.pushButtonCancel.setText(_translate("Dialog", "Cancel"))

