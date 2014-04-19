# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_actor_details.ui'
#
# Created: Mon Feb 24 17:52:30 2014
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
        Dialog.resize(638, 787)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("pypordb/8027068_splash.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout_4 = QtGui.QGridLayout(Dialog)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(300, 400))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labelBild1 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelBild1.sizePolicy().hasHeightForWidth())
        self.labelBild1.setSizePolicy(sizePolicy)
        self.labelBild1.setText(_fromUtf8(""))
        self.labelBild1.setObjectName(_fromUtf8("labelBild1"))
        self.gridLayout.addWidget(self.labelBild1, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 622, 340))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_3 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelName = QtGui.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelName.setFont(font)
        self.labelName.setAlignment(QtCore.Qt.AlignCenter)
        self.labelName.setObjectName(_fromUtf8("labelName"))
        self.verticalLayout.addWidget(self.labelName)
        self.line = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.labelTattoosC = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.labelTattoosC.setObjectName(_fromUtf8("labelTattoosC"))
        self.gridLayout_2.addWidget(self.labelTattoosC, 0, 0, 1, 1)
        self.plainTextEditTattoos = QtGui.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEditTattoos.setReadOnly(True)
        self.plainTextEditTattoos.setObjectName(_fromUtf8("plainTextEditTattoos"))
        self.gridLayout_2.addWidget(self.plainTextEditTattoos, 0, 1, 1, 1)
        self.labelUrl = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.labelUrl.setObjectName(_fromUtf8("labelUrl"))
        self.gridLayout_2.addWidget(self.labelUrl, 1, 0, 1, 1)
        self.textEditUrl = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        self.textEditUrl.setReadOnly(True)
        self.textEditUrl.setObjectName(_fromUtf8("textEditUrl"))
        self.gridLayout_2.addWidget(self.textEditUrl, 1, 1, 1, 1)
        self.labelDateC = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.labelDateC.setObjectName(_fromUtf8("labelDateC"))
        self.gridLayout_2.addWidget(self.labelDateC, 2, 0, 1, 1)
        self.lineEditDate = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEditDate.setReadOnly(True)
        self.lineEditDate.setObjectName(_fromUtf8("lineEditDate"))
        self.gridLayout_2.addWidget(self.lineEditDate, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.pushButtonOk = QtGui.QPushButton(Dialog)
        self.pushButtonOk.setAutoDefault(False)
        self.pushButtonOk.setDefault(True)
        self.pushButtonOk.setObjectName(_fromUtf8("pushButtonOk"))
        self.verticalLayout_2.addWidget(self.pushButtonOk)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "PorDB actor details", None))
        self.labelName.setText(_translate("Dialog", "TextLabel", None))
        self.labelTattoosC.setText(_translate("Dialog", "Tattoos:", None))
        self.labelUrl.setText(_translate("Dialog", "Url on IAFD:", None))
        self.labelDateC.setText(_translate("Dialog", "Date added in PorDB:", None))
        self.pushButtonOk.setText(_translate("Dialog", "OK", None))

