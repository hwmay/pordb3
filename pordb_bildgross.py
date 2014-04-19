# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_bildgross.ui'
#
# Created: Sat Apr 19 22:48:21 2014
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
        Dialog.resize(1271, 961)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("pypordb/8027068_splash.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.hboxlayout = QtGui.QHBoxLayout(Dialog)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelBildgross = QtGui.QLabel(Dialog)
        self.labelBildgross.setObjectName(_fromUtf8("labelBildgross"))
        self.horizontalLayout.addWidget(self.labelBildgross)
        self.hboxlayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "PorDB3", None))
        self.labelBildgross.setText(_translate("Dialog", "TextLabel", None))

