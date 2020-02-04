# -*- coding: utf-8 -*-

'''
    Copyright 2012-2020 HWM
    
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
from pordb_show_iafd_data import Ui_Dialog as pordb_show_iafd_data
from pypordb_dblesen import DBLesen
from pypordb_neu import Neueingabe
import os

class ShowIafdData(QtWidgets.QDialog, pordb_show_iafd_data):
    def __init__(self, verzeichnis, verzeichnis_original, verzeichnis_thumbs, verzeichnis_trash, verzeichnis_cover, video, titel=None, cd=None, bild=None, darsteller=None, gesehen=None, original=None, cs=None, vorhanden=None, definition=None, remarks=None, stars=None, cover=None, high_definition=None):
        
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        
        self.verzeichnis = verzeichnis
        self.verzeichnis_original = verzeichnis_original
        self.verzeichnis_thumbs = verzeichnis_thumbs
        self.verzeichnis_trash = verzeichnis_trash
        self.verzeichnis_cover = verzeichnis_cover
        self.video = video
        self.titel = titel
        self.cd = cd
        self.bild = bild
        self.darsteller = darsteller
        self.gesehen = gesehen
        self.original = original
        self.cs = cs
        self.vorhanden = vorhanden
        self.definition = definition
        self.remarks = remarks
        self.stars = stars
        self.cover = cover
        self.high_definition = high_definition
        
        self.pushButtonCancel.clicked.connect(self.close)
        self.pushButtonOK.clicked.connect(self.accept)
        
        self.imagesize = 200
        self.complete_size = QtCore.QSize(self.imagesize, self.imagesize)
        
        settings = QtCore.QSettings()
        window_size = settings.value("ShowIafdData/Size", QtCore.QSize(600, 500))
        self.resize(window_size)
        window_position = settings.value("ShowIafdData/Position", QtCore.QPoint(0, 0))
        self.move(window_position)
        
        self.graphicsView.setAlignment(QtCore.Qt.AlignLeft)
        self.scene = QtWidgets.QGraphicsScene()
        self.left_margin = 20
        
        self.font = QtGui.QFont()
        
        # set imagefiles from working directory
        self.populate_from_working_directory()
        
        # set original title
        self.y_pos = 0
        self.x_pos = self.imagesize + 30
        self.font.setBold(True)
        textitem = QtWidgets.QGraphicsTextItem(self.video[0])
        textitem.setPos(self.x_pos, self.y_pos)
        textitem.setFont(self.font)
        self.scene.addItem(textitem)
        self.y_pos += 40
        self.start_y_pos = self.y_pos
        
        # set alternate titles
        for i, wert in enumerate(self.video[1]):
            alt_title = wert
            textitem = QtWidgets.QGraphicsTextItem(alt_title)
            textitem.setPos(self.x_pos, self.y_pos)
            self.scene.addItem(textitem)
            self.y_pos += 30
            self.start_y_pos += self.y_pos
            
        # set scene and actors
        for i, wert in enumerate(self.video[2]): 
            for j, wert1 in enumerate(wert):
                darsteller_liste = wert1.split(", ")
                max_height = 0
                for k, wert2 in enumerate(darsteller_liste):
                    textitem = QtWidgets.QGraphicsTextItem(wert2)
                    if wert1.startswith("Scene "):
                        self.font.setBold(True)
                        textitem.setFont(self.font)
                        textitem.setPos(self.x_pos, self.y_pos)
                        self.scene.addItem(textitem)
                        self.y_pos += 30
                    elif wert2:
                        zu_lesen = "SELECT * from pordb_darsteller WHERE darsteller = %s"
                        lese_func = DBLesen(self, zu_lesen, wert2.title())
                        res = DBLesen.get_data(lese_func)
                        if res:
                            bilddatei = self.getBilddatei(res[0][0], res[0][1])
                        else:
                            bilddatei = self.getBilddatei(wert2.replace("'", "_apostroph_").title())
                        pixmap = QtGui.QPixmap(bilddatei).scaled(QtCore.QSize(self.complete_size),QtCore.Qt.KeepAspectRatio)
                        if pixmap.height() > max_height:
                            max_height = pixmap.height()
                        pixmapitem = QtWidgets.QGraphicsPixmapItem(pixmap)
                        pixmapitem.setPos(0, 20)
                        itemgroup = self.scene.createItemGroup([textitem, pixmapitem])
                        itemgroup.setPos(self.x_pos, self.y_pos)
                        itemgroup.setData(1, wert2)
                        itemgroup.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)
                        if self.titel: # imagefile is from thumbs directory
                            itemgroup.setSelected(True)
                        self.y_pos += pixmap.height() + 20
            self.x_pos += self.imagesize + 30
            self.y_pos = self.start_y_pos
            
        self.graphicsView.setScene(self.scene)
        self.graphicsView.centerOn(0, 0)
        
    def accept(self):
        scene_to_add = None
        actor_to_add = []
        for i in self.scene.selectedItems():
            if i.data(0):
                if scene_to_add:
                    QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("Please select only one scene"))
                    return
                else:
                    scene_to_add = str(i.data(0))
            if i.data(1):
                actor_to_add.append(str(i.data(1)))
                
        if not scene_to_add:
            QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("No scene selected"))
            return
        if not actor_to_add:
            QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("No actors selected"))
            return
        darsteller = ", ".join(actor_to_add)
        if self.titel:
            verzeichnis = self.verzeichnis_thumbs
        else: 
            verzeichnis = self.verzeichnis
        eingabedialog = Neueingabe(self.verzeichnis, self.verzeichnis_original, self.verzeichnis_thumbs, self.verzeichnis_trash, self.verzeichnis_cover, os.path.join(verzeichnis, scene_to_add), titel=self.titel, darsteller=darsteller, cd=self.cd, bild=self.bild, gesehen=self.gesehen, original=self.video[0], cs=self.cs, vorhanden=self.vorhanden, cover=self.cover, undo=None, cover_anlegen=None, original_weitere=self.video[1], access_from_iafd=True, high_definition=self.high_definition)
        if eingabedialog.exec_():
            for i in list(self.scene.items()):
                if i.data(0):
                    self.scene.removeItem(i)
            if not self.titel:
                self.populate_from_working_directory()
            else:
                self.close()
        
    def populate_from_working_directory(self):
        self.x_pos = self.left_margin
        self.y_pos = 0
        if self.titel:
            # get imagefile from thumbs directory
            dateiliste = []
            dateiliste.append(os.path.join("cd" + str(self.cd), self.bild.rstrip()))
        else:
            # get imagefiles from working directory
            dateiliste = [f for f in os.listdir(self.verzeichnis) if f.lower().endswith(".jpeg") or f.lower().endswith(".jpg") or f.lower().endswith(".png")]
        if dateiliste:
            dateiliste.sort()
            textitem = QtWidgets.QGraphicsTextItem(self.tr("Clips to add:"))
            self.font.setPointSize(16)
            self.font.setWeight(75)
            self.font.setBold(True)
            textitem.setFont(self.font)
            textitem.setPos(0, self.y_pos)
            self.scene.addItem(textitem)
            self.y_pos += 30
            max_height = 0
            for i in dateiliste:
                if self.titel:
                    bilddatei = os.path.join(self.verzeichnis_thumbs, i)
                else:
                    bilddatei = os.path.join(self.verzeichnis, i)
                pixmap = QtGui.QPixmap(bilddatei).scaled(QtCore.QSize(self.complete_size),QtCore.Qt.KeepAspectRatio)
                if pixmap.height() > max_height:
                    max_height = pixmap.height()
                self.pixmapitem_scene = QtWidgets.QGraphicsPixmapItem(pixmap)
                self.pixmapitem_scene.setPos(0, 20)
                datei = i[0:24]
                if len(i) > 25:
                    datei += "..."
                self.textitem_scene = QtWidgets.QGraphicsTextItem(datei)
                itemgroup = self.scene.createItemGroup([self.textitem_scene, self.pixmapitem_scene])
                itemgroup.setPos(self.x_pos, self.y_pos)
                itemgroup.setData(0, i)
                itemgroup.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)
                if self.titel: # imagefile is from thumbs directory
                    itemgroup.setSelected(True)
                self.y_pos += pixmap.height() + 20
            self.x_pos = self.left_margin
        else:
            self.close()
        #self.scene.clearSelection()
        self.scene.update()
        
    def getBilddatei(self, actor, sex = None):
        bilddatei = None
        if actor:
            if sex:
                bilddatei = os.path.join(self.verzeichnis_thumbs, "darsteller_" + sex, actor.lower().strip().replace(" ", "_").replace("'", "_apostroph_") + ".jpg")
            else:
                bilddatei = os.path.join(self.verzeichnis_thumbs, "darsteller_" + "w", actor.lower().strip().replace(" ", "_").replace("'", "_apostroph_") + ".jpg")
                if not os.path.exists(bilddatei):
                    bilddatei = os.path.join(self.verzeichnis_thumbs, "darsteller_" + "m", actor.lower().strip().replace(" ", "_").replace("'", "_apostroph_") + ".jpg")
        if not bilddatei or not os.path.exists(bilddatei):
            bilddatei = os.path.join(self.verzeichnis_thumbs, "nichtvorhanden", "nicht_vorhanden.jpg")
        return bilddatei
    
    def closeEvent(self, event):
        settings = QtCore.QSettings()
        settings.setValue("ShowIafdData/Size", self.size())
        settings.setValue("ShowIafdData/Position", self.pos())
