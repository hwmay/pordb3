# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_setup.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(638, 319)
        self.formLayout_4 = QtWidgets.QFormLayout(Dialog)
        self.formLayout_4.setObjectName("formLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.tab_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 531, 215))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listWidgetDB = QtWidgets.QListWidget(self.layoutWidget)
        self.listWidgetDB.setObjectName("listWidgetDB")
        self.verticalLayout.addWidget(self.listWidgetDB)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.formLayout = QtWidgets.QFormLayout(self.tab_3)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.pushButtonDir = QtWidgets.QPushButton(self.tab_3)
        self.pushButtonDir.setObjectName("pushButtonDir")
        self.horizontalLayout_3.addWidget(self.pushButtonDir)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.labelDirectory = QtWidgets.QLabel(self.tab_3)
        self.labelDirectory.setObjectName("labelDirectory")
        self.verticalLayout_3.addWidget(self.labelDirectory)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.pushButtonZip = QtWidgets.QPushButton(self.tab_3)
        self.pushButtonZip.setObjectName("pushButtonZip")
        self.horizontalLayout_4.addWidget(self.pushButtonZip)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.labelFile = QtWidgets.QLabel(self.tab_3)
        self.labelFile.setObjectName("labelFile")
        self.verticalLayout_3.addWidget(self.labelFile)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_3)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.formLayout_3 = QtWidgets.QFormLayout(self.tab_4)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_9 = QtWidgets.QLabel(self.tab_4)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.listWidget = QtWidgets.QListWidget(self.tab_5)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_4.addWidget(self.listWidget)
        self.label_10 = QtWidgets.QLabel(self.tab_5)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonBack = QtWidgets.QPushButton(Dialog)
        self.pushButtonBack.setObjectName("pushButtonBack")
        self.horizontalLayout.addWidget(self.pushButtonBack)
        self.pushButtonNext = QtWidgets.QPushButton(Dialog)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.horizontalLayout.addWidget(self.pushButtonNext)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.formLayout_4.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_5)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PorDB3 Setup"))
        self.label_3.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Welcome to the PorDB3</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This will install the PorDB3 on your computer.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 directories will be created in your home directory: </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. mpg: this is the working directory</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. thumbs_sammlung: this is the container for all thumbs, covers and pictures of actors</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">When these directories already exist, they will not be changed!</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Step 1 of 5"))
        self.label.setText(_translate("Dialog", "Database"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Step 2 of 5"))
        self.label_5.setText(_translate("Dialog", "Select the directory where to install PorDB3:"))
        self.pushButtonDir.setText(_translate("Dialog", "Select or create directory"))
        self.labelDirectory.setText(_translate("Dialog", "Directory: "))
        self.label_7.setText(_translate("Dialog", "Select the zip file of the downloaded PorDB3:"))
        self.pushButtonZip.setText(_translate("Dialog", "Select"))
        self.labelFile.setText(_translate("Dialog", "File: "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Step 3 of 5"))
        self.label_9.setText(_translate("Dialog", "Click on the Next button to install the PorDB3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Step 4 of 5"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Dialog", "Step 5 of 5"))
        self.pushButtonBack.setText(_translate("Dialog", "Back"))
        self.pushButtonNext.setText(_translate("Dialog", "Next"))

