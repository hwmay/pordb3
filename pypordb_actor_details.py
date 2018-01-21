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
from pordb_actor_details import Ui_Dialog as pordb_actor_details
from pypordb_dblesen import DBLesen
import os

class ActorDetails(QtWidgets.QDialog, pordb_actor_details):
    def __init__(self, darsteller, verzeichnis):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.pushButtonOk.clicked.connect(self.close)
        
        self.darsteller = darsteller
        self.verzeichnis = verzeichnis
        
        settings = QtCore.QSettings()
        window_size = settings.value("ActorDetails/Size", QtCore.QSize(600, 500))
        self.resize(window_size)
        window_position = settings.value("ActorDetails/Position", QtCore.QPoint(0, 0))
        self.move(window_position)
        
        self.pushButtonOk.setFocus()
        width = 400
        height = 600
        
        zu_lesen = "SELECT * FROM pordb_darsteller WHERE darsteller = %s"
        lese_func = DBLesen(self, zu_lesen, self.darsteller)
        res = DBLesen.get_data(lese_func)
        
        bildname = darsteller.lower().strip().replace(" ", "_").replace("'", "_apostroph_")
        bilddarsteller = os.path.join(verzeichnis, "darsteller_" + res[0][1], bildname +".jpg")
        if not os.path.isfile(bilddarsteller):
            bilddarsteller = os.path.join(verzeichnis, "darsteller_" + res[0][1], bildname + ".png")
            if not os.path.isfile(bilddarsteller):
                bilddarsteller = os.path.join(verzeichnis, "nichtvorhanden", "nicht_vorhanden.jpg")
        
        self.bildQImage = QtGui.QImage(bilddarsteller)
        self.labelBild1.setAlignment(QtCore.Qt.AlignCenter)
        image = self.bildQImage.scaled(width, height, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.labelBild1.setPixmap(QtGui.QPixmap.fromImage(image))

        self.labelName.setText(self.darsteller)
        
        self.plainTextEditTattoos.setPlainText(res[0][6])
        
        if res[0][11]:
            self.lineEditUrl.setText(res[0][11])
        
        self.lineEditDate.setText(str(res[0][3]))
        
    def closeEvent(self, event):
        settings = QtCore.QSettings()
        settings.setValue("ActorDetails/Size", self.size())
        settings.setValue("ActorDetails/Position", self.pos())
        
