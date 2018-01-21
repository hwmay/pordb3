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
from pordb_original import Ui_Dialog as pordb_original

class OriginalErfassen(QtWidgets.QDialog, pordb_original):
    def __init__(self, original_weitere=None, parent=None):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

        self.original_weitere = original_weitere
        row = 0
        if self.original_weitere:
            self.tableWidget.clearContents()
            for i in self.original_weitere:
                newitem = QtWidgets.QTableWidgetItem(i.title().strip())
                self.tableWidget.setItem(row, 0, newitem)
                row += 1
        newitem = QtWidgets.QTableWidgetItem("")
        self.tableWidget.setItem(row, 0, newitem)
        self.tableWidget.setCurrentItem(newitem)
        self.tableWidget.setFocus()
        self.tableWidget.editItem(self.tableWidget.currentItem())
        
        self.pushButtonSpeichern.clicked.connect(self.onSpeichern)
        self.pushButtonAbbrechen.clicked.connect(self.close)
        
    def onSpeichern(self):
        self.original = []
        for i in range(10):
            tableItem = self.tableWidget.item(i, 0)
            if tableItem:
                cellItem = str(QtWidgets.QTableWidgetItem(tableItem).text()).encode("utf-8")
                self.original.append(cellItem)
        self.close()
