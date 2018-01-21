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

import os
from PyQt5 import QtGui, QtCore, QtWidgets
from pordb_land import Ui_Landdialog as pordb_land
from pypordb_dblesen import DBLesen
from pypordb_dbupdate import DBUpdate

class LandBearbeiten(QtWidgets.QDialog, pordb_land):
    def __init__(self, comboBoxNation, nation_fuellen, parent=None):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        
        self.pushButtonLandSpeichern.clicked.connect(self.onSpeichern)
        self.pushButtonLandAbbrechen.clicked.connect(self.close)
        
        self.nation_fuellen = nation_fuellen
        
        zu_lesen = "SELECT * FROM pordb_iso_land ORDER BY land"
        lese_func = DBLesen(self, zu_lesen)
        res = DBLesen.get_data(lese_func)
        row = 0
        self.tableWidgetLaender.clear()
        self.tableWidgetLaender.setRowCount(len(res) + 1)
        for i in res:
            column = 0
            for j in i:
                if j:
                    if column == 0:
                        bild = os.path.join(os.curdir, "pypordb", i[0] + ".svg")
                        icon = QtGui.QIcon()
                        icon.addFile(bild, QtCore.QSize(24, 24), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                        newitem = QtWidgets.QTableWidgetItem(icon, "")
                        self.tableWidgetLaender.setItem(row, column, newitem)
                        column += 1
                        newitem = QtWidgets.QTableWidgetItem(j.strip())
                    else:
                        newitem = QtWidgets.QTableWidgetItem(j.strip())
                else:
                    newitem = QtWidgets.QTableWidgetItem(" ")
                self.tableWidgetLaender.setItem(row, column, newitem)
                column += 1
            row += 1
        newitem = QtWidgets.QTableWidgetItem("")
        self.tableWidgetLaender.setItem(row, 1, newitem)
        self.tableWidgetLaender.setCurrentItem(newitem)
        self.tableWidgetLaender.setFocus()
        self.tableWidgetLaender.editItem(self.tableWidgetLaender.currentItem())          
        self.tableWidgetLaender.setHorizontalHeaderLabels([self.tr("Flag"), "ISO Code", self.tr("Country"), self.tr("active"), self.tr("Nationality")])
        self.tableWidgetLaender.setAlternatingRowColors(True)
        self.tableWidgetLaender.resizeColumnsToContents()
        self.tableWidgetLaender.resizeRowsToContents()
        
    def onSpeichern(self):
        zu_erfassen = []
        zu_erfassen.append("DELETE FROM pordb_iso_land")
        for i in range(self.tableWidgetLaender.rowCount()):
            cell = []
            for j in range(self.tableWidgetLaender.columnCount()):
                if j == 0: # column 0 is only flag icon
                    continue
                tableItem = self.tableWidgetLaender.item(i, j)
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
                    werte.append(cell[2])
                    werte.append(cell[3])
                    zu_erfassen.append(["INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES (%s, %s, %s, %s)", werte])
            except:
                pass
        
        update_func = DBUpdate(self, zu_erfassen)
        DBUpdate.update_data(update_func)
        
        self.nation_fuellen()
        self.close()
