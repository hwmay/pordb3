# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from pordb_bilddatei_umbenennen import Ui_Dialog as pordb_bilddatei_umbenennen
import os

class BilddateiUmbenennen(QtGui.QDialog, pordb_bilddatei_umbenennen):
	def __init__(self, datei, parent=None):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		
		self.connect(self.pushButtonUmbenennen, QtCore.SIGNAL("clicked()"), self.accept)
		self.connect(self.pushButtonCancel, QtCore.SIGNAL("clicked()"), self.close)
		
		settings = QtCore.QSettings()
		window_size = settings.value("Bilddatei_Umbenennen/Size", QtCore.QSize(600, 500))
		self.resize(window_size)
		window_position = settings.value("Bilddatei_Umbenennen/Position", QtCore.QPoint(0, 0))
		self.move(window_position)
		
		self.datei = str(datei).replace("''", "'")
		
		dateiname = os.path.basename(self.datei)
		self.dateiname_basis = dateiname.split(".")[0]
		self.lineEditDateiname.clear()
		self.lineEditDateiname.insert(dateiname)
		self.lineEditDateiname.setFocus()
		try:
			dateiliste = os.listdir(os.path.dirname(self.datei))
			for i in dateiliste:
				if self.dateiname_basis in i:
					self.listWidgetDateinamen.addItem(i)
		except:
			pass
		self.listWidgetDateinamen.sortItems()
				
	def accept(self):
		neuer_dateiname = str(self.lineEditDateiname.text())
		if len(neuer_dateiname) > 256:
			self.labelDateiname.setText("<font color=red>" +self.trUtf8("Filename must not have more than 256 characters") +"</font>")
			message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Filename must not have more than 256 characters"))
			return
		if "/" in neuer_dateiname:
			self.labelDateiname.setText("<font color=red>" +self.trUtf8("Filename must not have any slash") +"</font>")
			message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Filename must not have any slash"))
			return
		if os.path.exists(os.path.dirname(self.datei) +os.sep +neuer_dateiname):
			self.labelDateiname.setText("<font color=red>" +self.trUtf8("File already exists") +"</font>")
			message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("File already exists"))
			return
		
		self.close()
		QtGui.QDialog.accept(self)
		
		
	def closeEvent(self, event):
		settings = QtCore.QSettings()
		settings.setValue("Bilddatei_Umbenennen/Size", self.size())
		settings.setValue("Bilddatei_Umbenennen/Position", self.pos())
