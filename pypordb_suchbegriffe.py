# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from pypordb_dblesen import DBLesen
from pordb_suchbegriffe import Ui_Suchbegriffedialog as pordb_suchbegriffe
from pypordb_dbupdate import DBUpdate

class SuchbegriffeBearbeiten(QtGui.QDialog, pordb_suchbegriffe):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        
        self.connect(self.pushButtonLandSpeichern, QtCore.SIGNAL("clicked()"), self.onSpeichern)
        self.connect(self.pushButtonLandAbbrechen, QtCore.SIGNAL("clicked()"), self.close)
        
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
                    newitem = QtGui.QTableWidgetItem(j.strip())
                else:
                    newitem = QtGui.QTableWidgetItem(" ")
                self.tableWidgetSuche.setItem(row, column, newitem)
                column += 1
            row += 1
        self.tableWidgetSuche.setHorizontalHeaderLabels([self.trUtf8("Search terms"), self.trUtf8("Alternative")])
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
                    cellItem = str(QtGui.QTableWidgetItem(tableItem).text())
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
