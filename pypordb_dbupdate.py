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

from PyQt5 import QtWidgets
import psycopg2
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)

class DBUpdate():
    def __init__(self, fenster, update):
        self.fenster = fenster
        self.update = update
        self.conn = None
        self.cur = None
        db_host = "localhost"
        try:
            self.conn = psycopg2.connect(database="por", host=db_host)
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.critical(self.fenster, self.fenster.tr("Error "), str(e))
            return 
        self.cur = self.conn.cursor()
        
    def update_data(self):
        update_db = []
        if type(self.update) == str:
            update_db.append([self.update, None])
        elif type(self.update) == bytes:
            update_db.append([self.update.decode(), None])
        else:
            for i in self.update:
                werte = None
                if type(i) == str:
                    befehl = i
                elif type(i) == bytes:
                    befehl = i.decode()
                else:
                    befehl = i[0]
                    werte = i[1]
                update_db.append([befehl, werte])
        for i in update_db:
            #print (i)
            try:
                self.cur.execute(i[0], i[1])
            except Exception as e:
                print("Error:", e)
                print(i)
                QtWidgets.QMessageBox.critical(self.fenster, self.fenster.tr("Error "), str(e))
                self.cur.close()
                return 
        self.commit()
        
    def commit(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()

# Testing procedure after this
if __name__ == "__main__":
    zu_erfassen = []
    
    werte = []
    befehl = "SELECT * FROM pordb_mpg_verzeichnisse"
    zu_erfassen.append(befehl)
    
    werte = []
    befehl = "UPDATE pordb_vid_neu SET cd = 690"
    zu_erfassen.append(befehl)
    
    befehl = "INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES (%s, %s, %s, %s)"
    werte.append("AA")
    werte.append("Antarktis")
    werte.append(" ")
    werte.append("Antarktika")
    zu_erfassen.append([befehl, werte])
    
    """
    werte = []
    befehl = "INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES (%s, %s, %s, %s)"
    werte.append("AB")
    werte.append("Aschaffenburg")
    werte.append(" ")
    werte.append("Aschaffenburger")
    zu_erfassen.append([befehl, werte])
    """

    print (zu_erfassen)

    fenster = None

    update_func = DBUpdate(fenster, zu_erfassen)
    DBUpdate.update_data(update_func)
