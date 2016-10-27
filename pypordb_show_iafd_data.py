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

from PyQt4 import QtGui, QtCore
from pordb_show_iafd_data import Ui_Dialog as pordb_show_iafd_data
from pypordb_dblesen import DBLesen
from pypordb_neu import Neueingabe
import os

class ShowIafdData(QtGui.QDialog, pordb_show_iafd_data):
    def __init__(self, verzeichnis, verzeichnis_original, verzeichnis_thumbs, verzeichnis_trash, verzeichnis_cover, video):
        
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        
        self.verzeichnis = verzeichnis
        self.verzeichnis_original = verzeichnis_original
        self.verzeichnis_thumbs = verzeichnis_thumbs
        self.verzeichnis_trash = verzeichnis_trash
        self.verzeichnis_cover = verzeichnis_cover
        self.video = video
        
        self.connect(self.pushButtonCancel, QtCore.SIGNAL("clicked()"), self.close)
        self.connect(self.pushButtonOK, QtCore.SIGNAL("clicked()"), self.accept)
        
        self.imagesize = 200
        self.complete_size = QtCore.QSize(self.imagesize, self.imagesize)
        
        settings = QtCore.QSettings()
        window_size = settings.value("ShowIafdData/Size", QtCore.QSize(600, 500))
        self.resize(window_size)
        window_position = settings.value("ShowIafdData/Position", QtCore.QPoint(0, 0))
        self.move(window_position)
        
        self.graphicsView.setAlignment(QtCore.Qt.AlignLeft)
        self.scene = QtGui.QGraphicsScene()
        self.left_margin = 20
        
        self.font = QtGui.QFont()
        
        # set imagefiles from working directory
        self.populate_from_working_directory()
        
        # set original title
        self.font.setBold(True)
        textitem = QtGui.QGraphicsTextItem(self.video[0])
        textitem.setPos(0, self.y_pos)
        textitem.setFont(self.font)
        self.scene.addItem(textitem)
        self.y_pos += 40
        
        # set alternate titles
        for i, wert in enumerate(self.video[1]):
            alt_title = wert
            textitem = QtGui.QGraphicsTextItem(alt_title)
            textitem.setPos(self.x_pos, self.y_pos)
            self.scene.addItem(textitem)
            self.y_pos += 30
            
        # set scene and actors
        for i, wert in enumerate(self.video[2]): 
            for j, wert1 in enumerate(wert):
                darsteller_liste = wert1.split(", ")
                image_shown = False
                max_height = 0
                for k, wert2 in enumerate(darsteller_liste):
                    textitem = QtGui.QGraphicsTextItem(wert2)
                    if wert1.startswith("Scene "):
                        self.y_pos += 30
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
                        pixmapitem = QtGui.QGraphicsPixmapItem(pixmap)
                        pixmapitem.setPos(0, 20)
                        itemgroup = self.scene.createItemGroup([textitem, pixmapitem])
                        itemgroup.setPos(self.x_pos, self.y_pos)
                        itemgroup.setData(1, wert2)
                        itemgroup.setFlag(QtGui.QGraphicsItem.ItemIsSelectable)
                        self.x_pos += self.imagesize + 20
                        image_shown = True
                self.x_pos = self.left_margin
                if image_shown:
                    self.y_pos += max_height + 20
            
        self.graphicsView.setScene(self.scene)
        self.graphicsView.centerOn(0, 0)
        
    def accept(self):
        scene_to_add = None
        actor_to_add = []
        for i in self.scene.selectedItems():
            if i.data(0):
                if scene_to_add:
                    message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Please select only one scene"))
                    return
                else:
                    scene_to_add = str(i.data(0))
            if i.data(1):
                actor_to_add.append(str(i.data(1)))
                
        if not scene_to_add:
            message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("No scene selected"))
            return
        if not actor_to_add:
            message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("No actors selected"))
            return
        darsteller = ", ".join(actor_to_add)
        eingabedialog = Neueingabe(self.verzeichnis, self.verzeichnis_original, self.verzeichnis_thumbs, self.verzeichnis_trash, self.verzeichnis_cover, os.path.join(self.verzeichnis, scene_to_add), titel=None, darsteller=darsteller, cd=None, bild=None, gesehen=None, original=self.video[0], cs=None, vorhanden=None, cover=None, undo=None, cover_anlegen=None, original_weitere=self.video[1], access_from_iafd=True)
        if eingabedialog.exec_():
            for i in list(self.scene.items()):
                if i.data(0):
                    self.scene.removeItem(i)
            self.populate_from_working_directory(close = 1)
        
    def populate_from_working_directory(self, close = None):
        self.x_pos = self.left_margin
        self.y_pos = 0
        # get imagefiles from working directory
        dateiliste = [f for f in os.listdir(self.verzeichnis) if f.lower().endswith(".jpeg") or f.lower().endswith(".jpg") or f.lower().endswith(".png")]
        zeile = -1
        if dateiliste:
            dateiliste.sort()
            textitem = QtGui.QGraphicsTextItem(self.trUtf8("Clips to add:"))
            self.font.setPointSize(16)
            self.font.setWeight(75)
            self.font.setBold(True)
            textitem.setFont(self.font)
            textitem.setPos(0, self.y_pos)
            self.scene.addItem(textitem)
            self.y_pos += 30
            max_height = 0
            for i in dateiliste:
                bilddatei = os.path.join(self.verzeichnis, i)
                pixmap = QtGui.QPixmap(bilddatei).scaled(QtCore.QSize(self.complete_size),QtCore.Qt.KeepAspectRatio)
                if pixmap.height() > max_height:
                    max_height = pixmap.height()
                self.pixmapitem_scene = QtGui.QGraphicsPixmapItem(pixmap)
                self.pixmapitem_scene.setPos(0, 20)
                datei = i[0:24]
                if len(i) > 25:
                    datei += "..."
                self.textitem_scene = QtGui.QGraphicsTextItem(datei)
                itemgroup = self.scene.createItemGroup([self.textitem_scene, self.pixmapitem_scene])
                itemgroup.setPos(self.x_pos, self.y_pos)
                itemgroup.setData(0, i)
                itemgroup.setFlag(QtGui.QGraphicsItem.ItemIsSelectable)
                self.x_pos += self.imagesize + 20
            self.x_pos = self.left_margin
            self.y_pos += max_height + 50
        else:
            self.close()
        self.scene.clearSelection()
        self.scene.update()
    
    def getBilddatei(self, actor, sex = None):
        bilddatei = None
        if actor:
            if sex:
                bilddatei = os.path.join(self.verzeichnis_thumbs, "darsteller_" + sex, actor.lower().strip().replace(" ", "_").replace("'", "_apostroph_") + ".jpg")
            else:
                bilddatei = os.path.join(self.verzeichnis_thumbs, "darsteller_" + "w", + actor.lower().strip().replace(" ", "_").replace("'", "_apostroph_") + ".jpg")
                if not os.path.exists(bilddatei):
                    bilddatei = os.path.join(self.verzeichnis_thumbs, "darsteller_" + "m", actor.lower().strip().replace(" ", "_").replace("'", "_apostroph_") + ".jpg")
        if not bilddatei or not os.path.exists(bilddatei):
            bilddatei = os.path.join(self.verzeichnis_thumbs, "nichtvorhanden", "nicht_vorhanden.jpg")
        return bilddatei
    
    def closeEvent(self, event):
        settings = QtCore.QSettings()
        settings.setValue("ShowIafdData/Size", self.size())
        settings.setValue("ShowIafdData/Position", self.pos())
