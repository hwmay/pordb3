# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from pordb_pseudo import Ui_Pseudo as pordb_pseudo
from pypordb_dbupdate import DBUpdate
from pypordb_checkpseudos import CheckPseudos

class PseudonymeBearbeiten(QtGui.QDialog, pordb_pseudo):
    def __init__(self, darsteller, pseudonyme):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        
        self.connect(self.pushButtonPseudo, QtCore.SIGNAL("clicked()"), self.onPseudo)
        self.connect(self.pushButtonSpeichern, QtCore.SIGNAL("clicked()"), self.onSpeichern)
        self.connect(self.pushButtonAbbrechen, QtCore.SIGNAL("clicked()"), self.close)
        
        self.pseudonyme = pseudonyme
        self.pushButtonSpeichern.setDefault(True)
        
        self.darsteller = darsteller.lstrip('=')
        self.setWindowTitle(self.trUtf8("Edit aliases for ") +self.darsteller)
        row = 0
        column = 0
        self.lineEditPseudo.setFocus()
        self.tableWidgetPseudo.clearContents()
        for i in self.pseudonyme:
            newitem = QtGui.QTableWidgetItem(i.strip())
            self.tableWidgetPseudo.setItem(row, column, newitem)
            row += 1
        newitem = QtGui.QTableWidgetItem("")
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
                newitem = QtGui.QTableWidgetItem(i.strip())
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
                    cellItem = str(QtGui.QTableWidgetItem(tableItem).text())
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
