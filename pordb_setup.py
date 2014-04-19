# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_setup.ui'
#
# Created: Sat Apr 19 22:40:48 2014
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
        Dialog.resize(638, 319)
        self.formLayout_4 = QtGui.QFormLayout(Dialog)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.tab_2)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.layoutWidget = QtGui.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 531, 215))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.listWidgetDB = QtGui.QListWidget(self.layoutWidget)
        self.listWidgetDB.setObjectName(_fromUtf8("listWidgetDB"))
        self.verticalLayout.addWidget(self.listWidgetDB)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.formLayout = QtGui.QFormLayout(self.tab_3)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_5 = QtGui.QLabel(self.tab_3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.pushButtonDir = QtGui.QPushButton(self.tab_3)
        self.pushButtonDir.setObjectName(_fromUtf8("pushButtonDir"))
        self.horizontalLayout_3.addWidget(self.pushButtonDir)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.labelDirectory = QtGui.QLabel(self.tab_3)
        self.labelDirectory.setObjectName(_fromUtf8("labelDirectory"))
        self.verticalLayout_3.addWidget(self.labelDirectory)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_7 = QtGui.QLabel(self.tab_3)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_4.addWidget(self.label_7)
        self.pushButtonZip = QtGui.QPushButton(self.tab_3)
        self.pushButtonZip.setObjectName(_fromUtf8("pushButtonZip"))
        self.horizontalLayout_4.addWidget(self.pushButtonZip)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.labelFile = QtGui.QLabel(self.tab_3)
        self.labelFile.setObjectName(_fromUtf8("labelFile"))
        self.verticalLayout_3.addWidget(self.labelFile)
        self.formLayout.setLayout(0, QtGui.QFormLayout.LabelRole, self.verticalLayout_3)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.formLayout_3 = QtGui.QFormLayout(self.tab_4)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_9 = QtGui.QLabel(self.tab_4)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_9)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_5)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.listWidget = QtGui.QListWidget(self.tab_5)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout_4.addWidget(self.listWidget)
        self.label_10 = QtGui.QLabel(self.tab_5)
        self.label_10.setText(_fromUtf8(""))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_4.addWidget(self.label_10)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.verticalLayout_5.addWidget(self.tabWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonBack = QtGui.QPushButton(Dialog)
        self.pushButtonBack.setObjectName(_fromUtf8("pushButtonBack"))
        self.horizontalLayout.addWidget(self.pushButtonBack)
        self.pushButtonNext = QtGui.QPushButton(Dialog)
        self.pushButtonNext.setObjectName(_fromUtf8("pushButtonNext"))
        self.horizontalLayout.addWidget(self.pushButtonNext)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.formLayout_4.setLayout(0, QtGui.QFormLayout.LabelRole, self.verticalLayout_5)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "PorDB3 Setup", None))
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
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">When these directories already exist, they will not be changed!</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Step 1 of 5", None))
        self.label.setText(_translate("Dialog", "Database", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Step 2 of 5", None))
        self.label_5.setText(_translate("Dialog", "Select the directory where to install PorDB3:", None))
        self.pushButtonDir.setText(_translate("Dialog", "Select or create directory", None))
        self.labelDirectory.setText(_translate("Dialog", "Directory: ", None))
        self.label_7.setText(_translate("Dialog", "Select the zip file of the downloaded PorDB3:", None))
        self.pushButtonZip.setText(_translate("Dialog", "Select", None))
        self.labelFile.setText(_translate("Dialog", "File: ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Step 3 of 5", None))
        self.label_9.setText(_translate("Dialog", "Click on the Next button to install the PorDB3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Step 4 of 5", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Dialog", "Step 5 of 5", None))
        self.pushButtonBack.setText(_translate("Dialog", "Back", None))
        self.pushButtonNext.setText(_translate("Dialog", "Next", None))

