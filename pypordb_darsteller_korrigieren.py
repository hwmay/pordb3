# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from pordb_darsteller_korrigieren import Ui_Darstellerkorrigieren as pordb_darsteller_korrigieren
from pypordb_dblesen import DBLesen

class DarstellerKorrigieren(QtGui.QDialog, pordb_darsteller_korrigieren):
	def __init__(self, darsteller_liste, parent=None):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		
		self.connect(self.pushButtonUebernehmen, QtCore.SIGNAL("clicked()"), self.accept)
		self.connect(self.pushButtonAbbrechen, QtCore.SIGNAL("clicked()"), self.close)
		self.connect(self.pushButtonSuchen, QtCore.SIGNAL("clicked()"), self.onSuchen)
		
		self.darsteller = ""
		self.tableWidgetDarsteller.setColumnCount(1)
		self.darsteller = str(darsteller_liste).split(", ")
		self.tableWidgetDarsteller.clear()
		self.tableWidgetDarsteller.setRowCount(len(self.darsteller) + 1)
		j = 0
		for i in self.darsteller:
			newitem = QtGui.QTableWidgetItem(i)
			self.tableWidgetDarsteller.setItem(j, 0, newitem)
			j += 1
		newitem = QtGui.QTableWidgetItem(" ")
		self.tableWidgetDarsteller.setItem(j, 0, newitem)
		self.tableWidgetDarsteller.setAlternatingRowColors(True)
		self.tableWidgetDarsteller.resizeColumnsToContents()
		self.tableWidgetDarsteller.resizeRowsToContents()
		
	def onSuchen(self):
		suchbegriff = str(self.lineEditFilter.text())
		zu_lesen = "select darsteller from pordb_darsteller where darsteller like '%" +suchbegriff  +"%'"
		if self.comboBoxGeschlecht.currentText() == self.trUtf8("Male"):
			zu_lesen += " and sex = 'm'"
		elif self.comboBoxGeschlecht.currentText() == self.trUtf8("Female"):
			zu_lesen += " and sex = 'w'"
		self.comboBoxGeschlecht.setCurrentIndex(0)
		zu_lesen += " order by darsteller"
		lese_func = DBLesen(self, zu_lesen)
		res = DBLesen.get_data(lese_func)
		self.tableWidgetDarstellerGefunden.setColumnCount(1)
		self.tableWidgetDarstellerGefunden.clear()
		self.tableWidgetDarstellerGefunden.setRowCount(len(res))
		j = 0
		for i in res:
			newitem = QtGui.QTableWidgetItem(i[0])
			self.tableWidgetDarstellerGefunden.setItem(j, 0, newitem)
			j += 1
		self.tableWidgetDarstellerGefunden.setAlternatingRowColors(True)
		self.tableWidgetDarstellerGefunden.resizeColumnsToContents()
		self.tableWidgetDarstellerGefunden.resizeRowsToContents()
		
	def accept(self):
		cell = []
		for i in range(self.tableWidgetDarsteller.rowCount()):
			tableItem = self.tableWidgetDarsteller.item(i, 0)
			cellItem = str(QtGui.QTableWidgetItem(tableItem).text()).strip()
			if cellItem:
				cell.append(cellItem)
				
		self.darsteller = ", ".join(cell)
		self.close()
