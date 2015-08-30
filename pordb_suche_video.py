# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_suche_video.ui'
#
# Created: Sun Aug 30 19:55:05 2015
#      by: PyQt4 UI code generator 4.11.3
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
        Dialog.resize(1003, 720)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("pypordb/8027068_splash.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 989, 675))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.listWidgetVideo = QtGui.QListWidget(self.scrollAreaWidgetContents)
        self.listWidgetVideo.setMinimumSize(QtCore.QSize(20, 0))
        self.listWidgetVideo.setMaximumSize(QtCore.QSize(20, 16777215))
        self.listWidgetVideo.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listWidgetVideo.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.listWidgetVideo.setViewMode(QtGui.QListView.ListMode)
        self.listWidgetVideo.setObjectName(_fromUtf8("listWidgetVideo"))
        self.horizontalLayout.addWidget(self.listWidgetVideo)
        self.textEditVideo = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        self.textEditVideo.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEditVideo.setObjectName(_fromUtf8("textEditVideo"))
        self.horizontalLayout.addWidget(self.textEditVideo)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_insgesamt = QtGui.QLabel(Dialog)
        self.label_insgesamt.setText(_fromUtf8(""))
        self.label_insgesamt.setObjectName(_fromUtf8("label_insgesamt"))
        self.horizontalLayout_2.addWidget(self.label_insgesamt)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_vorhanden = QtGui.QLabel(Dialog)
        self.label_vorhanden.setText(_fromUtf8(""))
        self.label_vorhanden.setObjectName(_fromUtf8("label_vorhanden"))
        self.horizontalLayout_2.addWidget(self.label_vorhanden)
        spacerItem = QtGui.QSpacerItem(378, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButtonSuchen = QtGui.QPushButton(Dialog)
        self.pushButtonSuchen.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("pypordb/suchen.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSuchen.setIcon(icon1)
        self.pushButtonSuchen.setObjectName(_fromUtf8("pushButtonSuchen"))
        self.horizontalLayout_2.addWidget(self.pushButtonSuchen)
        self.pushButtonAnzeigen = QtGui.QPushButton(Dialog)
        self.pushButtonAnzeigen.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("pypordb/video.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonAnzeigen.setIcon(icon2)
        self.pushButtonAnzeigen.setObjectName(_fromUtf8("pushButtonAnzeigen"))
        self.horizontalLayout_2.addWidget(self.pushButtonAnzeigen)
        self.pushButtonAbbrechen = QtGui.QPushButton(Dialog)
        self.pushButtonAbbrechen.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("pypordb/dialog-cancel.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonAbbrechen.setIcon(icon3)
        self.pushButtonAbbrechen.setObjectName(_fromUtf8("pushButtonAbbrechen"))
        self.horizontalLayout_2.addWidget(self.pushButtonAbbrechen)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Search in existing movies", None))
        self.listWidgetVideo.setToolTip(_translate("Dialog", "Presentation of the existing movies", None))
        self.listWidgetVideo.setWhatsThis(_translate("Dialog", "Presentation of the existing movies", None))
        self.textEditVideo.setWhatsThis(_translate("Dialog", "Insert text (Ctrl+v)", None))
        self.label_2.setText(_translate("Dialog", "overall:", None))
        self.label_3.setText(_translate("Dialog", "available:", None))
        self.pushButtonSuchen.setToolTip(_translate("Dialog", "Start search (Ctrl+S)", None))
        self.pushButtonSuchen.setWhatsThis(_translate("Dialog", "Starts searching", None))
        self.pushButtonSuchen.setShortcut(_translate("Dialog", "Ctrl+S", None))
        self.pushButtonAnzeigen.setToolTip(_translate("Dialog", "<html><head/><body><p>Show movies (Ctrl+D)</p></body></html>", None))
        self.pushButtonAnzeigen.setWhatsThis(_translate("Dialog", "Shows avaible movies", None))
        self.pushButtonAnzeigen.setShortcut(_translate("Dialog", "Ctrl+D", None))
        self.pushButtonAbbrechen.setToolTip(_translate("Dialog", "Cancel (Esc)", None))

