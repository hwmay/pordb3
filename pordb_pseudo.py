# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_pseudo.ui'
#
# Created: Tue Mar 13 22:32:19 2012
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Pseudo(object):
    def setupUi(self, Pseudo):
        Pseudo.setObjectName("Pseudo")
        Pseudo.resize(726, 800)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pypordb/8027068_splash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Pseudo.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Pseudo)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtGui.QFrame(Pseudo)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidgetPseudo = QtGui.QTableWidget(self.frame)
        self.tableWidgetPseudo.setMinimumSize(QtCore.QSize(381, 0))
        self.tableWidgetPseudo.setRowCount(25)
        self.tableWidgetPseudo.setObjectName("tableWidgetPseudo")
        self.tableWidgetPseudo.setColumnCount(1)
        self.tableWidgetPseudo.setRowCount(25)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetPseudo.setHorizontalHeaderItem(0, item)
        self.verticalLayout_2.addWidget(self.tableWidgetPseudo)
        self.verticalLayout_3.addWidget(self.frame)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditPseudo = QtGui.QLineEdit(Pseudo)
        self.lineEditPseudo.setObjectName("lineEditPseudo")
        self.horizontalLayout.addWidget(self.lineEditPseudo)
        self.pushButtonPseudo = QtGui.QPushButton(Pseudo)
        self.pushButtonPseudo.setObjectName("pushButtonPseudo")
        self.horizontalLayout.addWidget(self.pushButtonPseudo)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtGui.QSpacerItem(478, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButtonSpeichern = QtGui.QPushButton(Pseudo)
        self.pushButtonSpeichern.setObjectName("pushButtonSpeichern")
        self.horizontalLayout_2.addWidget(self.pushButtonSpeichern)
        self.pushButtonAbbrechen = QtGui.QPushButton(Pseudo)
        self.pushButtonAbbrechen.setObjectName("pushButtonAbbrechen")
        self.horizontalLayout_2.addWidget(self.pushButtonAbbrechen)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(Pseudo)
        QtCore.QMetaObject.connectSlotsByName(Pseudo)

    def retranslateUi(self, Pseudo):
        Pseudo.setWindowTitle(QtGui.QApplication.translate("Pseudo", "Edit aliases", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetPseudo.setSortingEnabled(True)
        self.tableWidgetPseudo.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Pseudo", "Alias", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditPseudo.setWhatsThis(QtGui.QApplication.translate("Pseudo", "Enter aliases comma separated", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonPseudo.setText(QtGui.QApplication.translate("Pseudo", "Adopt", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSpeichern.setText(QtGui.QApplication.translate("Pseudo", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAbbrechen.setText(QtGui.QApplication.translate("Pseudo", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

