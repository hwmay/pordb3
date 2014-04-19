# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_bilddatei_umbenennen.ui'
#
# Created: Mon Nov 18 00:33:46 2013
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1035, 307)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("pypordb/8027068_splash.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.listWidgetDateinamen = QtGui.QListWidget(self.groupBox)
        self.listWidgetDateinamen.setObjectName(_fromUtf8("listWidgetDateinamen"))
        self.gridLayout.addWidget(self.listWidgetDateinamen, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lineEditDateiname = QtGui.QLineEdit(self.groupBox_2)
        self.lineEditDateiname.setObjectName(_fromUtf8("lineEditDateiname"))
        self.gridLayout_2.addWidget(self.lineEditDateiname, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.labelDateiname = QtGui.QLabel(Dialog)
        self.labelDateiname.setText(_fromUtf8(""))
        self.labelDateiname.setObjectName(_fromUtf8("labelDateiname"))
        self.verticalLayout.addWidget(self.labelDateiname)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButtonUmbenennen = QtGui.QPushButton(Dialog)
        self.pushButtonUmbenennen.setDefault(True)
        self.pushButtonUmbenennen.setFlat(False)
        self.pushButtonUmbenennen.setObjectName(_fromUtf8("pushButtonUmbenennen"))
        self.horizontalLayout_2.addWidget(self.pushButtonUmbenennen)
        self.pushButtonCancel = QtGui.QPushButton(Dialog)
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))
        self.horizontalLayout_2.addWidget(self.pushButtonCancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Edit filename", None))
        self.label.setText(_translate("Dialog", "Filename already exists or has more than 256 characters", None))
        self.groupBox.setTitle(_translate("Dialog", "Similar files in directory", None))
        self.groupBox_2.setTitle(_translate("Dialog", "New filename", None))
        self.pushButtonUmbenennen.setText(_translate("Dialog", "Rename file", None))
        self.pushButtonUmbenennen.setShortcut(_translate("Dialog", "Return", None))
        self.pushButtonCancel.setText(_translate("Dialog", "Cancel", None))

