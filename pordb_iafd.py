# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_iafd.ui'
#
# Created: Sun Dec  7 14:44:15 2014
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

class Ui_DatenausderIAFD(object):
    def setupUi(self, DatenausderIAFD):
        DatenausderIAFD.setObjectName(_fromUtf8("DatenausderIAFD"))
        DatenausderIAFD.resize(937, 573)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("pypordb/8027068_splash.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DatenausderIAFD.setWindowIcon(icon)
        self.gridLayout_2 = QtGui.QGridLayout(DatenausderIAFD)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.checkBoxBild = QtGui.QCheckBox(DatenausderIAFD)
        self.checkBoxBild.setText(_fromUtf8(""))
        self.checkBoxBild.setObjectName(_fromUtf8("checkBoxBild"))
        self.horizontalLayout.addWidget(self.checkBoxBild)
        self.labelBild = QtGui.QLabel(DatenausderIAFD)
        self.labelBild.setMinimumSize(QtCore.QSize(231, 251))
        self.labelBild.setObjectName(_fromUtf8("labelBild"))
        self.horizontalLayout.addWidget(self.labelBild)
        self.labelName = QtGui.QLabel(DatenausderIAFD)
        self.labelName.setEnabled(True)
        self.labelName.setMinimumSize(QtCore.QSize(401, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelName.setFont(font)
        self.labelName.setObjectName(_fromUtf8("labelName"))
        self.horizontalLayout.addWidget(self.labelName)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.checkBoxName = QtGui.QCheckBox(DatenausderIAFD)
        self.checkBoxName.setText(_fromUtf8(""))
        self.checkBoxName.setObjectName(_fromUtf8("checkBoxName"))
        self.gridLayout.addWidget(self.checkBoxName, 0, 0, 1, 1)
        self.label_8 = QtGui.QLabel(DatenausderIAFD)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 0, 1, 1, 1)
        self.lineEditName = QtGui.QLineEdit(DatenausderIAFD)
        self.lineEditName.setObjectName(_fromUtf8("lineEditName"))
        self.gridLayout.addWidget(self.lineEditName, 0, 2, 1, 1)
        self.checkBoxGeschlecht = QtGui.QCheckBox(DatenausderIAFD)
        self.checkBoxGeschlecht.setText(_fromUtf8(""))
        self.checkBoxGeschlecht.setObjectName(_fromUtf8("checkBoxGeschlecht"))
        self.gridLayout.addWidget(self.checkBoxGeschlecht, 1, 0, 1, 1)
        self.label_6 = QtGui.QLabel(DatenausderIAFD)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 1, 1, 1, 1)
        self.lineEditGeschlecht = QtGui.QLineEdit(DatenausderIAFD)
        self.lineEditGeschlecht.setObjectName(_fromUtf8("lineEditGeschlecht"))
        self.gridLayout.addWidget(self.lineEditGeschlecht, 1, 2, 1, 1)
        self.checkBoxPseudo = QtGui.QCheckBox(DatenausderIAFD)
        self.checkBoxPseudo.setText(_fromUtf8(""))
        self.checkBoxPseudo.setObjectName(_fromUtf8("checkBoxPseudo"))
        self.gridLayout.addWidget(self.checkBoxPseudo, 2, 0, 1, 1)
        self.label = QtGui.QLabel(DatenausderIAFD)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.lineEditPseudo = QtGui.QLineEdit(DatenausderIAFD)
        self.lineEditPseudo.setObjectName(_fromUtf8("lineEditPseudo"))
        self.gridLayout.addWidget(self.lineEditPseudo, 2, 2, 1, 1)
        self.checkBoxGeboren = QtGui.QCheckBox(DatenausderIAFD)
        self.checkBoxGeboren.setText(_fromUtf8(""))
        self.checkBoxGeboren.setObjectName(_fromUtf8("checkBoxGeboren"))
        self.gridLayout.addWidget(self.checkBoxGeboren, 3, 0, 1, 1)
        self.label_2 = QtGui.QLabel(DatenausderIAFD)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)
        self.labelGeboren = QtGui.QLabel(DatenausderIAFD)
        self.labelGeboren.setObjectName(_fromUtf8("labelGeboren"))
        self.gridLayout.addWidget(self.labelGeboren, 3, 2, 1, 1)
        self.checkBoxLand = QtGui.QCheckBox(DatenausderIAFD)
        self.checkBoxLand.setText(_fromUtf8(""))
        self.checkBoxLand.setObjectName(_fromUtf8("checkBoxLand"))
        self.gridLayout.addWidget(self.checkBoxLand, 4, 0, 1, 1)
        self.label_3 = QtGui.QLabel(DatenausderIAFD)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 4, 1, 1, 1)
        self.lineEditLand = QtGui.QLineEdit(DatenausderIAFD)
        self.lineEditLand.setObjectName(_fromUtf8("lineEditLand"))
        self.gridLayout.addWidget(self.lineEditLand, 4, 2, 1, 1)
        self.checkBoxEthnic = QtGui.QCheckBox(DatenausderIAFD)
        self.checkBoxEthnic.setText(_fromUtf8(""))
        self.checkBoxEthnic.setObjectName(_fromUtf8("checkBoxEthnic"))
        self.gridLayout.addWidget(self.checkBoxEthnic, 5, 0, 1, 1)
        self.label_4 = QtGui.QLabel(DatenausderIAFD)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 5, 1, 1, 1)
        self.lineEditEthnic = QtGui.QLineEdit(DatenausderIAFD)
        self.lineEditEthnic.setObjectName(_fromUtf8("lineEditEthnic"))
        self.gridLayout.addWidget(self.lineEditEthnic, 5, 2, 1, 1)
        self.checkBoxHaare = QtGui.QCheckBox(DatenausderIAFD)
        self.checkBoxHaare.setText(_fromUtf8(""))
        self.checkBoxHaare.setObjectName(_fromUtf8("checkBoxHaare"))
        self.gridLayout.addWidget(self.checkBoxHaare, 6, 0, 1, 1)
        self.label_5 = QtGui.QLabel(DatenausderIAFD)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 6, 1, 1, 1)
        self.lineEditHaare = QtGui.QLineEdit(DatenausderIAFD)
        self.lineEditHaare.setObjectName(_fromUtf8("lineEditHaare"))
        self.gridLayout.addWidget(self.lineEditHaare, 6, 2, 1, 1)
        self.checkBoxTattos = QtGui.QCheckBox(DatenausderIAFD)
        self.checkBoxTattos.setText(_fromUtf8(""))
        self.checkBoxTattos.setObjectName(_fromUtf8("checkBoxTattos"))
        self.gridLayout.addWidget(self.checkBoxTattos, 7, 0, 1, 1)
        self.label_7 = QtGui.QLabel(DatenausderIAFD)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 7, 1, 1, 1)
        self.lineEditTattos = QtGui.QLineEdit(DatenausderIAFD)
        self.lineEditTattos.setObjectName(_fromUtf8("lineEditTattos"))
        self.gridLayout.addWidget(self.lineEditTattos, 7, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButtonRemoveBrackets = QtGui.QPushButton(DatenausderIAFD)
        self.pushButtonRemoveBrackets.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("pypordb/bracket.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonRemoveBrackets.setIcon(icon1)
        self.pushButtonRemoveBrackets.setObjectName(_fromUtf8("pushButtonRemoveBrackets"))
        self.horizontalLayout_2.addWidget(self.pushButtonRemoveBrackets)
        self.pushButtonUebernehmen = QtGui.QPushButton(DatenausderIAFD)
        self.pushButtonUebernehmen.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("pypordb/dialog-ok.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonUebernehmen.setIcon(icon2)
        self.pushButtonUebernehmen.setObjectName(_fromUtf8("pushButtonUebernehmen"))
        self.horizontalLayout_2.addWidget(self.pushButtonUebernehmen)
        self.pushButtonCancel = QtGui.QPushButton(DatenausderIAFD)
        self.pushButtonCancel.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("pypordb/dialog-cancel.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonCancel.setIcon(icon3)
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))
        self.horizontalLayout_2.addWidget(self.pushButtonCancel)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.retranslateUi(DatenausderIAFD)
        QtCore.QMetaObject.connectSlotsByName(DatenausderIAFD)

    def retranslateUi(self, DatenausderIAFD):
        DatenausderIAFD.setWindowTitle(_translate("DatenausderIAFD", "Data from the IAFD", None))
        self.labelBild.setText(_translate("DatenausderIAFD", "TextLabel", None))
        self.labelName.setText(_translate("DatenausderIAFD", "TextLabel", None))
        self.label_8.setText(_translate("DatenausderIAFD", "Name:", None))
        self.label_6.setText(_translate("DatenausderIAFD", "Gender:", None))
        self.label.setText(_translate("DatenausderIAFD", "Alias:", None))
        self.label_2.setText(_translate("DatenausderIAFD", "Born:", None))
        self.labelGeboren.setText(_translate("DatenausderIAFD", "TextLabel", None))
        self.label_3.setText(_translate("DatenausderIAFD", "Country:", None))
        self.label_4.setText(_translate("DatenausderIAFD", "Ethnic:", None))
        self.label_5.setText(_translate("DatenausderIAFD", "Hair color:", None))
        self.label_7.setText(_translate("DatenausderIAFD", "Tattoos:", None))
        self.pushButtonRemoveBrackets.setToolTip(_translate("DatenausderIAFD", "<html><head/><body><p>Delete comments in brackets, Ctrl+L</p></body></html>", None))
        self.pushButtonRemoveBrackets.setShortcut(_translate("DatenausderIAFD", "Ctrl+D", None))
        self.pushButtonUebernehmen.setToolTip(_translate("DatenausderIAFD", "<html><head/><body><p>Adopt marked data (enter)</p></body></html>", None))
        self.pushButtonCancel.setToolTip(_translate("DatenausderIAFD", "<html><head/><body><p>Cancel (escape)</p></body></html>", None))

