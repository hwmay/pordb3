# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_darsteller_suchen.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DarstellerSuche(object):
    def setupUi(self, DarstellerSuche):
        DarstellerSuche.setObjectName("DarstellerSuche")
        DarstellerSuche.resize(867, 672)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pypordb/8027068_splash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DarstellerSuche.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(DarstellerSuche)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(DarstellerSuche)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEditDarstellerSuche = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditDarstellerSuche.setObjectName("lineEditDarstellerSuche")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditDarstellerSuche)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.comboBoxDarstellerSucheGeschlecht = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxDarstellerSucheGeschlecht.setObjectName("comboBoxDarstellerSucheGeschlecht")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pypordb/female.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBoxDarstellerSucheGeschlecht.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("pypordb/male.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBoxDarstellerSucheGeschlecht.addItem(icon2, "")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBoxDarstellerSucheGeschlecht)
        spacerItem = QtWidgets.QSpacerItem(661, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditActor1 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditActor1.setObjectName("lineEditActor1")
        self.horizontalLayout.addWidget(self.lineEditActor1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        self.lineEditActor2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditActor2.setObjectName("lineEditActor2")
        self.horizontalLayout.addWidget(self.lineEditActor2)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.lineEditActor3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditActor3.setObjectName("lineEditActor3")
        self.horizontalLayout.addWidget(self.lineEditActor3)
        self.formLayout.setLayout(6, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.dateEditDarstellerSucheAb = QtWidgets.QDateEdit(self.groupBox)
        self.dateEditDarstellerSucheAb.setMinimumDate(QtCore.QDate(1752, 9, 14))
        self.dateEditDarstellerSucheAb.setCalendarPopup(True)
        self.dateEditDarstellerSucheAb.setObjectName("dateEditDarstellerSucheAb")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.dateEditDarstellerSucheAb)
        spacerItem1 = QtWidgets.QSpacerItem(631, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(11, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.dateEditDarstellerSucheBis = QtWidgets.QDateEdit(self.groupBox)
        self.dateEditDarstellerSucheBis.setCalendarPopup(True)
        self.dateEditDarstellerSucheBis.setDate(QtCore.QDate(2000, 1, 1))
        self.dateEditDarstellerSucheBis.setObjectName("dateEditDarstellerSucheBis")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.dateEditDarstellerSucheBis)
        spacerItem2 = QtWidgets.QSpacerItem(631, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(14, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.comboBoxDarstellerSucheHaar = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxDarstellerSucheHaar.setObjectName("comboBoxDarstellerSucheHaar")
        self.comboBoxDarstellerSucheHaar.addItem("")
        self.comboBoxDarstellerSucheHaar.setItemText(0, "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("pypordb/blond.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBoxDarstellerSucheHaar.addItem(icon3, "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("pypordb/brown.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBoxDarstellerSucheHaar.addItem(icon4, "")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("pypordb/grey.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBoxDarstellerSucheHaar.addItem(icon5, "")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("pypordb/red.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBoxDarstellerSucheHaar.addItem(icon6, "")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("pypordb/black.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBoxDarstellerSucheHaar.addItem(icon7, "")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("pypordb/bald.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBoxDarstellerSucheHaar.addItem(icon8, "")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.comboBoxDarstellerSucheHaar)
        spacerItem3 = QtWidgets.QSpacerItem(661, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(16, QtWidgets.QFormLayout.FieldRole, spacerItem3)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBoxDarstellerSucheNation1 = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxDarstellerSucheNation1.sizePolicy().hasHeightForWidth())
        self.comboBoxDarstellerSucheNation1.setSizePolicy(sizePolicy)
        self.comboBoxDarstellerSucheNation1.setObjectName("comboBoxDarstellerSucheNation1")
        self.horizontalLayout_2.addWidget(self.comboBoxDarstellerSucheNation1)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.comboBoxDarstellerSucheNation2 = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxDarstellerSucheNation2.sizePolicy().hasHeightForWidth())
        self.comboBoxDarstellerSucheNation2.setSizePolicy(sizePolicy)
        self.comboBoxDarstellerSucheNation2.setObjectName("comboBoxDarstellerSucheNation2")
        self.horizontalLayout_2.addWidget(self.comboBoxDarstellerSucheNation2)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        self.comboBoxDarstellerSucheNation3 = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxDarstellerSucheNation3.sizePolicy().hasHeightForWidth())
        self.comboBoxDarstellerSucheNation3.setSizePolicy(sizePolicy)
        self.comboBoxDarstellerSucheNation3.setObjectName("comboBoxDarstellerSucheNation3")
        self.horizontalLayout_2.addWidget(self.comboBoxDarstellerSucheNation3)
        self.formLayout.setLayout(18, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(21, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.comboBoxDarstellerSucheTattoo = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxDarstellerSucheTattoo.setObjectName("comboBoxDarstellerSucheTattoo")
        self.comboBoxDarstellerSucheTattoo.addItem("")
        self.comboBoxDarstellerSucheTattoo.setItemText(0, "")
        self.comboBoxDarstellerSucheTattoo.addItem("")
        self.comboBoxDarstellerSucheTattoo.addItem("")
        self.formLayout.setWidget(21, QtWidgets.QFormLayout.FieldRole, self.comboBoxDarstellerSucheTattoo)
        self.lineEditDarstellerSucheTattoo = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditDarstellerSucheTattoo.setObjectName("lineEditDarstellerSucheTattoo")
        self.formLayout.setWidget(22, QtWidgets.QFormLayout.FieldRole, self.lineEditDarstellerSucheTattoo)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(24, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.comboBoxDarstellerSucheEthnic = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxDarstellerSucheEthnic.setObjectName("comboBoxDarstellerSucheEthnic")
        self.comboBoxDarstellerSucheEthnic.addItem("")
        self.comboBoxDarstellerSucheEthnic.setItemText(0, "")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("pypordb/white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBoxDarstellerSucheEthnic.addItem(icon9, "")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("pypordb/yellow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBoxDarstellerSucheEthnic.addItem(icon10, "")
        self.comboBoxDarstellerSucheEthnic.addItem(icon7, "")
        self.comboBoxDarstellerSucheEthnic.addItem(icon4, "")
        self.formLayout.setWidget(24, QtWidgets.QFormLayout.FieldRole, self.comboBoxDarstellerSucheEthnic)
        spacerItem4 = QtWidgets.QSpacerItem(491, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(25, QtWidgets.QFormLayout.FieldRole, spacerItem4)
        self.verticalLayout.addWidget(self.groupBox)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.pushButtonSuchen = QtWidgets.QPushButton(DarstellerSuche)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("pypordb/suchen.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSuchen.setIcon(icon11)
        self.pushButtonSuchen.setObjectName("pushButtonSuchen")
        self.hboxlayout.addWidget(self.pushButtonSuchen)
        self.pushButtonRefresh = QtWidgets.QPushButton(DarstellerSuche)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("pypordb/clear_l.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonRefresh.setIcon(icon12)
        self.pushButtonRefresh.setObjectName("pushButtonRefresh")
        self.hboxlayout.addWidget(self.pushButtonRefresh)
        self.pushButtonCancel = QtWidgets.QPushButton(DarstellerSuche)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("pypordb/dialog-cancel.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonCancel.setIcon(icon13)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.hboxlayout.addWidget(self.pushButtonCancel)
        self.verticalLayout.addLayout(self.hboxlayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(DarstellerSuche)
        QtCore.QMetaObject.connectSlotsByName(DarstellerSuche)
        DarstellerSuche.setTabOrder(self.lineEditDarstellerSuche, self.comboBoxDarstellerSucheGeschlecht)
        DarstellerSuche.setTabOrder(self.comboBoxDarstellerSucheGeschlecht, self.lineEditActor1)
        DarstellerSuche.setTabOrder(self.lineEditActor1, self.lineEditActor2)
        DarstellerSuche.setTabOrder(self.lineEditActor2, self.lineEditActor3)
        DarstellerSuche.setTabOrder(self.lineEditActor3, self.dateEditDarstellerSucheAb)
        DarstellerSuche.setTabOrder(self.dateEditDarstellerSucheAb, self.dateEditDarstellerSucheBis)
        DarstellerSuche.setTabOrder(self.dateEditDarstellerSucheBis, self.comboBoxDarstellerSucheHaar)
        DarstellerSuche.setTabOrder(self.comboBoxDarstellerSucheHaar, self.comboBoxDarstellerSucheNation1)
        DarstellerSuche.setTabOrder(self.comboBoxDarstellerSucheNation1, self.comboBoxDarstellerSucheTattoo)
        DarstellerSuche.setTabOrder(self.comboBoxDarstellerSucheTattoo, self.lineEditDarstellerSucheTattoo)
        DarstellerSuche.setTabOrder(self.lineEditDarstellerSucheTattoo, self.comboBoxDarstellerSucheEthnic)
        DarstellerSuche.setTabOrder(self.comboBoxDarstellerSucheEthnic, self.pushButtonSuchen)
        DarstellerSuche.setTabOrder(self.pushButtonSuchen, self.pushButtonRefresh)
        DarstellerSuche.setTabOrder(self.pushButtonRefresh, self.pushButtonCancel)

    def retranslateUi(self, DarstellerSuche):
        _translate = QtCore.QCoreApplication.translate
        DarstellerSuche.setWindowTitle(_translate("DarstellerSuche", "Search actor"))
        self.groupBox.setTitle(_translate("DarstellerSuche", "Search criteria"))
        self.label.setText(_translate("DarstellerSuche", "Name"))
        self.label_2.setText(_translate("DarstellerSuche", "Gender"))
        self.comboBoxDarstellerSucheGeschlecht.setItemText(0, _translate("DarstellerSuche", "w"))
        self.comboBoxDarstellerSucheGeschlecht.setItemText(1, _translate("DarstellerSuche", "m"))
        self.label_9.setText(_translate("DarstellerSuche", "Has acted with"))
        self.label_10.setText(_translate("DarstellerSuche", "and"))
        self.label_11.setText(_translate("DarstellerSuche", "and"))
        self.label_3.setText(_translate("DarstellerSuche", "Date from"))
        self.dateEditDarstellerSucheAb.setWhatsThis(_translate("DarstellerSuche", "Date when the actor has been added to the PorDB database"))
        self.dateEditDarstellerSucheAb.setDisplayFormat(_translate("DarstellerSuche", "dd.MM.yyyy"))
        self.label_4.setText(_translate("DarstellerSuche", "Date to"))
        self.dateEditDarstellerSucheBis.setWhatsThis(_translate("DarstellerSuche", "Date when the actor has been added to the PorDB database"))
        self.dateEditDarstellerSucheBis.setDisplayFormat(_translate("DarstellerSuche", "dd.MM.yyyy"))
        self.label_5.setText(_translate("DarstellerSuche", "Hair color"))
        self.comboBoxDarstellerSucheHaar.setItemText(1, _translate("DarstellerSuche", "bl"))
        self.comboBoxDarstellerSucheHaar.setItemText(2, _translate("DarstellerSuche", "br"))
        self.comboBoxDarstellerSucheHaar.setItemText(3, _translate("DarstellerSuche", "gr"))
        self.comboBoxDarstellerSucheHaar.setItemText(4, _translate("DarstellerSuche", "r"))
        self.comboBoxDarstellerSucheHaar.setItemText(5, _translate("DarstellerSuche", "s"))
        self.comboBoxDarstellerSucheHaar.setItemText(6, _translate("DarstellerSuche", "ba"))
        self.label_6.setText(_translate("DarstellerSuche", "Nation"))
        self.label_12.setText(_translate("DarstellerSuche", "or"))
        self.label_13.setText(_translate("DarstellerSuche", "or"))
        self.label_7.setText(_translate("DarstellerSuche", "Tattoo"))
        self.comboBoxDarstellerSucheTattoo.setItemText(1, _translate("DarstellerSuche", "yes"))
        self.comboBoxDarstellerSucheTattoo.setItemText(2, _translate("DarstellerSuche", "no"))
        self.label_8.setText(_translate("DarstellerSuche", "Ethnic"))
        self.comboBoxDarstellerSucheEthnic.setItemText(1, _translate("DarstellerSuche", "w"))
        self.comboBoxDarstellerSucheEthnic.setItemText(2, _translate("DarstellerSuche", "a"))
        self.comboBoxDarstellerSucheEthnic.setItemText(3, _translate("DarstellerSuche", "s"))
        self.comboBoxDarstellerSucheEthnic.setItemText(4, _translate("DarstellerSuche", "l"))
        self.pushButtonSuchen.setToolTip(_translate("DarstellerSuche", "<html><head/><body><p>Search, enter</p></body></html>"))
        self.pushButtonSuchen.setText(_translate("DarstellerSuche", "Search"))
        self.pushButtonSuchen.setShortcut(_translate("DarstellerSuche", "Enter"))
        self.pushButtonRefresh.setToolTip(_translate("DarstellerSuche", "<html><head/><body><p>Clear all search fields, alt+L</p></body></html>"))
        self.pushButtonRefresh.setText(_translate("DarstellerSuche", "Clear all search fields"))
        self.pushButtonRefresh.setShortcut(_translate("DarstellerSuche", "Alt+L"))
        self.pushButtonCancel.setToolTip(_translate("DarstellerSuche", "<html><head/><body><p>Cancel, esc</p></body></html>"))
        self.pushButtonCancel.setText(_translate("DarstellerSuche", "Cancel"))
