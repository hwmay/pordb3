# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_land.ui'
#
# Created: Thu Oct  3 22:27:04 2013
#      by: PyQt4 UI code generator 4.9.6
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

class Ui_Landdialog(object):
    def setupUi(self, Landdialog):
        Landdialog.setObjectName(_fromUtf8("Landdialog"))
        Landdialog.resize(735, 905)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("pypordb/8027068_splash.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Landdialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Landdialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(Landdialog)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tableWidgetLaender = QtGui.QTableWidget(self.frame)
        self.tableWidgetLaender.setObjectName(_fromUtf8("tableWidgetLaender"))
        self.tableWidgetLaender.setColumnCount(4)
        self.tableWidgetLaender.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetLaender.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetLaender.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetLaender.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetLaender.setHorizontalHeaderItem(3, item)
        self.horizontalLayout_2.addWidget(self.tableWidgetLaender)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonLandSpeichern = QtGui.QPushButton(Landdialog)
        self.pushButtonLandSpeichern.setObjectName(_fromUtf8("pushButtonLandSpeichern"))
        self.horizontalLayout.addWidget(self.pushButtonLandSpeichern)
        self.pushButtonLandAbbrechen = QtGui.QPushButton(Landdialog)
        self.pushButtonLandAbbrechen.setObjectName(_fromUtf8("pushButtonLandAbbrechen"))
        self.horizontalLayout.addWidget(self.pushButtonLandAbbrechen)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Landdialog)
        QtCore.QMetaObject.connectSlotsByName(Landdialog)

    def retranslateUi(self, Landdialog):
        Landdialog.setWindowTitle(_translate("Landdialog", "Edit table of countries", None))
        self.tableWidgetLaender.setWhatsThis(_translate("Landdialog", "Here you can enter countries with their ISO codes and the corresponding nationality. By setting an \"X\" in column \"active\", this country will appear in the combo box on the actors tab and can be used for adding new actors.", None))
        item = self.tableWidgetLaender.horizontalHeaderItem(0)
        item.setText(_translate("Landdialog", "ISO Code", None))
        item = self.tableWidgetLaender.horizontalHeaderItem(1)
        item.setText(_translate("Landdialog", "Country", None))
        item = self.tableWidgetLaender.horizontalHeaderItem(2)
        item.setText(_translate("Landdialog", "active", None))
        item = self.tableWidgetLaender.horizontalHeaderItem(3)
        item.setText(_translate("Landdialog", "Nationality", None))
        self.pushButtonLandSpeichern.setText(_translate("Landdialog", "Save", None))
        self.pushButtonLandAbbrechen.setText(_translate("Landdialog", "Cancel", None))

