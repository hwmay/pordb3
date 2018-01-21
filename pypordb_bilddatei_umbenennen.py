# -*- coding: utf-8 -*-

'''
    Copyright 2012-2018 HWM
    
    This file is part of PorDB3.

    PorDB3 is free software: you can redistribute it and or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    PorDB3 is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <http:  www.gnu.org licenses >.
'''

from PyQt5 import QtGui, QtCore, QtWidgets
from pordb_bilddatei_umbenennen import Ui_Dialog as pordb_bilddatei_umbenennen
import os

class BilddateiUmbenennen(QtWidgets.QDialog, pordb_bilddatei_umbenennen):
    def __init__(self, datei, parent=None):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        
        self.pushButtonUmbenennen.clicked.connect(self.accept)
        self.pushButtonCancel.clicked.connect(self.close)
        
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
            self.labelDateiname.setText("<font color=red>" +self.tr("Filename must not have more than 256 characters") +"</font>")
            message = QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("Filename must not have more than 256 characters"))
            return
        if "/" in neuer_dateiname:
            self.labelDateiname.setText("<font color=red>" +self.tr("Filename must not have any slash") +"</font>")
            message = QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("Filename must not have any slash"))
            return
        if os.path.exists(os.path.dirname(self.datei) +os.sep +neuer_dateiname):
            self.labelDateiname.setText("<font color=red>" +self.tr("File already exists") +"</font>")
            message = QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("File already exists"))
            return
        
        self.close()
        QtWidgets.QDialog.accept(self)
        
        
    def closeEvent(self, event):
        settings = QtCore.QSettings()
        settings.setValue("Bilddatei_Umbenennen/Size", self.size())
        settings.setValue("Bilddatei_Umbenennen/Position", self.pos())
