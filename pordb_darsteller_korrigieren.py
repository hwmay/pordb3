# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_darsteller_korrigieren.ui'
#
# Created: Sun Mar 17 15:27:08 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Darstellerkorrigieren(object):
    def setupUi(self, Darstellerkorrigieren):
        Darstellerkorrigieren.setObjectName(_fromUtf8("Darstellerkorrigieren"))
        Darstellerkorrigieren.resize(696, 788)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("pypordb/8027068_splash.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Darstellerkorrigieren.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Darstellerkorrigieren)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Darstellerkorrigieren)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.tableWidgetDarsteller = QtGui.QTableWidget(self.groupBox)
        self.tableWidgetDarsteller.setMinimumSize(QtCore.QSize(672, 0))
        self.tableWidgetDarsteller.setObjectName(_fromUtf8("tableWidgetDarsteller"))
        self.tableWidgetDarsteller.setColumnCount(0)
        self.tableWidgetDarsteller.setRowCount(0)
        self.horizontalLayout_3.addWidget(self.tableWidgetDarsteller)
        self.verticalLayout.addWidget(self.groupBox)
        self.label_3 = QtGui.QLabel(Darstellerkorrigieren)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.groupBox_2 = QtGui.QGroupBox(Darstellerkorrigieren)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEditFilter = QtGui.QLineEdit(self.groupBox_2)
        self.lineEditFilter.setObjectName(_fromUtf8("lineEditFilter"))
        self.horizontalLayout_2.addWidget(self.lineEditFilter)
        self.comboBoxGeschlecht = QtGui.QComboBox(self.groupBox_2)
        self.comboBoxGeschlecht.setObjectName(_fromUtf8("comboBoxGeschlecht"))
        self.comboBoxGeschlecht.addItem(_fromUtf8(""))
        self.comboBoxGeschlecht.setItemText(0, _fromUtf8(""))
        self.comboBoxGeschlecht.addItem(_fromUtf8(""))
        self.comboBoxGeschlecht.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.comboBoxGeschlecht)
        self.pushButtonSuchen = QtGui.QPushButton(self.groupBox_2)
        self.pushButtonSuchen.setAutoDefault(False)
        self.pushButtonSuchen.setObjectName(_fromUtf8("pushButtonSuchen"))
        self.horizontalLayout_2.addWidget(self.pushButtonSuchen)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(Darstellerkorrigieren)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.tableWidgetDarstellerGefunden = QtGui.QTableWidget(self.groupBox_3)
        self.tableWidgetDarstellerGefunden.setObjectName(_fromUtf8("tableWidgetDarstellerGefunden"))
        self.tableWidgetDarstellerGefunden.setColumnCount(0)
        self.tableWidgetDarstellerGefunden.setRowCount(0)
        self.horizontalLayout_4.addWidget(self.tableWidgetDarstellerGefunden)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonUebernehmen = QtGui.QPushButton(Darstellerkorrigieren)
        self.pushButtonUebernehmen.setAutoDefault(True)
        self.pushButtonUebernehmen.setDefault(True)
        self.pushButtonUebernehmen.setFlat(False)
        self.pushButtonUebernehmen.setObjectName(_fromUtf8("pushButtonUebernehmen"))
        self.horizontalLayout.addWidget(self.pushButtonUebernehmen)
        self.pushButtonAbbrechen = QtGui.QPushButton(Darstellerkorrigieren)
        self.pushButtonAbbrechen.setAutoDefault(False)
        self.pushButtonAbbrechen.setObjectName(_fromUtf8("pushButtonAbbrechen"))
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
        Darstellerkorrigieren.setWindowTitle(QtGui.QApplication.translate("Darstellerkorrigieren", "Change actor", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Darstellerkorrigieren", "Actor", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Darstellerkorrigieren", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">Caution: case sensitive</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Darstellerkorrigieren", "Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditFilter.setToolTip(QtGui.QApplication.translate("Darstellerkorrigieren", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Part of the name</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxGeschlecht.setToolTip(QtGui.QApplication.translate("Darstellerkorrigieren", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Gender</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxGeschlecht.setItemText(1, QtGui.QApplication.translate("Darstellerkorrigieren", "Female", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxGeschlecht.setItemText(2, QtGui.QApplication.translate("Darstellerkorrigieren", "Male", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSuchen.setText(QtGui.QApplication.translate("Darstellerkorrigieren", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Darstellerkorrigieren", "Actors found", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonUebernehmen.setText(QtGui.QApplication.translate("Darstellerkorrigieren", "Adopt", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonUebernehmen.setShortcut(QtGui.QApplication.translate("Darstellerkorrigieren", "Return", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAbbrechen.setText(QtGui.QApplication.translate("Darstellerkorrigieren", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

