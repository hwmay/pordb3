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
from pordb_darsteller_korrigieren import Ui_Darstellerkorrigieren as pordb_darsteller_korrigieren
from pypordb_dblesen import DBLesen

class DarstellerKorrigieren(QtWidgets.QDialog, pordb_darsteller_korrigieren):
    def __init__(self, darsteller_liste, parent=None):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        
        self.pushButtonUebernehmen.clicked.connect(self.accept)
        self.pushButtonAbbrechen.clicked.connect(self.close)
        self.pushButtonSuchen.clicked.connect(self.onSuchen)
        
        self.darsteller = ""
        self.tableWidgetDarsteller.setColumnCount(1)
        self.darsteller = str(darsteller_liste).split(", ")
        self.tableWidgetDarsteller.clear()
        self.tableWidgetDarsteller.setRowCount(len(self.darsteller) + 1)
        j = 0
        for i in self.darsteller:
            newitem = QtWidgets.QTableWidgetItem(i)
            self.tableWidgetDarsteller.setItem(j, 0, newitem)
            j += 1
        newitem = QtWidgets.QTableWidgetItem(" ")
        self.tableWidgetDarsteller.setItem(j, 0, newitem)
        self.tableWidgetDarsteller.setAlternatingRowColors(True)
        self.tableWidgetDarsteller.resizeColumnsToContents()
        self.tableWidgetDarsteller.resizeRowsToContents()
        
    def onSuchen(self):
        suchbegriff = str(self.lineEditFilter.text())
        zu_lesen = "SELECT darsteller FROM pordb_darsteller WHERE darsteller LIKE '%" +suchbegriff  +"%'"
        if self.comboBoxGeschlecht.currentText() == self.tr("Male"):
            zu_lesen += " AND sex = 'm'"
        elif self.comboBoxGeschlecht.currentText() == self.tr("Female"):
            zu_lesen += " AND sex = 'w'"
        self.comboBoxGeschlecht.setCurrentIndex(0)
        zu_lesen += " ORDER BY darsteller"
        lese_func = DBLesen(self, zu_lesen)
        res = DBLesen.get_data(lese_func)
        self.tableWidgetDarstellerGefunden.setColumnCount(1)
        self.tableWidgetDarstellerGefunden.clear()
        self.tableWidgetDarstellerGefunden.setRowCount(len(res))
        j = 0
        for i in res:
            newitem = QtWidgets.QTableWidgetItem(i[0])
            self.tableWidgetDarstellerGefunden.setItem(j, 0, newitem)
            j += 1
        self.tableWidgetDarstellerGefunden.setAlternatingRowColors(True)
        self.tableWidgetDarstellerGefunden.resizeColumnsToContents()
        self.tableWidgetDarstellerGefunden.resizeRowsToContents()
        
    def accept(self):
        cell = []
        for i in range(self.tableWidgetDarsteller.rowCount()):
            tableItem = self.tableWidgetDarsteller.item(i, 0)
            cellItem = str(QtWidgets.QTableWidgetItem(tableItem).text()).strip()
            if cellItem:
                cell.append(cellItem)
                
        self.darsteller = ", ".join(cell)
        self.close()
