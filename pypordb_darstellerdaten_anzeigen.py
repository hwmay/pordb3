# -*- coding: utf-8 -*-

import os
import urllib.request, urllib.parse, urllib.error
import time
from PyQt4 import QtGui, QtCore
from pordb_iafd import Ui_DatenausderIAFD as pordb_iafd
from pypordb_dblesen import DBLesen
from pypordb_dbupdate import DBUpdate
from pypordb_checkpseudos import CheckPseudos
from pypordb_actordata import ActorData

class DarstellerdatenAnzeigen(QtGui.QDialog, pordb_iafd):
	def __init__(self, app, url, darstellerseite, verzeichnis_thumbs, name = None):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		
		self.connect(self.pushButtonUebernehmen, QtCore.SIGNAL("clicked()"), self.onUebernehmen)
		self.connect(self.pushButtonRemoveBrackets, QtCore.SIGNAL("clicked()"), self.onRemoveBrackets)
		self.connect(self.pushButtonCancel, QtCore.SIGNAL("clicked()"), self.onClose)
		
		self.darstellerseite = str(darstellerseite)
		self.app = app
		self.url = url
		self.verzeichnis_thumbs = verzeichnis_thumbs
		if name:
			self.name = name
		
		self.app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
		
		monate = {"January":"01", "February":"02", "March":"03", "April":"04", "May":"05", "June":"06", "July":"07", "August":"08", "September":"09", "October":"10", "November":"11", "December":"12", }
		haarfarben = {"Brown":"br", "Brown/Light Brown":"br", "Dark Brown":"br", "Light Brown":"br", "Black":"s", "Red":"r", "Blond":"bl", "Honey Blond":"bl", "Dark Blond":"bl", "Dirty Blond":"bl", "Sandy Blond":"bl", "Strawberry Blond":"bl", "Auburn":"r"}
		ethniticies = {"Caucasian": "w", "Black": "s", "Asian": "a", "Latin": "l"}
		
		actordata = ActorData(self.darstellerseite)
		
		# Darsteller Name
		if not name:
			self.name = ActorData.actor_name(actordata)
			if not self.name:
				self.app.restoreOverrideCursor()
				message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("This site seams not to be an actor site of the IAFD"))
				return
		self.labelName.setText(self.name)
		self.lineEditName.setText(self.name)
			
		# Darsteller Bild
		self.bild = ActorData.actor_image(actordata)
		if not self.bild:
			self.app.restoreOverrideCursor()
			message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("This site seams not to be an actor site of the IAFD"))
			return
		url =  'http://www.iafd.com/graphics/headshots/' + self.bild
		self.verz = self.verzeichnis_thumbs
		urllib.request._urlopener=urllib.request.URLopener()
		urllib.request.URLopener.version="Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; T312461)"
		urllib.request.FancyURLopener.prompt_user_passwd = lambda self, host, realm: (None, None)
		while True:
			try:
				bild=urllib.request.urlretrieve(url, self.verz +os.sep +self.bild)
				break
			except:
				pass
		bild = QtGui.QPixmap(self.verz +os.sep +self.bild)
		self.labelBild.setPixmap(bild)
			
		# Darsteller Geschlecht
		self.geschlecht = ActorData.actor_sex(actordata)
		if not self.bild:
			self.app.restoreOverrideCursor()
			message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("This site seams not to be an actor site of the IAFD"))
			return
		self.lineEditGeschlecht.setText(self.geschlecht)
		
		# Darsteller Pseudonyme
		self.pseudonyme = ActorData.actor_alias(actordata)
		self.lineEditPseudo.setText(self.pseudonyme)
	
		# Darsteller Land
		self.land = ActorData.actor_country(actordata)
		if self.land == "No data":
			self.lineEditLand.setText("")
			self.checkBoxLand.setCheckState(QtCore.Qt.Unchecked)
		else:
			self.lineEditLand.setText(self.land)
			zu_lesen = "select iso from pordb_iso_land where national = '" +self.land + "'"
			self.lese_func = DBLesen(self, zu_lesen)
			res = DBLesen.get_data(self.lese_func)
			if len(res) > 0:
				self.lineEditLand.setText(res[0][0])
				self.checkBoxLand.setCheckState(QtCore.Qt.Checked)
		
		# Darsteller Ethnic
		self.ethnic = ActorData.actor_ethnic(actordata)
		if self.ethnic == "No data":
			self.ethnic = ""
			self.checkBoxEthnic.setCheckState(QtCore.Qt.Unchecked)
		else:
			ethnic = ethniticies.get(self.ethnic, self.trUtf8("nicht vorhanden"))
			if ethnic != self.trUtf8("nicht vorhanden"):
				self.ethnic = ethnic
				self.checkBoxEthnic.setCheckState(QtCore.Qt.Checked)
		self.lineEditEthnic.setText(self.ethnic)
		
		# Darsteller Haarfarbe
		self.haare = ActorData.actor_hair(actordata)
		if self.haare == "No data":
			self.haare = ""
			self.checkBoxHaare.setCheckState(QtCore.Qt.Unchecked)
		else:
			haarfarbe = haarfarben.get(self.haare, self.trUtf8("nicht vorhanden"))
			if haarfarbe != self.trUtf8("nicht vorhanden"):
				self.haare = haarfarbe
				self.checkBoxHaare.setCheckState(QtCore.Qt.Checked)
		self.lineEditHaare.setText(self.haare)
		
		# Darsteller Tattoos
		self.tattoos = ActorData.actor_tattoos(actordata)
		if self.tattoos == "None" or self.tattoos == "none":
			self.lineEditTattos.setText("-")
			self.checkBoxTattos.setCheckState(QtCore.Qt.Checked)
		elif self.tattoos == "No data" or self.tattoos == "No Data":
			self.lineEditTattos.setText("")
			self.checkBoxTattos.setCheckState(QtCore.Qt.Unchecked)
		else:
			self.lineEditTattos.setText(self.tattoos)
			self.checkBoxTattos.setCheckState(QtCore.Qt.Checked)
			
		# Darsteller Geboren
		self.geboren = ActorData.actor_born(actordata)
		monat = monate.get(self.geboren[0:self.geboren.find(" ")], self.trUtf8("not available"))
		if monat != self.trUtf8("not available"):
			tag = self.geboren[self.geboren.find(" ")+1:self.geboren.find(",")]
			jahr = self.geboren[self.geboren.find(", ")+2:]
			self.geboren = jahr +"-" + monat + "-" + tag
			self.labelGeboren.setText(self.geboren)
		else:
			self.geboren = 0
			self.labelGeboren.setText("-")
		
		# Darsteller Anzahl Filme
		self.filme = ActorData.actor_movies(actordata)
		
		# Darsteller aktiv von / bis
		self.aktiv_von, self.aktiv_bis = ActorData.actor_activ(actordata)
		
		self.checkBoxPseudo.setCheckState(QtCore.Qt.Checked)
		self.checkBoxGeboren.setCheckState(QtCore.Qt.Checked)
		
		self.app.restoreOverrideCursor()
		
	def keyPressEvent(self, event):
		try:
			if event.modifiers() & QtCore.Qt.ControlModifier:
				if event.key() == QtCore.Qt.Key_L:
					self.onRemoveBrackets()
					self.update()
			elif event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
				self.onUebernehmen()
			elif event.key() == QtCore.Qt.Key_Escape:
				self.onClose()
			else:
				self.keyPressEvent(self)
		except:
			pass
		
	def onUebernehmen(self):
		if self.lineEditGeschlecht.text() != 'm' and self.lineEditGeschlecht.text() != 'w':
			message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Invalid gender"))
			self.app.restoreOverrideCursor()
		if self.checkBoxName.isChecked():
			zu_lesen = "select * from pordb_darsteller where darsteller = '" +str(self.lineEditName.text()).replace("'", "''").title() +"'"
		else:
			zu_lesen = "select * from pordb_darsteller where darsteller = '" +self.name.strip().title().replace("'", "''") +"'"
		self.lese_func = DBLesen(self, zu_lesen)
		res = DBLesen.get_data(self.lese_func)
		zu_erfassen = []
		
		# Darsteller existiert noch nicht
		if not res:
			messageBox = QtGui.QMessageBox()
			messageBox.addButton(self.trUtf8("Yes"), QtGui.QMessageBox.AcceptRole)
			messageBox.addButton(self.trUtf8("No"), QtGui.QMessageBox.RejectRole)
			messageBox.setWindowTitle(self.trUtf8("Actor ") +self.name.strip() +self.trUtf8(" not yet in database"))
			messageBox.setIcon(QtGui.QMessageBox.Question)
			messageBox.setText(self.trUtf8("Should the actor be created?"))
			message = messageBox.exec_()
			if message == 0:
				if str(self.labelGeboren.text()).strip() == "-":
					geboren = "0001-01-01"
				else:
					geboren = str(self.labelGeboren.text())
				datum = str(time.localtime()[0]) + '-' + str(time.localtime()[1]) + '-' + str(time.localtime()[2])
				name = str(self.lineEditName.text())
				zu_erfassen_zw = "INSERT into pordb_darsteller VALUES ('" 
				zu_erfassen_zw += name.title().replace("'", "''") 
				zu_erfassen_zw += "', '" 
				zu_erfassen_zw += str(self.lineEditGeschlecht.text()) 
				zu_erfassen_zw += "', '" 
				zu_erfassen_zw += str(0) 
				zu_erfassen_zw += "', '" 
				zu_erfassen_zw += datum 
				zu_erfassen_zw += "', '" 
				zu_erfassen_zw += str(self.lineEditHaare.text()).lower() 
				zu_erfassen_zw += "', '" 
				zu_erfassen_zw += str(self.lineEditLand.text()).upper()[0:2] 
				zu_erfassen_zw += "', '" 
				zu_erfassen_zw += str(self.lineEditTattos.text()).replace("'", "''") 
				zu_erfassen_zw += "', '" 
				zu_erfassen_zw += str(self.lineEditEthnic.text()).lower()
				zu_erfassen_zw += "', '" 
				zu_erfassen_zw += str(0) 
				zu_erfassen_zw += "', '" 
				zu_erfassen_zw += geboren 
				zu_erfassen_zw += "', '" 
				zu_erfassen_zw += str(self.filme) 
				zu_erfassen_zw += "', '" 
				zu_erfassen_zw += str(self.url).replace("'", "''")
				zu_erfassen_zw += "', '" +str(self.aktiv_von) +"', '" +str(self.aktiv_bis) +"', '" +datum +"')"
				zu_erfassen.append(zu_erfassen_zw)
				action = None
				if self.checkBoxPseudo.isChecked():
					action = self.pseudo_uebernehmen(name, zu_erfassen)
					if not action: 
						return
				extension = os.path.splitext(str(self.verz +os.sep +self.bild))[-1].lower()
				if extension == ".jpeg":
					extension = ".jpg"
				if extension != ".gif":
					newfilename = self.verzeichnis_thumbs +os.sep +"darsteller_" +str(self.lineEditGeschlecht.text()) +os.sep +name.strip().replace("'", "_apostroph_").replace(" ", "_").lower() + extension
					os.rename(self.verz +os.sep +self.bild, newfilename)
			else:
				self.onClose()
		# Darsteller existiert bereits
		else:
			if self.checkBoxBild.isChecked():
				extension = os.path.splitext(str(self.verz +os.sep +self.bild))[-1].lower()
				if extension == ".jpeg":
					extension = ".jpg"
				if extension != ".gif":
					if self.checkBoxName.isChecked():
						newfilename = self.verzeichnis_thumbs +os.sep +"darsteller_" +self.lineEditGeschlecht.text() +os.sep +str(self.lineEditName.text()).strip().replace("'", "_apostroph_").replace(" ", "_").lower() + extension
					else:
						newfilename = self.verzeichnis_thumbs +os.sep +"darsteller_" +self.lineEditGeschlecht.text() +os.sep +str(self.name).strip().replace("'", "_apostroph_").replace(" ", "_").lower() + extension
					os.rename(self.verz +os.sep +self.bild, newfilename)
			else:
				try:
					os.remove(self.verz +os.sep +self.bild)
				except:
					pass
			if self.checkBoxGeboren.isChecked():
				if str(self.labelGeboren.text()).strip() == "-":
					if res[0][9] and res[0][9] != '0001-01-01':
						pass
					else:
						zu_erfassen.append("update pordb_darsteller set geboren = '0001-01-01' where darsteller = '" +res[0][0].replace("'", "''") +"'")
				else:
					zu_erfassen.append("update pordb_darsteller set geboren = '" +str(self.labelGeboren.text()) +"' where darsteller = '" +res[0][0].replace("'", "''") +"'")
			if self.checkBoxLand.isChecked() and str(self.lineEditLand.text()):
				zu_erfassen.append("update pordb_darsteller set nation = '" +str(self.lineEditLand.text()).upper() +"' where darsteller = '" +res[0][0].replace("'", "''") +"'")
			if self.checkBoxEthnic.isChecked():
				zu_erfassen.append("update pordb_darsteller set ethnic = '" +str(self.lineEditEthnic.text()).lower() +"' where darsteller = '" +res[0][0].replace("'", "''") +"'")
			if self.checkBoxHaare.isChecked():
				zu_erfassen.append("update pordb_darsteller set haarfarbe = '" +str(self.lineEditHaare.text()).lower() +"' where darsteller = '" +res[0][0].replace("'", "''") +"'")
			if self.checkBoxTattos.isChecked() and str(self.lineEditTattos.text()):
				if len((self.lineEditTattos.text())) > 500:
					message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Too many characters in tattos (") +str(len((self.lineEditTattos.text()))) +")")
					return
				zu_erfassen.append("update pordb_darsteller set tattoo = '" +str(self.lineEditTattos.text()).replace("'", "''") +"' where darsteller = '" +res[0][0].replace("'", "''") +"'")
			zu_erfassen.append("update pordb_darsteller set filme = '" +str(self.filme) +"' where darsteller = '" +res[0][0].replace("'", "''") +"'")
			zu_erfassen.append("update pordb_darsteller set url = '" +self.url.replace("'", "''") +"' where darsteller = '" +res[0][0].replace("'", "''") +"'")
			zu_erfassen.append("update pordb_darsteller set aktivvon = '" +str(self.aktiv_von) +"' where darsteller = '" +res[0][0].replace("'", "''") +"'")
			zu_erfassen.append("update pordb_darsteller set aktivbis = '" +str(self.aktiv_bis) +"' where darsteller = '" +res[0][0].replace("'", "''") +"'")
			if self.checkBoxPseudo.isChecked():
				action = self.pseudo_uebernehmen(res[0][0], zu_erfassen)
				if not action: 
					return
				
			datum = str(time.localtime()[0]) + '-' + str(time.localtime()[1]) + '-' + str(time.localtime()[2])
			zu_erfassen.append("update pordb_darsteller set besuch = '" +datum +"' where darsteller = '" +res[0][0].replace("'", "''") +"'")
				
		if zu_erfassen:
			update_func = DBUpdate(self, zu_erfassen)
			DBUpdate.update_data(update_func)
		self.onClose()
	# end of onUebernehmen
	
	def onRemoveBrackets(self):
		pseudos = str(self.lineEditPseudo.text()).title().split(", ")
		pseudos_neu = []
		for i in pseudos:
			klammer_auf = i.find("(")
			klammer_zu = i.find(")")
			if klammer_auf > -1 and klammer_zu > -1:
				pseudos_neu.append(i[0:klammer_auf] + i[klammer_zu + 1 :])
			elif klammer_auf > -1 and klammer_zu == -1:
				pseudos_neu.append(i[0:klammer_auf])
			elif klammer_auf == -1 and klammer_zu > -1:
				pseudos_neu.append(i[klammer_zu + 1 :])
			else:
				pseudos_neu.append(i)
		self.lineEditPseudo.setText(", ".join(pseudos_neu))
		
	def pseudo_uebernehmen(self, name, zu_erfassen):
		pseudos = str(self.lineEditPseudo.text()).title().split(", ")
		pseudos = set(pseudos)
		for i in pseudos:
			if i and i != name.title().strip():
				res = []
				zu_lesen = "select darsteller from pordb_darsteller where darsteller = '" +i.strip().replace("'", "''").title() +"'"
				self.lese_func = DBLesen(self, zu_lesen)
				res = DBLesen.get_data(self.lese_func)
				if res:
					messageBox = QtGui.QMessageBox()
					messageBox.addButton(self.trUtf8("Yes"), QtGui.QMessageBox.AcceptRole)
					messageBox.addButton(self.trUtf8("No"), QtGui.QMessageBox.RejectRole)
					messageBox.setWindowTitle(i.strip().replace("'", "''").title() +self.trUtf8(": There is another actor in the database with this name."))
					messageBox.setIcon(QtGui.QMessageBox.Question)
					messageBox.setText(self.trUtf8("Do you want to add/change the actor anyway?"))
					message = messageBox.exec_()
					if message != 0:
						return False
				checkpseudo = CheckPseudos(i.strip().title().replace("'", "''"), name.strip().title().replace("'", "''"))
				check = CheckPseudos.check(checkpseudo)
				befehl = "insert into pordb_pseudo (pseudo, darsteller) values ('" +i.strip().title().replace("'", "''") +"', '" +name.strip().title().replace("'", "''") +"')"
				if check and befehl not in zu_erfassen:
					zu_erfassen.append(befehl)
		return True
					
	def onClose(self):
		try:
			os.remove(self.verz +os.sep +self.bild)
		except:
			pass
		self.close()
