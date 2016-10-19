# -*- coding: utf-8 -*-

'''
    Copyright 2012-2015 HWM
    
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
import datetime

size = QtCore.QSize(260, 260)
sizeneu = QtCore.QSize(300, 300)
size_darsteller = QtCore.QSize(1920, 1080)
videodateien = (".asf", ".avi", ".divx", ".f4v", ".m4v", ".mkv", ".mpg", ".mpeg", ".mp4", ".mov", ".wmv")

class Neueingabe(QtGui.QDialog, pordb_neu):
    def __init__(self, verzeichnis, verzeichnis_original, verzeichnis_thumbs, verzeichnis_trash, verzeichnis_cover, bilddatei, titel=None, darsteller=None, cd=None, bild=None, gesehen=None, original=None, cs=None, vorhanden=None, stars=None, cover=None, undo=None, cover_anlegen=None, original_weitere=None, original_cover = None, high_definition = None, access_from_iafd = None):
        
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
        self.stars = stars
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
        self.access_from_iafd = access_from_iafd
        self.icon_starred = QtGui.QIcon()
        self.icon_starred.addPixmap(QtGui.QPixmap("pypordb/starred.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_nonstarred = QtGui.QIcon()
        self.icon_nonstarred.addPixmap(QtGui.QPixmap("pypordb/non-starred.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.set_stars = 0
        
        self.connect(self.pushButtonNeuOK, QtCore.SIGNAL("clicked()"), self.accept)
        self.connect(self.pushButtonNeuCancel, QtCore.SIGNAL("clicked()"), self.close)
        self.connect(self.pushButtonNeuDelete, QtCore.SIGNAL("clicked()"), self.onDelete)
        self.connect(self.pushButtonOriginal, QtCore.SIGNAL("clicked()"), self.onOriginal)
        self.connect(self.pushButtonOriginalAlt, QtCore.SIGNAL("clicked()"), self.onOriginalAlt)
        self.connect(self.pushButtonAddYear, QtCore.SIGNAL("clicked()"), self.onAddYear)
        self.connect(self.pushButtonStar1, QtCore.SIGNAL("clicked()"), self.onStar1)
        self.connect(self.pushButtonStar2, QtCore.SIGNAL("clicked()"), self.onStar2)
        self.connect(self.pushButtonStar3, QtCore.SIGNAL("clicked()"), self.onStar3)
        self.connect(self.pushButtonStar4, QtCore.SIGNAL("clicked()"), self.onStar4)
        self.connect(self.pushButtonStar5, QtCore.SIGNAL("clicked()"), self.onStar5)
        self.connect(self.pushButtonClearRating, QtCore.SIGNAL("clicked()"), self.onClearRating)
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
        
        # populate combox for years
        today = datetime.date.today()
        self.comboBoxYear.clear()
        for i in range(today.year + 1, 1899, -1):
            self.comboBoxYear.addItem(str(i))
        self.comboBoxYear.setCurrentIndex(1)
        
        # set default position for cropping images
        self.positionX = 0
        self.positionY = 0
        
        zu_lesen = "SELECT * FROM pordb_vid_neu"
        self.lese_func = DBLesen(self, zu_lesen)
        self.res_vid_neu = DBLesen.get_data(self.lese_func)
        if self.res_vid_neu[0][3]:
            self.labelOriginal.setText(self.res_vid_neu[0][3])
        
        zu_lesen = "SELECT * FROM pordb_darsteller100 ORDER BY darsteller"
        self.lese_func = DBLesen(self, zu_lesen)
        res = DBLesen.get_data(self.lese_func)
        res.sort()
        res.reverse()
        darsteller_m = []
        darsteller_w = []
        for i in res:
            zu_lesen = "SELECT sex FROM pordb_darsteller WHERE darsteller = %s"
            self.lese_func = DBLesen(self, zu_lesen, tuple(i)[1].rstrip())
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
            if self.stars == 1:
                self.pushButtonStar1.setIcon(self.icon_starred)
            elif self.stars == 2:
                self.pushButtonStar1.setIcon(self.icon_starred)
                self.pushButtonStar2.setIcon(self.icon_starred)
            elif self.stars == 3:
                self.pushButtonStar1.setIcon(self.icon_starred)
                self.pushButtonStar2.setIcon(self.icon_starred)
                self.pushButtonStar3.setIcon(self.icon_starred)
            elif self.stars == 4:
                self.pushButtonStar1.setIcon(self.icon_starred)
                self.pushButtonStar2.setIcon(self.icon_starred)
                self.pushButtonStar3.setIcon(self.icon_starred)
                self.pushButtonStar4.setIcon(self.icon_starred)
            elif self.stars == 5:
                self.pushButtonStar1.setIcon(self.icon_starred)
                self.pushButtonStar2.setIcon(self.icon_starred)
                self.pushButtonStar3.setIcon(self.icon_starred)
                self.pushButtonStar4.setIcon(self.icon_starred)
                self.pushButtonStar5.setIcon(self.icon_starred)                 
            self.pushButtonBildloeschen.setEnabled(False)
            self.pushButtonBildbeschneiden.setEnabled(False)
            if self.undo:
                self.pushButtonNeuDelete.setEnabled(False)
            self.pushButtonVerz.setEnabled(False)
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
            elif self.high_definition == "3":
                self.comboBoxDefinition.setCurrentIndex(4)
            elif self.high_definition == "9":
                self.comboBoxDefinition.setCurrentIndex(5)
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
            else:
                self.radioButtonCoverJa.setChecked(False)
                self.radioButtonCoverNein.setChecked(True)
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
            self.lineEditNeuCD.setText(str(self.res_vid_neu[0][2]))
            self.lineEditNeuBild.setText(os.path.basename(str(self.bilddatei)))
            if self.access_from_iafd:
                self.pushButtonBildloeschen.setEnabled(False)
                self.pushButtonBildbeschneiden.setEnabled(False)
                self.pushButtonVerz.setEnabled(False)
            else:
                self.pushButtonBildloeschen.setEnabled(True)
                self.pushButtonBildbeschneiden.setEnabled(True)
                self.pushButtonVerz.setEnabled(True)
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
        
    def onAddYear(self):
        year = self.comboBoxYear.currentText()
        self.lineEditNeuOriginal.setText(self.lineEditNeuOriginal.text().strip() + " (" + str(year) + ")")
        self.pushButtonNeuOK.setFocus()
        
    def onStar1(self):
        self.pushButtonStar1.setIcon(self.icon_starred)
        self.pushButtonStar2.setIcon(self.icon_nonstarred)
        self.pushButtonStar3.setIcon(self.icon_nonstarred)
        self.pushButtonStar4.setIcon(self.icon_nonstarred)
        self.pushButtonStar5.setIcon(self.icon_nonstarred)
        self.pushButtonNeuOK.setFocus()
        self.set_stars = 1
        
    def onStar2(self):
        self.pushButtonStar1.setIcon(self.icon_starred)
        self.pushButtonStar2.setIcon(self.icon_starred)
        self.pushButtonStar3.setIcon(self.icon_nonstarred)
        self.pushButtonStar4.setIcon(self.icon_nonstarred)
        self.pushButtonStar5.setIcon(self.icon_nonstarred)
        self.pushButtonNeuOK.setFocus()
        self.set_stars = 2
        
    def onStar3(self):
        self.pushButtonStar1.setIcon(self.icon_starred)
        self.pushButtonStar2.setIcon(self.icon_starred)
        self.pushButtonStar3.setIcon(self.icon_starred)
        self.pushButtonStar4.setIcon(self.icon_nonstarred)
        self.pushButtonStar5.setIcon(self.icon_nonstarred)
        self.pushButtonNeuOK.setFocus()
        self.set_stars = 3
        
    def onStar4(self):
        self.pushButtonStar1.setIcon(self.icon_starred)
        self.pushButtonStar2.setIcon(self.icon_starred)
        self.pushButtonStar3.setIcon(self.icon_starred)
        self.pushButtonStar4.setIcon(self.icon_starred)
        self.pushButtonStar5.setIcon(self.icon_nonstarred)
        self.pushButtonNeuOK.setFocus()
        self.set_stars = 4
        
    def onStar5(self):
        self.pushButtonStar1.setIcon(self.icon_starred)
        self.pushButtonStar2.setIcon(self.icon_starred)
        self.pushButtonStar3.setIcon(self.icon_starred)
        self.pushButtonStar4.setIcon(self.icon_starred)
        self.pushButtonStar5.setIcon(self.icon_starred)
        self.pushButtonNeuOK.setFocus()
        self.set_stars = 5
        
    def onClearRating(self):
        self.pushButtonStar1.setIcon(self.icon_nonstarred)
        self.pushButtonStar2.setIcon(self.icon_nonstarred)
        self.pushButtonStar3.setIcon(self.icon_nonstarred)
        self.pushButtonStar4.setIcon(self.icon_nonstarred)
        self.pushButtonStar5.setIcon(self.icon_nonstarred)
        self.pushButtonNeuOK.setFocus()
        self.set_stars = 0
    
    def onDarstelleruebernehmen(self):
        selected = self.listWidgetW.selectedItems()
        selected.extend(self.listWidgetM.selectedItems())
        selected_str = []
        for i in selected:
            selected_str.append(str(i.text()))
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
                    zu_lesen = "SELECT darsteller FROM pordb_pseudo WHERE pseudo = %s"
                    self.lese_func = DBLesen(self, zu_lesen, darsteller[fehler_index].title().strip())
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
            original = str(self.lineEditNeuOriginal.text()).title().split()
        except:
            message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Error: original title has invalid characters"))
            return
        
        # get rid of double spaces
        original = " ".join(original)

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
            message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Video is not in stock: resolution deleted"))
            self.comboBoxDefinition.setCurrentIndex(0)
        zu_erfassen = []
        if self.korrektur and not self.undo:
            darsteller_liste = self.darsteller.strip().split(", ")
            if not darsteller_liste[0]:
                darsteller_liste = []
            for i in darsteller_liste:
                werte = []
                werte.append(i)
                zu_erfassen.append(["UPDATE pordb_darsteller SET anzahl = anzahl - 1 WHERE darsteller = %s", werte])
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
            werte = []
            werte.append(self.cd_alt)
            werte.append(bild)
            zu_erfassen.append(["DELETE FROM pordb_partner WHERE cd = %s AND bild = %s", werte])
            werte = []
            werte.append(titel)
            werte.append(", ".join(darsteller))
            werte.append(cd)
            werte.append(bild)
            werte.append(gesehen)
            werte.append(original)
            zu_erfassen_zw = "UPDATE pordb_vid SET titel = %s, darsteller = %s, cd = %s, bild = %s, gesehen = %s, original = %s, csf = %s, csh = %s, cst = %s, csc = %s, csx = %s, cso = %s, csv = %s, csb = %s, csa = %s, css = %s, csk = %s, hd = %s, vorhanden = %s, stars = %s WHERE cd = %s AND bild = %s"
            if self.spinBoxF.value() > 0:
                werte.append(self.spinBoxF.value())
                self.spinBoxK.setValue(0)
            else:
                werte.append(0)
            if self.spinBoxH.value() > 0:
                werte.append(self.spinBoxH.value())
                self.spinBoxK.setValue(0)
            else:
                werte.append(0)
            if self.spinBoxT.value() > 0:
                werte.append(self.spinBoxT.value())
                self.spinBoxK.setValue(0)
            else:
                werte.append(0)
            if self.spinBoxC.value() > 0:
                werte.append(self.spinBoxC.value())
                self.spinBoxK.setValue(0)
            else:
                werte.append(0)
            if self.spinBoxX.value() > 0:
                werte.append(self.spinBoxX.value())
                self.spinBoxK.setValue(0)
            else:
                werte.append(0)
            if self.spinBoxO.value() > 0:
                werte.append(self.spinBoxO.value())
                self.spinBoxK.setValue(0)
            else:
                werte.append(0)
            if self.spinBoxV.value() > 0:
                werte.append(self.spinBoxV.value())
                self.spinBoxK.setValue(0)
            else:
                werte.append(0)
            if self.spinBoxB.value() > 0:
                werte.append(self.spinBoxB.value())
                self.spinBoxK.setValue(0)
            else:
                werte.append(0)
            if self.spinBoxA.value() > 0:
                werte.append(self.spinBoxA.value())
                self.spinBoxK.setValue(0)
            else:
                werte.append(0)
            if self.spinBoxS.value() > 0:
                werte.append(self.spinBoxS.value())
                self.spinBoxK.setValue(0)
            else:
                werte.append(0)
            if self.spinBoxK.value() > 0:
                werte.append(self.spinBoxK.value())
            else:
                werte.append(0)
            if self.comboBoxDefinition.currentIndex() == 0:
                werte.append(None)
            elif self.comboBoxDefinition.currentIndex() == 1:
                werte.append("0")
            elif self.comboBoxDefinition.currentIndex() == 2:
                werte.append("1")
            elif self.comboBoxDefinition.currentIndex() == 3:
                werte.append("2")
            elif self.comboBoxDefinition.currentIndex() == 4:
                werte.append("3")
            elif self.comboBoxDefinition.currentIndex() == 5:
                werte.append("9")
            werte.append(vorhanden)
            werte.append(self.set_stars)
            werte.append(self.cd_alt)
            werte.append(bild)
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
            werte = []
            werte.append("pordb_vid_primkey_seq")
            zu_lesen = "SELECT nextval(%s)"
            self.lese_func = DBLesen(self, zu_lesen, werte)
            res = DBLesen.get_data(self.lese_func)
            werte = []
            werte.append(titel)
            werte.append(", ".join(darsteller))
            werte.append(cd)
            werte.append(bild)
            werte.append(gesehen)
            werte.append(original)
            werte.append("")
            werte.append(vorhanden)
            werte.append(self.set_stars)
            werte.append(res[0][0])
            zu_erfassen_zw = "INSERT INTO pordb_vid VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            if self.spinBoxF.value() > 0:
                cs = self.spinBoxF.value()
            else:
                cs = 0
            werte.append(cs)
            
            if self.spinBoxH.value() > 0:
                cs = self.spinBoxH.value()
            else:
                cs = 0
            werte.append(cs)
            
            if self.spinBoxT.value() > 0:
                cs = self.spinBoxT.value()
            else:
                cs = 0
            werte.append(cs)
            
            if self.spinBoxC.value() > 0:
                cs = self.spinBoxC.value()
            else:
                cs = 0
            werte.append(cs)
            
            if self.spinBoxX.value() > 0:
                cs = self.spinBoxX.value()
            else:
                cs = 0
            werte.append(cs)
            
            if self.spinBoxO.value() > 0:
                cs = self.spinBoxO.value()
            else:
                cs = 0
            werte.append(cs)
            
            if self.spinBoxV.value() > 0:
                cs = self.spinBoxV.value()
            else:
                cs = 0
            werte.append(cs)
            
            if self.spinBoxB.value() > 0:
                cs = self.spinBoxB.value()
            else:
                cs = 0
            werte.append(cs)
            
            if self.spinBoxA.value() > 0:
                cs = self.spinBoxA.value()
            else:
                cs = 0
            werte.append(cs)
            
            if self.spinBoxS.value() > 0:
                cs = self.spinBoxS.value()
            else:
                cs = 0
            werte.append(cs)
            
            if self.spinBoxK.value() > 0:
                cs = self.spinBoxK.value()
            else:
                cs = 0
            werte.append(cs)
                
            if self.comboBoxDefinition.currentIndex() == 0:
                werte.append(None)
            elif self.comboBoxDefinition.currentIndex() == 1:
                werte.append("0")
            elif self.comboBoxDefinition.currentIndex() == 2:
                werte.append("1")
            elif self.comboBoxDefinition.currentIndex() == 3:
                werte.append("2")
            elif self.comboBoxDefinition.currentIndex() == 4:
                werte.append("3")
            elif self.comboBoxDefinition.currentIndex() == 5:
                werte.append("9")
            
        zu_erfassen.append([zu_erfassen_zw, werte])
            
        for i in darsteller:
            if i.lstrip() == "" or i.lstrip() == "?":
                continue
            werte = []
            werte.append(i)
            zu_erfassen.append(["UPDATE pordb_darsteller SET anzahl = anzahl + 1 WHERE darsteller = %s", werte])
            if i == "" or i == "?" or i == "(Uninteressant)" or i == "(Komplett)" or i == "(Schlechte Qualitaet)":
                continue
            zu_erfassen.append(["DELETE FROM pordb_darsteller100 WHERE darsteller = %s", werte])
            zu_erfassen.append(["INSERT INTO pordb_darsteller100 (darsteller) VALUES (%s)", werte])
            
            partner_zaehler = 0
            if i.strip() != "(Uninteressant)" and i.strip() != "Defekt":
                zu_lesen = "SELECT sex FROM pordb_darsteller WHERE darsteller = %s"
                self.lese_func = DBLesen(self, zu_lesen, i)
                res = DBLesen.get_data(self.lese_func)
                geschlecht = res[0][0]
                for j in darsteller:
                    if j.strip() != "(Uninteressant)" and j.strip() != "Defekt" and i != j:
                        zu_lesen = "SELECT sex FROM pordb_darsteller WHERE darsteller = %s"
                        self.lese_func = DBLesen(self, zu_lesen, j)
                        res2 = DBLesen.get_data(self.lese_func)
                        geschlecht2 = res2[0][0]
                        if geschlecht != geschlecht2:
                            werte = []
                            werte.append(i)
                            werte.append(j)
                            werte.append(cd)
                            werte.append(bild)
                            zu_erfassen.append(["INSERT INTO pordb_partner VALUES (%s, %s, %s, %s)", werte])
                            zu_lesen = "SELECT darsteller FROM pordb_partner WHERE darsteller = %s AND partner = %s"
                            self.lese_func = DBLesen(self, zu_lesen, (i, j))
                            res3 = DBLesen.get_data(self.lese_func)
                            if not res3:
                                partner_zaehler += 1
                            
            if partner_zaehler > 0:
                werte = []
                werte.append(partner_zaehler)
                werte.append(i)
                zu_erfassen.append(["UPDATE pordb_darsteller SET partner = partner + %s WHERE darsteller = %s", werte])
                
        zu_lesen = "SELECT * FROM pordb_darsteller100"
        self.lese_func = DBLesen(self, zu_lesen)
        res1 = DBLesen.get_data(self.lese_func)
        anzahl_loeschen = len(res1) - 200
        if anzahl_loeschen > 0:
            res1.sort()
            for zaehler in range(anzahl_loeschen):
                werte = []
                werte.append(str(res1[zaehler][0]))
                zu_erfassen.append(["DELETE FROM pordb_darsteller100 WHERE nr = %s", werte])
        if not self.korrektur:
            werte = []
            werte.append(titel)
            werte.append(", ".join(darsteller))
            werte.append(cd)
            werte.append(original)
            zu_erfassen.append(["UPDATE pordb_vid_neu SET titel = %s, darsteller = %s, cd = %s, original = %s", werte])
        
        update_func = DBUpdate(self, zu_erfassen)
        DBUpdate.update_data(update_func)
        
        if self.original_weitere:
            zu_erfassen = []
            if self.korrektur:
                zu_lesen = "SELECT primkey FROM pordb_vid WHERE cd = %s AND bild = %s"
                self.lese_func = DBLesen(self, zu_lesen, (str(self.cd_alt), str(bild)))
                curr_key = DBLesen.get_data(self.lese_func)
                werte = []
                werte.append(str(curr_key[0][0]))
                zu_erfassen.append(["DELETE FROM pordb_original WHERE foreign_key_pordb_vid = %s", werte])
            else:
                zu_lesen = "SELECT primkey FROM pordb_vid WHERE cd = %s AND bild = %s"
                self.lese_func = DBLesen(self, zu_lesen, (str(cd), bild))
                curr_key = DBLesen.get_data(self.lese_func)
            for i in self.original_weitere:
                if i:
                    if type(i) == str:
                        werte = []
                        werte.append(i.title())
                        werte.append(str(curr_key[0][0]))
                        zu_erfassen.append(["INSERT INTO pordb_original (original, foreign_key_pordb_vid) VALUES (%s, %s)", werte])
                    else:
                        werte = []
                        werte.append(i.decode().title())
                        werte.append(str(curr_key[0][0]))
                        zu_erfassen.append(["INSERT INTO pordb_original (original, foreign_key_pordb_vid) VALUES (%s, %s)", werte])
                    
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
                        zu_lesen = "SELECT sex FROM pordb_darsteller WHERE darsteller = %s"
                        self.lese_func = DBLesen(self, zu_lesen, darsteller[fehler_index].strip())
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
        darstellerliste = darsteller_liste.split(",")
        darsteller = []
        for i in darstellerliste:
            darsteller.append(i.strip())
        fehler = 0
        k = -1
        for i in darsteller:
            k += 1
            if i and i != "Defekt":
                zu_lesen = "SELECT sex FROM pordb_darsteller WHERE darsteller = %s"
                self.lese_func = DBLesen(self, zu_lesen, i.strip().title())
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
                zu_lesen = "SELECT sex FROM pordb_darsteller WHERE darsteller = %s"
                self.lese_func = DBLesen(self, zu_lesen, i.strip().replace("''''", "''").title()) # 2nd replace when coming from actor renaming function
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
                werte = []
                werte.append(i)
                zu_erfassen.append(["UPDATE pordb_darsteller SET anzahl = anzahl - 1 WHERE darsteller = %s", werte])
        # Daten für undo sichern
        zu_lesen = "SELECT * FROM pordb_vid WHERE cd = %s AND bild = %s"
        self.lese_func = DBLesen(self, zu_lesen, (str(self.cd), self.bild))
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

        werte = []
        werte.append(str(self.cd))
        werte.append(self.bild.strip())
        zu_erfassen.append(["DELETE FROM pordb_vid WHERE cd = %s AND bild = %s", werte])
        werte = []
        werte.append(str(self.cd))
        werte.append(self.bild.strip())
        zu_erfassen.append(["DELETE FROM pordb_partner WHERE cd = %s AND bild = %s", werte])
        
        update_func = DBUpdate(self, zu_erfassen)
        DBUpdate.update_data(update_func)
        
        zu_erfassen = []
        for i in darsteller_liste:
            if i:
                zu_lesen = "SELECT DISTINCT ON (partner) partner FROM pordb_partner WHERE darsteller = %s"
                self.lese_func = DBLesen(self, zu_lesen, i)
                res1 = DBLesen.get_data(self.lese_func)
                werte = []
                werte.append(len(res1))
                werte.append(i)
                zu_erfassen.append(["UPDATE pordb_darsteller SET partner = %s WHERE darsteller = %s", werte])
        if zu_erfassen:
            update_func = DBUpdate(self, zu_erfassen)
            DBUpdate.update_data(update_func)
        
        self.close()
        
    def closeEvent(self, event):
        settings = QtCore.QSettings()
        settings.setValue("Neueingabe/Size", self.size())
        settings.setValue("Neueingabe/Position", self.pos())
        
