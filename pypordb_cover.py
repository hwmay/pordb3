# -*- coding: utf-8 -*-

import os
from PyQt4 import QtGui, QtCore
from pordb_cover import Ui_Dialog as pordb_cover
from pypordb_dblesen import DBLesen

class Cover(QtGui.QDialog, pordb_cover):
	def __init__(self, cover, verzeichnis_original, original=None, parent=None):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		self.cover = cover
		self.original = original
		self.verzeichnis_original = verzeichnis_original
		self.filename = None
		self.originaldatei = None
		
		self.connect(self.pushButtonCoverOriginalAlt, QtCore.SIGNAL("clicked()"), self.onCoverOriginalAlt)
		self.connect(self.pushButtonCover, QtCore.SIGNAL("clicked()"), self.accept)
		self.connect(self.pushButtonCancel, QtCore.SIGNAL("clicked()"), self.close)
		
		self.pushButtonCover.setFocus()
		width = 280
		height = 366
		self.bildQImage = QtGui.QImage(cover[0])
		self.labelBild1.setAlignment(QtCore.Qt.AlignTop)
		image = self.bildQImage.scaled(width, height, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
		self.labelBild1.setPixmap(QtGui.QPixmap.fromImage(image))
		self.labelBilddatei1.setText(cover[0])
		self.labelSize1.setText(str(self.bildQImage.width()) +"x" +str(self.bildQImage.height()))
		
		self.bildQImage = QtGui.QImage(cover[1])
		self.labelBild2.setAlignment(QtCore.Qt.AlignTop)
		image = self.bildQImage.scaled(width, height, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
		self.labelBild2.setPixmap(QtGui.QPixmap.fromImage(image))
		self.labelBilddatei2.setText(cover[1])
		self.labelSize2.setText(str(self.bildQImage.width()) +"x" +str(self.bildQImage.height()))
		
		self.radioButtonBild1.setChecked(True)
		self.lineEditDateiname.setFocus()
		
	def keyPressEvent(self, event):
		try:
			if event.modifiers() & QtCore.Qt.ControlModifier:
				if event.key() == QtCore.Qt.Key_Y:
					self.onCoverOriginalAlt()
					self.update()
			elif event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
				self.accept()
			elif event.key() == QtCore.Qt.Key_Escape:
				self.close()
			else:
				self.keyPressEvent(self)
		except:
			pass
	
	def onCoverOriginalAlt(self):
		zu_lesen = "SELECT * FROM pordb_vid_neu"
		lese_func = DBLesen(self, zu_lesen)
		res = DBLesen.get_data(lese_func)
		if res[0][3]:
			self.lineEditDateiname.setText(res[0][3])
		self.pushButtonCover.setFocus()
		
	def accept(self):
		if not self.radioButtonBild1.isChecked() and not self.radioButtonBild2.isChecked():
			message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Please mark front side"))
			return
		
		if self.radioButtonBild2.isChecked():
			self.cover.reverse()
			
		bild1 = QtGui.QPixmap(self.cover[0])
		bild2 = QtGui.QPixmap(self.cover[1])
		w = bild1.width() + bild2.width()
		h = max(bild1.height(), bild2.height())
		bild = QtGui.QPixmap(w, h)
		bild.fill(QtGui.QColor("white"))
		
		p = QtGui.QPainter(bild)
		p.drawPixmap(0, 0, bild1)
		p.drawPixmap(bild1.width(), 0, bild2)
		p.end()
		if self.original:
			self.lineEditDateiname.setText(self.original)
			self.originaldatei = self.original
		else:
			self.originaldatei = str(self.lineEditDateiname.text())
		dateiname = str(self.lineEditDateiname.text()).strip()
		if not dateiname:
			message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Please enter a file name"))
			return
		if dateiname.find("/") > -1:
			message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Error: Original has a character /"))
			return
		if not dateiname.endswith(".jpg"):
			dateiname += ".jpg"
		original = self.verzeichnis_original +os.sep +dateiname
		bild.save(original)
		if original != self.cover[0]:
			os.remove(self.cover[0])
		if original != self.cover[1]:
			os.remove(self.cover[1])
		self.filename = original
		
		self.close()
		
	def datei(self):
		return self.filename, self.originaldatei
