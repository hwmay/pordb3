# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_bildgross.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1271, 961)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pypordb/8027068_splash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.hboxlayout = QtWidgets.QHBoxLayout(Dialog)
        self.hboxlayout.setObjectName("hboxlayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelBildgross = QtWidgets.QLabel(Dialog)
        self.labelBildgross.setObjectName("labelBildgross")
        self.horizontalLayout.addWidget(self.labelBildgross)
        self.hboxlayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PorDB3"))
        self.labelBildgross.setText(_translate("Dialog", "TextLabel"))

