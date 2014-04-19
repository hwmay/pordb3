# -*- coding: utf-8 -*-

import time
from PyQt4 import QtGui, QtCore
from pypordb_dblesen import DBLesen
from pypordb_dbupdate import DBUpdate
from pordb_darstellerneu import Ui_Dialog as pordb_darstellerneu

class NeueingabeDarsteller(QtGui.QDialog, pordb_darstellerneu):
	def __init__(self, darsteller, parent=None):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		self.darsteller = darsteller
		
		self.connect(self.pushButtonDarstellerneuSpeichern, QtCore.SIGNAL("clicked()"), self.accept)
		self.connect(self.pushButtonDarstellerneuCancel, QtCore.SIGNAL("clicked()"), self.close)
		
		self.setWindowTitle(self.trUtf8("Actor ") +self.darsteller + self.trUtf8(" will be added"))
		# Combobox für Nation füllen
		zu_lesen = "select * from pordb_iso_land where aktiv = 'x' order by land"
		lese_func = DBLesen(self, zu_lesen)
		res = DBLesen.get_data(lese_func)
		for i in res:
			text = '%2s %-50s' % (i[0], i[1])
			self.comboBoxDarstellerneuNation.addItem(text)
		
	def accept(self):
		if not self.comboBoxDarstellerneuGeschlecht.currentText():
			message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Please select the gender"))
			return
		# insert/update-Anweisung aufbauen
		datum = str(time.localtime()[0]) + '-' + str(time.localtime()[1]) + '-' + str(time.localtime()[2])
		zu_erfassen = str("INSERT into pordb_darsteller VALUES ('" +self.darsteller.replace("'", "''") +"', '" +str(self.comboBoxDarstellerneuGeschlecht.currentText()) + "', '" +str(0) +"', '" +datum +"', '" +str(self.comboBoxDarstellerneuHaarfarbe.currentText()) +"', '" +str(self.comboBoxDarstellerneuNation.currentText())[0:2] +"', '" +self.lineEditDarstellerneuTattoo.text().replace("'", "''") +"', '" +str(self.comboBoxDarstellerneuEthnic.currentText()) +"')")
		update_func = DBUpdate(self, zu_erfassen)
		DBUpdate.update_data(update_func)
		self.close()
