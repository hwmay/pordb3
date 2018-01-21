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
from pordb_bildgross import Ui_Dialog as pordb_bildgross

class DarstellerAnzeigeGross(QtWidgets.QDialog, pordb_bildgross):
    def __init__(self, bild, parent=None):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        
        self.bild = bild
        
        # Workaround, weil keine Scrollarea in Qt Designer
        self.sa = QtWidgets.QScrollArea()
        self.labelBildgross.setParent(None)
        self.sa.setWidget(self.labelBildgross)
        self.hboxlayout.insertWidget(0, self.sa)
        self.bildQImage = QtGui.QImage(self.bild)
        self.showImage()
        
    def showImage(self):
        width = self.bildQImage.width()
        height = self.bildQImage.height()
        #self.resize(QtCore.QSize(QtCore.QRect(0,0,width+30,height+30).size()).expandedTo(self.minimumSizeHint()))
        #self.labelBildgross.setBaseSize(QtCore.QSize(width, height))
        self.labelBildgross.setGeometry(QtCore.QRect(0,0,width,height))
        #self.labelBildgross.setAlignment(QtCore.Qt.AlignCenter)
        image = self.bildQImage.scaled(width, height, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.labelBildgross.setPixmap(QtGui.QPixmap.fromImage(image))
        self.sa.ensureVisible(0, 0)
        self.showFullScreen()
