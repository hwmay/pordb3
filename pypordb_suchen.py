# -*- coding: utf-8 -*-

'''
    Copyright 2012-2018 HWM
    
    This file is part of PorDB3.

    PorDB3 is free software: you can redistribute it and or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    PorDB3 is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <http:  www.gnu.org licenses >.
'''

from PyQt5 import QtGui, QtCore, QtWidgets
from pordb_suchen import Ui_ErweiterteSuche as pordb_suchen

class Suchen(QtWidgets.QDialog, pordb_suchen):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        
        self.pushButtonStar1.clicked.connect(self.onStar1)
        self.pushButtonStar2.clicked.connect(self.onStar2)
        self.pushButtonStar3.clicked.connect(self.onStar3)
        self.pushButtonStar4.clicked.connect(self.onStar4)
        self.pushButtonStar5.clicked.connect(self.onStar5)
        self.pushButtonClear.clicked.connect(self.onClearStars)
        self.pushButtonSuchen.clicked.connect(self.accept)
        self.pushButtonCancel.clicked.connect(self.close)
        self.pushButtonRefresh.clicked.connect(self.onRefresh)
        
        self.set_stars = 0
        self.icon_starred = QtWidgets.QIcon()
        self.icon_starred.addPixmap(QtWidgets.QPixmap("pypordb/starred.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_nonstarred = QtGui.QIcon()
        self.icon_nonstarred.addPixmap(QtGui.QPixmap("pypordb/non-starred.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
    def onStar1(self):
        self.pushButtonStar1.setIcon(self.icon_starred)
        self.pushButtonStar2.setIcon(self.icon_nonstarred)
        self.pushButtonStar3.setIcon(self.icon_nonstarred)
        self.pushButtonStar4.setIcon(self.icon_nonstarred)
        self.pushButtonStar5.setIcon(self.icon_nonstarred)
        self.pushButtonSuchen.setFocus()
        self.set_stars = 1
        
    def onStar2(self):
        self.pushButtonStar1.setIcon(self.icon_starred)
        self.pushButtonStar2.setIcon(self.icon_starred)
        self.pushButtonStar3.setIcon(self.icon_nonstarred)
        self.pushButtonStar4.setIcon(self.icon_nonstarred)
        self.pushButtonStar5.setIcon(self.icon_nonstarred)
        self.pushButtonSuchen.setFocus()
        self.set_stars = 2
        
    def onStar3(self):
        self.pushButtonStar1.setIcon(self.icon_starred)
        self.pushButtonStar2.setIcon(self.icon_starred)
        self.pushButtonStar3.setIcon(self.icon_starred)
        self.pushButtonStar4.setIcon(self.icon_nonstarred)
        self.pushButtonStar5.setIcon(self.icon_nonstarred)
        self.pushButtonSuchen.setFocus()
        self.set_stars = 3
        
    def onStar4(self):
        self.pushButtonStar1.setIcon(self.icon_starred)
        self.pushButtonStar2.setIcon(self.icon_starred)
        self.pushButtonStar3.setIcon(self.icon_starred)
        self.pushButtonStar4.setIcon(self.icon_starred)
        self.pushButtonStar5.setIcon(self.icon_nonstarred)
        self.pushButtonSuchen.setFocus()
        self.set_stars = 4
        
    def onStar5(self):
        self.pushButtonStar1.setIcon(self.icon_starred)
        self.pushButtonStar2.setIcon(self.icon_starred)
        self.pushButtonStar3.setIcon(self.icon_starred)
        self.pushButtonStar4.setIcon(self.icon_starred)
        self.pushButtonStar5.setIcon(self.icon_starred)
        self.pushButtonSuchen.setFocus()
        self.set_stars = 5
        
    def onClearStars(self):
        self.pushButtonStar1.setIcon(self.icon_nonstarred)
        self.pushButtonStar2.setIcon(self.icon_nonstarred)
        self.pushButtonStar3.setIcon(self.icon_nonstarred)
        self.pushButtonStar4.setIcon(self.icon_nonstarred)
        self.pushButtonStar5.setIcon(self.icon_nonstarred)
        self.pushButtonSuchen.setFocus()
        self.set_stars = 0
        
    def onRefresh(self):
        self.lineEditDarsteller.clear()
        self.lineEditCD.clear()
        self.lineEditTitel.clear()
        self.lineEditOriginal.clear()
        self.checkBoxVid.setChecked(True)
        self.checkBoxWatched.setChecked(True)
        self.checkBoxNotVid.setChecked(True)
        self.checkBoxNotWatched.setChecked(True)
        self.comboBoxCS.setCurrentIndex(-1)
        self.pushButtonStar1.setIcon(self.icon_nonstarred)
        self.pushButtonStar2.setIcon(self.icon_nonstarred)
        self.pushButtonStar3.setIcon(self.icon_nonstarred)
        self.pushButtonStar4.setIcon(self.icon_nonstarred)
        self.pushButtonStar5.setIcon(self.icon_nonstarred)
        self.set_stars = 0
        self.lineEditRemarks.clear()
        self.lineEditDarsteller.setFocus()
