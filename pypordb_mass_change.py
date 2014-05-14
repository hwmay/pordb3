# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from pordb_mass_change import Ui_Dialog as pordb_mass_change

class MassChange(QtGui.QDialog, pordb_mass_change):
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		self.buttonBox.accepted.connect(self.accept)
		self.buttonBox.rejected.connect(self.close)
		
	def accept(self):
		if not self.radioButtonVorhandenJa.isChecked() and not self.radioButtonVorhandenNein.isChecked():
			message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Please mark whether movie is available"))
			return
		if self.radioButtonVorhandenNein.isChecked() and self.comboBoxResolution.currentIndex() != 0:
			message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Video is not in stock: resolution is set to unknown"))
			self.comboBoxResolution.setCurrentIndex(0)
			
		if self.radioButtonVorhandenJa.isChecked():
			self.vorhanden = True
		else:
			self.vorhanden = False
			
		self.resolution = self.comboBoxResolution.currentIndex()
			
		self.close()
		