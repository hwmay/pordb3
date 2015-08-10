# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_darsteller_umbenennen.ui'
#
# Created: Mon Aug 10 20:02:11 2015
#      by: PyQt4 UI code generator 4.11.3
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
        Dialog.resize(483, 121)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("pypordb/8027068_splash.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEditNeuerName = QtGui.QLineEdit(self.groupBox)
        self.lineEditNeuerName.setObjectName(_fromUtf8("lineEditNeuerName"))
        self.horizontalLayout.addWidget(self.lineEditNeuerName)
        self.verticalLayout.addWidget(self.groupBox)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.pushButtonUmbenennen = QtGui.QPushButton(Dialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("pypordb/umbenennen.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonUmbenennen.setIcon(icon1)
        self.pushButtonUmbenennen.setObjectName(_fromUtf8("pushButtonUmbenennen"))
        self.hboxlayout.addWidget(self.pushButtonUmbenennen)
        self.pushButtonCancel = QtGui.QPushButton(Dialog)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("pypordb/dialog-cancel.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonCancel.setIcon(icon2)
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))
        self.hboxlayout.addWidget(self.pushButtonCancel)
        self.verticalLayout.addLayout(self.hboxlayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Enter new name", None))
        self.groupBox.setTitle(_translate("Dialog", "New name:", None))
        self.pushButtonUmbenennen.setText(_translate("Dialog", "Rename", None))
        self.pushButtonCancel.setText(_translate("Dialog", "Cancel", None))

