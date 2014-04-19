# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_suchbegriffe.ui'
#
# Created: Thu Oct  3 22:17:46 2013
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

class Ui_Suchbegriffedialog(object):
    def setupUi(self, Suchbegriffedialog):
        Suchbegriffedialog.setObjectName(_fromUtf8("Suchbegriffedialog"))
        Suchbegriffedialog.resize(735, 905)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("pypordb/8027068_splash.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Suchbegriffedialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Suchbegriffedialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(Suchbegriffedialog)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tableWidgetSuche = QtGui.QTableWidget(self.frame)
        self.tableWidgetSuche.setObjectName(_fromUtf8("tableWidgetSuche"))
        self.tableWidgetSuche.setColumnCount(2)
        self.tableWidgetSuche.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetSuche.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetSuche.setHorizontalHeaderItem(1, item)
        self.horizontalLayout_2.addWidget(self.tableWidgetSuche)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonLandSpeichern = QtGui.QPushButton(Suchbegriffedialog)
        self.pushButtonLandSpeichern.setObjectName(_fromUtf8("pushButtonLandSpeichern"))
        self.horizontalLayout.addWidget(self.pushButtonLandSpeichern)
        self.pushButtonLandAbbrechen = QtGui.QPushButton(Suchbegriffedialog)
        self.pushButtonLandAbbrechen.setObjectName(_fromUtf8("pushButtonLandAbbrechen"))
        self.horizontalLayout.addWidget(self.pushButtonLandAbbrechen)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Suchbegriffedialog)
        QtCore.QMetaObject.connectSlotsByName(Suchbegriffedialog)

    def retranslateUi(self, Suchbegriffedialog):
        Suchbegriffedialog.setWindowTitle(_translate("Suchbegriffedialog", "Edit search items", None))
        self.tableWidgetSuche.setWhatsThis(_translate("Suchbegriffedialog", "Here you can enter synomyms for searching, e. g. \"18\" and \"eighteen\". When you enter \"18\", search will not only look for \"18\", but also for \"eighteen\". Be very careful with this function for avoiding long searchs with a lot of results.", None))
        item = self.tableWidgetSuche.horizontalHeaderItem(0)
        item.setText(_translate("Suchbegriffedialog", "search item", None))
        item = self.tableWidgetSuche.horizontalHeaderItem(1)
        item.setText(_translate("Suchbegriffedialog", "Alternative", None))
        self.pushButtonLandSpeichern.setText(_translate("Suchbegriffedialog", "Save", None))
        self.pushButtonLandAbbrechen.setText(_translate("Suchbegriffedialog", "Cancel", None))

