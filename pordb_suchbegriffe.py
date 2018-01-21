# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_suchbegriffe.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Suchbegriffedialog(object):
    def setupUi(self, Suchbegriffedialog):
        Suchbegriffedialog.setObjectName("Suchbegriffedialog")
        Suchbegriffedialog.resize(735, 905)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pypordb/8027068_splash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Suchbegriffedialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Suchbegriffedialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Suchbegriffedialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidgetSuche = QtWidgets.QTableWidget(self.frame)
        self.tableWidgetSuche.setObjectName("tableWidgetSuche")
        self.tableWidgetSuche.setColumnCount(2)
        self.tableWidgetSuche.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetSuche.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetSuche.setHorizontalHeaderItem(1, item)
        self.horizontalLayout_2.addWidget(self.tableWidgetSuche)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonLandSpeichern = QtWidgets.QPushButton(Suchbegriffedialog)
        self.pushButtonLandSpeichern.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pypordb/media-floppy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonLandSpeichern.setIcon(icon1)
        self.pushButtonLandSpeichern.setObjectName("pushButtonLandSpeichern")
        self.horizontalLayout.addWidget(self.pushButtonLandSpeichern)
        self.pushButtonLandAbbrechen = QtWidgets.QPushButton(Suchbegriffedialog)
        self.pushButtonLandAbbrechen.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("pypordb/dialog-cancel.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonLandAbbrechen.setIcon(icon2)
        self.pushButtonLandAbbrechen.setObjectName("pushButtonLandAbbrechen")
        self.horizontalLayout.addWidget(self.pushButtonLandAbbrechen)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Suchbegriffedialog)
        QtCore.QMetaObject.connectSlotsByName(Suchbegriffedialog)

    def retranslateUi(self, Suchbegriffedialog):
        _translate = QtCore.QCoreApplication.translate
        Suchbegriffedialog.setWindowTitle(_translate("Suchbegriffedialog", "Edit search items"))
        self.tableWidgetSuche.setWhatsThis(_translate("Suchbegriffedialog", "Here you can enter synomyms for searching, e. g. \"18\" and \"eighteen\". When you enter \"18\", search will not only look for \"18\", but also for \"eighteen\". Be very careful with this function for avoiding long searchs with a lot of results."))
        item = self.tableWidgetSuche.horizontalHeaderItem(0)
        item.setText(_translate("Suchbegriffedialog", "search item"))
        item = self.tableWidgetSuche.horizontalHeaderItem(1)
        item.setText(_translate("Suchbegriffedialog", "Alternative"))
        self.pushButtonLandSpeichern.setToolTip(_translate("Suchbegriffedialog", "<html><head/><body><p>Save</p></body></html>"))
        self.pushButtonLandAbbrechen.setToolTip(_translate("Suchbegriffedialog", "<html><head/><body><p>Cancel</p></body></html>"))

