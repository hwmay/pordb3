# -*- coding: utf-8 -*-

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
		zu_lesen = "select * from pordb_pseudo where pseudo = '" + self.pseudo + "' and darsteller = '" +self.darsteller + "'"
		try:
			self.cur.execute(zu_lesen)
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
