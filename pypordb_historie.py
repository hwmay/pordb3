# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from pordb_historie import Ui_Dialog as pordb_historie
from pypordb_dblesen import DBLesen
from pypordb_dbupdate import DBUpdate

class Historie(QtGui.QDialog, pordb_historie):
	def __init__(self, parent=None):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		
		self.connect(self.pushButtonSearch, QtCore.SIGNAL("clicked()"), self.onSearch)
		self.connect(self.pushButtonGo, QtCore.SIGNAL("clicked()"), self.onGo)
		self.connect(self.pushButtonAbbrechen, QtCore.SIGNAL("clicked()"), self.close)
		self.connect(self.pushButtonClear, QtCore.SIGNAL("clicked()"), self.onClear)
		
		self.row = 0
		self.column = 0
		self.zu_lesen = None
		self.tableWidgetHistory.setAlternatingRowColors(True)
		self.tableWidgetHistory.clearContents()
		self.lineEditSearch.setFocus()
		
		self.zu_lesen = "SELECT * from pordb_history order by time DESC"
		self.lese_func = DBLesen(self, self.zu_lesen)
		self.res = DBLesen.get_data(self.lese_func)
		res = DBLesen.get_data(self.lese_func)
		self.tableWidgetHistory.setRowCount(len(self.res))
		for i in self.res:
			# Checkbox
			newitem = QtGui.QTableWidgetItem()
			newitem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable)
			newitem.setCheckState(QtCore.Qt.Unchecked)
			self.tableWidgetHistory.setItem(self.row, self.column, newitem)
			# Befehl
			self.column += 1
			newitem = QtGui.QTableWidgetItem(i[0])
			self.tableWidgetHistory.setItem(self.row, self.column, newitem)
			# Time
			self.column += 1
			newitem = QtGui.QTableWidgetItem(str(i[1]))
			self.tableWidgetHistory.setItem(self.row, self.column, newitem)
			self.column = 0
			self.row += 1
		self.tableWidgetHistory.resizeColumnsToContents()
		
	def onSearch(self):
		self.tableWidgetHistory.clearSelection()
		self.tableWidgetHistory.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
		suchbegriff = str(self.lineEditSearch.text()).lower()
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
		for i in range(len(self.res)):
			if self.tableWidgetHistory.item(i, 0).checkState():
				self.zu_lesen = str(self.tableWidgetHistory.item(i, 1).text().replace('"', "'"))
				break
		
		self.close()
		
	def onClear(self):
		zu_lesen = "SELECT * from pordb_history order by time DESC LIMIT 50"
		lese_func = DBLesen(self, zu_lesen)
		res = DBLesen.get_data(lese_func)
		if res:
			zu_erfassen = "delete from pordb_history where time < '" +str(res[-1][-1]) +"'"
			update_func = DBUpdate(self, zu_erfassen)
			DBUpdate.update_data(update_func)
			
		self.close()
