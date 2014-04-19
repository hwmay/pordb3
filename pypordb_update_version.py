# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from pordb_update_version import Ui_Dialog as pordb_update_version
import os
import urllib.request, urllib.error, urllib.parse
import tempfile
import zipfile

file_download = "https://github.com/hwmay/pordb3/archive/master.zip"

class UpdateVersion(QtGui.QDialog, pordb_update_version):
	def __init__(self, version, whatsnew):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		self.connect(self.pushButtonYes, QtCore.SIGNAL("clicked()"), self.accept)
		self.connect(self.pushButtonNo, QtCore.SIGNAL("clicked()"), self.close)
		
		self.version = version
		self.whatsnew = whatsnew
		
		settings = QtCore.QSettings()
		window_size = settings.value("UpdateVersion/Size", QtCore.QSize(600, 500))
		self.resize(window_size)
		window_position = settings.value("UpdateVersion/Position", QtCore.QPoint(0, 0))
		self.move(window_position)
		
		self.pushButtonYes.setFocus()
		
		self.plainTextEditWhatsnew.setPlainText("Version: " + self.version + "\n" + "\n")
		
		whatsnew_list = self.whatsnew.split("\\")
		for i in whatsnew_list:
			self.plainTextEditWhatsnew.appendPlainText(i)
		
	def accept(self):
		self.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
		zaehler = 0
		seite = None
		while True:
			zaehler += 1
			try:
				seite = urllib.request.urlopen(file_download)
				if seite:
					break
				else:
					pass
			except:
			    pass
			if zaehler > 1:
				break
			
		if seite:
			tmp = tempfile.TemporaryFile()
			tmp.write(seite.read())
			datei = zipfile.ZipFile(tmp, "r")
			tmp_zip = tempfile.TemporaryFile()
			liste = zipfile.ZipFile.namelist(datei)
			for i in liste:
				data = datei.read(i)
				df = i.replace("pordb3-master/", "")
				print (df)
				if df:
					if df != "pypordb/":
						writefile = open(df, "wb")
						writefile.write(data)
						writefile.close()
			
		self.unsetCursor()
		self.close
		QtGui.QDialog.accept(self)
	
	def closeEvent(self, event):
		settings = QtCore.QSettings()
		settings.setValue("UpdateVersion/Size", self.size())
		settings.setValue("UpdateVersion/Position", self.pos())
		