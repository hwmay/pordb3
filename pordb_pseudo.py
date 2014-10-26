# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_pseudo.ui'
#
# Created: Sun Oct 26 22:36:22 2014
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

class Ui_Pseudo(object):
    def setupUi(self, Pseudo):
        Pseudo.setObjectName(_fromUtf8("Pseudo"))
        Pseudo.resize(676, 800)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("pypordb/8027068_splash.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Pseudo.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Pseudo)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.frame = QtGui.QFrame(Pseudo)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tableWidgetPseudo = QtGui.QTableWidget(self.frame)
        self.tableWidgetPseudo.setMinimumSize(QtCore.QSize(381, 0))
        self.tableWidgetPseudo.setRowCount(50)
        self.tableWidgetPseudo.setObjectName(_fromUtf8("tableWidgetPseudo"))
        self.tableWidgetPseudo.setColumnCount(1)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetPseudo.setHorizontalHeaderItem(0, item)
        self.tableWidgetPseudo.horizontalHeader().setDefaultSectionSize(600)
        self.tableWidgetPseudo.horizontalHeader().setMinimumSectionSize(600)
        self.verticalLayout_2.addWidget(self.tableWidgetPseudo)
        self.verticalLayout_3.addWidget(self.frame)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEditPseudo = QtGui.QLineEdit(Pseudo)
        self.lineEditPseudo.setObjectName(_fromUtf8("lineEditPseudo"))
        self.horizontalLayout.addWidget(self.lineEditPseudo)
        self.pushButtonPseudo = QtGui.QPushButton(Pseudo)
        self.pushButtonPseudo.setObjectName(_fromUtf8("pushButtonPseudo"))
        self.horizontalLayout.addWidget(self.pushButtonPseudo)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(478, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButtonSpeichern = QtGui.QPushButton(Pseudo)
        self.pushButtonSpeichern.setObjectName(_fromUtf8("pushButtonSpeichern"))
        self.horizontalLayout_2.addWidget(self.pushButtonSpeichern)
        self.pushButtonAbbrechen = QtGui.QPushButton(Pseudo)
        self.pushButtonAbbrechen.setObjectName(_fromUtf8("pushButtonAbbrechen"))
        self.horizontalLayout_2.addWidget(self.pushButtonAbbrechen)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(Pseudo)
        QtCore.QMetaObject.connectSlotsByName(Pseudo)

    def retranslateUi(self, Pseudo):
        Pseudo.setWindowTitle(_translate("Pseudo", "Edit aliases", None))
        self.tableWidgetPseudo.setSortingEnabled(True)
        item = self.tableWidgetPseudo.horizontalHeaderItem(0)
        item.setText(_translate("Pseudo", "Alias", None))
        self.lineEditPseudo.setWhatsThis(_translate("Pseudo", "Enter aliases comma separated", None))
        self.pushButtonPseudo.setText(_translate("Pseudo", "Adopt", None))
        self.pushButtonSpeichern.setText(_translate("Pseudo", "Save", None))
        self.pushButtonAbbrechen.setText(_translate("Pseudo", "Cancel", None))

