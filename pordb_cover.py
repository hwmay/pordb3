# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_cover.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(638, 548)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pypordb/8027068_splash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(300, 400))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelBild1 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelBild1.sizePolicy().hasHeightForWidth())
        self.labelBild1.setSizePolicy(sizePolicy)
        self.labelBild1.setText("")
        self.labelBild1.setObjectName("labelBild1")
        self.gridLayout_2.addWidget(self.labelBild1, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.labelBilddatei1 = QtWidgets.QLabel(Dialog)
        self.labelBilddatei1.setText("")
        self.labelBilddatei1.setObjectName("labelBilddatei1")
        self.verticalLayout.addWidget(self.labelBilddatei1)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButtonBild1 = QtWidgets.QRadioButton(Dialog)
        self.radioButtonBild1.setText("")
        self.radioButtonBild1.setObjectName("radioButtonBild1")
        self.horizontalLayout_2.addWidget(self.radioButtonBild1)
        self.labelSize1 = QtWidgets.QLabel(Dialog)
        self.labelSize1.setObjectName("labelSize1")
        self.horizontalLayout_2.addWidget(self.labelSize1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(300, 400))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.labelBild2 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelBild2.sizePolicy().hasHeightForWidth())
        self.labelBild2.setSizePolicy(sizePolicy)
        self.labelBild2.setText("")
        self.labelBild2.setObjectName("labelBild2")
        self.gridLayout_3.addWidget(self.labelBild2, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.labelBilddatei2 = QtWidgets.QLabel(Dialog)
        self.labelBilddatei2.setText("")
        self.labelBilddatei2.setObjectName("labelBilddatei2")
        self.verticalLayout_2.addWidget(self.labelBilddatei2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButtonBild2 = QtWidgets.QRadioButton(Dialog)
        self.radioButtonBild2.setText("")
        self.radioButtonBild2.setObjectName("radioButtonBild2")
        self.horizontalLayout_3.addWidget(self.radioButtonBild2)
        self.labelSize2 = QtWidgets.QLabel(Dialog)
        self.labelSize2.setObjectName("labelSize2")
        self.horizontalLayout_3.addWidget(self.labelSize2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEditDateiname = QtWidgets.QLineEdit(Dialog)
        self.lineEditDateiname.setObjectName("lineEditDateiname")
        self.horizontalLayout.addWidget(self.lineEditDateiname)
        self.pushButtonCoverOriginalAlt = QtWidgets.QPushButton(Dialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pypordb/appointment-recurring.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonCoverOriginalAlt.setIcon(icon1)
        self.pushButtonCoverOriginalAlt.setObjectName("pushButtonCoverOriginalAlt")
        self.horizontalLayout.addWidget(self.pushButtonCoverOriginalAlt)
        self.pushButtonCover = QtWidgets.QPushButton(Dialog)
        self.pushButtonCover.setAutoDefault(False)
        self.pushButtonCover.setDefault(True)
        self.pushButtonCover.setObjectName("pushButtonCover")
        self.horizontalLayout.addWidget(self.pushButtonCover)
        self.pushButtonCancel = QtWidgets.QPushButton(Dialog)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.labelOriginal = QtWidgets.QLabel(Dialog)
        self.labelOriginal.setText("")
        self.labelOriginal.setObjectName("labelOriginal")
        self.horizontalLayout_5.addWidget(self.labelOriginal)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Create cover"))
        self.groupBox.setTitle(_translate("Dialog", "Image1"))
        self.labelSize1.setText(_translate("Dialog", "TextLabel"))
        self.groupBox_2.setTitle(_translate("Dialog", "Image2"))
        self.labelSize2.setText(_translate("Dialog", "TextLabel"))
        self.label.setWhatsThis(_translate("Dialog", "Please mark the frontpage. This will be inserted on the left site of the new cover."))
        self.label.setText(_translate("Dialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Please mark the frontpage</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "Filename:"))
        self.lineEditDateiname.setWhatsThis(_translate("Dialog", "Filename of the new cover"))
        self.pushButtonCoverOriginalAlt.setWhatsThis(_translate("Dialog", "Last used original title will be entered"))
        self.pushButtonCover.setText(_translate("Dialog", "Create cover"))
        self.pushButtonCancel.setText(_translate("Dialog", "Cancel"))
        self.label_3.setText(_translate("Dialog", "Title in clipboard:"))

