# -*- coding: iso-8859-1 -*-

'''
    Copyright 2012-2015 HWM
    
    This file is part of PorDB3.

    PorDB3 is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    PorDB3 is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
'''

import os
import urllib.request, urllib.parse, urllib.error
import time
from PyQt4 import QtGui, QtCore

class SaveMovieData(QtGui.QDialog):
    def __init__(self, app, url, text):
        QtGui.QDialog.__init__(self)
        self.app = app
        self.url = url
        self.text = text
        
    def get_data(self):
        # get movie title
        anfang = self.text.find("<h1>")
        if anfang < 0:
            self.app.restoreOverrideCursor()
            message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("This site seams not to be a movie site of the IAFD"))
            return
        ende = self.text.find("</h1>", anfang)
        movie = str(self.text[anfang + 4:ende].strip())
        
        # get alternative titles
        alternatives = []
        anfang = self.text.find("Also Known As", ende)
        if anfang > 0:
            anfang = self.text.find("<dd>", anfang)
            ende = self.text.find("</dd></dl>", anfang)
            print (anfang, ende)
            alternatives = self.text[anfang + 4 : ende].strip().replace("&amp;", "&").split("</dd><dd>")
        
        # get actors and scenes
        scenes = []
        anfang = self.text.find("Scene Breakdowns")
        if anfang < 0:
            scenes = self.get_actors()
        else:
            anfang_scene = self.text.find("Scene ", anfang + 1)
            if anfang_scene < 0:
                self.app.restoreOverrideCursor()
                message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Seams there are no scenes on the IAFD"))
                return
            while True:
                anfang_scene = self.text.find("Scene ", anfang + 1)
                try:
                    zahl = int(self.text[anfang_scene + 6])
                except:
                    break
                ende_scene = self.text.find(". ", anfang_scene + 1)
                if anfang_scene < 0:
                    break
                scene = self.text[anfang_scene : ende_scene].strip()
                anfang = self.text.find(". ", anfang_scene + 1)
                ende = self.text.find("</li>", anfang)
                darsteller = self.text[anfang + 2 : ende].strip()
                scenes.append((scene, darsteller))
            
        return movie, alternatives, scenes
    
    def get_actors(self):
        anfang_actors = self.text.find("<h3>Performers</h3>")
        if anfang_actors < 0:
            self.app.restoreOverrideCursor()
            message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Seams there are no scenes/actors on the IAFD"))
            return
        scenes = []
        # get the actors
        anfang = anfang_actors
        scene = "Scene 0"
        darsteller = ""
        last_anfang_actor = 0
        while True:
            anfang_actor = self.text.find('><br>', anfang + 1)
            if anfang_actor < 0 or anfang_actor < last_anfang_actor:
                break
            last_anfang_actor = anfang_actor
            ende_actor = self.text.find("</a><br>", anfang_actor + 1)
            if darsteller:
                darsteller += ", "
            darsteller += self.text[anfang_actor + 5: ende_actor].strip()
            alias = darsteller.find("(as ")
            if alias > 0:
                darsteller = darsteller[0 : alias].strip()
            anfang = ende_actor + 12
        scenes.append((scene, darsteller))
            
        return scenes
    