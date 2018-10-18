# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_pseudo.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Pseudo(object):
    def setupUi(self, Pseudo):
        Pseudo.setObjectName("Pseudo")
        Pseudo.resize(676, 800)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pypordb/8027068_splash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Pseudo.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Pseudo)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(Pseudo)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidgetPseudo = QtWidgets.QTableWidget(self.frame)
        self.tableWidgetPseudo.setMinimumSize(QtCore.QSize(381, 0))
        self.tableWidgetPseudo.setRowCount(50)
        self.tableWidgetPseudo.setObjectName("tableWidgetPseudo")
        self.tableWidgetPseudo.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPseudo.setHorizontalHeaderItem(0, item)
        self.tableWidgetPseudo.horizontalHeader().setDefaultSectionSize(600)
        self.tableWidgetPseudo.horizontalHeader().setMinimumSectionSize(600)
        self.verticalLayout_2.addWidget(self.tableWidgetPseudo)
        self.verticalLayout_3.addWidget(self.frame)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditPseudo = QtWidgets.QLineEdit(Pseudo)
        self.lineEditPseudo.setObjectName("lineEditPseudo")
        self.horizontalLayout.addWidget(self.lineEditPseudo)
        self.pushButtonPseudo = QtWidgets.QPushButton(Pseudo)
        self.pushButtonPseudo.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pypordb/go-up.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonPseudo.setIcon(icon1)
        self.pushButtonPseudo.setObjectName("pushButtonPseudo")
        self.horizontalLayout.addWidget(self.pushButtonPseudo)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(478, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButtonSpeichern = QtWidgets.QPushButton(Pseudo)
        self.pushButtonSpeichern.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("pypordb/media-floppy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSpeichern.setIcon(icon2)
        self.pushButtonSpeichern.setObjectName("pushButtonSpeichern")
        self.horizontalLayout_2.addWidget(self.pushButtonSpeichern)
        self.pushButtonAbbrechen = QtWidgets.QPushButton(Pseudo)
        self.pushButtonAbbrechen.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("pypordb/dialog-cancel.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonAbbrechen.setIcon(icon3)
        self.pushButtonAbbrechen.setObjectName("pushButtonAbbrechen")
        self.horizontalLayout_2.addWidget(self.pushButtonAbbrechen)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(Pseudo)
        QtCore.QMetaObject.connectSlotsByName(Pseudo)

    def retranslateUi(self, Pseudo):
        _translate = QtCore.QCoreApplication.translate
        Pseudo.setWindowTitle(_translate("Pseudo", "Edit aliases"))
        self.tableWidgetPseudo.setSortingEnabled(True)
        item = self.tableWidgetPseudo.horizontalHeaderItem(0)
        item.setText(_translate("Pseudo", "Alias"))
        self.lineEditPseudo.setWhatsThis(_translate("Pseudo", "<html><head/><body><p>Enter aliases comma separated here. When ready press the button on the right side, this will move your entries into the list above, then press the save button.</p></body></html>"))
        self.pushButtonPseudo.setToolTip(_translate("Pseudo", "<html><head/><body><p>Adopt the aliases</p></body></html>"))
        self.pushButtonSpeichern.setToolTip(_translate("Pseudo", "<html><head/><body><p>Save</p></body></html>"))
        self.pushButtonAbbrechen.setToolTip(_translate("Pseudo", "<html><head/><body><p>Cancel</p></body></html>"))

