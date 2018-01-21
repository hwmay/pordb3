# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_bildschneiden.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1244, 924)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pypordb/8027068_splash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.vboxlayout = QtWidgets.QVBoxLayout()
        self.vboxlayout.setObjectName("vboxlayout")
        self.labelBild = QtWidgets.QLabel(Dialog)
        self.labelBild.setMinimumSize(QtCore.QSize(260, 260))
        self.labelBild.setWhatsThis("")
        self.labelBild.setObjectName("labelBild")
        self.vboxlayout.addWidget(self.labelBild)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.pushButtonNeuSpeichern = QtWidgets.QPushButton(Dialog)
        self.pushButtonNeuSpeichern.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pypordb/media-floppy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonNeuSpeichern.setIcon(icon1)
        self.pushButtonNeuSpeichern.setObjectName("pushButtonNeuSpeichern")
        self.hboxlayout.addWidget(self.pushButtonNeuSpeichern)
        self.pushButtonNeuSpeichernAls = QtWidgets.QPushButton(Dialog)
        self.pushButtonNeuSpeichernAls.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("pypordb/document-save-as.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonNeuSpeichernAls.setIcon(icon2)
        self.pushButtonNeuSpeichernAls.setObjectName("pushButtonNeuSpeichernAls")
        self.hboxlayout.addWidget(self.pushButtonNeuSpeichernAls)
        self.pushButtonNeuCancel = QtWidgets.QPushButton(Dialog)
        self.pushButtonNeuCancel.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("pypordb/dialog-cancel.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonNeuCancel.setIcon(icon3)
        self.pushButtonNeuCancel.setObjectName("pushButtonNeuCancel")
        self.hboxlayout.addWidget(self.pushButtonNeuCancel)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.gridLayout.addLayout(self.vboxlayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Crop image"))
        self.labelBild.setText(_translate("Dialog", "Image"))
        self.pushButtonNeuSpeichern.setToolTip(_translate("Dialog", "<html><head/><body><p>Save</p></body></html>"))
        self.pushButtonNeuSpeichernAls.setToolTip(_translate("Dialog", "<html><head/><body><p>Save as ...</p></body></html>"))
        self.pushButtonNeuCancel.setToolTip(_translate("Dialog", "<html><head/><body><p>Cancel</p></body></html>"))

