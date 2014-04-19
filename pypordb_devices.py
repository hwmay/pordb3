# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from pordb_devices import Ui_Dialog as pordb_devices
from pypordb_dblesen import DBLesen
from pypordb_dbupdate import DBUpdate

class Devices(QtGui.QDialog, pordb_devices):
	def __init__(self, device_fuellen, parent=None):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		
		self.connect(self.pushButtonSpeichern, QtCore.SIGNAL("clicked()"), self.accept)
		self.connect(self.pushButtonAbbrechen, QtCore.SIGNAL("clicked()"), self.close)
		
		self.device_fuellen = device_fuellen
		
		zu_lesen = "select * from pordb_mpg_verzeichnisse order by dir"
		lese_func = DBLesen(self, zu_lesen)
		res = DBLesen.get_data(lese_func)
		row = 0
		self.tableWidget.clear()
		self.tableWidget.setRowCount(len(res) + 1)
		for i in res:
			column = 0
			for j in i:
				if j:
					newitem = QtGui.QTableWidgetItem(j.strip())
				else:
					newitem = QtGui.QTableWidgetItem(" ")
				self.tableWidget.setItem(row, column, newitem)
			row += 1
		self.tableWidget.setHorizontalHeaderLabels([self.trUtf8("Device")])
		self.tableWidget.setAlternatingRowColors(True)
		self.tableWidget.resizeColumnsToContents()
		self.tableWidget.resizeRowsToContents()
		
	def accept(self):
		position = 0
		zu_erfassen = []
		zu_erfassen.append("delete from pordb_mpg_verzeichnisse")
		for i in range(self.tableWidget.rowCount()):
			cell = []
			position += 1
			for j in range(self.tableWidget.columnCount()):
				tableItem = self.tableWidget.item(i, j)
				try:
					cellItem = str(QtGui.QTableWidgetItem(tableItem).text())
					cell.append(cellItem)
				except:
					pass
			try:
				if cell[0]:
					zu_erfassen.append("insert into pordb_mpg_verzeichnisse (dir) values ('" +cell[0] +"')")
			except:
				pass
		
		update_func = DBUpdate(self, zu_erfassen)
		DBUpdate.update_data(update_func)
		
		self.device_fuellen()
		self.close()
