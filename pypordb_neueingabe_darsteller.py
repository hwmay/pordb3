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

import time
import os
from PyQt5 import QtGui, QtCore, QtWidgets
from pypordb_dblesen import DBLesen
from pypordb_dbupdate import DBUpdate
from pordb_darstellerneu import Ui_Dialog as pordb_darstellerneu

class NeueingabeDarsteller(QtWidgets.QDialog, pordb_darstellerneu):
    def __init__(self, darsteller, parent=None):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.darsteller = darsteller
        
        self.pushButtonDarstellerneuSpeichern.clicked.connect(self.accept)
        self.pushButtonDarstellerneuCancel.clicked.connect(self.close)
        
        self.setWindowTitle(self.tr("Actor ") +self.darsteller + self.tr(" will be added"))
        # Combobox für Nation füllen
        zu_lesen = "SELECT * FROM pordb_iso_land WHERE aktiv = %s ORDER BY land"
        lese_func = DBLesen(self, zu_lesen, "x")
        res = DBLesen.get_data(lese_func)
        self.comboBoxDarstellerneuNation.clear()
        for i in res:
            text = '%2s %-50s' % (i[0], i[1])
            bild = os.path.join(os.curdir, "pypordb", i[0] + ".svg")
            icon = QtGui.QIcon()
            icon.addFile(bild, QtCore.QSize(16, 16), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.comboBoxDarstellerneuNation.addItem(icon, text)
            
    def accept(self):
        if not self.comboBoxDarstellerneuGeschlecht.currentText():
            message = QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("Please select the gender"))
            return
        # insert/update-Anweisung aufbauen
        datum = str(time.localtime()[0]) + '-' + str(time.localtime()[1]) + '-' + str(time.localtime()[2])
        werte = []
        zu_erfassen = []
        werte.append(self.darsteller)
        werte.append(str(self.comboBoxDarstellerneuGeschlecht.currentText()))
        werte.append("0")
        werte.append(datum)
        werte.append(str(self.comboBoxDarstellerneuHaarfarbe.currentText()))
        werte.append(str(self.comboBoxDarstellerneuNation.currentText())[0:2])
        werte.append(self.lineEditDarstellerneuTattoo.text())
        werte.append(str(self.comboBoxDarstellerneuEthnic.currentText()))
        zu_erfassen.append(["INSERT into pordb_darsteller VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", werte])
        update_func = DBUpdate(self, zu_erfassen)
        DBUpdate.update_data(update_func)
        self.close()
