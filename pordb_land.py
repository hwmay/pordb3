# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_land.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Landdialog(object):
    def setupUi(self, Landdialog):
        Landdialog.setObjectName("Landdialog")
        Landdialog.resize(735, 905)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pypordb/8027068_splash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Landdialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Landdialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Landdialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidgetLaender = QtWidgets.QTableWidget(self.frame)
        self.tableWidgetLaender.setObjectName("tableWidgetLaender")
        self.tableWidgetLaender.setColumnCount(5)
        self.tableWidgetLaender.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetLaender.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetLaender.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetLaender.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetLaender.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetLaender.setHorizontalHeaderItem(4, item)
        self.horizontalLayout_2.addWidget(self.tableWidgetLaender)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonLandSpeichern = QtWidgets.QPushButton(Landdialog)
        self.pushButtonLandSpeichern.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pypordb/media-floppy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonLandSpeichern.setIcon(icon1)
        self.pushButtonLandSpeichern.setObjectName("pushButtonLandSpeichern")
        self.horizontalLayout.addWidget(self.pushButtonLandSpeichern)
        self.pushButtonLandAbbrechen = QtWidgets.QPushButton(Landdialog)
        self.pushButtonLandAbbrechen.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("pypordb/dialog-cancel.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonLandAbbrechen.setIcon(icon2)
        self.pushButtonLandAbbrechen.setObjectName("pushButtonLandAbbrechen")
        self.horizontalLayout.addWidget(self.pushButtonLandAbbrechen)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Landdialog)
        QtCore.QMetaObject.connectSlotsByName(Landdialog)

    def retranslateUi(self, Landdialog):
        _translate = QtCore.QCoreApplication.translate
        Landdialog.setWindowTitle(_translate("Landdialog", "Edit table of countries"))
        self.tableWidgetLaender.setWhatsThis(_translate("Landdialog", "Here you can enter countries with their ISO codes and the corresponding nationality. By setting an \"X\" in column \"active\", this country will appear in the combo box on the actors tab and can be used for adding new actors."))
        self.tableWidgetLaender.setSortingEnabled(True)
        item = self.tableWidgetLaender.horizontalHeaderItem(0)
        item.setText(_translate("Landdialog", "Flag"))
        item = self.tableWidgetLaender.horizontalHeaderItem(1)
        item.setText(_translate("Landdialog", "ISO Code"))
        item = self.tableWidgetLaender.horizontalHeaderItem(2)
        item.setText(_translate("Landdialog", "Country"))
        item = self.tableWidgetLaender.horizontalHeaderItem(3)
        item.setText(_translate("Landdialog", "active"))
        item = self.tableWidgetLaender.horizontalHeaderItem(4)
        item.setText(_translate("Landdialog", "Nationality"))
        self.pushButtonLandSpeichern.setToolTip(_translate("Landdialog", "<html><head/><body><p>Save</p></body></html>"))
        self.pushButtonLandAbbrechen.setToolTip(_translate("Landdialog", "<html><head/><body><p>Cancel</p></body></html>"))

