# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_darstellerneu.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(747, 280)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pypordb/8027068_splash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBoxDarstellerneuGeschlecht = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxDarstellerneuGeschlecht.sizePolicy().hasHeightForWidth())
        self.comboBoxDarstellerneuGeschlecht.setSizePolicy(sizePolicy)
        self.comboBoxDarstellerneuGeschlecht.setObjectName("comboBoxDarstellerneuGeschlecht")
        self.comboBoxDarstellerneuGeschlecht.addItem("")
        self.comboBoxDarstellerneuGeschlecht.setItemText(0, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pypordb/male.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBoxDarstellerneuGeschlecht.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("pypordb/female.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBoxDarstellerneuGeschlecht.addItem(icon2, "")
        self.gridLayout.addWidget(self.comboBoxDarstellerneuGeschlecht, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.comboBoxDarstellerneuHaarfarbe = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxDarstellerneuHaarfarbe.sizePolicy().hasHeightForWidth())
        self.comboBoxDarstellerneuHaarfarbe.setSizePolicy(sizePolicy)
        self.comboBoxDarstellerneuHaarfarbe.setObjectName("comboBoxDarstellerneuHaarfarbe")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("pypordb/blond.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBoxDarstellerneuHaarfarbe.addItem(icon3, "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("pypordb/brown.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBoxDarstellerneuHaarfarbe.addItem(icon4, "")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("pypordb/grey.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBoxDarstellerneuHaarfarbe.addItem(icon5, "")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("pypordb/red.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBoxDarstellerneuHaarfarbe.addItem(icon6, "")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("pypordb/black.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBoxDarstellerneuHaarfarbe.addItem(icon7, "")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("pypordb/bald.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBoxDarstellerneuHaarfarbe.addItem(icon8, "")
        self.gridLayout.addWidget(self.comboBoxDarstellerneuHaarfarbe, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.comboBoxDarstellerneuNation = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxDarstellerneuNation.setObjectName("comboBoxDarstellerneuNation")
        self.gridLayout.addWidget(self.comboBoxDarstellerneuNation, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEditDarstellerneuTattoo = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditDarstellerneuTattoo.setObjectName("lineEditDarstellerneuTattoo")
        self.gridLayout.addWidget(self.lineEditDarstellerneuTattoo, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.comboBoxDarstellerneuEthnic = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxDarstellerneuEthnic.sizePolicy().hasHeightForWidth())
        self.comboBoxDarstellerneuEthnic.setSizePolicy(sizePolicy)
        self.comboBoxDarstellerneuEthnic.setObjectName("comboBoxDarstellerneuEthnic")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("pypordb/white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBoxDarstellerneuEthnic.addItem(icon9, "")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("pypordb/yellow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBoxDarstellerneuEthnic.addItem(icon10, "")
        self.comboBoxDarstellerneuEthnic.addItem(icon7, "")
        self.comboBoxDarstellerneuEthnic.addItem(icon4, "")
        self.gridLayout.addWidget(self.comboBoxDarstellerneuEthnic, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 2)
        self.pushButtonDarstellerneuSpeichern = QtWidgets.QPushButton(Dialog)
        self.pushButtonDarstellerneuSpeichern.setObjectName("pushButtonDarstellerneuSpeichern")
        self.gridLayout_2.addWidget(self.pushButtonDarstellerneuSpeichern, 1, 0, 1, 1)
        self.pushButtonDarstellerneuCancel = QtWidgets.QPushButton(Dialog)
        self.pushButtonDarstellerneuCancel.setObjectName("pushButtonDarstellerneuCancel")
        self.gridLayout_2.addWidget(self.pushButtonDarstellerneuCancel, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "New actor"))
        self.groupBox.setTitle(_translate("Dialog", "Enter new actor"))
        self.label.setText(_translate("Dialog", "Gender"))
        self.comboBoxDarstellerneuGeschlecht.setItemText(1, _translate("Dialog", "m"))
        self.comboBoxDarstellerneuGeschlecht.setItemText(2, _translate("Dialog", "w"))
        self.label_2.setText(_translate("Dialog", "Hair color"))
        self.comboBoxDarstellerneuHaarfarbe.setItemText(0, _translate("Dialog", "bl"))
        self.comboBoxDarstellerneuHaarfarbe.setItemText(1, _translate("Dialog", "br"))
        self.comboBoxDarstellerneuHaarfarbe.setItemText(2, _translate("Dialog", "gr"))
        self.comboBoxDarstellerneuHaarfarbe.setItemText(3, _translate("Dialog", "r"))
        self.comboBoxDarstellerneuHaarfarbe.setItemText(4, _translate("Dialog", "s"))
        self.comboBoxDarstellerneuHaarfarbe.setItemText(5, _translate("Dialog", "bald"))
        self.label_3.setText(_translate("Dialog", "Nation"))
        self.label_4.setText(_translate("Dialog", "Tattoo"))
        self.label_5.setText(_translate("Dialog", "Ethnic"))
        self.comboBoxDarstellerneuEthnic.setItemText(0, _translate("Dialog", "w"))
        self.comboBoxDarstellerneuEthnic.setItemText(1, _translate("Dialog", "a"))
        self.comboBoxDarstellerneuEthnic.setItemText(2, _translate("Dialog", "s"))
        self.comboBoxDarstellerneuEthnic.setItemText(3, _translate("Dialog", "l"))
        self.pushButtonDarstellerneuSpeichern.setText(_translate("Dialog", "Save"))
        self.pushButtonDarstellerneuCancel.setText(_translate("Dialog", "Back"))
