# -*- coding: utf-8 -*-

import time
import os
from PyQt4 import QtGui, QtCore
from pypordb_dblesen import DBLesen
from pypordb_dbupdate import DBUpdate
from pordb_darstellerneu import Ui_Dialog as pordb_darstellerneu

class NeueingabeDarsteller(QtGui.QDialog, pordb_darstellerneu):
    def __init__(self, darsteller, parent=None):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.darsteller = darsteller
        
        self.connect(self.pushButtonDarstellerneuSpeichern, QtCore.SIGNAL("clicked()"), self.accept)
        self.connect(self.pushButtonDarstellerneuCancel, QtCore.SIGNAL("clicked()"), self.close)
        
        self.setWindowTitle(self.trUtf8("Actor ") +self.darsteller + self.trUtf8(" will be added"))
        # Combobox für Nation füllen
        zu_lesen = "SELECT * FROM pordb_iso_land WHERE aktiv = %s ORDER BY land"
        lese_func = DBLesen(self, zu_lesen, "x")
        res = DBLesen.get_data(lese_func)
        self.comboBoxDarstellerneuNation.clear()
        for i in res:
            text = '%2s %-50s' % (i[0], i[1])
            bild = os.path.join(os.curdir, "pypordb", i[0] + ".svg")
            icon = QtGui.QIcon()
            icon.addFile(bild, QtCore.QSize(16, 16), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.comboBoxDarstellerneuNation.addItem(icon, text)
            
    def accept(self):
        if not self.comboBoxDarstellerneuGeschlecht.currentText():
            message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Please select the gender"))
            return
        # insert/update-Anweisung aufbauen
        datum = str(time.localtime()[0]) + '-' + str(time.localtime()[1]) + '-' + str(time.localtime()[2])
        werte = []
        zu_erfassen = []
        werte.append(self.darsteller)
        werte.append(str(self.comboBoxDarstellerneuGeschlecht.currentText()))
        werte.append("0")
        werte.append(datum)
        werte.append(str(self.comboBoxDarstellerneuHaarfarbe.currentText()))
        werte.append(str(self.comboBoxDarstellerneuNation.currentText())[0:2])
        werte.append(self.lineEditDarstellerneuTattoo.text())
        werte.append(str(self.comboBoxDarstellerneuEthnic.currentText()))
        zu_erfassen.append(["INSERT into pordb_darsteller VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", werte])
        update_func = DBUpdate(self, zu_erfassen)
        DBUpdate.update_data(update_func)
        self.close()
