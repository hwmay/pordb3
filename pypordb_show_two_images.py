# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from pordb_show_two_images import Ui_Dialog as pordb_show_two_images

class ShowTwoImages(QtGui.QDialog, pordb_show_two_images):
	def __init__(self, bilddatei1, bilddatei2):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		self.bilddatei1 = bilddatei1
		self.bilddatei2 = bilddatei2
		self.filename = None
		
		self.connect(self.pushButtonOk, QtCore.SIGNAL("clicked()"), self.accept)
		self.connect(self.pushButtonCancel, QtCore.SIGNAL("clicked()"), self.close)
		
		self.pushButtonOk.setFocus()
		width = 280
		height = 366
		self.bildQImage = QtGui.QImage(self.bilddatei1)
		self.labelBild1.setAlignment(QtCore.Qt.AlignTop)
		image = self.bildQImage.scaled(width, height, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
		self.labelBild1.setPixmap(QtGui.QPixmap.fromImage(image))
		self.labelBilddatei1.setText(self.bilddatei1)
		
		self.bildQImage = QtGui.QImage(self.bilddatei2)
		self.labelBild2.setAlignment(QtCore.Qt.AlignTop)
		image = self.bildQImage.scaled(width, height, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
		self.labelBild2.setPixmap(QtGui.QPixmap.fromImage(image))
		self.labelBilddatei2.setText(self.bilddatei2)
		self.radioButtonBild1.setChecked(True)
		
	def accept(self):
		if self.radioButtonBild1.isChecked():
			self.wanted_file = 1
		else:
			self.wanted_file = 2
		
		self.close()
		
	def datei(self):
		return self.wanted_file
