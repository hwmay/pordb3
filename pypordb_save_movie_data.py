# -*- coding: iso-8859-1 -*-

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
		anfang = self.text.find("<h2>")
		if anfang < 0:
			self.app.restoreOverrideCursor()
			message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("This site seams not to be a movie site of the IAFD"))
			return
		ende = self.text.find("</h2>", anfang)
		movie = str(self.text[anfang + 4:ende].strip())
		
		# get alternative titles
		alternatives = []
		anfang = self.text.find("Also Known As", ende)
		if anfang > 0:
			anfang = self.text.find("</dt><dd>", anfang)
			ende = self.text.find("</dd></dl>", anfang)
			alternatives = self.text[anfang + 9 : ende].strip().replace("&amp;", "&").split("</dd><dd>")
		
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
		anfang_actresses = self.text.find("<h3>Actresses")
		anfang_actors = self.text.find("<h3>Actors")
		ende_komplett = self.text.find("correct.asp")
		if anfang_actors < 0:
			anfang_actors = len(self.text)
		if anfang_actresses < 0 and anfang_actors < 0:
			self.app.restoreOverrideCursor()
			message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Seams there are no scenes/actors on the IAFD"))
			return
		scenes = []
		# get the actresses
		anfang = anfang_actresses
		scene = "Scene 0"
		darsteller = ""
		while True:
			anfang_actor = self.text.find('.htm">', anfang + 1)
			ende_actor = self.text.find("</a>", anfang_actor + 1)
			if anfang_actor < 0 or anfang_actor > ende_komplett or anfang_actors > 0 and anfang_actor > anfang_actors:
				break
			if darsteller:
				darsteller += ", "
			darsteller += self.text[anfang_actor + 6: ende_actor].strip()
			alias = darsteller.find("(as ")
			if alias > 0:
				darsteller = darsteller[0 : alias].strip()
			anfang = ende_actor
		scenes.append((scene, darsteller))
		# get the actors
		anfang = anfang_actors
		scene = "Scene 0"
		darsteller = ""
		while True:
			anfang_actor = self.text.find('.htm">', anfang + 1)
			ende_actor = self.text.find("</a>", anfang_actor + 1)
			if anfang_actor < 0 or anfang_actor > ende_komplett:
				break
			if darsteller:
				darsteller += ", "
			darsteller += self.text[anfang_actor + 6: ende_actor].strip()
			alias = darsteller.find("(as ")
			if alias > 0:
				darsteller = darsteller[0 : alias].strip()
			anfang = ende_actor
		scenes.append((scene, darsteller))
			
		return scenes
	