# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from pordb_neu import Ui_Dialog as pordb_neu
from pypordb_dblesen import DBLesen
from pypordb_dbupdate import DBUpdate
from pypordb_bilddatei_umbenennen import BilddateiUmbenennen
from pypordb_bildbeschneiden import Bildbeschneiden
from pypordb_neueingabe_darsteller import NeueingabeDarsteller
from pypordb_darsteller_korrigieren import DarstellerKorrigieren
from pypordb_cover import Cover
from pypordb_original import OriginalErfassen
import os

size = QtCore.QSize(260, 260)
sizeneu = QtCore.QSize(300, 300)
size_darsteller = QtCore.QSize(1280, 1024)
videodateien = (".asf", ".avi", ".divx", ".f4v", ".m4v", ".mkv", ".mpg", ".mpeg", ".mp4", ".mov", ".wmv")

class Neueingabe(QtGui.QDialog, pordb_neu):
	def __init__(self, verzeichnis, verzeichnis_original, verzeichnis_thumbs, verzeichnis_trash, verzeichnis_cover, bilddatei, titel=None, darsteller=None, cd=None, bild=None, gesehen=None, original=None, cs=None, vorhanden=None, cover=None, undo=None, cover_anlegen=None, original_weitere=None, original_cover = None, high_definition = None):
		
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		self.bilddatei = bilddatei
		self.titel = titel
		self.darsteller = darsteller
		self.cd = cd
		self.bild = bild
		self.gesehen = gesehen
		self.original = original
		self.cs = cs
		self.vorhanden = vorhanden
		self.undo = undo
		self.cover = cover
		self.cover_anlegen = cover_anlegen
		self.cover_austauschen = 0
		self.original_weitere = original_weitere
		self.verzeichnis = verzeichnis
		self.verzeichnis_original = verzeichnis_original 
		self.verzeichnis_thumbs = verzeichnis_thumbs 
		self.verzeichnis_trash = verzeichnis_trash 
		self.verzeichnis_cover = verzeichnis_cover
		self.original_cover = original_cover
		self.high_definition = high_definition
		
		self.connect(self.pushButtonNeuOK, QtCore.SIGNAL("clicked()"), self.accept)
		self.connect(self.pushButtonNeuCancel, QtCore.SIGNAL("clicked()"), self.close)
		self.connect(self.pushButtonNeuDelete, QtCore.SIGNAL("clicked()"), self.onDelete)
		self.connect(self.pushButtonOriginal, QtCore.SIGNAL("clicked()"), self.onOriginal)
		self.connect(self.pushButtonOriginalAlt, QtCore.SIGNAL("clicked()"), self.onOriginalAlt)
		self.connect(self.listWidgetW, QtCore.SIGNAL("itemDoubleClicked(QListWidgetItem*)"), self.onDarstelleruebernehmen)
		self.connect(self.listWidgetM, QtCore.SIGNAL("itemDoubleClicked(QListWidgetItem*)"), self.onDarstelleruebernehmen)
		self.connect(self.pushButtonNeuDarstelleruebernehmen, QtCore.SIGNAL("clicked()"), self.onDarstelleruebernehmen)
		self.connect(self.pushButtonBildloeschen, QtCore.SIGNAL("clicked()"), self.onBildloeschen)
		self.connect(self.pushButtonVerz, QtCore.SIGNAL("clicked()"), self.onVerzeichnisWechseln)
		self.connect(self.pushButtonBildbeschneiden, QtCore.SIGNAL("clicked()"), self.onBildbeschneiden)
		
		self.pushButtonNeuOK.setDefault(True)
		
		settings = QtCore.QSettings()
		window_size = settings.value("Neueingabe/Size", QtCore.QSize(600, 500))
		self.resize(window_size)
		window_position = settings.value("Neueingabe/Position", QtCore.QPoint(0, 0))
		self.move(window_position)
		
		# set default position for cropping images
		self.positionX = 0
		self.positionY = 0
		
		zu_lesen = "SELECT * FROM pordb_vid_neu"
		self.lese_func = DBLesen(self, zu_lesen)
		self.res_vid_neu = DBLesen.get_data(self.lese_func)
		if self.res_vid_neu[0][3]:
			self.labelOriginal.setText(self.res_vid_neu[0][3])
		
		zu_lesen = "SELECT * FROM pordb_darsteller100 order by darsteller"
		self.lese_func = DBLesen(self, zu_lesen)
		res = DBLesen.get_data(self.lese_func)
		res.sort()
		res.reverse()
		darsteller_m = []
		darsteller_w = []
		for i in res:
			zu_lesen = "SELECT sex FROM pordb_darsteller where darsteller = '" + tuple(i)[1].replace("'", "''").rstrip() + "'"
			self.lese_func = DBLesen(self, zu_lesen)
			res2 = DBLesen.get_data(self.lese_func)
			try:
				if res2 [0][0] == "w":
					darsteller_w.append(tuple (i)[1].rstrip())
				else:
					darsteller_m.append(tuple (i)[1].rstrip())
			except:
				pass
		darsteller_w.sort()
		darsteller_m.sort()
		self.listWidgetM.clear()
		self.listWidgetW.clear()
		initial = ' '
		for i in darsteller_w:
			newitem = QtGui.QListWidgetItem(i)
			if i[0] != initial:
				initial = i[0]
				newitem.setTextColor(QtGui.QColor('red'))
			else:
				newitem.setTextColor(QtGui.QColor('black'))
			self.listWidgetW.addItem(newitem)
		initial = ' '
		for i in darsteller_m:
			newitem = QtGui.QListWidgetItem(i)
			if i[0] != initial:
				initial = i[0]
				newitem.setTextColor(QtGui.QColor('red'))
			else:
				newitem.setTextColor(QtGui.QColor('black'))
			self.listWidgetM.addItem(newitem)
			
		self.bilddarstellen()
		
		if self.titel:
			self.korrektur = True
			self.lineEditNeuTitel.setText(self.titel.strip())
			self.lineEditNeuDarsteller.setText(self.darsteller.strip())
			self.lineEditNeuCD.setText(str(self.cd))
			self.cd_alt = str(self.cd)
			self.lineEditNeuBild.setText(self.bild.strip())
			if self.gesehen == "x":
				self.radioButtonGesehenJa.setChecked(True)
			else:
				self.radioButtonGesehenNein.setChecked(True)
			self.lineEditNeuOriginal.setText(self.original.strip())
			for i in cs:
				anzahl = i[0]
				if i[1] == "f":
					self.spinBoxF.setValue(int(anzahl))
				elif i[1] == "h":
					self.spinBoxH.setValue(int(anzahl))
				elif i[1] == "t":
					self.spinBoxT.setValue(int(anzahl))
				elif i[1] == "c":
					self.spinBoxC.setValue(int(anzahl))
				elif i[1] == "x":
					self.spinBoxX.setValue(int(anzahl))
				elif i[1] == "o":
					self.spinBoxO.setValue(int(anzahl))
				elif i[1] == "v":
					self.spinBoxV.setValue(int(anzahl))
				elif i[1] == "b":
					self.spinBoxB.setValue(int(anzahl))
				elif i[1] == "a":
					self.spinBoxA.setValue(int(anzahl))
				elif i[1] == "s":
					self.spinBoxS.setValue(int(anzahl))
				elif i[1] == "k":
					self.spinBoxK.setValue(int(anzahl))
			if self.vorhanden == "x":
				self.radioButtonVorhandenJa.setChecked(True)
			else:
				self.radioButtonVorhandenNein.setChecked(True)
			self.pushButtonBildloeschen.setEnabled(False)
			self.pushButtonBildbeschneiden.setEnabled(False)
			if self.undo:
				self.pushButtonNeuDelete.setEnabled(False)
			if self.cover or self.original_cover:
				self.radioButtonCoverJa.setChecked(True)
				self.radioButtonCoverNein.setChecked(False)
			else:
				self.radioButtonCoverNein.setChecked(True)
				self.radioButtonCoverJa.setChecked(False)
			if self.high_definition == "0":
				self.comboBoxDefinition.setCurrentIndex(1)
			elif self.high_definition == "1":
				self.comboBoxDefinition.setCurrentIndex(2)
			elif self.high_definition == "2":
				self.comboBoxDefinition.setCurrentIndex(3)
			elif self.high_definition == "9":
				self.comboBoxDefinition.setCurrentIndex(4)
			else:
				self.comboBoxDefinition.setCurrentIndex(0)
		else:
			self.korrektur = False
			if self.darsteller:
				self.lineEditNeuDarsteller.setText(self.darsteller)
			if self.original:
				self.lineEditNeuOriginal.setText(self.original.strip())
			if self.cover_anlegen:
				self.radioButtonCoverJa.setChecked(True)
				self.radioButtonCoverNein.setChecked(False)
				anfang = os.path.basename(self.bilddatei).rfind('.')
				if self.original:
					self.lineEditNeuOriginal.setText(self.original)
				else:
					self.lineEditNeuOriginal.setText((os.path.basename(str(self.bilddatei)))[0:anfang])
			anfang = os.path.basename(str(self.bilddatei)).rfind('.')
			self.lineEditNeuTitel.setText((os.path.basename(str(self.bilddatei)))[0:anfang])
			dateiliste = os.listdir(self.verzeichnis)
			videodatei = os.path.splitext(os.path.basename(str(self.bilddatei)))[0]
			self.lineEditNeuTitel.setFocus()
			for i in dateiliste:
				datei = os.path.splitext(i)[0]
				ext = os.path.splitext(i)[1].lower()
				if ext in videodateien: 
					if videodatei == datei or videodatei[0:len(videodatei) -1] == datei or videodatei[0:len(videodatei) -2] == datei: 
						self.lineEditNeuTitel.setText(os.path.basename(i))
						self.lineEditNeuDarsteller.setFocus()
						break
			if len((os.path.basename(str(self.bilddatei)))[0:anfang]) > 256:
				self.labelTitel.setText("<font color=red>" +self.trUtf8("Characters: ") +str(len((os.path.basename(str(self.bilddatei)))[0:anfang])) +"</font>")
			else:
				self.labelTitel.setText(self.trUtf8("Characters: ") +str(len((os.path.basename(str(self.bilddatei)))[0:anfang])))
			self.lineEditNeuCD.setText(str(self.res_vid_neu[0][2]))
			self.lineEditNeuBild.setText(os.path.basename(str(self.bilddatei)))
			if len(os.path.basename(str(self.bilddatei))) > 256:
				self.labelBild.setText("<font color=red>" +self.trUtf8("Characters: ") +str(len(os.path.basename(str(self.bilddatei)))) +"</font>")
			else:
				self.labelBild.setText(self.trUtf8("Characters: ") +str(len(os.path.basename(str(self.bilddatei)))))
			self.pushButtonBildloeschen.setEnabled(True)
			self.pushButtonBildbeschneiden.setEnabled(True)
			self.pushButtonNeuDelete.setEnabled(False)
			
	def keyPressEvent(self, event):
		try:
			if event.modifiers() & QtCore.Qt.ControlModifier:
				if event.key() == QtCore.Qt.Key_Y:
					self.onOriginalAlt()
					self.update()
			elif event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
				self.accept()
			elif event.key() == QtCore.Qt.Key_Escape:
				self.close()
			else:
				self.keyPressEvent(self)
		except:
			pass
			
	def onOriginal(self):
		originaldialog = OriginalErfassen(self.original_weitere)
		originaldialog.exec_()
		try:
			self.original_weitere = originaldialog.original
		except:
			pass
		self.pushButtonNeuOK.setFocus()
		      
	def onOriginalAlt(self):
		if self.res_vid_neu[0][3]:
			self.lineEditNeuOriginal.setText(self.res_vid_neu[0][3])
		self.pushButtonNeuOK.setFocus()
	
	def onDarstelleruebernehmen(self):
		selected = self.listWidgetW.selectedItems()
		selected.extend(self.listWidgetM.selectedItems())
		selected_str = []
		for i in selected:
			ein = str(i.text())
			selected_str.append(ein)
		text = ", ".join(selected_str)
		self.lineEditNeuDarsteller.setText(text)
		self.lineEditNeuDarsteller.setFocus()
		self.lineEditNeuDarsteller.setCursorPosition(len(text))
		
	def onBildloeschen(self):
		os.remove(self.bilddatei)
		self.close()
			
	def onVerzeichnisWechseln(self):
		self.file = QtGui.QFileDialog.getOpenFileName(self, self.trUtf8("Image files"), os.path.dirname(str(self.bilddatei)), self.trUtf8("Image files (*.jpg *.jpeg *.png);;all files (*.*)"))
		if not self.file:
			return
		self.bilddatei = str(self.file)
		self.bilddarstellen()
		anfang = (os.path.basename(str(self.bilddatei))).rfind('.')
		self.lineEditNeuTitel.setText((os.path.basename(str(self.file)))[0:anfang])
		self.lineEditNeuBild.setText(os.path.basename(str(self.file)))
		self.verzeichnis = os.path.dirname(str(self.file))
		
	def onBildbeschneiden(self):
		bilddialog = Bildbeschneiden(self.bilddatei, self.positionX, self.positionY)
		bilddialog.exec_()
		self.positionX = bilddialog.positionX
		self.positionY = bilddialog.positionY
		self.bilddarstellen()
		
	def bilddarstellen(self):
		bild = QtGui.QPixmap(self.bilddatei).scaled(sizeneu, QtCore.Qt.KeepAspectRatio)
		self.labelNeuBildanzeige.setPixmap(bild)
		text = str(QtGui.QPixmap(self.bilddatei).width()) +"x" +str(QtGui.QPixmap(self.bilddatei).height())
		self.groupBox_2.setTitle(text)
		
	def accept(self):
		fehler = 1
		actor_added = False
		actor_adding_asked = False
		while fehler:
			darsteller, fehler, fehler_index = self.darsteller_pruefen(str(self.lineEditNeuDarsteller.text()).title())
			if fehler:
				if fehler == 1:
					zu_lesen = "select darsteller from pordb_pseudo where pseudo = '" +darsteller[fehler_index].title().replace("'", "''").strip()  +"'"
					self.lese_func = DBLesen(self, zu_lesen)
					res = DBLesen.get_data(self.lese_func)
					if res:
						messageBox = QtGui.QMessageBox()
						messageBox.addButton(self.trUtf8("Yes"), QtGui.QMessageBox.AcceptRole)
						messageBox.addButton(self.trUtf8("No, correct entry"), QtGui.QMessageBox.RejectRole)
						messageBox.addButton(self.trUtf8("No, add new actor"), QtGui.QMessageBox.ActionRole)
						messageBox.setWindowTitle(darsteller[fehler_index] +self.trUtf8(" does not exist") +self.trUtf8(", but I have found ") +res[0][0].strip() +self.trUtf8(" as alias."))
						messageBox.setIcon(QtGui.QMessageBox.Question)
						messageBox.setText(self.trUtf8("Do you want to take this actor instead?"))
						messageBox.setDetailedText(darsteller[fehler_index] +self.trUtf8(" does not exist") +self.trUtf8(", but I have found ") +res[0][0].strip() +self.trUtf8(" as alias. If you want to take this actor, click on yes, else change your entry or add a new actor to the database."))
						message = messageBox.exec_()
						if message == 0:
							darsteller_alt = str(self.lineEditNeuDarsteller.text()).title().strip()
							darsteller_neu = darsteller_alt.replace(darsteller[fehler_index].strip(), str(res[0][0]).strip())
							try:
								self.lineEditNeuDarsteller.setText(darsteller_neu)
							except:
								pass
							return
						elif message == 2:
							self.darsteller_addieren(darsteller, fehler_index)
							actor_added = True
				elif fehler == 2:
					message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("You have entered some actors twice, please correct"))
					return
				if actor_adding_asked:
					return
				if not actor_added:
					self.darsteller_addieren(darsteller, fehler_index)
					actor_adding_asked = True
		titel = self.lineEditNeuTitel.text()
		if darsteller:
			darsteller = self.darsteller_sortieren(darsteller)
		if self.checkBoxUninteressant.isChecked():
			darsteller.append("(Uninteressant)")
		try:
			cd = int(self.lineEditNeuCD.text())
		except:
			message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("CD is not a number"))
			return
		bild = self.lineEditNeuBild.text()

		if not self.radioButtonVorhandenJa.isChecked() and not self.radioButtonVorhandenNein.isChecked():
			message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Please mark whether movie is available"))
			return
		if self.radioButtonVorhandenJa.isChecked():
			vorhanden = "x"
		else:
			vorhanden = ""

		if not self.radioButtonGesehenNein.isChecked() and not self.radioButtonGesehenJa.isChecked():
			message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Please mark whether movie has been watched"))
			return
		if self.radioButtonGesehenNein.isChecked():
			gesehen = " "
		else:
			gesehen = "x"
			
		try:
			original = str(self.lineEditNeuOriginal.text()).replace("'", "''").title()
		except:
			message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Error: original title has invalid characters"))
			return

		if len(original) > 256:
			message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Error, original title is longer than 256 characters."))
			return
		if not self.radioButtonCoverJa.isChecked() and not self.radioButtonCoverNein.isChecked():
			message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Please check if image file is a cover"))
			return
		if self.radioButtonVorhandenJa.isChecked() and self.comboBoxDefinition.currentIndex() == 0 and not self.cover_austauschen:
			message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Please select a resolution"))
			return
		if self.radioButtonVorhandenNein.isChecked() and self.comboBoxDefinition.currentIndex() != 0:
			message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Video is not in stock: resolution is set to unknown"))
			self.comboBoxDefinition.setCurrentIndex(0)
		zu_erfassen = []
		if self.korrektur and not self.undo:
			darsteller_liste = self.darsteller.strip().split(", ")
			if not darsteller_liste[0]:
				darsteller_liste = []
			for i in darsteller_liste:
				zu_erfassen.append("UPDATE pordb_darsteller set anzahl = anzahl - 1 where darsteller = '" + i.replace("'", "''") + "'")
			if not self.radioButtonCoverJa.isChecked():
				bilddatei_alt = self.verzeichnis_thumbs +os.sep +"cd" +str(self.cd_alt) +os.sep +str(bild).rstrip()
				if str(cd) != self.cd_alt:
					bilddatei_neu = self.verzeichnis_thumbs +os.sep +"cd" +str(cd) +os.sep +str(bild).rstrip()
					os.renames(bilddatei_alt, bilddatei_neu)
				else:
					if self.bilddatei != bilddatei_alt:
						bilddatei = QtGui.QImage(self.bilddatei).scaled(size, QtCore.Qt.KeepAspectRatio)
						if bilddatei.save(bilddatei_alt):
							os.remove(self.bilddatei)
						else:
							message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Error saving image file"))
							return
			zu_erfassen.append("delete from pordb_partner where cd = " +str(cd) + " and bild = '" +bild.replace("'", "''") +"'")
			cs = ""
			zu_erfassen_zw = "UPDATE pordb_vid SET titel = '" +titel.replace("'", "''") +"', darsteller = '" +", ".join(darsteller).replace("'", "''") +"', cd = " +str(cd) +", bild = '" +bild.replace("'", "''") +"', gesehen = '" +gesehen +"', original = '" +original 
			if self.spinBoxF.value() > 0:
				cs = str(self.spinBoxF.value())
				zu_erfassen_zw += "', csf = '" +cs 
				self.spinBoxK.setValue(0)
			else:
				zu_erfassen_zw += "', csf = '" +"0"
			if self.spinBoxH.value() > 0:
				cs = str(self.spinBoxH.value())
				zu_erfassen_zw += "', csh = '" +cs 
				self.spinBoxK.setValue(0)
			else:
				zu_erfassen_zw += "', csh = '" +"0"
			if self.spinBoxT.value() > 0:
				cs = str(self.spinBoxT.value())
				zu_erfassen_zw += "', cst = '" +cs 
				self.spinBoxK.setValue(0)
			else:
				zu_erfassen_zw += "', cst = '" +"0"
			if self.spinBoxC.value() > 0:
				cs = str(self.spinBoxC.value())
				zu_erfassen_zw += "', csc = '" +cs 
				self.spinBoxK.setValue(0)
			else:
				zu_erfassen_zw += "', csc = '" +"0"
			if self.spinBoxX.value() > 0:
				cs = str(self.spinBoxX.value())
				zu_erfassen_zw += "', csx = '" +cs 
				self.spinBoxK.setValue(0)
			else:
				zu_erfassen_zw += "', csx = '" +"0"
			if self.spinBoxO.value() > 0:
				cs = str(self.spinBoxO.value())
				zu_erfassen_zw += "', cso = '" +cs 
				self.spinBoxK.setValue(0)
			else:
				zu_erfassen_zw += "', cso = '" +"0"
			if self.spinBoxV.value() > 0:
				cs = str(self.spinBoxV.value())
				zu_erfassen_zw += "', csv = '" +cs 
				self.spinBoxK.setValue(0)
			else:
				zu_erfassen_zw += "', csv = '" +"0"
			if self.spinBoxB.value() > 0:
				cs = str(self.spinBoxB.value())
				zu_erfassen_zw += "', csb = '" +cs 
				self.spinBoxK.setValue(0)
			else:
				zu_erfassen_zw += "', csb = '" +"0"
			if self.spinBoxA.value() > 0:
				cs = str(self.spinBoxA.value())
				zu_erfassen_zw += "', csa = '" +cs 
				self.spinBoxK.setValue(0)
			else:
				zu_erfassen_zw += "', csa = '" +"0"
			if self.spinBoxS.value() > 0:
				cs = str(self.spinBoxS.value())
				zu_erfassen_zw += "', css = '" +cs 
				self.spinBoxK.setValue(0)
			else:
				zu_erfassen_zw += "', css = '" +"0"
			if self.spinBoxK.value() > 0:
				cs = str(self.spinBoxK.value())
				zu_erfassen_zw += "', csk = '" +cs 
			else:
				zu_erfassen_zw += "', csk = '" +"0"
			if self.comboBoxDefinition.currentIndex() == 0:
				zu_erfassen_zw += "', hd = null"
			elif self.comboBoxDefinition.currentIndex() == 1:
				zu_erfassen_zw += "', hd = '0'"
			elif self.comboBoxDefinition.currentIndex() == 2:
				zu_erfassen_zw += "', hd = '1'"
			elif self.comboBoxDefinition.currentIndex() == 3:
				zu_erfassen_zw += "', hd = '2'"
			elif self.comboBoxDefinition.currentIndex() == 4:
				zu_erfassen_zw += "', hd = '9'"
			zu_erfassen_zw +=", vorhanden = '" +vorhanden +"'" +" where cd = " +str(self.cd_alt) + " and bild = '" +bild.replace("'", "''") +"'"
			if self.radioButtonCoverJa.isChecked() and self.cover_austauschen:
				if os.path.exists(self.verzeichnis_thumbs +os.sep +"cd" +str(self.cd_alt) +os.sep +bild.rstrip()):
					# Bild war Thumbnail im CD Verzeichnis -> dieses löschen und neues im Cover Verzeichnis anlegen
					os.remove(self.verzeichnis_thumbs +os.sep +"cd" +str(self.cd_alt) +os.sep +bild.rstrip())
					os.rename(self.bilddatei, self.verzeichnis_cover +os.sep +self.bild.strip())
				else:
					os.rename(self.bilddatei, self.verzeichnis_cover +os.sep +self.bild.strip())
		else:
			if self.radioButtonCoverJa.isChecked() and not original:
				message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("When adding a cover you must also enter a movie title"))
				return
			if self.undo:
				bilddatei = QtGui.QImage(self.verzeichnis_trash +os.sep +bild)
			else:
				if self.radioButtonCoverJa.isChecked():
					bilddatei = QtGui.QImage(self.verzeichnis +os.sep +bild)
				else:
					bilddatei = QtGui.QImage(self.verzeichnis +os.sep +bild).scaled(size, QtCore.Qt.KeepAspectRatio)
			if self.radioButtonCoverJa.isChecked():
				newfilename = str(self.verzeichnis_cover +os.sep +bild)
			else:
				newfilename = str(self.verzeichnis_thumbs +os.sep +"cd" +str(cd) +os.sep +bild)
			# hier klappt noch etwas nicht richtig mit den Partnern, wenn len>256
			if len(bild) > 256 or os.path.exists(newfilename):
				neue_bilddatei = BilddateiUmbenennen(newfilename)
				if neue_bilddatei.exec_():
					try:
						bild_alt = str(self.verzeichnis +os.sep +bild)
						bild_neu = str(self.verzeichnis +os.sep +neue_bilddatei.lineEditDateiname.text())
						os.rename(bild_alt, bild_neu)
						newfilename = os.path.dirname(newfilename) +os.sep +neue_bilddatei.lineEditDateiname.text()
						bild = neue_bilddatei.lineEditDateiname.text()
						titel = str(bild.split('.')[0])
					except:
						message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Error on renaming image file"))
						return
				else:
					return
			else:
				if not os.path.exists(os.path.dirname(newfilename)):
					os.mkdir(os.path.dirname(newfilename))
			if bilddatei.save(newfilename):
				if not self.undo:
					os.remove(self.verzeichnis +os.sep +str(bild))
			else:
				message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Error saving image file"))
				return
			cs = ""
			zu_erfassen_zw = str("INSERT into pordb_vid VALUES ('" +titel.replace("'", "''") +"', '" +", ".join(darsteller).replace("'", "''") +"', " +str(cd) +", '" +bild.replace("'", "''") +"', '" +gesehen +"', '" +original +"', ' " +"', '" +vorhanden +"', DEFAULT") 
			if self.spinBoxF.value() > 0:
				cs = str(self.spinBoxF.value())
				zu_erfassen_zw += ", " +cs 
			else:
				zu_erfassen_zw += ", 0"
			if self.spinBoxH.value() > 0:
				cs = str(self.spinBoxH.value())
				zu_erfassen_zw += ", " +cs 
			else:
				zu_erfassen_zw += ", 0"
			if self.spinBoxT.value() > 0:
				cs = str(self.spinBoxT.value())
				zu_erfassen_zw += ", " +cs 
			else:
				zu_erfassen_zw += ", 0"
			if self.spinBoxC.value() > 0:
				cs = str(self.spinBoxC.value())
				zu_erfassen_zw += ", " +cs 
			else:
				zu_erfassen_zw += ", 0"
			if self.spinBoxX.value() > 0:
				cs = str(self.spinBoxX.value())
				zu_erfassen_zw += ", " +cs 
			else:
				zu_erfassen_zw += ", 0"
			if self.spinBoxO.value() > 0:
				cs = str(self.spinBoxO.value())
				zu_erfassen_zw += ", " +cs 
			else:
				zu_erfassen_zw += ", 0"
			if self.spinBoxV.value() > 0:
				cs = str(self.spinBoxV.value())
				zu_erfassen_zw += ", " +cs 
			else:
				zu_erfassen_zw += ", 0"
			if self.spinBoxB.value() > 0:
				cs = str(self.spinBoxB.value())
				zu_erfassen_zw += ", " +cs 
			else:
				zu_erfassen_zw += ", 0"
			if self.spinBoxA.value() > 0:
				cs = str(self.spinBoxA.value())
				zu_erfassen_zw += ", " +cs 
			else:
				zu_erfassen_zw += ", 0"
			if self.spinBoxS.value() > 0:
				cs = str(self.spinBoxS.value())
				zu_erfassen_zw += ", " +cs 
			else:
				zu_erfassen_zw += ", 0"
			if self.spinBoxK.value() > 0:
				cs = str(self.spinBoxK.value())
				zu_erfassen_zw += ", " +cs 
			else:
				zu_erfassen_zw += ", 0"
				
			if self.comboBoxDefinition.currentIndex() == 0:
				zu_erfassen_zw += ", null"
			elif self.comboBoxDefinition.currentIndex() == 1:
				zu_erfassen_zw += ", '0'"
			elif self.comboBoxDefinition.currentIndex() == 2:
				zu_erfassen_zw += ", '1'"
			elif self.comboBoxDefinition.currentIndex() == 3:
				zu_erfassen_zw += ", '2'"
			elif self.comboBoxDefinition.currentIndex() == 4:
				zu_erfassen_zw += ", '9'"
			zu_erfassen_zw += ")"
			
		zu_erfassen.append(zu_erfassen_zw)
			
		for i in darsteller:
			if i.lstrip() == "" or i.lstrip() == "?":
				continue
			zu_erfassen.append("UPDATE pordb_darsteller set anzahl = anzahl + 1 where darsteller = '" + i.replace("'", "''") + "'")
			if i == "" or i == "?" or i == "(Uninteressant)" or i == "(Komplett)" or i == "(Schlechte Qualitaet)":
				continue
			zu_lesen = "SELECT * FROM pordb_darsteller100 where darsteller = '" + i.replace("'", "''") + "'"
			self.lese_func = DBLesen(self, zu_lesen)
			res1 = DBLesen.get_data(self.lese_func)
			if len(res1) != 0:
				zu_erfassen.append("delete from pordb_darsteller100 where nr = '" + str(res1[0][0]) +"'")
			zu_erfassen.append("INSERT into pordb_darsteller100 (darsteller) VALUES ('" +i.replace("'", "''") +"')")
			
			partner_zaehler = 0
			if i.strip() != "(Uninteressant)" and i.strip() != "Defekt":
				zu_lesen = "select sex from pordb_darsteller where darsteller = '" +i.replace("'", "''")  +"'"
				self.lese_func = DBLesen(self, zu_lesen)
				res = DBLesen.get_data(self.lese_func)
				geschlecht = res[0][0]
				for j in darsteller:
					if j.strip() != "(Uninteressant)" and j.strip() != "Defekt" and i != j:
						zu_lesen = "select sex from pordb_darsteller where darsteller = '" +j.replace("'", "''")  +"'"
						self.lese_func = DBLesen(self, zu_lesen)
						res2 = DBLesen.get_data(self.lese_func)
						geschlecht2 = res2[0][0]
						if geschlecht != geschlecht2:
							zu_erfassen.append("insert into pordb_partner values ('" +i.replace("'", "''") +"', '" +j.replace("'", "''") +"', " +str(cd) +", '" +str(bild).replace("'", "''") +"')")
							zu_lesen = "select darsteller from pordb_partner where darsteller = '" +i.replace("'", "''") +"' and partner = '" +j.replace("'", "''") +"'"
							self.lese_func = DBLesen(self, zu_lesen)
							res3 = DBLesen.get_data(self.lese_func)
							if not res3:
								partner_zaehler += 1
							
			if partner_zaehler > 0:
				zu_erfassen.append("UPDATE pordb_darsteller set partner = partner + " +str(partner_zaehler) +" where darsteller = '" + i.replace("'", "''") + "'")
				
		zu_lesen = "select * from pordb_darsteller100"
		self.lese_func = DBLesen(self, zu_lesen)
		res1 = DBLesen.get_data(self.lese_func)
		anzahl_loeschen = len(res1) - 200
		if anzahl_loeschen > 0:
			res1.sort()
			for zaehler in range(anzahl_loeschen):
				zu_erfassen.append("delete from pordb_darsteller100 where nr = '" + str(res1[zaehler][0]) +"'")
		if not self.korrektur and original:
			zu_erfassen.append("UPDATE pordb_vid_neu SET titel = '" +titel.replace("'", "''") +"', darsteller = '" +", ".join(darsteller).replace("'", "''") +"', cd = " +str(cd) +", original = '" +original +"'")
		
		update_func = DBUpdate(self, zu_erfassen)
		DBUpdate.update_data(update_func)
		
		if self.original_weitere:
			zu_erfassen = []
			if self.korrektur:
				zu_lesen = "select primkey from pordb_vid where cd = " +str(self.cd_alt) + " and bild = '" +str(bild) +"'"
				self.lese_func = DBLesen(self, zu_lesen)
				curr_key = DBLesen.get_data(self.lese_func)
				zu_erfassen.append("delete from pordb_original where foreign_key_pordb_vid = " +str(curr_key[0][0]))
			else:
				zu_lesen = "select primkey from pordb_vid where cd = " +str(cd) + " and bild = '" +bild +"'"
				self.lese_func = DBLesen(self, zu_lesen)
				curr_key = DBLesen.get_data(self.lese_func)
			for i in self.original_weitere:
				if i:
					zu_erfassen.append("insert into pordb_original (original, foreign_key_pordb_vid) values ('" +i.replace("'", "''").title() +"', " +str(curr_key[0][0]) +")")
					
			update_func = DBUpdate(self, zu_erfassen)
			DBUpdate.update_data(update_func)
		
		self.close()
		QtGui.QDialog.accept(self)
	# end of accept
	
	def darsteller_addieren (self, darsteller, fehler_index):
		messageBox = QtGui.QMessageBox()
		messageBox.addButton(self.trUtf8("Yes, image exists"), QtGui.QMessageBox.AcceptRole)
		messageBox.addButton(self.trUtf8("Yes, no image"), QtGui.QMessageBox.YesRole)
		messageBox.addButton(self.trUtf8("No, correct entry"), QtGui.QMessageBox.RejectRole)
		messageBox.setWindowTitle(darsteller[fehler_index] +self.trUtf8(" does not exist"))
		messageBox.setIcon(QtGui.QMessageBox.Question)
		messageBox.setText(self.trUtf8("Do you want to add this actor?"))
		message = messageBox.exec_()
		if message == 2:
			korrekt = DarstellerKorrigieren(self.lineEditNeuDarsteller.text())
			korrekt.exec_()
			try:
				self.lineEditNeuDarsteller.setText(korrekt.darsteller)
			except:
				pass
			return

		neuer_darsteller = NeueingabeDarsteller(darsteller[fehler_index])
		neuer_darsteller.exec_()
		if message == 0:
			actor_file = False
			while not actor_file:
				self.file = QtGui.QFileDialog.getOpenFileName(self, self.trUtf8("Image of the actor ") +darsteller[fehler_index] +": " +self.trUtf8("please select one"), self.verzeichnis, self.trUtf8("Image files (*.jpg *.jpeg *.png);;all files (*.*)"))
				if self.file:
					if self.file == self.bilddatei:
						message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Selected image is the one which should be added to the database. Please select another one."))
						continue
					else:
						bild = QtGui.QImage(self.file)
						if bild.width() > size_darsteller.width() or bild.height() > size_darsteller.height():
							message = QtGui.QMessageBox.warning(self, self.trUtf8("Caution! "), self.trUtf8("Image of the actor is very big"))
						zu_lesen = "select sex from pordb_darsteller where darsteller = '" +darsteller[fehler_index].replace("'", "''").strip()  +"'"
						self.lese_func = DBLesen(self, zu_lesen)
						res = DBLesen.get_data(self.lese_func)
						extension = os.path.splitext(str(self.file))[-1].lower()
						if extension == '.jpeg':
							extension = '.jpg'
						try:
							sex = res[0][0]
							newfilename = self.verzeichnis_thumbs +os.sep +"darsteller_" +sex +os.sep +darsteller[fehler_index].strip().replace(" ", "_").replace("'", "_apostroph_").lower() + extension.strip()
							os.rename(self.file, newfilename)
						except:
							pass
						actor_file = True
						
	# end of darsteller_addieren

	def darsteller_pruefen(self, darsteller_liste):
		darsteller = darsteller_liste.split(", ")
		fehler = 0
		k = -1
		for i in darsteller:
			k += 1
			if i and i != "Defekt":
				zu_lesen = "select sex from pordb_darsteller where darsteller = '" +i.replace("'", "''").strip().title() +"'"
				self.lese_func = DBLesen(self, zu_lesen)
				res = DBLesen.get_data(self.lese_func)
				if not res:
					fehler = 1
				for j in range(0, k):
					if i == darsteller[j]:
						fehler = 2
						break
				if fehler:
					break
		return (darsteller, fehler, k)
	
	def darsteller_sortieren(self, darsteller):
		darsteller_m = []
		darsteller_w = []
		defekt_schalter = False
		for i in darsteller:
			if i:
				if i == "Defekt":
					defekt_schalter = True
				zu_lesen = "select sex from pordb_darsteller where darsteller = '" + i.strip().replace("'", "''").title() + "'"
				# When coming from actor renaming function
				zu_lesen = zu_lesen.replace("''''", "''")
				self.lese_func = DBLesen(self, zu_lesen)
				res = DBLesen.get_data(self.lese_func)
				try:
					sex = res[0][0]
					try:
						if sex == "w":
							darsteller_w.append(i.strip().title())
						else:
							darsteller_m.append(i.strip().title())
					except:
						pass
				except:
					pass
		darsteller_w.sort()
		darsteller_m.sort()
		darsteller_liste = darsteller_w + darsteller_m
		if defekt_schalter:
			darsteller_liste.append("Defekt")
		return darsteller_liste
					
	def onDelete(self):
		if self.undo:
			self.close()
			return
		darsteller_liste = self.darsteller.strip().split(", ")
		zu_erfassen = []
		for i in darsteller_liste:
			if i:
				zu_erfassen.append("UPDATE pordb_darsteller set anzahl = anzahl - 1 where darsteller = '" + i.replace("'", "''") + "'")
		# Daten für undo sichern
		zu_lesen = "select * FROM pordb_vid where cd = " +str(self.cd) + " and bild = '" +self.bild.replace("'", "''") + "'"
		self.lese_func = DBLesen(self, zu_lesen)
		res = DBLesen.get_data(self.lese_func)

		# Dateien in Trash Verzeichnis löschen
		dateiliste = os.listdir(self.verzeichnis_trash)
		for datei in dateiliste:
			if datei.find("pypordb_bildalt") == -1:
				os.remove(self.verzeichnis_trash + '/' + datei)

		# Bild in Trash Verzeichnis verschieben
		if not os.path.exists(self.verzeichnis_trash):
			os.mkdir(self.verzeichnis_trash)
		filename = self.verzeichnis_thumbs +os.sep +"cd" +str(self.cd) +os.sep +self.bild.strip()
		cover = None
		if not os.path.exists(filename):
			filename = self.verzeichnis_cover +os.sep +self.bild.strip()
			cover = "x"
		newfilename = str(self.verzeichnis_trash +os.sep +self.bild.strip())
		if os.path.exists(filename):
			os.rename(filename, newfilename)

		# Textdatei erstellen mit alten Daten
		textdatei = open(self.verzeichnis_trash +os.sep +self.bild[-2] +".txt", "w")
		zaehler = 0
		for i in res:
			for j in i:
				try:
					textdatei.write(j.encode("utf-8").rstrip() +"\n")
				except:
					textdatei.write(str(j).rstrip() +"\n")
		if cover:
			textdatei.write("COVER" +"\n")
		textdatei.close()

		zu_erfassen.append("DELETE FROM pordb_vid where cd = " +str(self.cd) + " and bild = '" +self.bild.strip().replace("'", "''") +"'")
		zu_erfassen.append("delete from pordb_partner where cd = " +str(self.cd) + " and bild = '" +self.bild.strip().replace("'", "''") +"'")
		
		update_func = DBUpdate(self, zu_erfassen)
		DBUpdate.update_data(update_func)
		
		zu_erfassen = []
		for i in darsteller_liste:
			if i:
				zu_lesen = "select distinct on (partner) partner from pordb_partner where darsteller = '" + i.replace("'", "''") + "'"
				self.lese_func = DBLesen(self, zu_lesen)
				res1 = DBLesen.get_data(self.lese_func)
				zu_erfassen.append("UPDATE pordb_darsteller set partner = " +str(len(res1)) +" where darsteller = '" + i.replace("'", "''") + "'")
		if zu_erfassen:
			update_func = DBUpdate(self, zu_erfassen)
			DBUpdate.update_data(update_func)
		
		self.close()
		
	def closeEvent(self, event):
		settings = QtCore.QSettings()
		settings.setValue("Neueingabe/Size", self.size())
		settings.setValue("Neueingabe/Position", self.pos())
		
