# -*- coding: utf-8 -*-

'''
    Copyright 2012-2017 HWM
    
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

import psycopg2
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)

class CheckPseudos():
    def __init__(self, pseudo, darsteller):
        self.pseudo = pseudo
        self.darsteller = darsteller
        self.res = []
        self.conn = None
        self.cur = None
        db_host="localhost"
        try:
            self.conn = psycopg2.connect(database="por", host=db_host)
        except Exception as e:
            print(e)
            message = QtGui.QMessageBox.critical(self.fenster, self.fenster.trUtf8("Error "), str(e))
            self.cur.close()
            return 
        self.cur = self.conn.cursor()
        
    def check(self):
        zu_lesen = "SELECT * FROM pordb_pseudo WHERE pseudo = %s AND darsteller = %s"
        try:
            self.cur.execute(zu_lesen, (self.pseudo, self.darsteller))
        except Exception as e:
            print(zu_lesen, type(zu_lesen))
            print(e)
            self.cur.close()
            return 
        self.res = self.cur.fetchall()
        self.cur.close()
        if len(self.res) > 0:
            return False
        else:
            return True
