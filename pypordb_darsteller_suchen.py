# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from pordb_darsteller_suchen import Ui_DarstellerSuche as pordb_darsteller_suchen
from pypordb_dblesen import DBLesen

class DarstellerSuchen(QtGui.QDialog, pordb_darsteller_suchen):
	def __init__(self, parent=None):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		
		self.maximum = QtCore.QDate.currentDate()
		self.minimum = QtCore.QDate.fromString("20000101", "yyyyMMdd")
		self.dateEditDarstellerSucheAb.setDateRange(self.minimum, self.maximum)
		self.dateEditDarstellerSucheBis.setDateRange(self.minimum, self.maximum)
		self.dateEditDarstellerSucheBis.setDate(self.maximum)
		
		self.connect(self.pushButtonSuchen, QtCore.SIGNAL("clicked()"), self.accept)
		self.connect(self.pushButtonCancel, QtCore.SIGNAL("clicked()"), self.close)
		self.connect(self.pushButtonRefresh, QtCore.SIGNAL("clicked()"), self.onRefresh)
		
		# Combobox für Nation füllen
		zu_lesen = "select * from pordb_iso_land where aktiv = 'x' order by land"
		lese_func = DBLesen(self, zu_lesen)
		res = DBLesen.get_data(lese_func)
		self.comboBoxDarstellerSucheNation.addItem("")
		for i in res:
			text = '%2s %-50s' % (i[0], i[1])
			self.comboBoxDarstellerSucheNation.addItem(text)
		
	def onRefresh(self):
		self.lineEditDarstellerSuche.setText("")
		self.comboBoxDarstellerSucheGeschlecht.setCurrentIndex(-1)
		self.lineEditActor1.setText("")
		self.lineEditActor2.setText("")
		self.lineEditActor3.setText("")
		self.dateEditDarstellerSucheAb.setDate(self.minimum)
		self.dateEditDarstellerSucheBis.setDate(self.maximum)
		self.comboBoxDarstellerSucheHaar.setCurrentIndex(-1)
		self.comboBoxDarstellerSucheNation.setCurrentIndex(0)
		self.comboBoxDarstellerSucheTattoo.setCurrentIndex(-1)
		self.lineEditDarstellerSucheTattoo.setText("")
		self.comboBoxDarstellerSucheEthnic.setCurrentIndex(-1)
		self.lineEditDarstellerSuche.setFocus()
