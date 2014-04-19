# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from pordb_bildgross import Ui_Dialog as pordb_bildgross

class DarstellerAnzeigeGross(QtGui.QDialog, pordb_bildgross):
	def __init__(self, bild, parent=None):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		
		self.bild = bild
		
		# Workaround, weil keine Scrollarea in Qt Designer
		self.sa = QtGui.QScrollArea()
		self.labelBildgross.setParent(None)
		self.sa.setWidget(self.labelBildgross)
		self.hboxlayout.insertWidget(0, self.sa)
		self.bildQImage = QtGui.QImage(self.bild)
		self.showImage()
		
	def showImage(self):
		width = self.bildQImage.width()
		height = self.bildQImage.height()
		self.resize(QtCore.QSize(QtCore.QRect(0,0,width+30,height+30).size()).expandedTo(self.minimumSizeHint()))
		self.labelBildgross.setBaseSize(QtCore.QSize(width, height))
		self.labelBildgross.setAlignment(QtCore.Qt.AlignTop)
		
		self.labelBildgross.setGeometry(QtCore.QRect(0,0,width,height))
		image = self.bildQImage.scaled(width, height, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
		self.labelBildgross.setPixmap(QtGui.QPixmap.fromImage(image))
		self.sa.ensureVisible(0, 0)
