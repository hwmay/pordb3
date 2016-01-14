# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore

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
            message = QtGui.QMessageBox.critical(self.fenster, self.fenster.trUtf8("Error "), str(e))
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
            message = QtGui.QMessageBox.critical(self.fenster, self.fenster.trUtf8("Error "), str(e))
            self.cur.close()
            return 
        self.res = self.cur.fetchall()
        self.cur.close()
        return self.res
