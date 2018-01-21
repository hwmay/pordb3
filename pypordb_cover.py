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

import os
from PyQt5 import QtGui, QtCore, QtWidgets
from pordb_cover import Ui_Dialog as pordb_cover
from pypordb_dblesen import DBLesen

class Cover(QtWidgets.QDialog, pordb_cover):
    def __init__(self, cover, verzeichnis_original, original=None, parent=None):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.cover = cover
        self.original = original
        self.verzeichnis_original = verzeichnis_original
        self.filename = None
        self.originaldatei = None
        
        self.pushButtonCoverOriginalAlt.clicked.connect(self.onCoverOriginalAlt)
        self.pushButtonCover.clicked.connect(self.accept)
        self.pushButtonCancel.clicked.connect(self.close)
        
        self.pushButtonCover.setFocus()
        width = 280
        height = 366
        self.bildQImage = QtGui.QImage(cover[0])
        self.labelBild1.setAlignment(QtCore.Qt.AlignTop)
        image = self.bildQImage.scaled(width, height, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.labelBild1.setPixmap(QtWidgets.QPixmap.fromImage(image))
        self.labelBilddatei1.setText(cover[0])
        self.labelSize1.setText(str(self.bildQImage.width()) +"x" +str(self.bildQImage.height()))
        
        self.bildQImage = QtGui.QImage(cover[1])
        self.labelBild2.setAlignment(QtCore.Qt.AlignTop)
        image = self.bildQImage.scaled(width, height, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.labelBild2.setPixmap(QtWidgets.QPixmap.fromImage(image))
        self.labelBilddatei2.setText(cover[1])
        self.labelSize2.setText(str(self.bildQImage.width()) +"x" +str(self.bildQImage.height()))
        
        zu_lesen = "SELECT * FROM pordb_vid_neu"
        self.lese_func = DBLesen(self, zu_lesen)
        self.res_vid_neu = DBLesen.get_data(self.lese_func)
        if self.res_vid_neu[0][3]:
            self.labelOriginal.setText(self.res_vid_neu[0][3])        
        
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
        if self.res_vid_neu[0][3]:
            self.lineEditDateiname.setText(self.res_vid_neu[0][3])
        self.pushButtonCover.setFocus()
        
    def accept(self):
        if not self.radioButtonBild1.isChecked() and not self.radioButtonBild2.isChecked():
            message = QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("Please mark front side"))
            return
        
        if self.radioButtonBild2.isChecked():
            self.cover.reverse()
            
        bild1 = QtWidgets.QPixmap(self.cover[0])
        bild2 = QtWidgets.QPixmap(self.cover[1])
        w = bild1.width() + bild2.width()
        h = max(bild1.height(), bild2.height())
        bild = QtWidgets.QPixmap(w, h)
        bild.fill(QtGui.QColor("white"))
        
        p = QtWidgets.QPainter(bild)
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
            message = QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("Please enter a file name"))
            return
        if dateiname.find("/") > -1:
            message = QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("Error: Original has a character /"))
            return
        if not dateiname.endswith(".jpg"):
            dateiname += ".jpg"
        original = os.path.join(self.verzeichnis_original, dateiname)
        bild.save(original)
        if original != self.cover[0]:
            os.remove(self.cover[0])
        if original != self.cover[1]:
            os.remove(self.cover[1])
        self.filename = original
        
        self.close()
        
    def datei(self):
        return self.filename, self.originaldatei
