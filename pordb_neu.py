# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pordb_neu.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1388, 561)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pypordb/8027068_splash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setMinimumSize(QtCore.QSize(130, 59))
        self.groupBox_4.setWhatsThis("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_4)
        self.formLayout_2.setObjectName("formLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButtonVorhandenJa = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButtonVorhandenJa.setObjectName("radioButtonVorhandenJa")
        self.horizontalLayout_3.addWidget(self.radioButtonVorhandenJa)
        self.radioButtonVorhandenNein = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButtonVorhandenNein.setObjectName("radioButtonVorhandenNein")
        self.horizontalLayout_3.addWidget(self.radioButtonVorhandenNein)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_3)
        self.horizontalLayout_11.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_5.setMinimumSize(QtCore.QSize(130, 59))
        self.groupBox_5.setObjectName("groupBox_5")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox_5)
        self.formLayout_3.setObjectName("formLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radioButtonGesehenJa = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButtonGesehenJa.setObjectName("radioButtonGesehenJa")
        self.horizontalLayout_4.addWidget(self.radioButtonGesehenJa)
        self.radioButtonGesehenNein = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButtonGesehenNein.setObjectName("radioButtonGesehenNein")
        self.horizontalLayout_4.addWidget(self.radioButtonGesehenNein)
        self.formLayout_3.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_4)
        self.horizontalLayout_11.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_6.setMinimumSize(QtCore.QSize(130, 59))
        self.groupBox_6.setWhatsThis("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.formLayout_4 = QtWidgets.QFormLayout(self.groupBox_6)
        self.formLayout_4.setObjectName("formLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.radioButtonCoverJa = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioButtonCoverJa.setObjectName("radioButtonCoverJa")
        self.horizontalLayout_6.addWidget(self.radioButtonCoverJa)
        self.radioButtonCoverNein = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioButtonCoverNein.setObjectName("radioButtonCoverNein")
        self.horizontalLayout_6.addWidget(self.radioButtonCoverNein)
        self.formLayout_4.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_6)
        self.horizontalLayout_11.addWidget(self.groupBox_6)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_13.addWidget(self.label_8)
        self.labelOriginal = QtWidgets.QLabel(Dialog)
        self.labelOriginal.setText("")
        self.labelOriginal.setObjectName("labelOriginal")
        self.horizontalLayout_13.addWidget(self.labelOriginal)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.checkBoxUninteressant = QtWidgets.QCheckBox(Dialog)
        self.checkBoxUninteressant.setObjectName("checkBoxUninteressant")
        self.horizontalLayout_7.addWidget(self.checkBoxUninteressant)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_7.addWidget(self.line)
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_7.addWidget(self.label_17)
        self.comboBoxDefinition = QtWidgets.QComboBox(Dialog)
        self.comboBoxDefinition.setIconSize(QtCore.QSize(10, 10))
        self.comboBoxDefinition.setObjectName("comboBoxDefinition")
        self.comboBoxDefinition.addItem("")
        self.comboBoxDefinition.setItemText(0, "")
        self.comboBoxDefinition.addItem("")
        self.comboBoxDefinition.addItem("")
        self.comboBoxDefinition.addItem("")
        self.comboBoxDefinition.addItem("")
        self.comboBoxDefinition.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBoxDefinition)
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_7.addWidget(self.label_18)
        self.pushButtonStar1 = QtWidgets.QPushButton(Dialog)
        self.pushButtonStar1.setMaximumSize(QtCore.QSize(16, 16))
        self.pushButtonStar1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pypordb/non-starred.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonStar1.setIcon(icon1)
        self.pushButtonStar1.setFlat(True)
        self.pushButtonStar1.setObjectName("pushButtonStar1")
        self.horizontalLayout_7.addWidget(self.pushButtonStar1)
        self.pushButtonStar2 = QtWidgets.QPushButton(Dialog)
        self.pushButtonStar2.setMaximumSize(QtCore.QSize(16, 16))
        self.pushButtonStar2.setText("")
        self.pushButtonStar2.setIcon(icon1)
        self.pushButtonStar2.setFlat(True)
        self.pushButtonStar2.setObjectName("pushButtonStar2")
        self.horizontalLayout_7.addWidget(self.pushButtonStar2)
        self.pushButtonStar3 = QtWidgets.QPushButton(Dialog)
        self.pushButtonStar3.setMaximumSize(QtCore.QSize(16, 16))
        self.pushButtonStar3.setText("")
        self.pushButtonStar3.setIcon(icon1)
        self.pushButtonStar3.setFlat(True)
        self.pushButtonStar3.setObjectName("pushButtonStar3")
        self.horizontalLayout_7.addWidget(self.pushButtonStar3)
        self.pushButtonStar4 = QtWidgets.QPushButton(Dialog)
        self.pushButtonStar4.setMaximumSize(QtCore.QSize(16, 16))
        self.pushButtonStar4.setText("")
        self.pushButtonStar4.setIcon(icon1)
        self.pushButtonStar4.setFlat(True)
        self.pushButtonStar4.setObjectName("pushButtonStar4")
        self.horizontalLayout_7.addWidget(self.pushButtonStar4)
        self.pushButtonStar5 = QtWidgets.QPushButton(Dialog)
        self.pushButtonStar5.setMaximumSize(QtCore.QSize(16, 16))
        self.pushButtonStar5.setText("")
        self.pushButtonStar5.setIcon(icon1)
        self.pushButtonStar5.setFlat(True)
        self.pushButtonStar5.setObjectName("pushButtonStar5")
        self.horizontalLayout_7.addWidget(self.pushButtonStar5)
        self.pushButtonClearRating = QtWidgets.QPushButton(Dialog)
        self.pushButtonClearRating.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButtonClearRating.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("pypordb/clear_l.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonClearRating.setIcon(icon2)
        self.pushButtonClearRating.setIconSize(QtCore.QSize(10, 10))
        self.pushButtonClearRating.setObjectName("pushButtonClearRating")
        self.horizontalLayout_7.addWidget(self.pushButtonClearRating)
        spacerItem1 = QtWidgets.QSpacerItem(358, 22, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_10.addLayout(self.verticalLayout)
        self.gridLayout_2.addLayout(self.horizontalLayout_10, 1, 0, 1, 2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.spinBoxF = QtWidgets.QSpinBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxF.sizePolicy().hasHeightForWidth())
        self.spinBoxF.setSizePolicy(sizePolicy)
        self.spinBoxF.setObjectName("spinBoxF")
        self.horizontalLayout_5.addWidget(self.spinBoxF)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.spinBoxH = QtWidgets.QSpinBox(Dialog)
        self.spinBoxH.setObjectName("spinBoxH")
        self.horizontalLayout_5.addWidget(self.spinBoxH)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.spinBoxT = QtWidgets.QSpinBox(Dialog)
        self.spinBoxT.setObjectName("spinBoxT")
        self.horizontalLayout_5.addWidget(self.spinBoxT)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.spinBoxC = QtWidgets.QSpinBox(Dialog)
        self.spinBoxC.setObjectName("spinBoxC")
        self.horizontalLayout_5.addWidget(self.spinBoxC)
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.spinBoxX = QtWidgets.QSpinBox(Dialog)
        self.spinBoxX.setObjectName("spinBoxX")
        self.horizontalLayout_5.addWidget(self.spinBoxX)
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_5.addWidget(self.label_11)
        self.spinBoxO = QtWidgets.QSpinBox(Dialog)
        self.spinBoxO.setObjectName("spinBoxO")
        self.horizontalLayout_5.addWidget(self.spinBoxO)
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_5.addWidget(self.label_12)
        self.spinBoxV = QtWidgets.QSpinBox(Dialog)
        self.spinBoxV.setObjectName("spinBoxV")
        self.horizontalLayout_5.addWidget(self.spinBoxV)
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_5.addWidget(self.label_13)
        self.spinBoxB = QtWidgets.QSpinBox(Dialog)
        self.spinBoxB.setObjectName("spinBoxB")
        self.horizontalLayout_5.addWidget(self.spinBoxB)
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_5.addWidget(self.label_14)
        self.spinBoxA = QtWidgets.QSpinBox(Dialog)
        self.spinBoxA.setObjectName("spinBoxA")
        self.horizontalLayout_5.addWidget(self.spinBoxA)
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_5.addWidget(self.label_15)
        self.spinBoxS = QtWidgets.QSpinBox(Dialog)
        self.spinBoxS.setObjectName("spinBoxS")
        self.horizontalLayout_5.addWidget(self.spinBoxS)
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_5.addWidget(self.label_16)
        self.spinBoxK = QtWidgets.QSpinBox(Dialog)
        self.spinBoxK.setObjectName("spinBoxK")
        self.horizontalLayout_5.addWidget(self.spinBoxK)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 2, 0, 1, 2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButtonNeuDarstelleruebernehmen = QtWidgets.QPushButton(Dialog)
        self.pushButtonNeuDarstelleruebernehmen.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("pypordb/go-up.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonNeuDarstelleruebernehmen.setIcon(icon3)
        self.pushButtonNeuDarstelleruebernehmen.setIconSize(QtCore.QSize(24, 24))
        self.pushButtonNeuDarstelleruebernehmen.setCheckable(False)
        self.pushButtonNeuDarstelleruebernehmen.setObjectName("pushButtonNeuDarstelleruebernehmen")
        self.verticalLayout_3.addWidget(self.pushButtonNeuDarstelleruebernehmen)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.listWidgetW = QtWidgets.QListWidget(Dialog)
        self.listWidgetW.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidgetW.setObjectName("listWidgetW")
        self.horizontalLayout_8.addWidget(self.listWidgetW)
        self.listWidgetM = QtWidgets.QListWidget(Dialog)
        self.listWidgetM.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidgetM.setObjectName("listWidgetM")
        self.horizontalLayout_8.addWidget(self.listWidgetM)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 3, 0, 1, 1)
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonBildbeschneiden = QtWidgets.QPushButton(Dialog)
        self.pushButtonBildbeschneiden.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("pypordb/transform-crop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonBildbeschneiden.setIcon(icon4)
        self.pushButtonBildbeschneiden.setIconSize(QtCore.QSize(10, 10))
        self.pushButtonBildbeschneiden.setObjectName("pushButtonBildbeschneiden")
        self.horizontalLayout.addWidget(self.pushButtonBildbeschneiden)
        self.pushButtonBildloeschen = QtWidgets.QPushButton(Dialog)
        self.pushButtonBildloeschen.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("pypordb/user-trash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonBildloeschen.setIcon(icon5)
        self.pushButtonBildloeschen.setIconSize(QtCore.QSize(10, 10))
        self.pushButtonBildloeschen.setObjectName("pushButtonBildloeschen")
        self.horizontalLayout.addWidget(self.pushButtonBildloeschen)
        self.pushButtonNeuOK = QtWidgets.QPushButton(Dialog)
        self.pushButtonNeuOK.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("pypordb/media-floppy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonNeuOK.setIcon(icon6)
        self.pushButtonNeuOK.setIconSize(QtCore.QSize(10, 10))
        self.pushButtonNeuOK.setAutoDefault(False)
        self.pushButtonNeuOK.setDefault(True)
        self.pushButtonNeuOK.setObjectName("pushButtonNeuOK")
        self.horizontalLayout.addWidget(self.pushButtonNeuOK)
        self.pushButtonNeuCancel = QtWidgets.QPushButton(Dialog)
        self.pushButtonNeuCancel.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("pypordb/dialog-cancel.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonNeuCancel.setIcon(icon7)
        self.pushButtonNeuCancel.setIconSize(QtCore.QSize(10, 10))
        self.pushButtonNeuCancel.setObjectName("pushButtonNeuCancel")
        self.horizontalLayout.addWidget(self.pushButtonNeuCancel)
        self.pushButtonNeuDelete = QtWidgets.QPushButton(Dialog)
        self.pushButtonNeuDelete.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("pypordb/user-trash.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonNeuDelete.setIcon(icon8)
        self.pushButtonNeuDelete.setIconSize(QtCore.QSize(10, 10))
        self.pushButtonNeuDelete.setObjectName("pushButtonNeuDelete")
        self.horizontalLayout.addWidget(self.pushButtonNeuDelete)
        self.pushButtonVerz = QtWidgets.QPushButton(Dialog)
        self.pushButtonVerz.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("pypordb/folder.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonVerz.setIcon(icon9)
        self.pushButtonVerz.setIconSize(QtCore.QSize(10, 10))
        self.pushButtonVerz.setObjectName("pushButtonVerz")
        self.horizontalLayout.addWidget(self.pushButtonVerz)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.formLayout_5.setLayout(2, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setMinimumSize(QtCore.QSize(500, 200))
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.labelNeuBildanzeige = QtWidgets.QLabel(self.groupBox_2)
        self.labelNeuBildanzeige.setText("")
        self.labelNeuBildanzeige.setObjectName("labelNeuBildanzeige")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelNeuBildanzeige)
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.groupBox_2)
        self.label_19 = QtWidgets.QLabel(Dialog)
        self.label_19.setObjectName("label_19")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_19)
        self.plainTextEditRemarks = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEditRemarks.setObjectName("plainTextEditRemarks")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.plainTextEditRemarks)
        self.gridLayout_2.addLayout(self.formLayout_5, 3, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEditNeuTitel = QtWidgets.QLineEdit(Dialog)
        self.lineEditNeuTitel.setObjectName("lineEditNeuTitel")
        self.gridLayout.addWidget(self.lineEditNeuTitel, 0, 1, 1, 1)
        self.lineEditNeuCD = QtWidgets.QLineEdit(Dialog)
        self.lineEditNeuCD.setObjectName("lineEditNeuCD")
        self.gridLayout.addWidget(self.lineEditNeuCD, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.pushButtonOriginalAlt = QtWidgets.QPushButton(Dialog)
        self.pushButtonOriginalAlt.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("pypordb/appointment-recurring.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButtonOriginalAlt.setIcon(icon10)
        self.pushButtonOriginalAlt.setIconSize(QtCore.QSize(10, 10))
        self.pushButtonOriginalAlt.setAutoDefault(True)
        self.pushButtonOriginalAlt.setObjectName("pushButtonOriginalAlt")
        self.gridLayout.addWidget(self.pushButtonOriginalAlt, 4, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEditNeuBild = QtWidgets.QLineEdit(Dialog)
        self.lineEditNeuBild.setReadOnly(True)
        self.lineEditNeuBild.setObjectName("lineEditNeuBild")
        self.gridLayout.addWidget(self.lineEditNeuBild, 3, 1, 1, 1)
        self.lineEditNeuOriginal = QtWidgets.QLineEdit(Dialog)
        self.lineEditNeuOriginal.setObjectName("lineEditNeuOriginal")
        self.gridLayout.addWidget(self.lineEditNeuOriginal, 4, 1, 1, 1)
        self.pushButtonOriginal = QtWidgets.QPushButton(Dialog)
        self.pushButtonOriginal.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("pypordb/go-next.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonOriginal.setIcon(icon11)
        self.pushButtonOriginal.setIconSize(QtCore.QSize(10, 10))
        self.pushButtonOriginal.setObjectName("pushButtonOriginal")
        self.gridLayout.addWidget(self.pushButtonOriginal, 4, 6, 1, 1)
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEditNeuDarsteller = QtWidgets.QLineEdit(Dialog)
        self.lineEditNeuDarsteller.setToolTip("")
        self.lineEditNeuDarsteller.setObjectName("lineEditNeuDarsteller")
        self.gridLayout.addWidget(self.lineEditNeuDarsteller, 1, 1, 1, 1)
        self.pushButtonAddYear = QtWidgets.QPushButton(Dialog)
        self.pushButtonAddYear.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("pypordb/x-office-calendar-symbolic.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonAddYear.setIcon(icon12)
        self.pushButtonAddYear.setIconSize(QtCore.QSize(10, 10))
        self.pushButtonAddYear.setObjectName("pushButtonAddYear")
        self.gridLayout.addWidget(self.pushButtonAddYear, 4, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.comboBoxYear = QtWidgets.QComboBox(Dialog)
        self.comboBoxYear.setObjectName("comboBoxYear")
        self.gridLayout.addWidget(self.comboBoxYear, 4, 3, 1, 1)
        self.pushButtonRepeat = QtWidgets.QPushButton(Dialog)
        self.pushButtonRepeat.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("pypordb/repeat.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonRepeat.setIcon(icon13)
        self.pushButtonRepeat.setIconSize(QtCore.QSize(10, 10))
        self.pushButtonRepeat.setObjectName("pushButtonRepeat")
        self.gridLayout.addWidget(self.pushButtonRepeat, 3, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEditNeuTitel, self.lineEditNeuDarsteller)
        Dialog.setTabOrder(self.lineEditNeuDarsteller, self.lineEditNeuCD)
        Dialog.setTabOrder(self.lineEditNeuCD, self.lineEditNeuBild)
        Dialog.setTabOrder(self.lineEditNeuBild, self.lineEditNeuOriginal)
        Dialog.setTabOrder(self.lineEditNeuOriginal, self.pushButtonRepeat)
        Dialog.setTabOrder(self.pushButtonRepeat, self.pushButtonOriginalAlt)
        Dialog.setTabOrder(self.pushButtonOriginalAlt, self.comboBoxYear)
        Dialog.setTabOrder(self.comboBoxYear, self.pushButtonAddYear)
        Dialog.setTabOrder(self.pushButtonAddYear, self.pushButtonOriginal)
        Dialog.setTabOrder(self.pushButtonOriginal, self.radioButtonVorhandenJa)
        Dialog.setTabOrder(self.radioButtonVorhandenJa, self.radioButtonVorhandenNein)
        Dialog.setTabOrder(self.radioButtonVorhandenNein, self.radioButtonGesehenJa)
        Dialog.setTabOrder(self.radioButtonGesehenJa, self.radioButtonGesehenNein)
        Dialog.setTabOrder(self.radioButtonGesehenNein, self.radioButtonCoverJa)
        Dialog.setTabOrder(self.radioButtonCoverJa, self.radioButtonCoverNein)
        Dialog.setTabOrder(self.radioButtonCoverNein, self.checkBoxUninteressant)
        Dialog.setTabOrder(self.checkBoxUninteressant, self.comboBoxDefinition)
        Dialog.setTabOrder(self.comboBoxDefinition, self.pushButtonStar1)
        Dialog.setTabOrder(self.pushButtonStar1, self.pushButtonStar2)
        Dialog.setTabOrder(self.pushButtonStar2, self.pushButtonStar3)
        Dialog.setTabOrder(self.pushButtonStar3, self.pushButtonStar4)
        Dialog.setTabOrder(self.pushButtonStar4, self.pushButtonStar5)
        Dialog.setTabOrder(self.pushButtonStar5, self.pushButtonClearRating)
        Dialog.setTabOrder(self.pushButtonClearRating, self.spinBoxF)
        Dialog.setTabOrder(self.spinBoxF, self.spinBoxH)
        Dialog.setTabOrder(self.spinBoxH, self.spinBoxT)
        Dialog.setTabOrder(self.spinBoxT, self.spinBoxC)
        Dialog.setTabOrder(self.spinBoxC, self.spinBoxX)
        Dialog.setTabOrder(self.spinBoxX, self.spinBoxO)
        Dialog.setTabOrder(self.spinBoxO, self.spinBoxV)
        Dialog.setTabOrder(self.spinBoxV, self.spinBoxB)
        Dialog.setTabOrder(self.spinBoxB, self.spinBoxA)
        Dialog.setTabOrder(self.spinBoxA, self.spinBoxS)
        Dialog.setTabOrder(self.spinBoxS, self.spinBoxK)
        Dialog.setTabOrder(self.spinBoxK, self.pushButtonNeuDarstelleruebernehmen)
        Dialog.setTabOrder(self.pushButtonNeuDarstelleruebernehmen, self.listWidgetW)
        Dialog.setTabOrder(self.listWidgetW, self.listWidgetM)
        Dialog.setTabOrder(self.listWidgetM, self.plainTextEditRemarks)
        Dialog.setTabOrder(self.plainTextEditRemarks, self.pushButtonBildbeschneiden)
        Dialog.setTabOrder(self.pushButtonBildbeschneiden, self.pushButtonBildloeschen)
        Dialog.setTabOrder(self.pushButtonBildloeschen, self.pushButtonNeuOK)
        Dialog.setTabOrder(self.pushButtonNeuOK, self.pushButtonNeuCancel)
        Dialog.setTabOrder(self.pushButtonNeuCancel, self.pushButtonNeuDelete)
        Dialog.setTabOrder(self.pushButtonNeuDelete, self.pushButtonVerz)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "New / Change / Delete"))
        self.groupBox_4.setTitle(_translate("Dialog", "present"))
        self.radioButtonVorhandenJa.setWhatsThis(_translate("Dialog", "Mark here when video is present."))
        self.radioButtonVorhandenJa.setText(_translate("Dialog", "yes"))
        self.radioButtonVorhandenNein.setWhatsThis(_translate("Dialog", "Mark here when video is NOT present."))
        self.radioButtonVorhandenNein.setText(_translate("Dialog", "no"))
        self.groupBox_5.setTitle(_translate("Dialog", "watched"))
        self.radioButtonGesehenJa.setWhatsThis(_translate("Dialog", "Mark here when this video has been watched."))
        self.radioButtonGesehenJa.setText(_translate("Dialog", "yes"))
        self.radioButtonGesehenNein.setWhatsThis(_translate("Dialog", "Mark here when this video has NOT yet watched."))
        self.radioButtonGesehenNein.setText(_translate("Dialog", "no"))
        self.groupBox_6.setTitle(_translate("Dialog", "Cover"))
        self.radioButtonCoverJa.setWhatsThis(_translate("Dialog", "Mark here when the image to be added in database is a video cover."))
        self.radioButtonCoverJa.setText(_translate("Dialog", "yes"))
        self.radioButtonCoverNein.setWhatsThis(_translate("Dialog", "Mark here when the image to be added in database is NOT a video cover."))
        self.radioButtonCoverNein.setText(_translate("Dialog", "no"))
        self.label_8.setText(_translate("Dialog", "Title in clipboard:"))
        self.checkBoxUninteressant.setWhatsThis(_translate("Dialog", "Check this box, if you did not like the movie"))
        self.checkBoxUninteressant.setText(_translate("Dialog", "Not interesting"))
        self.label_17.setWhatsThis(_translate("Dialog", "Please select the resolution of the clip."))
        self.label_17.setText(_translate("Dialog", "Resolution:"))
        self.comboBoxDefinition.setItemText(1, _translate("Dialog", "SD"))
        self.comboBoxDefinition.setItemText(2, _translate("Dialog", "HD 720p"))
        self.comboBoxDefinition.setItemText(3, _translate("Dialog", "HD 1080p"))
        self.comboBoxDefinition.setItemText(4, _translate("Dialog", "UltraHD"))
        self.comboBoxDefinition.setItemText(5, _translate("Dialog", "Unknown"))
        self.label_18.setText(_translate("Dialog", "Rating:"))
        self.pushButtonClearRating.setToolTip(_translate("Dialog", "<html><head/><body><p>Clear rating</p></body></html>"))
        self.label.setText(_translate("Dialog", "Facial"))
        self.label_5.setText(_translate("Dialog", "Handjob"))
        self.label_7.setText(_translate("Dialog", "Tits"))
        self.label_9.setText(_translate("Dialog", "Cmp"))
        self.label_10.setText(_translate("Dialog", "Analcmp"))
        self.label_11.setText(_translate("Dialog", "Oralcmp"))
        self.label_12.setText(_translate("Dialog", "Cunt"))
        self.label_13.setText(_translate("Dialog", "Belly"))
        self.label_14.setText(_translate("Dialog", "Ass"))
        self.label_15.setText(_translate("Dialog", "Others"))
        self.label_16.setText(_translate("Dialog", "None"))
        self.pushButtonNeuDarstelleruebernehmen.setToolTip(_translate("Dialog", "<html><head/><body><p>Adopt actor, F2</p></body></html>"))
        self.pushButtonNeuDarstelleruebernehmen.setWhatsThis(_translate("Dialog", "Copy the marked actors to the actors field"))
        self.pushButtonNeuDarstelleruebernehmen.setShortcut(_translate("Dialog", "F2"))
        self.listWidgetW.setWhatsThis(_translate("Dialog", "Last used female actors. Adopt marked actors with a doubleclick or click on the button above."))
        self.listWidgetM.setWhatsThis(_translate("Dialog", "Last used male actors. Adopt marked actors with a doubleclick or click on the button above."))
        self.pushButtonBildbeschneiden.setToolTip(_translate("Dialog", "<html><head/><body><p>Crop image</p></body></html>"))
        self.pushButtonBildbeschneiden.setWhatsThis(_translate("Dialog", "Crop image.\n"
"\n"
"How does cropping work?\n"
"\n"
"First click with the left mouse button in the left top corner, then click with the right mouse button at the bottom right."))
        self.pushButtonBildloeschen.setToolTip(_translate("Dialog", "<html><head/><body><p>Delete image file from working directory</p></body></html>"))
        self.pushButtonBildloeschen.setWhatsThis(_translate("Dialog", "Delete image file in working directory"))
        self.pushButtonNeuOK.setToolTip(_translate("Dialog", "<html><head/><body><p>Save</p></body></html>"))
        self.pushButtonNeuOK.setWhatsThis(_translate("Dialog", "Save"))
        self.pushButtonNeuOK.setShortcut(_translate("Dialog", "Enter, Return"))
        self.pushButtonNeuCancel.setToolTip(_translate("Dialog", "<html><head/><body><p>Cancel</p></body></html>"))
        self.pushButtonNeuCancel.setWhatsThis(_translate("Dialog", "Cancel"))
        self.pushButtonNeuDelete.setToolTip(_translate("Dialog", "<html><head/><body><p>Delete from database</p></body></html>"))
        self.pushButtonNeuDelete.setWhatsThis(_translate("Dialog", "Entry in database will be deleted, inclusive image file"))
        self.pushButtonVerz.setToolTip(_translate("Dialog", "<html><head/><body><p>Change working directory</p></body></html>"))
        self.pushButtonVerz.setWhatsThis(_translate("Dialog", "Change the working directory"))
        self.groupBox_2.setTitle(_translate("Dialog", "Image"))
        self.labelNeuBildanzeige.setWhatsThis(_translate("Dialog", "Preview"))
        self.label_19.setText(_translate("Dialog", "Remarks:"))
        self.lineEditNeuTitel.setWhatsThis(_translate("Dialog", "Enter file name"))
        self.lineEditNeuCD.setWhatsThis(_translate("Dialog", "Enter directory"))
        self.label_6.setText(_translate("Dialog", "Original"))
        self.pushButtonOriginalAlt.setToolTip(_translate("Dialog", "<html><head/><body><p>Reuse last entered original title, Ctrl+Y</p></body></html>"))
        self.pushButtonOriginalAlt.setWhatsThis(_translate("Dialog", "Reuse last entered original title"))
        self.pushButtonOriginalAlt.setShortcut(_translate("Dialog", "Ctrl+Y"))
        self.label_4.setText(_translate("Dialog", "Image"))
        self.lineEditNeuBild.setWhatsThis(_translate("Dialog", "Enter file name of image file"))
        self.lineEditNeuOriginal.setWhatsThis(_translate("Dialog", "Enter original title of the movie. For adding more titles, please press the button on the right side."))
        self.pushButtonOriginal.setToolTip(_translate("Dialog", "Enter more movie titles"))
        self.pushButtonOriginal.setWhatsThis(_translate("Dialog", "Enter more movie titles"))
        self.label_1.setText(_translate("Dialog", "Title"))
        self.label_2.setText(_translate("Dialog", "Actor"))
        self.lineEditNeuDarsteller.setWhatsThis(_translate("Dialog", "Enter the list of actors, separated by comma"))
        self.pushButtonAddYear.setToolTip(_translate("Dialog", "<html><head/><body><p>Select year from the combo box on the left and add it to the original title, ALT+Q</p></body></html>"))
        self.pushButtonAddYear.setWhatsThis(_translate("Dialog", "<html><head/><body><p>Select year from the combo box on the left and add it to the original title<br/></p></body></html>"))
        self.pushButtonAddYear.setShortcut(_translate("Dialog", "Alt+Q"))
        self.label_3.setText(_translate("Dialog", "CD"))
        self.pushButtonRepeat.setToolTip(_translate("Dialog", "<html><head/><body><p>Repeat you last input, F12</p></body></html>"))
        self.pushButtonRepeat.setShortcut(_translate("Dialog", "F12"))

