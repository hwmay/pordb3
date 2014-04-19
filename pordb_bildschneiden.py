# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_bildschneiden.ui'
#
# Created: Tue Mar 13 22:32:19 2012
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1244, 924)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pypordb/8027068_splash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setObjectName("vboxlayout")
        self.labelBild = QtGui.QLabel(Dialog)
        self.labelBild.setMinimumSize(QtCore.QSize(260, 260))
        self.labelBild.setWhatsThis("")
        self.labelBild.setObjectName("labelBild")
        self.vboxlayout.addWidget(self.labelBild)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.pushButtonNeuSpeichern = QtGui.QPushButton(Dialog)
        self.pushButtonNeuSpeichern.setObjectName("pushButtonNeuSpeichern")
        self.hboxlayout.addWidget(self.pushButtonNeuSpeichern)
        self.pushButtonNeuSpeichernAls = QtGui.QPushButton(Dialog)
        self.pushButtonNeuSpeichernAls.setObjectName("pushButtonNeuSpeichernAls")
        self.hboxlayout.addWidget(self.pushButtonNeuSpeichernAls)
        self.pushButtonNeuCancel = QtGui.QPushButton(Dialog)
        self.pushButtonNeuCancel.setObjectName("pushButtonNeuCancel")
        self.hboxlayout.addWidget(self.pushButtonNeuCancel)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.gridLayout.addLayout(self.vboxlayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Crop image", None, QtGui.QApplication.UnicodeUTF8))
        self.labelBild.setText(QtGui.QApplication.translate("Dialog", "Image", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonNeuSpeichern.setText(QtGui.QApplication.translate("Dialog", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonNeuSpeichernAls.setText(QtGui.QApplication.translate("Dialog", "Save as ...", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonNeuCancel.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

