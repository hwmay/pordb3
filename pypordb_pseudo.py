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
from pordb_pseudo import Ui_Pseudo as pordb_pseudo
from pypordb_dbupdate import DBUpdate
from pypordb_checkpseudos import CheckPseudos

class PseudonymeBearbeiten(QtWidgets.QDialog, pordb_pseudo):
    def __init__(self, darsteller, pseudonyme):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        
        self.pushButtonPseudo.clicked.connect(self.onPseudo)
        self.pushButtonSpeichern.clicked.connect(self.onSpeichern)
        self.pushButtonAbbrechen.clicked.connect(self.close)
        
        self.pseudonyme = pseudonyme
        self.pushButtonSpeichern.setDefault(True)
        
        self.darsteller = darsteller.lstrip('=')
        self.setWindowTitle(self.tr("Edit aliases for ") +self.darsteller)
        row = 0
        column = 0
        self.lineEditPseudo.setFocus()
        self.tableWidgetPseudo.clearContents()
        for i in self.pseudonyme:
            newitem = QtWidgets.QTableWidgetItem(i.strip())
            self.tableWidgetPseudo.setItem(row, column, newitem)
            row += 1
        newitem = QtWidgets.QTableWidgetItem("")
        self.tableWidgetPseudo.setItem(row, 0, newitem)
        self.tableWidgetPseudo.setCurrentItem(newitem)
        self.tableWidgetPseudo.setFocus()
        self.tableWidgetPseudo.editItem(self.tableWidgetPseudo.currentItem())            
        self.tableWidgetPseudo.setAlternatingRowColors(True)
        self.tableWidgetPseudo.resizeColumnsToContents()
        self.tableWidgetPseudo.resizeRowsToContents()
        
    def onPseudo(self):
        pseudos = str(self.lineEditPseudo.text()).strip().split(",")
        pseudos.extend(self.pseudonyme)
        row = 0
        column = 0
        for i in pseudos:
            if len(i) > 0:
                newitem = QtWidgets.QTableWidgetItem(i.strip())
                self.tableWidgetPseudo.setItem(row, column, newitem)
                row += 1
    
    def onSpeichern(self):
        zu_erfassen = []
        werte = []
        position = 0
        werte.append(self.darsteller)
        zu_erfassen.append(["DELETE FROM pordb_pseudo WHERE darsteller = %s", werte])
        update_func = DBUpdate(self, zu_erfassen)
        DBUpdate.update_data(update_func)
        for i in range(self.tableWidgetPseudo.rowCount()):
            cell = []
            position += 1
            for j in range(self.tableWidgetPseudo.columnCount()):
                tableItem = self.tableWidgetPseudo.item(i, j)
                if tableItem:
                    cellItem = str(QtWidgets.QTableWidgetItem(tableItem).text())
                    cell.append(cellItem)
            if cell and cell[0] and cell[0].title().replace("'", "''") != self.darsteller:
                checkpseudo = CheckPseudos(cell[0].title().replace("'", "''"), self.darsteller)
                check = CheckPseudos.check(checkpseudo)
                if check:
                    zu_erfassen = []
                    werte = []
                    werte.append(cell[0].title())
                    werte.append(self.darsteller)
                    zu_erfassen.append(["INSERT INTO pordb_pseudo (pseudo, darsteller) VALUES (%s, %s)", werte])
                    update_func = DBUpdate(self, zu_erfassen)
                    DBUpdate.update_data(update_func)
        
        self.close()
