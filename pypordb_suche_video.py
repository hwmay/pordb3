# -*- coding: utf-8 -*-

'''
    Copyright 2012-2018 HWM
    
    This file is part of PorDB3.

    PorDB3 is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    PorDB3 is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
'''

from PyQt5 import QtGui, QtCore, QtWidgets
from pordb_suche_video import Ui_Dialog as pordb_suche_video
from pypordb_dblesen import DBLesen

class SucheVideo(QtWidgets.QDialog, pordb_suche_video):
    def __init__(self, app, titel=None, parent=None):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        
        self.pushButtonSuchen.clicked.connect(self.onSuchen)
        self.pushButtonAnzeigen.clicked.connect(self.onAnzeigen)
        self.pushButtonAbbrechen.clicked.connect(self.close)
        self.listWidgetVideo.verticalScrollBar().valueChanged.connect(self.listWidgetTitle.verticalScrollBar().setValue)
        self.listWidgetTitle.verticalScrollBar().valueChanged.connect(self.listWidgetVideo.verticalScrollBar().setValue)
        
        self.app = app
        
        self.zu_lesen = ""
        self.listWidgetTitle.setFocus()
        self.res_alle = []
        self.titel = titel
        self.werte = []
        if self.titel:
            self.pushButtonSuchen.setEnabled(False)
            self.listWidgetTitle.addItems(self.titel)
            self.onSuchen()
        else:
            self.pushButtonSuchen.setEnabled(True)
        
    def onSuchen(self):
        self.listWidgetVideo.clear()
        vorhanden = []
        self.res_alle = []
        self.app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        for i in self.titel:
            if i:
                zu_lesen = "SELECT DISTINCT ON (original) * FROM pordb_vid WHERE original LIKE %s OR original LIKE %s"
                lese_func = DBLesen(self, zu_lesen, (i.title() + "  % ", i.title() + " (%"))
                res = DBLesen.get_data(lese_func)
                if res:
                    vorhanden.append("x")
                    self.res_alle.extend(res)
                else:
                    vorhanden.append(" ")
        self.label_insgesamt.setText(str(len(self.titel)))
        self.label_vorhanden.setText(str(len(self.res_alle)))
        #self.listWidgetVideo.setMinimumHeight(len(self.titel))
        self.listWidgetVideo.addItems(vorhanden)
        self.app.restoreOverrideCursor()
        
    def onAnzeigen(self):
        self.zu_lesen = ""
        if self.res_alle:
            self.zu_lesen = "SELECT * FROM pordb_vid WHERE original = %s"
            for i in self.res_alle:
                if i[5].strip() not in self.werte: # This can happen, when an actor is also director
                    self.werte.append(i[5].strip())
                    if i != self.res_alle[len(self.res_alle) -1]:
                        self.zu_lesen += " OR original = %s"
            self.zu_lesen += " ORDER BY original"
        self.close()
