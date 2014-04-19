# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from pordb_suchen import Ui_ErweiterteSuche as pordb_suchen

class Suchen(QtGui.QDialog, pordb_suchen):
	def __init__(self, parent=None):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		
		self.connect(self.pushButtonSuchen, QtCore.SIGNAL("clicked()"), self.accept)
		self.connect(self.pushButtonCancel, QtCore.SIGNAL("clicked()"), self.close)
		self.connect(self.pushButtonRefresh, QtCore.SIGNAL("clicked()"), self.onRefresh)
		
	def onRefresh(self):
		self.lineEditDarsteller.setText("")
		self.lineEditCD.setText("")
		self.lineEditTitel.setText("")
		self.lineEditOriginal.setText("")
		self.checkBoxVid.setChecked(False)
		self.comboBoxCS.setCurrentIndex(-1)
		self.lineEditDarsteller.setFocus()
