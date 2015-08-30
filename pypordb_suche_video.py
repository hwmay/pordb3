# -*- coding: utf-8 -*-

'''
    Copyright 2012-2015 HWM
    
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

from PyQt4 import QtGui, QtCore
from pordb_suche_video import Ui_Dialog as pordb_suche_video
from pypordb_dblesen import DBLesen

class SucheVideo(QtGui.QDialog, pordb_suche_video):
    def __init__(self, app, titel=None, parent=None):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        
        self.connect(self.pushButtonSuchen, QtCore.SIGNAL("clicked()"), self.onSuchen)
        self.connect(self.pushButtonAnzeigen, QtCore.SIGNAL("clicked()"), self.onAnzeigen)
        self.connect(self.pushButtonAbbrechen, QtCore.SIGNAL("clicked()"), self.close)
        
        self.app = app
        
        self.zu_lesen = ""
        self.textEditVideo.setFocus()
        self.res_alle = []
        self.titel = titel
        self.werte = []
        if self.titel:
            self.pushButtonSuchen.setEnabled(False)
            j = ""
            for i in self.titel:
                j += i + "\n"
            self.textEditVideo.setText(j)
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
        self.listWidgetVideo.setMinimumHeight(len(self.titel) * 20)
        self.listWidgetVideo.addItems(vorhanden)
        self.app.restoreOverrideCursor()
        
    def onAnzeigen(self):
        self.zu_lesen = ""
        if self.res_alle:
            self.zu_lesen = "SELECT * FROM pordb_vid WHERE original = %s"
            for i in self.res_alle:
                self.werte.append(i[5].strip())
                if i != self.res_alle[len(self.res_alle) -1]:
                    self.zu_lesen += " OR original = %s"
            self.zu_lesen += " ORDER BY original"
        self.close()
