# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_actor_details.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(638, 787)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pypordb/8027068_splash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout_4 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(300, 400))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.labelBild1 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelBild1.sizePolicy().hasHeightForWidth())
        self.labelBild1.setSizePolicy(sizePolicy)
        self.labelBild1.setText("")
        self.labelBild1.setObjectName("labelBild1")
        self.gridLayout.addWidget(self.labelBild1, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 622, 340))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelName = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelName.setFont(font)
        self.labelName.setAlignment(QtCore.Qt.AlignCenter)
        self.labelName.setObjectName("labelName")
        self.verticalLayout.addWidget(self.labelName)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelTattoosC = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelTattoosC.setObjectName("labelTattoosC")
        self.gridLayout_2.addWidget(self.labelTattoosC, 0, 0, 1, 1)
        self.plainTextEditTattoos = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEditTattoos.setObjectName("plainTextEditTattoos")
        self.gridLayout_2.addWidget(self.plainTextEditTattoos, 0, 1, 1, 1)
        self.labelUrl = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelUrl.setObjectName("labelUrl")
        self.gridLayout_2.addWidget(self.labelUrl, 1, 0, 1, 1)
        self.labelDateC = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelDateC.setObjectName("labelDateC")
        self.gridLayout_2.addWidget(self.labelDateC, 2, 0, 1, 1)
        self.lineEditDate = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditDate.setReadOnly(True)
        self.lineEditDate.setObjectName("lineEditDate")
        self.gridLayout_2.addWidget(self.lineEditDate, 2, 1, 1, 1)
        self.lineEditUrl = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditUrl.setObjectName("lineEditUrl")
        self.gridLayout_2.addWidget(self.lineEditUrl, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.pushButtonOk = QtWidgets.QPushButton(Dialog)
        self.pushButtonOk.setAutoDefault(False)
        self.pushButtonOk.setDefault(True)
        self.pushButtonOk.setObjectName("pushButtonOk")
        self.verticalLayout_2.addWidget(self.pushButtonOk)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Actor details"))
        self.labelName.setText(_translate("Dialog", "TextLabel"))
        self.labelTattoosC.setText(_translate("Dialog", "Tattoos:"))
        self.labelUrl.setText(_translate("Dialog", "Url on IAFD:"))
        self.labelDateC.setText(_translate("Dialog", "Date added in PorDB:"))
        self.pushButtonOk.setText(_translate("Dialog", "OK"))

