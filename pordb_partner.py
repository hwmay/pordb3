#!/usr/bin/python
# -*- coding: utf-8 -*-

''' Programm dient zum Erstellen der Partnertabelle'''

from pyPgSQL import PgSQL

dbname = "por"
ausschluss = ("(Schlechte Qualitaet)", "(Uninteressant)", "(Komplett)", "?", "und noch einer")

cnx = PgSQL.connect(database=dbname)
cur = cnx.cursor()

zu_lesen = "select * from darsteller where darsteller not in " +str(ausschluss) +" order by darsteller"
try:
    cur.execute(zu_lesen)
except PgSQL.Error as msg:
    print(msg)
    
try:
    res = cur.fetchall()
except Exception as msg:
    print(msg)

    
#for i in res:
for i in [["Jayna Oso", "w"]]:
    print(i[0], i[1])
    zu_lesen = "SELECT darsteller, cd, bild, cs FROM vid where darsteller like '"+i[0].strip() +"  ' or darsteller like '" +i[0].strip() +",%' or darsteller like '%, " +i[0].strip() +",%' or darsteller like '%, " +i[0].strip() + "  %' order by cd, bild, darsteller"
    ergebnis = []
    try:
        cur.execute(zu_lesen)
    except PgSQL.Error as msg:
        print("1", msg)
        
    try:
        res2 = cur.fetchall()
    except Exception as msg:
        print("2", msg)
    ergebnis.extend(res2)
    
    geschlecht = i[1]
    paarung = []
    for j in ergebnis:
        darsteller_liste = j[0].split(',')
        for k in darsteller_liste:
            if k.strip() != i[0].strip() and k.strip() not in ausschluss:
                paar = []
                zu_lesen = "SELECT * FROM darsteller where darsteller = '" +k.strip().replace("'", "''") +"'"
                try:
                    cur.execute(zu_lesen)
                except PgSQL.Error as msg:
                    print("3", msg)
                    
                try:
                    res2 = cur.fetchall()
                except Exception as msg:
                    print("4", msg)
                try:
                    if geschlecht != res2[0][1] and res2[0][1] != ' ':
                        paar.append(k.strip())
                        paar.append(j[1])
                        paar.append(j[2].strip())
                        if j[3]:
                            paar.append(j[3])
                        else:
                            paar.append(" ")
                        paarung.append(paar)
                except Exception as msg:
                    print("5", msg)
    for j in paarung:
        zu_erfassen = "insert into partner values ('" +i[0] +"', '" +j[0] +"', " +str(j[1]) +", '" +j[2] +"', '" +j[3] +"')"
        print(zu_erfassen)
        try:
            cur.execute(zu_erfassen)
        except PgSQL.Error as msg:
            print("6", msg)
    cnx.commit()