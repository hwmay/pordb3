# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_bilddatei_umbenennen.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1035, 307)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pypordb/8027068_splash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidgetDateinamen = QtWidgets.QListWidget(self.groupBox)
        self.listWidgetDateinamen.setObjectName("listWidgetDateinamen")
        self.gridLayout.addWidget(self.listWidgetDateinamen, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEditDateiname = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditDateiname.setObjectName("lineEditDateiname")
        self.gridLayout_2.addWidget(self.lineEditDateiname, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.labelDateiname = QtWidgets.QLabel(Dialog)
        self.labelDateiname.setText("")
        self.labelDateiname.setObjectName("labelDateiname")
        self.verticalLayout.addWidget(self.labelDateiname)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonUmbenennen = QtWidgets.QPushButton(Dialog)
        self.pushButtonUmbenennen.setDefault(True)
        self.pushButtonUmbenennen.setFlat(False)
        self.pushButtonUmbenennen.setObjectName("pushButtonUmbenennen")
        self.horizontalLayout_2.addWidget(self.pushButtonUmbenennen)
        self.pushButtonCancel = QtWidgets.QPushButton(Dialog)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout_2.addWidget(self.pushButtonCancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Edit filename"))
        self.label.setText(_translate("Dialog", "Filename already exists or has more than 256 characters"))
        self.groupBox.setTitle(_translate("Dialog", "Similar files in directory"))
        self.groupBox_2.setTitle(_translate("Dialog", "New filename"))
        self.pushButtonUmbenennen.setText(_translate("Dialog", "Rename file"))
        self.pushButtonUmbenennen.setShortcut(_translate("Dialog", "Return"))
        self.pushButtonCancel.setText(_translate("Dialog", "Cancel"))

