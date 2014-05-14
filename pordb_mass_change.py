# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_mass_change.ui'
#
# Created: Thu May 15 00:20:38 2014
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(251, 142)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("pypordb/8027068_splash.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.formLayout = QtGui.QFormLayout(Dialog)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.frame_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.radioButtonVorhandenJa = QtGui.QRadioButton(self.frame_2)
        self.radioButtonVorhandenJa.setObjectName(_fromUtf8("radioButtonVorhandenJa"))
        self.horizontalLayout_2.addWidget(self.radioButtonVorhandenJa)
        self.radioButtonVorhandenNein = QtGui.QRadioButton(self.frame_2)
        self.radioButtonVorhandenNein.setObjectName(_fromUtf8("radioButtonVorhandenNein"))
        self.horizontalLayout_2.addWidget(self.radioButtonVorhandenNein)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.frame_3 = QtGui.QFrame(self.frame)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.frame_3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.comboBoxResolution = QtGui.QComboBox(self.frame_3)
        self.comboBoxResolution.setObjectName(_fromUtf8("comboBoxResolution"))
        self.comboBoxResolution.addItem(_fromUtf8(""))
        self.comboBoxResolution.setItemText(0, _fromUtf8(""))
        self.comboBoxResolution.addItem(_fromUtf8(""))
        self.comboBoxResolution.addItem(_fromUtf8(""))
        self.comboBoxResolution.addItem(_fromUtf8(""))
        self.comboBoxResolution.addItem(_fromUtf8(""))
        self.comboBoxResolution.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.comboBoxResolution)
        self.horizontalLayout_3.addWidget(self.frame_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(self.frame)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Mass change", None))
        self.label.setText(_translate("Dialog", "Present", None))
        self.radioButtonVorhandenJa.setWhatsThis(_translate("Dialog", "<html><head/><body><p>Mark here when video is NOT present.</p></body></html>", None))
        self.radioButtonVorhandenJa.setText(_translate("Dialog", "Yes", None))
        self.radioButtonVorhandenNein.setWhatsThis(_translate("Dialog", "<html><head/><body><p>Mark here when video is present.</p></body></html>", None))
        self.radioButtonVorhandenNein.setText(_translate("Dialog", "No", None))
        self.label_2.setText(_translate("Dialog", "Resolution", None))
        self.comboBoxResolution.setItemText(1, _translate("Dialog", "SD", None))
        self.comboBoxResolution.setItemText(2, _translate("Dialog", "HD 720p", None))
        self.comboBoxResolution.setItemText(3, _translate("Dialog", "HD 1080p", None))
        self.comboBoxResolution.setItemText(4, _translate("Dialog", "UltraHD", None))
        self.comboBoxResolution.setItemText(5, _translate("Dialog", "Unknown", None))

