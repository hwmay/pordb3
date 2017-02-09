# -*- coding: utf-8 -*-

'''
    Copyright 2012-2017 HWM
    
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

from PyQt4 import QtGui, QtCore
from pordb_bookmarks import Ui_Dialog as pordb_bookmarks
from pypordb_dblesen import DBLesen
from pypordb_dbupdate import DBUpdate

class Bookmarks(QtGui.QDialog, pordb_bookmarks):
    def __init__(self, url, parent=None):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        
        self.connect(self.pushButtonSpeichern, QtCore.SIGNAL("clicked()"), self.accept)
        self.connect(self.pushButtonAnzeigen, QtCore.SIGNAL("clicked()"), self.anzeigen)
        self.connect(self.pushButtonLoeschen, QtCore.SIGNAL("clicked()"), self.loeschen)
        
        self.url = url
        
        zu_lesen = "SELECT * FROM pordb_bookmarks ORDER BY z"
        lese_func = DBLesen(self, zu_lesen)
        res = DBLesen.get_data(lese_func)
        row = 0
        self.tableWidgetBookmarks.clearContents()
        self.tableWidgetBookmarks.setRowCount(len(res))
        self.tableWidgetBookmarks.setColumnCount(2)
        for i in res:
            column = 0
            for j in i:
                newitem = QtGui.QTableWidgetItem(str(j))
                self.tableWidgetBookmarks.setItem(row, column, newitem)
                column += 1
            row += 1
        self.tableWidgetBookmarks.setAlternatingRowColors(True)
        self.tableWidgetBookmarks.resizeColumnsToContents()
        self.tableWidgetBookmarks.resizeRowsToContents()
        
    def accept(self):
        werte = []
        zu_erfassen = []
        werte.append(self.url)
        zu_erfassen.append(["INSERT INTO pordb_bookmarks (url) VALUES (%s)", werte])
        update_func = DBUpdate(self, zu_erfassen)
        DBUpdate.update_data(update_func)
        
        self.close()
        
    def anzeigen(self):
        items = self.tableWidgetBookmarks.selectedItems()
        self.neue_url = str(items[0].text())
        self.close()
        return self.neue_url
        
    def loeschen(self):
        row = self.tableWidgetBookmarks.currentRow()
        item = self.tableWidgetBookmarks.item(row, 1)
        a = item.text()
        try:
            werte = []
            zu_erfassen = []
            werte.append(str(item.text()))
            zu_erfassen.append(["DELETE FROM pordb_bookmarks WHERE z = %s", werte])
            update_func = DBUpdate(self, zu_erfassen)
            DBUpdate.update_data(update_func)
            self.close()
        except:
            pass
