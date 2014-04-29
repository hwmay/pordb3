# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from pordb_bildschneiden import Ui_Dialog as pordb_bildschneiden

size = QtCore.QSize(260, 260)

class Bildbeschneiden(QtGui.QDialog, pordb_bildschneiden):
	def __init__(self, bilddatei, positionX, positionY, parent=None):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		self.bilddatei = bilddatei
		self.positionX = positionX
		self.positionY = positionY
		
		self.connect(self.pushButtonNeuSpeichern, QtCore.SIGNAL("clicked()"), self.onSpeichern)
		self.connect(self.pushButtonNeuSpeichernAls, QtCore.SIGNAL("clicked()"), self.onSpeichernAls)
		self.connect(self.pushButtonNeuCancel, QtCore.SIGNAL("clicked()"), self.close)
		
		# Workaround, weil keine Scrollarea in Qt Designer
		self.sa = QtGui.QScrollArea()
		self.labelBild.setParent(None)
		self.sa.setWidget(self.labelBild)
		self.vboxlayout.insertWidget(0, self.sa)
		
		settings = QtCore.QSettings()
		window_size = settings.value("Bildbeschneiden/Size", QtCore.QSize(600, 500))
		self.resize(window_size)
		window_position = settings.value("Bildbeschneiden/Position", QtCore.QPoint(0, 0))
		self.move(window_position)
		
		self.bildQImage = QtGui.QImage(bilddatei)
		self.showImage(self.positionX, self.positionY)
		
	def showImage(self, positionX, positionY):
		width = self.bildQImage.width()
		height = self.bildQImage.height()
		self.labelBild.setMinimumSize(QtCore.QSize(width, height))
		self.labelBild.setAlignment(QtCore.Qt.AlignTop)
		image = self.bildQImage.scaled(width, height, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
		self.labelBild.setPixmap(QtGui.QPixmap.fromImage(image))
		self.sa.horizontalScrollBar().setMaximum(positionX)
		self.sa.verticalScrollBar().setMaximum(positionY)
		self.sa.horizontalScrollBar().setValue(positionX)
		self.sa.verticalScrollBar().setValue(positionY)
		
	def mousePressEvent(self, event):
		if event.button() == QtCore.Qt.LeftButton:
			# save position of scrollbars
			self.positionX = self.sa.horizontalScrollBar().value()
			self.positionY = self.sa.verticalScrollBar().value()
			# get the position of the left mouse cursor
			self.x1 = int(event.x()) - self.labelBild.x() - self.sa.x()
			self.y1 = int(event.y()) - self.labelBild.y() - self.sa.y()
		elif event.button() == QtCore.Qt.RightButton:
			# get the position of the right mouse cursor
			self.x2 = int(event.x()) - self.labelBild.x() - self.sa.x()
			self.y2 = int(event.y()) - self.labelBild.y() - self.sa.y()
			# crop the image and show it
			try:
				self.point1 = QtCore.QPoint(self.x1, self.y1)
				self.point2 = QtCore.QPoint(self.x2 - self.x1, self.y2 - self.y1)
				self.bildQImage = QtGui.QImage.copy(self.bildQImage, self.point1.x(), self.point1.y(), self.point2.x(), self.point2.y())
				self.showImage(0, 0)
			except:
				pass
			
	def onSpeichern(self):
		self.bildQImage = self.bildQImage.scaled(size, QtCore.Qt.KeepAspectRatio)
		if self.bildQImage.save(self.bilddatei):
			self.close()
		else:
			message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Error, image file could not be saved"))
			return 
	
	def onSpeichernAls(self):
		filename = QtGui.QFileDialog.getSaveFileName(self, self.trUtf8("jpg files"), self.bilddatei, self.trUtf8("jpg files (*.jpg)"))
		self.bildQImage = self.bildQImage.scaled(size, QtCore.Qt.KeepAspectRatio)
		if self.bildQImage.save(filename):
			self.close()
		else:
			message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Error, image file could not be saved"))
			return 
		
	def closeEvent(self, event):
		settings = QtCore.QSettings()
		settings.setValue("Bildbeschneiden/Size", self.size())
		settings.setValue("Bildbeschneiden/Position", self.pos())
