# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_darsteller_umbenennen.ui'
#
# Created: Tue Mar 13 22:32:20 2012
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(483, 121)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pypordb/8027068_splash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditNeuerName = QtGui.QLineEdit(self.groupBox)
        self.lineEditNeuerName.setObjectName("lineEditNeuerName")
        self.horizontalLayout.addWidget(self.lineEditNeuerName)
        self.verticalLayout.addWidget(self.groupBox)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.pushButtonUmbenennen = QtGui.QPushButton(Dialog)
        self.pushButtonUmbenennen.setObjectName("pushButtonUmbenennen")
        self.hboxlayout.addWidget(self.pushButtonUmbenennen)
        self.pushButtonCancel = QtGui.QPushButton(Dialog)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.hboxlayout.addWidget(self.pushButtonCancel)
        self.verticalLayout.addLayout(self.hboxlayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Enter new name", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "New name:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonUmbenennen.setText(QtGui.QApplication.translate("Dialog", "Rename", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancel.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

