# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from pordb_suche_video import Ui_Dialog as pordb_suche_video
from pypordb_dblesen import DBLesen

class SucheVideo(QtGui.QDialog, pordb_suche_video):
	def __init__(self, app, titel=None, parent=None):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		
		self.connect(self.pushButtonSuchen, QtCore.SIGNAL("clicked()"), self.onSuchen)
		self.connect(self.pushButtonAnzeigen, QtCore.SIGNAL("clicked()"), self.onAnzeigen)
		self.connect(self.pushButtonAbbrechen, QtCore.SIGNAL("clicked()"), self.close)
		
		self.app = app
		
		self.zu_lesen = ""
		self.textEditVideo.setFocus()
		self.res_alle = []
		self.titel = titel
		if self.titel:
			self.pushButtonSuchen.setEnabled(False)
			j = ""
			for i in self.titel:
				j += i + "\n"
			self.textEditVideo.setText(j)
			self.onSuchen()
		else:
			self.pushButtonSuchen.setEnabled(True)
		
	def onSuchen(self):
		self.listWidgetVideo.clear()
		vorhanden = []
		self.res_alle = []
		self.app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
		for i in self.titel:
			if i:
				zu_lesen = "select distinct on (original) * from pordb_vid where original like '" +i.replace("'", "''").title() +"  %' or original like '" +i.replace("'", "''").title() +" (%'"
				lese_func = DBLesen(self, zu_lesen)
				res = DBLesen.get_data(lese_func)
				if res:
					vorhanden.append("x")
					self.res_alle.extend(res)
				else:
					vorhanden.append(" ")
		self.label_insgesamt.setText(str(len(self.titel)))
		self.label_vorhanden.setText(str(len(self.res_alle)))
		self.listWidgetVideo.setMinimumHeight(len(self.titel) * 20)
		self.listWidgetVideo.addItems(vorhanden)
		self.app.restoreOverrideCursor()
		
	def onAnzeigen(self):
		self.zu_lesen = ""
		if self.res_alle:
			self.zu_lesen = "SELECT * FROM pordb_vid where original = '"
			for i in self.res_alle:
				original = i[5]
				self.zu_lesen += original.strip().replace("'", "''") 
				if i != self.res_alle[len(self.res_alle) -1]:
					self.zu_lesen += "' or original = '"
				else:
					self.zu_lesen += "'"
			self.zu_lesen += " order by original"
		self.close()
