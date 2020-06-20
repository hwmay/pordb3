# -*- coding: utf-8 -*-

'''
    Copyright 2012-2020 HWM
    
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

from PyQt5 import QtCore, QtWidgets
from pordb_historie import Ui_Dialog as pordb_historie
from pypordb_dblesen import DBLesen
from pypordb_dbupdate import DBUpdate

class Historie(QtWidgets.QDialog, pordb_historie):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        
        self.pushButtonSearch.clicked.connect(self.onSearch)
        self.pushButtonGo.clicked.connect(self.onGo)
        self.pushButtonAbbrechen.clicked.connect(self.close)
        self.pushButtonClear.clicked.connect(self.onClear)
        
        self.row = 0
        self.column = 0
        self.zu_lesen = None
        self.werte = None
        self.tableWidgetHistory.setAlternatingRowColors(True)
        self.tableWidgetHistory.clearContents()
        self.lineEditSearch.setFocus()
        
        self.zu_lesen = "SELECT * FROM pordb_history ORDER BY time DESC"
        self.lese_func = DBLesen(self, self.zu_lesen)
        self.res = DBLesen.get_data(self.lese_func)
        self.tableWidgetHistory.setRowCount(len(self.res))
        for i in self.res:
            # Checkbox
            newitem = QtWidgets.QTableWidgetItem()
            newitem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable)
            newitem.setCheckState(QtCore.Qt.Unchecked)
            self.tableWidgetHistory.setItem(self.row, self.column, newitem)
            # Befehl
            self.column += 1
            newitem = QtWidgets.QTableWidgetItem(i[0])
            self.tableWidgetHistory.setItem(self.row, self.column, newitem)
            # Time
            self.column += 1
            newitem = QtWidgets.QTableWidgetItem(str(i[1]))
            self.tableWidgetHistory.setItem(self.row, self.column, newitem)
            self.column = 0
            self.row += 1
        self.tableWidgetHistory.resizeColumnsToContents()
        
        self.labelLines.setText(str(len(self.res)))
        
    def onSearch(self):
        self.tableWidgetHistory.clearSelection()
        self.tableWidgetHistory.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        suchbegriff = str(self.lineEditSearch.text()).lower()
        item_scroll = None
        if suchbegriff:
            zaehler = 0
            item_scroll = None
            for i in range(len(self.res)):
                item = self.tableWidgetHistory.item(i, 1)
                text = str(item.text()).lower()
                if suchbegriff in text:
                    zaehler += 1
                    if zaehler == 1:
                        item_scroll = item
                    self.tableWidgetHistory.selectRow(i)
            if item_scroll:
                self.tableWidgetHistory.scrollToItem(item_scroll)
            self.tableWidgetHistory.setFocus()
    
    def onGo(self):
        text = None
        for i in range(len(self.res)):
            if self.tableWidgetHistory.item(i, 0).checkState():
                text = str(self.tableWidgetHistory.item(i, 1).text())
                index = text.find("ORDER BY")
                if index == -1:
                    index = 0
                index += text[index : ].find(" (")
                self.werte = str(text)[index :].lstrip(" (")
                if self.werte.endswith(")"):
                    self.werte = self.werte[:-1]
                self.zu_lesen = str(text)[0 : index]
                break
        if not text:
            QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("Please check one history entry"))
            return
        else:
            self.close()
        
    def onClear(self):
        zu_lesen = "SELECT * FROM pordb_history ORDER BY time DESC LIMIT 50"
        lese_func = DBLesen(self, zu_lesen)
        res = DBLesen.get_data(lese_func)
        if res:
            werte = []
            zu_erfassen = []
            werte.append(str(res[-1][-1]))
            zu_erfassen.append(["DELETE FROM pordb_history WHERE time < %s", werte])
            update_func = DBUpdate(self, zu_erfassen)
            DBUpdate.update_data(update_func)
            
        self.close()
