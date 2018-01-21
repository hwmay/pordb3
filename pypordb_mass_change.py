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
from pordb_mass_change import Ui_Dialog as pordb_mass_change

class MassChange(QtWidgets.QDialog, pordb_mass_change):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.close)
        
        self.vorhanden = False
        self.watched = False
        self.resolution = False
        
    def accept(self):
        if not self.radioButtonVorhandenJa.isChecked() and not self.radioButtonVorhandenNein.isChecked():
            message = QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("Please mark whether movie is available"))
            return
        if not self.radioButtonWatchedJa.isChecked() and not self.radioButtonWatchedNein.isChecked():
            message = QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("Please mark whether movie has been watched"))
            return
        if self.radioButtonVorhandenNein.isChecked() and self.comboBoxResolution.currentIndex() != 0:
            message = QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("Video is not in stock: resolution is set to unknown"))
            self.comboBoxResolution.setCurrentIndex(0)
        if self.radioButtonVorhandenJa.isChecked() and self.comboBoxResolution.currentIndex() == 0:
            message = QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("Please select a resolution"))
            return
            
        if self.radioButtonVorhandenJa.isChecked():
            self.vorhanden = True
        else:
            self.vorhanden = False
        
        if self.radioButtonWatchedJa.isChecked():
            self.watched = True
        else:
            self.watched = False            
            
        if self.comboBoxResolution.currentIndex() == 1:
            self.resolution = "0"
        elif self.comboBoxResolution.currentIndex() == 2:
            self.resolution = "1"
        elif self.comboBoxResolution.currentIndex() == 3:
            self.resolution = "2"
        elif self.comboBoxResolution.currentIndex() == 4:
            self.resolution = "3"
        elif self.comboBoxResolution.currentIndex() == 5:
            self.resolution = "9"
            
        self.close()
        
