# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_suchen.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ErweiterteSuche(object):
    def setupUi(self, ErweiterteSuche):
        ErweiterteSuche.setObjectName("ErweiterteSuche")
        ErweiterteSuche.resize(832, 322)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pypordb/8027068_splash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ErweiterteSuche.setWindowIcon(icon)
        self.gridLayout_3 = QtWidgets.QGridLayout(ErweiterteSuche)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtWidgets.QGroupBox(ErweiterteSuche)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditDarsteller = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditDarsteller.setObjectName("lineEditDarsteller")
        self.gridLayout_2.addWidget(self.lineEditDarsteller, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEditCD = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditCD.setObjectName("lineEditCD")
        self.gridLayout_2.addWidget(self.lineEditCD, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEditTitel = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditTitel.setObjectName("lineEditTitel")
        self.gridLayout_2.addWidget(self.lineEditTitel, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEditOriginal = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditOriginal.setObjectName("lineEditOriginal")
        self.gridLayout_2.addWidget(self.lineEditOriginal, 3, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.checkBoxVid = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxVid.setToolTip("")
        self.checkBoxVid.setText("")
        self.checkBoxVid.setObjectName("checkBoxVid")
        self.gridLayout.addWidget(self.checkBoxVid, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 2, 1, 1)
        self.checkBoxNotVid = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxNotVid.setText("")
        self.checkBoxNotVid.setObjectName("checkBoxNotVid")
        self.gridLayout.addWidget(self.checkBoxNotVid, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.checkBoxWatched = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxWatched.setText("")
        self.checkBoxWatched.setObjectName("checkBoxWatched")
        self.gridLayout.addWidget(self.checkBoxWatched, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 2, 1, 1)
        self.checkBoxNotWatched = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxNotWatched.setText("")
        self.checkBoxNotWatched.setObjectName("checkBoxNotWatched")
        self.gridLayout.addWidget(self.checkBoxNotWatched, 1, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 4, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 4, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 5, 0, 1, 1)
        self.comboBoxCS = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxCS.setMaximumSize(QtCore.QSize(723, 16777215))
        self.comboBoxCS.setObjectName("comboBoxCS")
        self.comboBoxCS.addItem("")
        self.comboBoxCS.setItemText(0, "")
        self.comboBoxCS.addItem("")
        self.comboBoxCS.addItem("")
        self.comboBoxCS.addItem("")
        self.comboBoxCS.addItem("")
        self.comboBoxCS.addItem("")
        self.comboBoxCS.addItem("")
        self.comboBoxCS.addItem("")
        self.comboBoxCS.addItem("")
        self.comboBoxCS.addItem("")
        self.comboBoxCS.addItem("")
        self.comboBoxCS.addItem("")
        self.gridLayout_2.addWidget(self.comboBoxCS, 5, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 6, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonStar1 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonStar1.sizePolicy().hasHeightForWidth())
        self.pushButtonStar1.setSizePolicy(sizePolicy)
        self.pushButtonStar1.setMaximumSize(QtCore.QSize(16, 16))
        self.pushButtonStar1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pypordb/non-starred.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonStar1.setIcon(icon1)
        self.pushButtonStar1.setFlat(True)
        self.pushButtonStar1.setObjectName("pushButtonStar1")
        self.horizontalLayout_2.addWidget(self.pushButtonStar1)
        self.pushButtonStar2 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonStar2.sizePolicy().hasHeightForWidth())
        self.pushButtonStar2.setSizePolicy(sizePolicy)
        self.pushButtonStar2.setMaximumSize(QtCore.QSize(16, 16))
        self.pushButtonStar2.setText("")
        self.pushButtonStar2.setIcon(icon1)
        self.pushButtonStar2.setFlat(True)
        self.pushButtonStar2.setObjectName("pushButtonStar2")
        self.horizontalLayout_2.addWidget(self.pushButtonStar2)
        self.pushButtonStar3 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonStar3.sizePolicy().hasHeightForWidth())
        self.pushButtonStar3.setSizePolicy(sizePolicy)
        self.pushButtonStar3.setMaximumSize(QtCore.QSize(16, 16))
        self.pushButtonStar3.setText("")
        self.pushButtonStar3.setIcon(icon1)
        self.pushButtonStar3.setFlat(True)
        self.pushButtonStar3.setObjectName("pushButtonStar3")
        self.horizontalLayout_2.addWidget(self.pushButtonStar3)
        self.pushButtonStar4 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonStar4.sizePolicy().hasHeightForWidth())
        self.pushButtonStar4.setSizePolicy(sizePolicy)
        self.pushButtonStar4.setMaximumSize(QtCore.QSize(16, 16))
        self.pushButtonStar4.setText("")
        self.pushButtonStar4.setIcon(icon1)
        self.pushButtonStar4.setFlat(True)
        self.pushButtonStar4.setObjectName("pushButtonStar4")
        self.horizontalLayout_2.addWidget(self.pushButtonStar4)
        self.pushButtonStar5 = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonStar5.sizePolicy().hasHeightForWidth())
        self.pushButtonStar5.setSizePolicy(sizePolicy)
        self.pushButtonStar5.setMaximumSize(QtCore.QSize(16, 16))
        self.pushButtonStar5.setText("")
        self.pushButtonStar5.setIcon(icon1)
        self.pushButtonStar5.setFlat(True)
        self.pushButtonStar5.setObjectName("pushButtonStar5")
        self.horizontalLayout_2.addWidget(self.pushButtonStar5)
        self.pushButtonClear = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonClear.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("pypordb/clear_l.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonClear.setIcon(icon2)
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.horizontalLayout_2.addWidget(self.pushButtonClear)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 6, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 7, 0, 1, 1)
        self.lineEditRemarks = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditRemarks.setObjectName("lineEditRemarks")
        self.gridLayout_2.addWidget(self.lineEditRemarks, 7, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonSuchen = QtWidgets.QPushButton(ErweiterteSuche)
        self.pushButtonSuchen.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("pypordb/suchen.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSuchen.setIcon(icon3)
        self.pushButtonSuchen.setObjectName("pushButtonSuchen")
        self.horizontalLayout.addWidget(self.pushButtonSuchen)
        self.pushButtonRefresh = QtWidgets.QPushButton(ErweiterteSuche)
        self.pushButtonRefresh.setText("")
        self.pushButtonRefresh.setIcon(icon2)
        self.pushButtonRefresh.setObjectName("pushButtonRefresh")
        self.horizontalLayout.addWidget(self.pushButtonRefresh)
        self.pushButtonCancel = QtWidgets.QPushButton(ErweiterteSuche)
        self.pushButtonCancel.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("pypordb/dialog-cancel.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonCancel.setIcon(icon4)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(ErweiterteSuche)
        QtCore.QMetaObject.connectSlotsByName(ErweiterteSuche)
        ErweiterteSuche.setTabOrder(self.lineEditDarsteller, self.lineEditCD)
        ErweiterteSuche.setTabOrder(self.lineEditCD, self.lineEditTitel)
        ErweiterteSuche.setTabOrder(self.lineEditTitel, self.lineEditOriginal)
        ErweiterteSuche.setTabOrder(self.lineEditOriginal, self.checkBoxVid)
        ErweiterteSuche.setTabOrder(self.checkBoxVid, self.checkBoxWatched)
        ErweiterteSuche.setTabOrder(self.checkBoxWatched, self.comboBoxCS)
        ErweiterteSuche.setTabOrder(self.comboBoxCS, self.pushButtonSuchen)
        ErweiterteSuche.setTabOrder(self.pushButtonSuchen, self.pushButtonRefresh)
        ErweiterteSuche.setTabOrder(self.pushButtonRefresh, self.pushButtonCancel)

    def retranslateUi(self, ErweiterteSuche):
        _translate = QtCore.QCoreApplication.translate
        ErweiterteSuche.setWindowTitle(_translate("ErweiterteSuche", "Extended search"))
        self.groupBox.setTitle(_translate("ErweiterteSuche", "Search criteria"))
        self.label.setText(_translate("ErweiterteSuche", "Actor"))
        self.lineEditDarsteller.setWhatsThis(_translate("ErweiterteSuche", "<html><head/><body><p>Search for actors</p></body></html>"))
        self.label_2.setText(_translate("ErweiterteSuche", "CD"))
        self.lineEditCD.setToolTip(_translate("ErweiterteSuche", "<html><head/><body><p><br/></p></body></html>"))
        self.lineEditCD.setWhatsThis(_translate("ErweiterteSuche", "<html><head/><body><p>Search for data storage medium</p></body></html>"))
        self.label_3.setText(_translate("ErweiterteSuche", "Title"))
        self.lineEditTitel.setWhatsThis(_translate("ErweiterteSuche", "<html><head/><body><p>Search for title</p></body></html>"))
        self.label_4.setText(_translate("ErweiterteSuche", "Original"))
        self.lineEditOriginal.setToolTip(_translate("ErweiterteSuche", "<html><head/><body><p><br/></p></body></html>"))
        self.lineEditOriginal.setWhatsThis(_translate("ErweiterteSuche", "<html><head/><body><p>Search for original title</p></body></html>"))
        self.label_5.setText(_translate("ErweiterteSuche", "Video present"))
        self.checkBoxVid.setWhatsThis(_translate("ErweiterteSuche", "<html><head/><body><p>Filter search results only for videos which are present</p></body></html>"))
        self.label_10.setText(_translate("ErweiterteSuche", "Video not present"))
        self.label_7.setText(_translate("ErweiterteSuche", "Video watched"))
        self.label_11.setText(_translate("ErweiterteSuche", "Video not watched"))
        self.label_6.setText(_translate("ErweiterteSuche", "CS"))
        self.comboBoxCS.setWhatsThis(_translate("ErweiterteSuche", "<html><head/><body><p>Filter search results with cumshots</p></body></html>"))
        self.comboBoxCS.setItemText(1, _translate("ErweiterteSuche", "f Facial"))
        self.comboBoxCS.setItemText(2, _translate("ErweiterteSuche", "h Handjob"))
        self.comboBoxCS.setItemText(3, _translate("ErweiterteSuche", "t Tits"))
        self.comboBoxCS.setItemText(4, _translate("ErweiterteSuche", "c Creampie"))
        self.comboBoxCS.setItemText(5, _translate("ErweiterteSuche", "x Analcreampie"))
        self.comboBoxCS.setItemText(6, _translate("ErweiterteSuche", "o Oralcreampie"))
        self.comboBoxCS.setItemText(7, _translate("ErweiterteSuche", "v Cunt"))
        self.comboBoxCS.setItemText(8, _translate("ErweiterteSuche", "b Belly"))
        self.comboBoxCS.setItemText(9, _translate("ErweiterteSuche", "a Ass"))
        self.comboBoxCS.setItemText(10, _translate("ErweiterteSuche", "s Others"))
        self.comboBoxCS.setItemText(11, _translate("ErweiterteSuche", "k No"))
        self.label_8.setText(_translate("ErweiterteSuche", "Rating"))
        self.label_9.setText(_translate("ErweiterteSuche", "Remarks"))
        self.pushButtonSuchen.setToolTip(_translate("ErweiterteSuche", "<html><head/><body><p>Search (enter)</p></body></html>"))
        self.pushButtonSuchen.setWhatsThis(_translate("ErweiterteSuche", "Start search"))
        self.pushButtonSuchen.setShortcut(_translate("ErweiterteSuche", "Enter"))
        self.pushButtonRefresh.setToolTip(_translate("ErweiterteSuche", "<html><head/><body><p>Clear all search fields, alt+L</p></body></html>"))
        self.pushButtonRefresh.setWhatsThis(_translate("ErweiterteSuche", "Clear all fields in search form"))
        self.pushButtonRefresh.setShortcut(_translate("ErweiterteSuche", "Alt+L"))
        self.pushButtonCancel.setToolTip(_translate("ErweiterteSuche", "<html><head/><body><p>Cancel (escape)</p></body></html>"))
        self.pushButtonCancel.setWhatsThis(_translate("ErweiterteSuche", "<html><head/><body><p>Cancel search</p></body></html>"))

