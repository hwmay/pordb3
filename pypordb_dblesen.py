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

import psycopg2
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)

class DBLesen():
    def __init__(self, fenster, zu_lesen, werte = None):
        self.fenster = fenster
        self.zu_lesen = str(zu_lesen)
        if werte:
            if type(werte) == str:
                self.werte = []
                self.werte.append(werte)
            elif type(werte) == tuple or type(werte) == list:
                self.werte = werte
        else:
            self.werte = None
        self.res = []
        self.conn = None
        self.cur = None
        
    def get_data(self):
        db_host="localhost"
        try:
            self.conn = psycopg2.connect(database="por", host=db_host)
        except Exception as e:
            print(e)
            message = QtWidgets.QMessageBox.critical(self.fenster, self.fenster.trUtf8("Error "), str(e))
            self.cur.close()
            return 
        self.cur = self.conn.cursor()
        try:
            if self.werte:
                self.cur.execute(self.zu_lesen, self.werte)
                #print (self.zu_lesen, self.werte)
            else:
                self.cur.execute(self.zu_lesen)
                #print (self.zu_lesen)
        except Exception as e:
            print(self.zu_lesen, type(self.zu_lesen))
            print(e)
            message = QtWidgets.QMessageBox.critical(self.fenster, self.fenster.trUtf8("Error "), str(e))
            self.cur.close()
            return 
        self.res = self.cur.fetchall()
        self.cur.close()
        return self.res
