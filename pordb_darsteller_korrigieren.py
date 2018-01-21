# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_darsteller_korrigieren.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Darstellerkorrigieren(object):
    def setupUi(self, Darstellerkorrigieren):
        Darstellerkorrigieren.setObjectName("Darstellerkorrigieren")
        Darstellerkorrigieren.resize(696, 788)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pypordb/8027068_splash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Darstellerkorrigieren.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Darstellerkorrigieren)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Darstellerkorrigieren)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableWidgetDarsteller = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidgetDarsteller.setMinimumSize(QtCore.QSize(672, 0))
        self.tableWidgetDarsteller.setObjectName("tableWidgetDarsteller")
        self.tableWidgetDarsteller.setColumnCount(0)
        self.tableWidgetDarsteller.setRowCount(0)
        self.horizontalLayout_3.addWidget(self.tableWidgetDarsteller)
        self.verticalLayout.addWidget(self.groupBox)
        self.label_3 = QtWidgets.QLabel(Darstellerkorrigieren)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.groupBox_2 = QtWidgets.QGroupBox(Darstellerkorrigieren)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEditFilter = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditFilter.setObjectName("lineEditFilter")
        self.horizontalLayout_2.addWidget(self.lineEditFilter)
        self.comboBoxGeschlecht = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBoxGeschlecht.setObjectName("comboBoxGeschlecht")
        self.comboBoxGeschlecht.addItem("")
        self.comboBoxGeschlecht.setItemText(0, "")
        self.comboBoxGeschlecht.addItem("")
        self.comboBoxGeschlecht.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBoxGeschlecht)
        self.pushButtonSuchen = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButtonSuchen.setAutoDefault(False)
        self.pushButtonSuchen.setObjectName("pushButtonSuchen")
        self.horizontalLayout_2.addWidget(self.pushButtonSuchen)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(Darstellerkorrigieren)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tableWidgetDarstellerGefunden = QtWidgets.QTableWidget(self.groupBox_3)
        self.tableWidgetDarstellerGefunden.setMinimumSize(QtCore.QSize(672, 0))
        self.tableWidgetDarstellerGefunden.setObjectName("tableWidgetDarstellerGefunden")
        self.tableWidgetDarstellerGefunden.setColumnCount(0)
        self.tableWidgetDarstellerGefunden.setRowCount(0)
        self.horizontalLayout_4.addWidget(self.tableWidgetDarstellerGefunden)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonUebernehmen = QtWidgets.QPushButton(Darstellerkorrigieren)
        self.pushButtonUebernehmen.setAutoDefault(True)
        self.pushButtonUebernehmen.setDefault(True)
        self.pushButtonUebernehmen.setFlat(False)
        self.pushButtonUebernehmen.setObjectName("pushButtonUebernehmen")
        self.horizontalLayout.addWidget(self.pushButtonUebernehmen)
        self.pushButtonAbbrechen = QtWidgets.QPushButton(Darstellerkorrigieren)
        self.pushButtonAbbrechen.setAutoDefault(False)
        self.pushButtonAbbrechen.setObjectName("pushButtonAbbrechen")
        self.horizontalLayout.addWidget(self.pushButtonAbbrechen)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Darstellerkorrigieren)
        QtCore.QMetaObject.connectSlotsByName(Darstellerkorrigieren)
        Darstellerkorrigieren.setTabOrder(self.lineEditFilter, self.comboBoxGeschlecht)
        Darstellerkorrigieren.setTabOrder(self.comboBoxGeschlecht, self.pushButtonSuchen)
        Darstellerkorrigieren.setTabOrder(self.pushButtonSuchen, self.pushButtonUebernehmen)
        Darstellerkorrigieren.setTabOrder(self.pushButtonUebernehmen, self.tableWidgetDarsteller)
        Darstellerkorrigieren.setTabOrder(self.tableWidgetDarsteller, self.tableWidgetDarstellerGefunden)

    def retranslateUi(self, Darstellerkorrigieren):
        _translate = QtCore.QCoreApplication.translate
        Darstellerkorrigieren.setWindowTitle(_translate("Darstellerkorrigieren", "Change actor"))
        self.groupBox.setTitle(_translate("Darstellerkorrigieren", "Actor"))
        self.label_3.setText(_translate("Darstellerkorrigieren", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">Caution: search is case sensitive</span></p></body></html>"))
        self.groupBox_2.setTitle(_translate("Darstellerkorrigieren", "Filter"))
        self.lineEditFilter.setToolTip(_translate("Darstellerkorrigieren", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Part of the name</p></body></html>"))
        self.comboBoxGeschlecht.setToolTip(_translate("Darstellerkorrigieren", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Gender</p></body></html>"))
        self.comboBoxGeschlecht.setItemText(1, _translate("Darstellerkorrigieren", "Female"))
        self.comboBoxGeschlecht.setItemText(2, _translate("Darstellerkorrigieren", "Male"))
        self.pushButtonSuchen.setText(_translate("Darstellerkorrigieren", "Search"))
        self.groupBox_3.setTitle(_translate("Darstellerkorrigieren", "Actors found"))
        self.pushButtonUebernehmen.setText(_translate("Darstellerkorrigieren", "Adopt"))
        self.pushButtonUebernehmen.setShortcut(_translate("Darstellerkorrigieren", "Return"))
        self.pushButtonAbbrechen.setText(_translate("Darstellerkorrigieren", "Cancel"))

