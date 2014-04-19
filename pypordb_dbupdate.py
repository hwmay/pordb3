# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
import psycopg2
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)

class DBUpdate():
	def __init__(self, fenster, update):
		self.fenster = fenster
		self.update = update
		self.conn = None
		self.cur = None
		db_host='localhost'
		try:
			self.conn = psycopg2.connect(database="por", host=db_host)
		except Exception as e:
			print(e)
			message = QtGui.QMessageBox.critical(self.fenster, self.fenster.trUtf8("Fehler "), str(e))
			return 
		self.cur = self.conn.cursor()
		
	def update_data(self):
		update_db = []
		if type(self.update) == str:
			update_db.append(self.update)
		elif type(self.update) == bytes:
			update_db.append(self.update.decode())
		else:
			for i in self.update:
				if type(i) == bytes:
					update_db.append(i.decode())
				else:
					update_db.append(i)
		for i in update_db:
			try:
				self.cur.execute(i)
			except Exception as e:
				print("Error:", e)
				print(i)
				message = QtGui.QMessageBox.critical(self.fenster, self.fenster.trUtf8("Error "), str(e))
				self.cur.close()
				return 
		self.commit()
		
	def commit(self):
		self.conn.commit()
		self.cur.close()
		self.conn.close()
