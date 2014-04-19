# -*- coding: utf-8 -*-

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
		
		zu_lesen = "select * from pordb_bookmarks order by z"
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
		zu_erfassen = "insert into pordb_bookmarks (url) values ('" +self.url +"')"
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
			zu_erfassen = "delete from pordb_bookmarks where z = " +str(item.text())
			update_func = DBUpdate(self, zu_erfassen)
			DBUpdate.update_data(update_func)
			self.close()
		except:
			pass
