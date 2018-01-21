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
from pordb_show_two_images import Ui_Dialog as pordb_show_two_images

class ShowTwoImages(QtWidgets.QDialog, pordb_show_two_images):
    def __init__(self, bilddatei1, bilddatei2):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.bilddatei1 = bilddatei1
        self.bilddatei2 = bilddatei2
        self.filename = None
        self.wanted_file = None
        
        self.pushButtonOk.clicked.connect(self.accept)
        self.pushButtonCancel.clicked.connect(self.close)
        
        self.pushButtonOk.setFocus()
        width = 280
        height = 366
        self.bildQImage = QtGui.QImage(self.bilddatei1)
        self.labelBild1.setAlignment(QtCore.Qt.AlignTop)
        image = self.bildQImage.scaled(width, height, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.labelBild1.setPixmap(QtGui.QPixmap.fromImage(image))
        self.labelBilddatei1.setText(self.bilddatei1)
        self.labelSize1.setText(str(QtGui.QPixmap(self.bilddatei1).width()) +"x" +str(QtGui.QPixmap(self.bilddatei1).height()))
        
        self.bildQImage = QtGui.QImage(self.bilddatei2)
        self.labelBild2.setAlignment(QtCore.Qt.AlignTop)
        image = self.bildQImage.scaled(width, height, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.labelBild2.setPixmap(QtGui.QPixmap.fromImage(image))
        self.labelBilddatei2.setText(self.bilddatei2)
        self.labelSize2.setText(str(QtGui.QPixmap(self.bilddatei2).width()) +"x" +str(QtGui.QPixmap(self.bilddatei2).height()))
        
        self.radioButtonBild1.setChecked(True)
        
    def accept(self):
        if self.radioButtonBild1.isChecked():
            self.wanted_file = 1
        else:
            self.wanted_file = 2
            
        self.close()
        
    def datei(self):
        return self.wanted_file
