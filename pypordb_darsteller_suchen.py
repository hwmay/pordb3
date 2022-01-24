# -*- coding: utf-8 -*-

'''
    Copyright 2012-2022 HWM
    
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

import os
from PyQt5 import QtGui, QtCore, QtWidgets
from pordb_darsteller_suchen import Ui_DarstellerSuche as pordb_darsteller_suchen
from pypordb_dblesen import DBLesen

class DarstellerSuchen(QtWidgets.QDialog, pordb_darsteller_suchen):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        
        self.maximum = QtCore.QDate.currentDate()
        self.minimum = QtCore.QDate.fromString("20000101", "yyyyMMdd")
        self.dateEditDarstellerSucheAb.setDateRange(self.minimum, self.maximum)
        self.dateEditDarstellerSucheBis.setDateRange(self.minimum, self.maximum)
        self.dateEditDarstellerSucheBis.setDate(self.maximum)
        
        self.pushButtonSuchen.clicked.connect(self.accept)
        self.pushButtonCancel.clicked.connect(self.close)
        self.pushButtonRefresh.clicked.connect(self.onRefresh)
        
        # Fill comboboxes nation
        zu_lesen = "SELECT * FROM pordb_iso_land WHERE aktiv = %s ORDER BY land"
        lese_func = DBLesen(self, zu_lesen, "x")
        res = DBLesen.get_data(lese_func)
        self.comboBoxDarstellerSucheNation1.addItem("")
        self.comboBoxDarstellerSucheNation2.addItem("")
        self.comboBoxDarstellerSucheNation3.addItem("")
        for i in res:
            text = '%2s %-50s' % (i[0], i[1])
            bild = os.path.join(os.curdir, "pypordb", i[0] + ".svg")
            icon = QtGui.QIcon()
            icon.addFile(bild, QtCore.QSize(16, 16), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.comboBoxDarstellerSucheNation1.addItem(icon, text)
            self.comboBoxDarstellerSucheNation2.addItem(icon, text)
            self.comboBoxDarstellerSucheNation3.addItem(icon, text)
        
    def onRefresh(self):
        self.lineEditDarstellerSuche.setText("")
        self.comboBoxDarstellerSucheGeschlecht.setCurrentIndex(-1)
        self.lineEditActor1.setText("")
        self.lineEditActor2.setText("")
        self.lineEditActor3.setText("")
        self.dateEditDarstellerSucheAb.setDate(self.minimum)
        self.dateEditDarstellerSucheBis.setDate(self.maximum)
        self.comboBoxDarstellerSucheHaar.setCurrentIndex(-1)
        self.comboBoxDarstellerSucheNation1.setCurrentIndex(0)
        self.comboBoxDarstellerSucheNation2.setCurrentIndex(0)
        self.comboBoxDarstellerSucheNation3.setCurrentIndex(0)
        self.comboBoxDarstellerSucheTattoo.setCurrentIndex(-1)
        self.lineEditDarstellerSucheTattoo.setText("")
        self.comboBoxDarstellerSucheEthnic.setCurrentIndex(-1)
        self.lineEditDarstellerSuche.setFocus()
