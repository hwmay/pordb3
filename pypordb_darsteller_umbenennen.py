# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from pordb_darsteller_umbenennen import Ui_Dialog as pordb_darsteller_umbenennen

class DarstellerUmbenennen(QtGui.QDialog, pordb_darsteller_umbenennen):
	def __init__(self, alter_name, parent=None):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		
		self.connect(self.pushButtonUmbenennen, QtCore.SIGNAL("clicked()"), self.accept)
		self.connect(self.pushButtonCancel, QtCore.SIGNAL("clicked()"), self.close)
		
		self.lineEditNeuerName.setText(alter_name.strip("=").replace("''", "'"))
