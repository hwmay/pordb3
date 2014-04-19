# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from pordb_land import Ui_Landdialog as pordb_land
from pypordb_dblesen import DBLesen
from pypordb_dbupdate import DBUpdate

class LandBearbeiten(QtGui.QDialog, pordb_land):
	def __init__(self, comboBoxNation, nation_fuellen, parent=None):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		
		self.connect(self.pushButtonLandSpeichern, QtCore.SIGNAL("clicked()"), self.onSpeichern)
		self.connect(self.pushButtonLandAbbrechen, QtCore.SIGNAL("clicked()"), self.close)
		
		self.nation_fuellen = nation_fuellen
		
		zu_lesen = "select * from pordb_iso_land order by land"
		lese_func = DBLesen(self, zu_lesen)
		res = DBLesen.get_data(lese_func)
		row = 0
		self.tableWidgetLaender.clear()
		self.tableWidgetLaender.setRowCount(len(res) + 1)
		for i in res:
			column = 0
			for j in i:
				if j:
					newitem = QtGui.QTableWidgetItem(j.strip())
				else:
					newitem = QtGui.QTableWidgetItem(" ")
				self.tableWidgetLaender.setItem(row, column, newitem)
				column += 1
			row += 1
		self.tableWidgetLaender.setHorizontalHeaderLabels(["ISO Code", self.trUtf8("Country"), self.trUtf8("active"), self.trUtf8("Nationality")])
		self.tableWidgetLaender.setAlternatingRowColors(True)
		self.tableWidgetLaender.resizeColumnsToContents()
		self.tableWidgetLaender.resizeRowsToContents()
		
	def onSpeichern(self):
		position = 0
		zu_erfassen = []
		zu_erfassen.append("delete from pordb_iso_land")
		for i in range(self.tableWidgetLaender.rowCount()):
			cell = []
			position += 1
			for j in range(self.tableWidgetLaender.columnCount()):
				tableItem = self.tableWidgetLaender.item(i, j)
				try:
					cellItem = str(QtGui.QTableWidgetItem(tableItem).text())
					cell.append(cellItem)
				except:
					pass
			try:
				if cell[0]:
					zu_erfassen.append("insert into pordb_iso_land (iso, land, aktiv, national) values ('" +cell[0] +"', '" +cell[1] +"', '" +cell[2] +"', '" +cell[3] +"')")
			except:
				pass
		
		update_func = DBUpdate(self, zu_erfassen)
		DBUpdate.update_data(update_func)
		
		self.nation_fuellen()
		self.close()
