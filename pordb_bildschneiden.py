# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_bildschneiden.ui'
#
# Created: Tue Nov  4 22:06:36 2014
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
        Dialog.resize(1244, 924)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("pypordb/8027068_splash.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.labelBild = QtGui.QLabel(Dialog)
        self.labelBild.setMinimumSize(QtCore.QSize(260, 260))
        self.labelBild.setWhatsThis(_fromUtf8(""))
        self.labelBild.setObjectName(_fromUtf8("labelBild"))
        self.vboxlayout.addWidget(self.labelBild)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.pushButtonNeuSpeichern = QtGui.QPushButton(Dialog)
        self.pushButtonNeuSpeichern.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("pypordb/media-floppy.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonNeuSpeichern.setIcon(icon1)
        self.pushButtonNeuSpeichern.setObjectName(_fromUtf8("pushButtonNeuSpeichern"))
        self.hboxlayout.addWidget(self.pushButtonNeuSpeichern)
        self.pushButtonNeuSpeichernAls = QtGui.QPushButton(Dialog)
        self.pushButtonNeuSpeichernAls.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("pypordb/document-save-as.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonNeuSpeichernAls.setIcon(icon2)
        self.pushButtonNeuSpeichernAls.setObjectName(_fromUtf8("pushButtonNeuSpeichernAls"))
        self.hboxlayout.addWidget(self.pushButtonNeuSpeichernAls)
        self.pushButtonNeuCancel = QtGui.QPushButton(Dialog)
        self.pushButtonNeuCancel.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("pypordb/dialog-cancel.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonNeuCancel.setIcon(icon3)
        self.pushButtonNeuCancel.setObjectName(_fromUtf8("pushButtonNeuCancel"))
        self.hboxlayout.addWidget(self.pushButtonNeuCancel)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.gridLayout.addLayout(self.vboxlayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Crop image", None))
        self.labelBild.setText(_translate("Dialog", "Image", None))
        self.pushButtonNeuSpeichern.setToolTip(_translate("Dialog", "<html><head/><body><p>Save</p></body></html>", None))
        self.pushButtonNeuSpeichernAls.setToolTip(_translate("Dialog", "<html><head/><body><p>Save as ...</p></body></html>", None))
        self.pushButtonNeuCancel.setToolTip(_translate("Dialog", "<html><head/><body><p>Cancel</p></body></html>", None))

