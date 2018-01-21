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
from pypordb_dblesen import DBLesen
from pordb_suchbegriffe import Ui_Suchbegriffedialog as pordb_suchbegriffe
from pypordb_dbupdate import DBUpdate

class SuchbegriffeBearbeiten(QtWidgets.QDialog, pordb_suchbegriffe):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        
        self.pushButtonLandSpeichern.clicked.connect(self.onSpeichern)
        self.pushButtonLandAbbrechen.clicked.connect(self.close)
        
        zu_lesen = "SELECT * FROM pordb_suchbegriffe ORDER BY suchbegriff"
        lese_func = DBLesen(self, zu_lesen)
        res = DBLesen.get_data(lese_func)
        row = 0
        self.tableWidgetSuche.clear()
        self.tableWidgetSuche.setRowCount(len(res) + 2)
        self.tableWidgetSuche.setSortingEnabled(False)
        for i in res:
            column = 0
            for j in i:
                if j:
                    newitem = QtWidgets.QTableWidgetItem(j.strip())
                else:
                    newitem = QtWidgets.QTableWidgetItem(" ")
                self.tableWidgetSuche.setItem(row, column, newitem)
                column += 1
            row += 1
        newitem = QtWidgets.QTableWidgetItem("")
        self.tableWidgetSuche.setItem(row, 0, newitem)
        self.tableWidgetSuche.setCurrentItem(newitem)
        self.tableWidgetSuche.setFocus()
        self.tableWidgetSuche.editItem(self.tableWidgetSuche.currentItem())            
        self.tableWidgetSuche.setHorizontalHeaderLabels([self.tr("Search terms"), self.tr("Alternative")])
        self.tableWidgetSuche.setAlternatingRowColors(True)
        self.tableWidgetSuche.resizeColumnsToContents()
        self.tableWidgetSuche.resizeRowsToContents()
        #self.tableWidgetSuche.setSortingEnabled(True)
        
    def onSpeichern(self):
        position = 0
        zu_erfassen = []
        zu_erfassen.append("DELETE FROM pordb_suchbegriffe")
        for i in range(self.tableWidgetSuche.rowCount()):
            cell = []
            position += 1
            for j in range(self.tableWidgetSuche.columnCount()):
                tableItem = self.tableWidgetSuche.item(i, j)
                try:
                    cellItem = str(QtWidgets.QTableWidgetItem(tableItem).text())
                    cell.append(cellItem)
                except:
                    pass
            try:
                if cell[0]:
                    werte = []
                    werte.append(cell[0])
                    werte.append(cell[1])
                    zu_erfassen.append(["INSERT INTO pordb_suchbegriffe (suchbegriff, alternative) VALUES (%s, %s)", werte])
            except:
                pass
        
        update_func = DBUpdate(self, zu_erfassen)
        DBUpdate.update_data(update_func)
        
        self.close()
