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
from pordb_devices import Ui_Dialog as pordb_devices
from pypordb_dblesen import DBLesen
from pypordb_dbupdate import DBUpdate

class Devices(QtWidgets.QDialog, pordb_devices):
    def __init__(self, device_fuellen, parent=None):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        
        self.pushButtonSpeichern.clicked.connect(self.accept)
        self.pushButtonAbbrechen.clicked.connect(self.close)
        
        self.device_fuellen = device_fuellen
        
        zu_lesen = "SELECT * FROM pordb_mpg_verzeichnisse ORDER BY dir"
        lese_func = DBLesen(self, zu_lesen)
        res = DBLesen.get_data(lese_func)
        row = 0
        self.tableWidget.clear()
        self.tableWidget.setRowCount(len(res) + 1)
        for i in res:
            column = 0
            for j in i:
                if j:
                    newitem = QtWidgets.QTableWidgetItem(j.strip())
                else:
                    newitem = QtWidgets.QTableWidgetItem(" ")
                self.tableWidget.setItem(row, column, newitem)
            row += 1
        newitem = QtWidgets.QTableWidgetItem("")
        self.tableWidget.setItem(row, 0, newitem)
        self.tableWidget.setCurrentItem(newitem)
        self.tableWidget.setFocus()
        self.tableWidget.editItem(self.tableWidget.currentItem())            
        self.tableWidget.setHorizontalHeaderLabels([self.tr("Device")])
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        
    def accept(self):
        position = 0
        zu_erfassen = []
        zu_erfassen.append("DELETE FROM pordb_mpg_verzeichnisse")
        for i in range(self.tableWidget.rowCount()):
            cell = []
            position += 1
            for j in range(self.tableWidget.columnCount()):
                tableItem = self.tableWidget.item(i, j)
                try:
                    cellItem = str(QtWidgets.QTableWidgetItem(tableItem).text())
                    cell.append(cellItem)
                except:
                    pass
            try:
                if cell[0]:
                    werte = []
                    werte.append(cell[0])
                    zu_erfassen.append(["INSERT INTO pordb_mpg_verzeichnisse (dir) VALUES (%s)", werte])
            except:
                pass
        
        update_func = DBUpdate(self, zu_erfassen)
        DBUpdate.update_data(update_func)
        
        self.device_fuellen()
        self.close()
