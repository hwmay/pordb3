#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    Copyright 2012-2018 HWM
    
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

import sys
import os
import time
import datetime
import platform
import urllib.request, urllib.error, urllib.parse
import socket
from operator import itemgetter
import psycopg2
import subprocess
from PyQt5 import QtGui, QtCore, QtWidgets, QtPrintSupport
from pordb_hauptdialog import Ui_MainWindow as MainWindow

from pypordb_suchen import Suchen
from pypordb_cover import Cover
from pypordb_show_two_images import ShowTwoImages
from pypordb_neu import Neueingabe
from pypordb_dblesen import DBLesen
from pypordb_dbupdate import DBUpdate
from pypordb_original import OriginalErfassen
from pypordb_darsteller_suchen import DarstellerSuchen
from pypordb_darsteller_anzeige_gross import DarstellerAnzeigeGross
from pypordb_actor_details import ActorDetails
from pypordb_darsteller_umbenennen import DarstellerUmbenennen
from pypordb_land import LandBearbeiten
from pypordb_suchbegriffe import SuchbegriffeBearbeiten
from pypordb_suche_video import SucheVideo
from pypordb_historie import Historie
from pypordb_pseudo import PseudonymeBearbeiten
from pypordb_bookmarks import Bookmarks
from pypordb_darstellerdaten_anzeigen import DarstellerdatenAnzeigen
from pypordb_save_movie_data import SaveMovieData
from pypordb_show_iafd_data import ShowIafdData
from pypordb_devices import Devices
from pypordb_update_version import UpdateVersion
from pypordb_mass_change import MassChange
from pypordb_actordata import ActorData
#from pypordb_genericthread import GenericThread            

size = QtCore.QSize(260, 260)
sizeneu = QtCore.QSize(500, 400)
size_neu = QtCore.QSize(130, 130)
size_darsteller = QtCore.QSize(1920, 1080)

DBNAME = "por"

__version__ = "1.10.1"
FILE_VERSION = "https://github.com/hwmay/pordb3/blob/master/version"
IMAGE_FILES = (".jpg", ".jpeg", ".png")

# Make a connection to the database and check to see if it succeeded.
db_host = "localhost"
try:
    conn = psycopg2.connect(database=DBNAME, host=db_host)
except Exception as e:
    print("FATAL PorDB3: Database server not running")
    sys.exit()

def age(dob):
    today = datetime.date.today()
    if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
        return today.year - dob.year - 1
    else:
        return today.year - dob.year
# end of age

class MeinDialog(QtWidgets.QMainWindow, MainWindow):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        
        # Slot für Splitter zum Re-Scalen des Darstellerbildes
        self.splitter.splitterMoved[int, int].connect(self.bildSetzen)
        
        # Slot für Aktivieren von Buttons bei Wechsel des Tabs
        self.tabWidget.currentChanged.connect(self.onTabwechsel)
        
        # Slots einrichten für Bilder
        self.actionNeueingabe.triggered.connect(self.onNeueingabe)
        self.actionDarsteller.triggered.connect(self.onDarsteller)
        self.actionCd.triggered.connect(self.onCD)
        self.actionTitel.triggered.connect(self.onTitel)
        self.actionOriginal.triggered.connect(self.onOriginal)
        self.actionSuche.triggered.connect(self.onSuche)
        self.actionDrucken.triggered.connect(self.onDrucken)
        self.tableWidgetBilder.cellDoubleClicked.connect(self.onKorrektur)
        self.tableWidgetBilderAktuell.cellDoubleClicked.connect(self.onNeuDoubleClick)
        self.tableWidgetBilder.customContextMenuRequested.connect(self.onContexttableWidgetBilder)
        self.tableWidgetBilderAktuell.__class__.dragEnterEvent = self.tableWidgetBilderAktuelldragEnterEvent
        self.tableWidgetBilder.__class__.dropEvent = self.tableWidgetBilderdropEvent
        self.actionDarstellerUebernehmen.triggered.connect(self.onDarstellerUebernehmen)
        self.actionAnzeigenOriginal.triggered.connect(self.onAnzeigenOriginal)
        self.actionAnzeigenTitle.triggered.connect(self.onAnzeigenTitle)
        self.actionSortieren_nach_Darsteller.triggered.connect(self.onSortieren_nach_Darsteller)
        self.actionSortieren_nach_CD.triggered.connect(self.onSortieren_nach_CD)
        self.actionSortieren_nach_Titel.triggered.connect(self.onSortieren_nach_Titel)
        self.actionMassChange.triggered.connect(self.onMassChange)
        self.actionOriginal_umbenennen.triggered.connect(self.onOriginal_umbenennen)
        self.actionOriginal_weitere.triggered.connect(self.onOriginal_weitere)
        self.actionRedoImageChange.triggered.connect(self.onRedoImageChange)
        self.actionSortieren_nach_Original.triggered.connect(self.onSortieren_nach_Original)
        self.actionOriginalIntoClipboard.triggered.connect(self.onOriginalIntoClipboard)
        self.actionCovergross.triggered.connect(self.onCovergross)
        self.tableWidgetBilderAktuell.customContextMenuRequested.connect(self.onContexttableWidgetBilderAktuell)
        self.actionBildLoeschen.triggered.connect(self.onBildLoeschen)
        self.actionFirst.triggered.connect(self.onPageFirst)
        self.actionPrev.triggered.connect(self.onPageUp)
        self.actionNext.triggered.connect(self.onPageDown)
        self.actionLast.triggered.connect(self.onPageLast)
        self.actionUndo.triggered.connect(self.onUndo)
        self.actionOnHelp.triggered.connect(self.onHelp)
        self.pushButtonDir.clicked.connect(self.onDirectoryChange)
        self.pushButtonRefresh.clicked.connect(self.onDirectoryRefresh)
        
        # Slots einrichten für Darsteller
        self.bildAnzeige.clicked.connect(self.onbildAnzeige)
        self.comboBoxSex.currentIndexChanged[int].connect(self.setFocus)
        
        self.pushButtonDarstellerspeichern.clicked.connect(self.onDarstellerspeichern)
        self.pushButtonIAFDholen.clicked.connect(self.onIAFD)
        self.pushButtonIAFDBackground.clicked.connect(self.onIAFDBackground)
        self.pushButtonDarstellerLoeschen.clicked.connect(self.onDarstellerloeschen)
        self.listWidgetDarsteller.customContextMenuRequested.connect(self.onContextDarsteller)
        self.listWidgetDarsteller.itemDoubleClicked.connect(self.onbildAnzeige)
        self.actionAnzeigenPaar.triggered.connect(self.onAnzeigenPaar)
        self.labelBildanzeige.customContextMenuRequested.connect(self.onBildgross)
        self.labelBildanzeige.__class__.dragEnterEvent = self.tableWidgetBilderAktuelldragEnterEvent
        self.labelBildanzeige.__class__.dropEvent = self.labelBildanzeigedropEvent
        self.actionGetUrl.triggered.connect(self.onGetUrl)
        self.actionGoToUrl.triggered.connect(self.onGoToUrl)
        self.actionShowDetails.triggered.connect(self.onShowDetails)
        self.actionBildanzeigegross.triggered.connect(self.onDarstellerGross)
        self.listWidgetFilme.customContextMenuRequested.connect(self.onContextFilm)
        self.actionFilm_zeigen.triggered.connect(self.onFilm_zeigen)
        self.listWidgetFilme.itemDoubleClicked.connect(self.onFilm_zeigen)
        self.listWidgetStatistik.customContextMenuRequested.connect(self.onContextCS)
        self.actionCSZeigen.triggered.connect(self.onCSZeigen)
        self.listWidgetStatistik.itemDoubleClicked.connect(self.onCSZeigen)
        self.pushButtonDarstellerSuchen.clicked.connect(self.onDarstellerSuchen)
        self.pushButtonUmbenennen.clicked.connect(self.onDarstellerUmbenennen)
        self.pushButtonSortPartner.clicked.connect(self.onPartnerSortieren)
        self.pushButtonSort.clicked.connect(self.onFilmeSortieren)
        self.lineEditFilter.textChanged[str].connect(self.onFilmeFilter)
        self.pushButtonPartnerZeigen.clicked.connect(self.onPartnerZeigen)
        self.pushButtonPseudo.clicked.connect(self.onPseudo)
        
        # Slots einrichten für Dateien suchen
        self.pushButtonClear.clicked.connect(self.onClear)
        self.pushButtonSuchen.clicked.connect(self.onSuchen)
        self.pushButtonUebernehmen.clicked.connect(self.onDateinamenUebernehmen)
        self.pushButtonSearchMpg.clicked.connect(self.onSearchMpg)
        self.pushButtonSearchVid.clicked.connect(self.onSearchVid)
        self.pushButtonFilterMpgKatalog.clicked.connect(self.onFilterMpg)
        self.pushButtonFilterVid.clicked.connect(self.onFilterVid)
        self.pushButtonDelete.clicked.connect(self.onDeleteMpgKatalog)
        
        # Slots einrichten für Web
        self.pushButtonVideo.clicked.connect(self.onVideoSuchen)
        self.pushButtonBack.clicked.connect(self.webView.back)
        self.pushButtonForward.clicked.connect(self.webView.forward)
        self.pushButtonIAFD.clicked.connect(self.onIAFDSeite)
        self.pushButtonAbholen.clicked.connect(self.onDarstellerdatenAbholen)
        self.pushButtonMovie.clicked.connect(self.onMovieData)
        self.pushButtonClearURL.clicked.connect(self.onClearURL)
        self.pushButtonUrl.clicked.connect(self.onUrlVerwalten)
        self.pushButtonSearchWebsite.clicked.connect(self.onSearchWebsite)
        self.webView.loadStarted.connect(self.onLoadStarted)
        self.webView.loadFinished.connect(self.onLoadFinished)
        #self.connect(self.webView, QtCore.SIGNAL("linkClicked (const QUrl&)"), self.onLinkClicked)
        self.webView.urlChanged.connect(self.onUrlChanged)
        
        # Slots einrichten für Statistiken
        self.pushButtonCS.clicked.connect(self.onStatistikCS)
        self.pushButtonDarstellerW.clicked.connect(self.onStatistikDarstellerW)
        self.pushButtonDarstellerM.clicked.connect(self.onStatistikDarstellerM)
        self.pushButtonAnzahlClips.clicked.connect(self.onStatistikAnzahlClips)
        self.pushButtonClipsJahr.clicked.connect(self.onStatistikAnzahlClipsJahr)
        
        # Slots einrichten für Tools
        self.pushButtonCheckNewVersion.clicked.connect(self.onCheckNewVersion)
        self.pushButtonSuchbegriffe.clicked.connect(self.onSuchbegriffe)
        self.pushButtonLand.clicked.connect(self.onLand)
        self.pushButtonBackup.clicked.connect(self.onBackup)
        self.pushButtonRestore.clicked.connect(self.onRestore)
        self.pushButtonWartung.clicked.connect(self.onWartung)
        self.pushButtonDateikatalog.toggled.connect(self.frame_Dateikatalog.setVisible)
        self.frame_Dateikatalog.hide()
        self.pushButtonVerwalten.clicked.connect(self.onDevicesVerwalten)
        self.pushButtonStart.clicked.connect(self.onStartScan)
        self.pushButtonDeleteDuplicates.clicked.connect(self.onDeleteDuplicates)
        self.pushButtonDeselect.clicked.connect(self.onDeselect)
        self.pushButtonDeleteDuplicates.setEnabled(False)
        self.pushButtonDeselect.setEnabled(False)
        
        self.initial_run = True
        if self.initial_run:
            bild = QtGui.QPixmap(os.path.join(os.getcwd(), "pypordb", "8027068_splash.png")).scaled(276, 246, QtCore.Qt.KeepAspectRatio)
            splash = QtWidgets.QSplashScreen(bild)
            splash.show()
            zu_lesen = "SELECT * FROM pordb_history ORDER BY time DESC LIMIT 50"
            lese_func = DBLesen(self, zu_lesen)
            res = DBLesen.get_data(lese_func)
            if res:
                werte = []
                werte.append(str(res[-1][-1]))
                zu_erfassen = []
                zu_erfassen.append(["DELETE FROM pordb_history WHERE time < %s", werte])
                update_func = DBUpdate(self, zu_erfassen)
                DBUpdate.update_data(update_func)
            self.verzeichnis = os.path.join(os.curdir, "mpg")
            self.verzeichnis_original = self.verzeichnis
            self.verzeichnis_thumbs = os.path.join(os.curdir, "thumbs_sammlung")
            self.verzeichnis_trash = os.path.join(self.verzeichnis_thumbs, "trash")
            self.verzeichnis_cover = os.path.join(self.verzeichnis_thumbs, "cover")
            self.verzeichnis_tools = None
            settings = QtCore.QSettings()
            window_size = settings.value("MeinDialog/Size", QtCore.QSize(600, 500))
            self.resize(window_size)
            window_position = settings.value("MeinDialog/Position", QtCore.QPoint(0, 0))
            self.move(window_position)
            try:
                self.restoreState(settings.value("MeinDialog/State"))
            except:
                pass
            try:
                self.splitter.restoreState(settings.value("splitter"))
            except:
                pass
            
        # Populate statusbar
        self.anzahl = QtWidgets.QLabel()
        self.statusBar.addPermanentWidget(self.anzahl)
        
        self.mpg_aktuell = QtWidgets.QLabel()
        self.mpg_aktuell.setText(self.tr("Actual volume: "))
        self.statusBar.addPermanentWidget(self.mpg_aktuell)
        
        self.spinBoxAktuell = QtWidgets.QSpinBox()
        self.spinBoxAktuell.setRange(1, 9999)
        self.statusBar.addPermanentWidget(self.spinBoxAktuell)
        self.spinBoxAktuell.valueChanged[int].connect(self.onVidNeuAktualisieren)
        
        self.pushButtonHistorie = QtWidgets.QPushButton()
        self.pushButtonHistorie.setText(QtWidgets.QApplication.translate("Dialog", "Historie", None))
        self.pushButtonHistorie.setToolTip(self.tr("Open search history"))
        self.statusBar.addPermanentWidget(self.pushButtonHistorie)
        self.pushButtonHistorie.clicked.connect(self.onHistorie)
        
        self.labelSeite = QtWidgets.QLabel()
        self.statusBar.addPermanentWidget(self.labelSeite)
        
        # populate toolbar
        self.suchfeld = QtWidgets.QComboBox()
        self.suchfeld.setMinimumWidth(250)
        self.suchfeld.setEditable(True)
        self.suchfeld.setWhatsThis(self.tr("Searching field. By pressing the escape key it will be cleared and gets the focus."))
        self.toolBar.insertWidget(self.actionSuchfeld, self.suchfeld)
        self.toolBar.removeAction(self.actionSuchfeld)
        
        self.toolBar.removeAction(self.actionAnzahlBilder)
        
        self.setWindowTitle("PorDB3")
        if self.initial_run:
            splash.showMessage("Loading history", color = QtGui.QColor("red"))
            app.processEvents()
        self.historie()
        if self.initial_run:
            splash.showMessage("Initializing ...", color = QtGui.QColor("red"))
            for i in os.listdir(os.path.expanduser(os.path.join("~", "tmp"))):
                os.remove(os.path.expanduser(os.path.join("~", "tmp", i)))
            app.processEvents()
        
        self.aktuelle_ausgabe = " "
        self.suche_darsteller = self.suche_cd = self.suche_titel = self.suche_original = self.suche_cs = self.suche_remarks = ""
        self.suche_stars = 0
        self.sucheD_darsteller = self.sucheD_geschlecht = self.sucheD_haar = self.sucheD_nation = self.sucheD_tattoo = self.sucheD_etattoo = self.sucheD_ethnic = ""
        self.sucheD_actor1 = self.sucheD_actor2 = self.sucheD_actor3 = ""
        self.sucheD_ab = ""
        self.sucheD_bis = ""
        
        self.tabWidget.setCurrentIndex(0)
        self.present = True
        self.watched = True
        self.notpresent = True
        self.notwatched = True
        self.bilddarsteller = None
        self.columns = 3.0
        self.tableWidgetBilder.setColumnCount(self.columns)
        self.tableWidgetBilder.setIconSize(size)
        self.letzter_select = ""
        self.letzter_select_komplett = ""
        self.letzter_select_komplett_werte = []
        self.aktuelles_res = []
        self.start_bilder = 0
        self.nationen = []
        self.paarung = []
        self.bilderliste = []
        self.tableWidgetBilderAktuell.clear()
        self.partner = 0
        self.anzeige_komplett = False
        self.angezeigt_komplett = False
        self.url = ""
        self.searchResultsMpg = None
        self.searchResultsVid = None
        self.context_actor_image = False
        self.files_added = ""
        self.forced_image_refresh_done = False
        
        self.pushButtonIAFDBackground.setEnabled(False)
        
        self.updatetimer = QtCore.QTimer()
        self.updatetimer.timeout.connect(self.bilder_aktuell)
        self.updatefrequenz = 1000
        self.updatetimer.start(self.updatefrequenz)
        
        self.tableWidgetBilderAktuell.setColumnCount(1)
        self.tableWidgetBilderAktuell.setIconSize(size_neu)

        self.printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.ScreenResolution)
        self.printer.setOutputFileName(os.path.join(self.verzeichnis_original, "print.pdf"))
        
        zu_lesen = "SELECT cd, partnerw, partnerm, anzahl_bilder, anzahl_spalten FROM pordb_vid_neu"
        lese_func = DBLesen(self, zu_lesen)
        res = DBLesen.get_data(lese_func)
        self.spinBoxAktuell.setValue(res[0][0])
        self.lineEditAnzahlM.setText(str(res[0][2]))
        self.lineEditAnzahlW.setText(str(res[0][1]))
        
        self.spinBoxZeilen = QtWidgets.QSpinBox()
        self.spinBoxZeilen.setRange(1, 99)
        try:
            self.spinBoxZeilen.setValue(res[0][3])
        except:
            self.spinBoxZeilen.setValue(12)
        self.spinBoxZeilen.setToolTip(self.tr("Images per page"))
        self.toolBar.insertWidget(self.actionAnzahlBilder, self.spinBoxZeilen)
        self.spinBoxZeilen.valueChanged[int].connect(self.onAnzahlZeilen)
        
        self.spinBoxSpalten = QtWidgets.QSpinBox()
        self.spinBoxSpalten.setRange(1, 10)
        try:
            self.spinBoxSpalten.setValue(res[0][4])
        except:
            self.spinBoxSpalten.setValue(3)
        self.spinBoxSpalten.setToolTip(self.tr("Columns"))
        self.toolBar.insertWidget(self.actionAnzahlBilder, self.spinBoxSpalten)
        self.spinBoxSpalten.valueChanged[int].connect(self.onAnzahlSpalten)
        
        self.anzahl_bilder = self.spinBoxZeilen.value()
        self.onAnzahlZeilen()
        self.onAnzahlSpalten()
        
        if self.initial_run:
            splash.showMessage("Getting search items", color = QtGui.QColor("red"))
            app.processEvents()
            self.suchbegriffe_lesen()
        
        zu_lesen = "SELECT * FROM information_schema.columns WHERE table_name = %s"
        lese_func = DBLesen(self, zu_lesen, "pordb_vid")
        felder = DBLesen.get_data(lese_func)
        felder.sort(key = lambda x: x[4])
        self.fieldnames_vid = []
        for i in felder:
            x = i[3]
            self.fieldnames_vid.append(x.title())
            
        zu_lesen = "SELECT * FROM information_schema.columns WHERE table_name = %s"
        lese_func = DBLesen(self, zu_lesen, "pordb_mpg_katalog")
        felder = DBLesen.get_data(lese_func)
        felder.sort(key = lambda x: x[4])
        self.fieldnames_mpg = []
        for i in felder:
            x = i[3]
            self.fieldnames_mpg.append(x.title())
        self.fieldnames_mpg.append("MB")
        self.fieldnames_mpg.append("GB")
        self.cumshots = {"f":"Facial", "h":"Handjob", "t":str(self.tr("Tits")), "c":"Creampie", "x":"Analcreampie", "o":"Oralcreampie", "v":str(self.tr("Cunt")), "b":str(self.tr("Belly")), "a":str(self.tr("Ass")), "s":str(self.tr("Others"))}
        self.cumshots_reverse = {"Facial":"f", "Handjob":"h", str(self.tr("Tits")):"t", "Creampie":"c", "Analcreampie":"x", "Oralcreampie":"o", str(self.tr("Cunt")):"v", str(self.tr("Belly")):"b", str(self.tr("Ass")):"a", str(self.tr("Others")):"s"}
        
        if self.initial_run:
            splash.showMessage("Getting device names", color = QtGui.QColor("red"))
            app.processEvents()
            self.device_fuellen()
        
        if self.initial_run: 
            splash.showMessage("Loading IAFD", color = QtGui.QColor("red"))
            app.processEvents()
            seite = None
            try:
                seite = urllib.request.urlopen("http://www.iafd.com/", timeout=10).read()
                
                #if seite:
                    #self.webView.load(QtCore.QUrl("http://www.iafd.com/"))
                #else:
                    #pass
            except (urllib.error.URLError, socket.timeout):
                pass
            
            #TODO: linkclicked funktioniert nicht mehr
            #self.webView.page().setLinkDelegationPolicy(QWebPage.DelegateAllLinks)
            if not seite:
                self.statusBar.showMessage(self.tr("Either your computer is not online or the IAFD is not reachable"))
                
        if self.initial_run:
            splash.showMessage("Ready", color = QtGui.QColor("green"))
            app.processEvents()
            splash.finish(self)
        
        # Get version file from github
        if self.initial_run: 
            self.onCheckNewVersion()
            self.initial_run = False
            
    def setFocus(self, i):
        self.suchfeld.setFocus()
    
    def closeEvent(self, event):
        settings = QtCore.QSettings()
        settings.setValue("MeinDialog/Size", self.size())
        settings.setValue("MeinDialog/Position", self.pos())
        settings.setValue("MeinDialog/State", self.saveState())
        settings.setValue("splitter", self.splitter.saveState())
        self.onDarstellerspeichern(refresh=False)
        
    def bilder_aktuell(self, force = False):
        self.label_akt_verzeichnis.setText(self.verzeichnis)
        dateiliste = os.listdir(self.verzeichnis)
        dateiliste_bereinigt = []
        for i in dateiliste:
            if os.path.splitext(i)[-1].lower() in IMAGE_FILES:
                dateiliste_bereinigt.append(i)
        self.tableWidgetBilderAktuell.setRowCount(len(dateiliste_bereinigt))
        dateiliste_bereinigt.sort()
        if self.bilderliste != dateiliste_bereinigt or force:
            self.updatetimer.stop()
            self.showImages(dateiliste_bereinigt)
            # generic thread
            #self.threadPool = QtCore.QThreadPool()
            #self.threadPool.append(GenericThread(self.showImages, dateiliste_bereinigt))
            #self.disconnect(self, QtCore.SIGNAL("add(QImage, QString, int)"), self.makePixmap)
            #self.connect(self, QtCore.SIGNAL("add(QImage, QString, int)"), self.makePixmap)
            ## signal for finished
            #self.disconnect(self, QtCore.SIGNAL("finished"), self.update_image_files_finished)
            #self.connect(self, QtCore.SIGNAL("finished"), self.update_image_files_finished)
            ## start thread
            #self.threadPool[len(self.threadPool)-1].start()
            
            self.bilderliste = dateiliste_bereinigt[:]
            
    # end of bilder_aktuell
    
    def showImages(self, list_of_image_files):
        zeile = -1
        for i in list_of_image_files:
            bild = QtGui.QImage(os.path.join(self.verzeichnis, i))
            text = i + "\n" + str(QtGui.QImage(bild).width()) + "x" + str(QtGui.QImage(bild).height())
            #self.emit(QtCore.SIGNAL("add(QImage, QString, int)"), bild, text, zeile)
            self.makePixmap(bild, text, zeile)
            zeile += 1
        self.update_image_files_finished()
        #self.emit(QtCore.SIGNAL("finished"))
            
    def makePixmap(self, image, text, zeile):
        pixmap = QtGui.QPixmap()
        pixmap.convertFromImage(image)
        bild = QtGui.QIcon(pixmap.scaled(size_neu, QtCore.Qt.KeepAspectRatio))
        newitem = QtWidgets.QTableWidgetItem(bild, text)
        self.tableWidgetBilderAktuell.setItem(zeile, 1, newitem)
        
    def update_image_files_finished(self):
        self.tableWidgetBilderAktuell.resizeColumnsToContents()
        self.tableWidgetBilderAktuell.resizeRowsToContents()
        self.tableWidgetBilderAktuell.setCurrentCell(0, 0)
        self.updatetimer.start(self.updatefrequenz)
        
    def suchbegriffe_lesen(self):
        zu_lesen = "SELECT * FROM pordb_suchbegriffe"
        lese_func = DBLesen(self, zu_lesen)
        self.suchbegriffe = dict(DBLesen.get_data(lese_func))
        self.suchbegriffe_rekursiv = {}
        for i in self.suchbegriffe:
            self.suchbegriffe_rekursiv[self.suchbegriffe[i]] = i.strip()
        self.suchbegriffe.update(self.suchbegriffe_rekursiv)

    def nation_fuellen(self):
        # Combobox für Nation füllen
        zu_lesen = "SELECT * FROM pordb_iso_land WHERE aktiv = %s ORDER BY land"
        lese_func = DBLesen(self, zu_lesen, "x")
        res = DBLesen.get_data(lese_func)
        self.nationen = []
        self.comboBoxNation.clear()
        for i in res:
            text = '%2s %-50s' % (i[0], i[1])
            bild = os.path.join(os.curdir, "pypordb", i[0] + ".svg")
            icon = QtGui.QIcon()
            icon.addFile(bild, QtCore.QSize(16, 16), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.comboBoxNation.addItem(icon, text)
            self.nationen.append(i[0])
            
    def keyPressEvent(self, event):
        if event.modifiers() & QtCore.Qt.MetaModifier:
            if event.key() == QtCore.Qt.Key_F1:
                self.tabWidget.setCurrentIndex(0)
                self.suchfeld.setFocus()
            elif event.key() == QtCore.Qt.Key_F2:
                self.tabWidget.setCurrentIndex(1)
                self.suchfeld.setFocus()
            elif event.key() == QtCore.Qt.Key_F3:
                self.tabWidget.setCurrentIndex(2)
                self.suchfeld.setFocus()
            elif event.key() == QtCore.Qt.Key_F4:
                self.tabWidget.setCurrentIndex(3)
                self.suchfeld.setFocus()
            elif event.key() == QtCore.Qt.Key_F5:
                self.tabWidget.setCurrentIndex(4)
                self.suchfeld.setFocus()
            elif event.key() == QtCore.Qt.Key_F6:
                self.tabWidget.setCurrentIndex(5)
                self.suchfeld.setFocus()
        elif event.key() == QtCore.Qt.Key_F2:
            self.changeTab("F2")
        elif event.key() == QtCore.Qt.Key_F3:
            self.changeTab("F3")
        elif event.key() == QtCore.Qt.Key_Escape:
            self.suchfeld.setCurrentIndex(-1)
            self.suchfeld.setFocus()
        elif event.key() == QtCore.Qt.Key_PageUp:
            self.onPageUp()
        elif event.key() == QtCore.Qt.Key_PageDown:
            self.onPageDown()
        elif event.key() == QtCore.Qt.Key_Delete:
            self.onBildLoeschen()
        elif event.key() == QtCore.Qt.Key_F12 and self.tabWidget.currentIndex() == 0 and self.aktuelle_ausgabe == "Bilder":
            if self.angezeigt_komplett == False:
                self.anzeige_komplett = True
            else:
                self.anzeige_komplett = False
            self.ausgabe_in_table()
        elif event.key() in (QtCore.Qt.Key_Enter, QtCore.Qt.Key_Return) and self.tabWidget.currentIndex() == 3:
            self.GetWebsite()
        elif event.key() == QtCore.Qt.Key_Z and self.tabWidget.currentIndex() == 3:
            self.webView.back()
        elif event.key() == QtCore.Qt.Key_X and self.tabWidget.currentIndex() == 3:
            self.webView.forward()
        elif event.key() == QtCore.Qt.Key_S and self.tabWidget.currentIndex() == 3:
            self.webView.stop()
        elif event.modifiers() & QtCore.Qt.ControlModifier:
            if event.key() == QtCore.Qt.Key_B:
                self.tabWidget.setCurrentIndex(1)
                self.onbildAnzeige()
                
    def tableWidgetBilderAktuelldragEnterEvent(self, event):
        event.accept()
    
    def tableWidgetBilderdropEvent(self, event):
        if self.aktuelle_ausgabe == "Darsteller":
            return
        items = self.tableWidgetBilderAktuell.selectedItems()
        item = self.tableWidgetBilder.itemAt(event.pos())
        if not item:
            return
        column = self.tableWidgetBilder.column(item)
        row = self.tableWidgetBilder.row(item)
        index = int(row * self.columns + column + self.start_bilder)
        cd = self.aktuelles_res[index][2]
        bild = self.aktuelles_res[index][3]
        dateien = []
        for i in items:
            dateien.append(os.path.join(self.verzeichnis, i.text().split("\n")[0]))
        if len(dateien) > 2:
            QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("You can only drag 1 or 2 pictures"))
            return    
        else:
            bilddatei_alt = os.path.join(self.verzeichnis_thumbs, "cd" + str(cd), bild.rstrip())
            if len(dateien) == 2:
                if os.path.exists(bilddatei_alt):
                    QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("You can only drag 1 picture"))
                    return    
                original = self.aktuelles_res[index][5]
                dialog = Cover(dateien, self.verzeichnis_original, original)
                dialog.exec_()
                datei, original = dialog.datei()
                bilddatei = QtGui.QImage(datei)
                bilddatei_alt = os.path.join(self.verzeichnis_cover, bild.rstrip())
                ext = os.path.splitext(bilddatei_alt)[-1].lower()
                if ext == ".jpeg":
                    ext = "jpg"
                if not os.path.exists(bilddatei_alt):
                    QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("Image to replace does not exist"))
                    return
                os.rename(bilddatei_alt, os.path.join(self.verzeichnis_trash, "pypordb_bildalt" + ext))
            else:
                if os.path.exists(bilddatei_alt):
                    try:
                        os.remove(os.path.join(self.verzeichnis_trash, "pypordb_bildalt.*"))
                    except:
                        pass
                    ext = os.path.splitext(bilddatei_alt)[-1].lower()
                    if ext == ".jpeg":
                        ext = "jpg"
                    os.rename(bilddatei_alt, os.path.join(self.verzeichnis_trash, "pypordb_bildalt" +ext))
                    bilddatei = QtGui.QImage(dateien[0]).scaled(size, QtCore.Qt.KeepAspectRatio)
                else:
                    bilddatei = QtGui.QImage(dateien[0])
                    bilddatei_alt = os.path.join(self.verzeichnis_cover, bild.rstrip())
            
        if bilddatei.save(bilddatei_alt):
            if len(dateien) == 1:
                os.remove(dateien[0])
            else:
                os.remove(datei)
        else:
            QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("Error saving image file"))
            return
            
        self.ausgabe_in_table()
        self.bilder_aktuell()
        self.suchfeld.setFocus()
    # end of tableWidgetBilderdropEvent
    
    def labelBildanzeigedropEvent(self, event):
        items = self.tableWidgetBilderAktuell.selectedItems()
        dateien = []
        for i in items:
            dateien.append(os.path.join(self.verzeichnis, i.text().split("\n")[0]))
        if len(dateien) > 1:
            QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("You can only drag 1 picture"))
            return    
        else:
            name = str(self.labelDarsteller.text()).strip().lstrip("=")
            if not name:
                return
            bild = QtGui.QImage(dateien[0])
            if bild.width() > size_darsteller.width() or bild.height() > size_darsteller.height():
                QtWidgets.QMessageBox.warning(self, self.tr("Caution! "), self.tr("Image of the actor is very big"))
            zu_lesen = "SELECT sex FROM pordb_darsteller WHERE darsteller = %s"
            lese_func = DBLesen(self, zu_lesen, name)
            res = DBLesen.get_data(lese_func)
            extension_new = os.path.splitext(str(dateien[0]))[-1].lower()
            if extension_new == '.jpeg':
                extension_new = '.jpg'
            sex = res[0][0]
            if sex:
                oldfilename = os.path.join(self.verzeichnis_thumbs, "darsteller_" + sex, name.replace(" ", "_").replace("'", "_apostroph_").lower() + ".jpg")
                extension_old = None
                if not os.path.isfile(oldfilename):
                    oldfilename = os.path.join(self.verzeichnis_thumbs, "darsteller_" + sex, name.replace(" ", "_").replace("'", "_apostroph_").lower() + ".png")
                    if os.path.isfile(oldfilename):
                        extension_old = ".png"
                else:
                    extension_old = ".jpg"
                if extension_new != extension_old and os.path.isfile(oldfilename):
                    os.remove(oldfilename)
                oldfilename = os.path.splitext(oldfilename)[0] + extension_new 
                os.rename(dateien[0], oldfilename)
            self.bilder_aktuell()
            self.onbildAnzeige()
                
    def onPageFirst(self):
        self.start_bilder = 0
        if self.aktuelle_ausgabe == "Darsteller":
            self.ausgabedarsteller()
        else:
            self.ausgabe_in_table()
    
    def onPageUp(self):
        self.start_bilder = self.start_bilder - self.anzahl_bilder
        if self.start_bilder > -1:
            if self.aktuelle_ausgabe == "Darsteller":
                self.ausgabedarsteller()
            else:
                self.ausgabe_in_table()
        else:
            self.start_bilder = 0
            if self.aktuelle_ausgabe == "Darsteller":
                self.ausgabedarsteller()
            else:
                self.ausgabe_in_table()
            
    def onPageDown(self):
        self.start_bilder = self.start_bilder + self.anzahl_bilder
        if self.start_bilder < len(self.aktuelles_res):
            if self.aktuelle_ausgabe == "Darsteller":
                self.ausgabedarsteller()
            else:
                self.ausgabe_in_table()
        else:
            self.start_bilder = len(self.aktuelles_res)
            
    def onPageLast(self):
        self.start_bilder = int(len(self.aktuelles_res) / self.anzahl_bilder) * self.anzahl_bilder
        if self.start_bilder == len(self.aktuelles_res):
            self.start_bilder = self.start_bilder - self.anzahl_bilder
        if self.start_bilder > -1:
            if self.aktuelle_ausgabe == "Darsteller":
                self.ausgabedarsteller()
            else:
                self.ausgabe_in_table()
        else:
            self.start_bilder = 0
            if self.aktuelle_ausgabe == "Darsteller":
                self.ausgabedarsteller()
            else:
                self.ausgabe_in_table()
    
    def onNeuDoubleClick(self):
        items = self.tableWidgetBilderAktuell.selectedItems()
        dateien = []
        for i in items:
            dateien.append(os.path.join(self.verzeichnis, i.text().split("\n")[0]))
        self.onNeueingabe(dateien=dateien)
        self.bilder_aktuell()
                
    def onAnzahlZeilen(self):
        if self.columns == float(self.spinBoxZeilen.value()):
            return
        werte = []
        werte.append(str(int(self.spinBoxZeilen.value())))
        zu_erfassen = []
        zu_erfassen.append(["UPDATE pordb_vid_neu SET anzahl_bilder = %s", werte])
        update_func = DBUpdate(self, zu_erfassen)
        DBUpdate.update_data(update_func)
        self.rows = float(self.spinBoxZeilen.value())
        self.tableWidgetBilder.setRowCount(self.rows)
        self.anzahl_bilder = self.rows
        if self.aktuelle_ausgabe == "Darsteller" or not self.letzter_select_komplett:
            self.ausgabedarsteller()
        else:
            if len(self.aktuelles_res) > 0:
                self.ausgabe(self.letzter_select_komplett, self.letzter_select_komplett, self.letzter_select_komplett_werte)
    
    def onAnzahlSpalten(self):
        if self.columns == float(self.spinBoxSpalten.value()):
            return
        werte = []
        werte.append(str(int(self.spinBoxSpalten.value())))
        zu_erfassen = []
        zu_erfassen.append(["UPDATE pordb_vid_neu SET anzahl_spalten = %s", werte])
        update_func = DBUpdate(self, zu_erfassen)
        DBUpdate.update_data(update_func)
        self.columns = float(self.spinBoxSpalten.value())
        self.tableWidgetBilder.setColumnCount(self.columns)
        if self.aktuelle_ausgabe == "Darsteller" or not self.letzter_select_komplett:
            self.ausgabedarsteller()
        else:
            if len(self.aktuelles_res) > 0:
                self.ausgabe(self.letzter_select_komplett, self.letzter_select_komplett, self.letzter_select_komplett_werte)
                
    def onDirectoryChange(self):
        datei = QtWidgets.QFileDialog.getExistingDirectory(self, self.tr("Select directory"), self.verzeichnis)
        if datei:
            self.verzeichnis = str(datei)
            app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
            self.bilder_aktuell()
            app.restoreOverrideCursor()
        self.suchfeld.setFocus()
            
    def onDirectoryRefresh(self):
        self.bilder_aktuell(force = True)
        
    def onHistorie(self):
        historiedialog = Historie()
        historiedialog.exec_()
        zu_lesen = str(historiedialog.zu_lesen)
        werte = str(historiedialog.werte).split(";")
        if zu_lesen and not "pordb_history" in zu_lesen:
            self.start_bilder = 0
            self.letzter_select_komplett = zu_lesen
            self.letzter_select_komplett_werte = werte
            i = zu_lesen.find("ORDER")
            if i > -1:
                self.letzter_select = zu_lesen[: i]
            else:
                self.letzter_select = zu_lesen
            self.ausgabe(zu_lesen, zu_lesen, werte)
        else:
            self.suchfeld.setFocus()
            
    def onVidNeuAktualisieren(self):
        werte = []
        werte.append(str(self.spinBoxAktuell.value()))
        zu_erfassen = []
        zu_erfassen.append(["UPDATE pordb_vid_neu SET cd = %s", werte])
        update_func = DBUpdate(self, zu_erfassen)
        DBUpdate.update_data(update_func)
            
    def changeTab(self, taste):
        if taste == "F3":
            neuer_tab = self.tabWidget.currentIndex() + 1
            if neuer_tab == 6:
                neuer_tab = 0
            self.tabWidget.setCurrentIndex(neuer_tab)
            self.suchfeld.setFocus()
        elif taste == "F2":
            neuer_tab = self.tabWidget.currentIndex() - 1
            if neuer_tab == -1:
                neuer_tab = 5
            self.tabWidget.setCurrentIndex(neuer_tab)
            self.suchfeld.setFocus()
            
    def onContextDarsteller(self, event):
        menu = QtWidgets.QMenu(self.listWidgetDarsteller)
        menu.addAction(self.actionAnzeigenPaar)
        menu.addAction(self.actionBildanzeigegross)
        self.context_actor_image = False
        menu.exec_(self.listWidgetDarsteller.mapToGlobal(event))
            
    def onContextCS(self, event):
        menu = QtWidgets.QMenu(self.listWidgetStatistik)
        menu.addAction(self.actionCSZeigen)
        menu.exec_(self.listWidgetStatistik.mapToGlobal(event))
        
    def onContextFilm(self, event):
        menu = QtWidgets.QMenu(self.listWidgetFilme)
        menu.addAction(self.actionFilm_zeigen)
        menu.exec_(self.listWidgetFilme.mapToGlobal(event))
        
    def onContexttableWidgetBilder(self, event):
        item = self.tableWidgetBilder.currentItem()
        if not item:
            return
        menu = QtWidgets.QMenu(self.tableWidgetBilder)
        if self.aktuelle_ausgabe == "Darsteller":
            menu.addAction(self.actionDarstellerUebernehmen)
            menu.addAction(self.actionBildanzeigegross)
        else:
            menu.addAction(self.actionAnzeigenOriginal)
            menu.addAction(self.actionAnzeigenTitle)
            menu.addAction(self.actionSortieren_nach_Darsteller)
            menu.addAction(self.actionSortieren_nach_CD)
            menu.addAction(self.actionSortieren_nach_Original)
            menu.addAction(self.actionSortieren_nach_Titel)
            menu.addAction(self.actionOriginal_umbenennen)
            menu.addAction(self.actionMassChange)
            menu.addAction(self.actionOriginal_weitere)
            dateiliste = os.listdir(self.verzeichnis_trash)
            for i in dateiliste:
                if os.path.splitext(i)[0] == "pypordb_bildalt":
                    menu.addAction(self.actionRedoImageChange)
                    break
            if item:
                text = str(item.text())
                if "Cover (" in text:
                    menu.addAction(self.actionCovergross)
            menu.addAction(self.actionOriginalIntoClipboard)
        menu.exec_(self.tableWidgetBilder.mapToGlobal(event))
            
    def onContexttableWidgetBilderAktuell(self, event):
        if len(self.bilderliste) > 0:
            menu = QtWidgets.QMenu(self.tableWidgetBilderAktuell)
            menu.addAction(self.actionBildLoeschen)
            menu.exec_(self.tableWidgetBilderAktuell.mapToGlobal(event))
        
    def onDarstellerUebernehmen(self):
        item = self.tableWidgetBilder.currentItem()
        if not item:
            return
        text = item.text().split("\n")
        if text:
            self.suchfeld.insertItem(0, "=" + text[0])
            self.suchfeld.setCurrentIndex(0)
    
    def onBildgross(self, event):
        menu = QtWidgets.QMenu(self.labelBildanzeige)
        menu.addAction(self.actionBildanzeigegross)
        self.context_actor_image = True
        menu.addAction(self.actionShowDetails)
        menu.addAction(self.actionGetUrl)
        menu.addAction(self.actionGoToUrl)
        menu.exec_(self.labelBildanzeige.mapToGlobal(event))
        
    def onAnzeigenPaar(self):
        ein = self.eingabe_auswerten().lstrip("=")
        if not ein:
            return
        name = str(self.labelDarsteller.text()).strip().lstrip("=")
        if name and ein != name:
            if self.comboBoxGeschlecht.currentText() == 'w':
                suchtext = name + ", %" + ein
            else:
                suchtext = ein + ", %" + name
            zu_erfassen = []
            werte = []
            werte.append(ein)
            zu_erfassen.append(["DELETE FROM pordb_darsteller100 WHERE darsteller = %s", werte])
            zu_erfassen.append(["INSERT INTO pordb_darsteller100 (darsteller) VALUES (%s)", werte])
            update_func = DBUpdate(self, zu_erfassen)
            DBUpdate.update_data(update_func)            
            self.suchfeld.insertItem(0, suchtext)
            self.suchfeld.setCurrentIndex(0)
            self.tabWidget.setCurrentIndex(0)
            self.onDarsteller()
            self.listWidgetDarsteller.clearSelection()
        
    def onFilm_zeigen(self):
        selected = self.listWidgetFilme.selectedItems()
        if selected:
            original = "=" + str(selected[0].text()).strip()
            self.suchfeld.insertItem(0, original)
            self.suchfeld.setCurrentIndex(0)
            self.tabWidget.setCurrentIndex(0)
            self.onOriginal()
            self.listWidgetFilme.clearSelection()
        
    def onCSZeigen(self):
        selected = self.listWidgetStatistik.selectedItems()
        if selected:
            cs = str(selected[0].text()).strip()
            cs_found = None
            for i in list(self.cumshots.values()):
                if i in cs:
                    cs_found = self.cumshots_reverse.get(i)
            if cs_found:
                ein = str(self.labelDarsteller.text()).strip().title()
                self.start_bilder = 0
                app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
                eingabe = ein.title()
                werte = []
                zu_lesen = "SELECT * FROM pordb_vid WHERE (darsteller = %s OR darsteller LIKE %s OR darsteller LIKE %s OR darsteller LIKE %s)"
                werte.append(eingabe)
                werte.append(eingabe +",%")
                werte.append("%, " + eingabe + ",%")
                werte.append("%, " + eingabe)
                zu_lesen += " AND cs" +cs_found + " <> %s" 
                werte.append("0")
                if self.actionVid.isChecked():
                    zu_lesen += " AND vorhanden = %s"
                    werte.append("x")
                    self.actionVid.toggle()
                self.letzter_select = zu_lesen
                zu_lesen += " ORDER BY cd, lower(bild), darsteller"
                self.letzter_select_komplett = zu_lesen
                self.letzter_select_komplett_werte = werte
                self.partner = 0
                self.ausgabe(ein, zu_lesen, werte)
                app.restoreOverrideCursor()
        
    def onAnzeigenOriginal(self):
        item = self.tableWidgetBilder.currentItem()
        if not item:
            return
        column = self.tableWidgetBilder.column(item)
        row = self.tableWidgetBilder.row(item)
        index = int(row * self.columns + column + self.start_bilder)
        if self.aktuelles_res[index][5]:
            original = self.aktuelles_res[index][5]
        else:
            original = ""
        if original:
            original = "=" + original
            self.suchfeld.insertItem(0, original)
            self.suchfeld.setCurrentIndex(0)
            self.onOriginal()
            
    def onAnzeigenTitle(self):
        item = self.tableWidgetBilder.currentItem()
        if not item:
            return
        column = self.tableWidgetBilder.column(item)
        row = self.tableWidgetBilder.row(item)
        index = int(row * self.columns + column + self.start_bilder)
        titel = self.aktuelles_res[index][0]
        self.suchfeld.insertItem(0, titel)
        self.suchfeld.setCurrentIndex(0)
        self.onTitel()
            
    def onSortieren_nach_Darsteller(self):
        app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        finde = self.letzter_select_komplett.find("ORDER BY")
        zu_lesen = self.letzter_select_komplett[0:finde] + " ORDER BY darsteller, cd, lower(bild)"
        self.letzter_select_komplett = zu_lesen
        self.ausgabe(zu_lesen, zu_lesen, self.letzter_select_komplett_werte)
        app.restoreOverrideCursor()
        
    def onSortieren_nach_CD(self):
        app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        finde = self.letzter_select_komplett.find("ORDER BY")
        zu_lesen = self.letzter_select_komplett[0:finde] + " ORDER BY cd, darsteller, lower(bild)"
        self.letzter_select_komplett = zu_lesen
        self.ausgabe(zu_lesen, zu_lesen, self.letzter_select_komplett_werte)
        app.restoreOverrideCursor()
        
    def onSortieren_nach_Original(self):
        app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        finde = self.letzter_select_komplett.find("ORDER BY")
        zu_lesen = self.letzter_select_komplett[0:finde] + " ORDER BY original, cd, darsteller, lower(bild)"
        self.letzter_select_komplett = zu_lesen
        self.ausgabe(zu_lesen, zu_lesen, self.letzter_select_komplett_werte)
        app.restoreOverrideCursor()
        
    def onSortieren_nach_Titel(self):
        app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        finde = self.letzter_select_komplett.find("ORDER BY")
        zu_lesen = self.letzter_select_komplett[0:finde] + " ORDER BY lower(titel), cd, darsteller, bild"
        self.letzter_select_komplett = zu_lesen
        self.ausgabe(zu_lesen, zu_lesen, self.letzter_select_komplett_werte)
        app.restoreOverrideCursor()
        
    def onOriginal_umbenennen(self):
        item = self.tableWidgetBilder.currentItem()
        if not item:
            return
        column = self.tableWidgetBilder.column(item)
        row = self.tableWidgetBilder.row(item)
        index = int(row * self.columns + column + self.start_bilder)
        if self.aktuelles_res[index][5]:
            original = self.aktuelles_res[index][5]
        else:
            original = ""
        if not original:
            QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("There is no original title: cannot be renamed"))
            app.restoreOverrideCursor()
            return
        umbenennen = DarstellerUmbenennen(original)
        if umbenennen.exec_():
            neuer_name = str(umbenennen.lineEditNeuerName.text())
            if neuer_name:
                app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
                werte = []
                werte.append(neuer_name.title())
                werte.append(original)
                zu_erfassen = []
                zu_erfassen.append(["UPDATE pordb_vid SET original = %s WHERE original = %s", werte])
                update_func = DBUpdate(self, zu_erfassen)
                DBUpdate.update_data(update_func)
                zu_lesen = "SELECT * FROM pordb_vid WHERE original = %s ORDER BY original, cd, lower(bild), darsteller"
                werte = []
                werte.append(neuer_name.title())
                self.letzter_select_komplett = zu_lesen
                self.letzter_select_komplett_werte = werte
                self.start_bilder = 0
                self.partner = 0
                self.ausgabe(zu_lesen, zu_lesen, werte)
                app.restoreOverrideCursor()
                
        self.suchfeld.setFocus()
        
    def onMassChange(self):
        masschangedialog = MassChange()
        masschangedialog.exec_()
        vorhanden = masschangedialog.vorhanden
        if vorhanden:
            vorhanden = "x"
        else:
            vorhanden = " "
        watched = masschangedialog.watched
        if watched:
            watched = "x"
        else:
            watched = " "
        items = self.tableWidgetBilder.selectedItems()
        zu_erfassen = []
        for i in items:
            column = self.tableWidgetBilder.column(i)
            row = self.tableWidgetBilder.row(i)
            index = int(row * self.columns + column + self.start_bilder)
            werte = []
            werte.append(vorhanden)
            werte.append(watched)
            if masschangedialog.resolution:
                werte.append(masschangedialog.resolution)
            else:
                werte.append(None)            
            werte.append(str(self.aktuelles_res[index][2]))
            werte.append(self.aktuelles_res[index][3])
            zu_erfassen.append(["UPDATE pordb_vid SET vorhanden = %s, gesehen = %s, hd = %s WHERE cd = %s AND bild = %s", werte])
        if zu_erfassen:
            update_func = DBUpdate(self, zu_erfassen)
            DBUpdate.update_data(update_func)
            self.ausgabe("", self.letzter_select_komplett, self.letzter_select_komplett_werte)
        self.bilder_aktuell()
        self.suchfeld.setFocus()
                
    def onOriginal_weitere(self):
        item = self.tableWidgetBilder.currentItem()
        if not item:
            return
        column = self.tableWidgetBilder.column(item)
        row = self.tableWidgetBilder.row(item)
        index = int(row * self.columns + column + self.start_bilder)
        if self.aktuelles_res[index][5]:
            original = self.aktuelles_res[index][5]
        else:
            original = ""
        if not original:
            QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("Movie has no original title"))
            app.restoreOverrideCursor()
            return
        zu_lesen = "SELECT primkey FROM pordb_vid WHERE original = %s"
        lese_func = DBLesen(self, zu_lesen, str(original))
        res_primkey = DBLesen.get_data(lese_func)
        for i in res_primkey:
            zu_lesen = "SELECT original FROM pordb_original WHERE foreign_key_pordb_vid = %s"
            lese_func = DBLesen(self, zu_lesen, str(i[0]))
            res = DBLesen.get_data(lese_func)
            if res:
                break
        original_vorhanden = []
        for i in res:
            original_vorhanden.append(i[0])
        if res:
            originaldialog = OriginalErfassen(original_vorhanden)
        else:
            originaldialog = OriginalErfassen()
        originaldialog.exec_()
        original_weitere = []
        try:
            original_weitere = originaldialog.original
        except:
            pass
        
        if original_weitere:
            zu_erfassen = []
            for i in res_primkey:
                werte = []
                werte.append(str(i[0]))
                zu_erfassen.append(["DELETE FROM pordb_original WHERE foreign_key_pordb_vid = %s", werte])
            
                for j in original_weitere:
                    if j:
                        werte = []
                        werte.append(j.decode())
                        werte.append(str(i[0]))
                        zu_erfassen.append(["INSERT INTO pordb_original (original, foreign_key_pordb_vid) VALUES (%s, %s)", werte])
                        
            update_func = DBUpdate(self, zu_erfassen)
            DBUpdate.update_data(update_func)
            self.ausgabe("", self.letzter_select_komplett, self.letzter_select_komplett_werte)
                        
        self.suchfeld.setFocus()
    # end of onOriginal_weitere
        
    def onRedoImageChange(self):
        item = self.tableWidgetBilder.currentItem()
        if not item:
            return
        column = self.tableWidgetBilder.column(item)
        row = self.tableWidgetBilder.row(item)
        index = int(row * self.columns + column + self.start_bilder)
        cd = self.aktuelles_res[index][2]
        bild = self.aktuelles_res[index][3]
        dateiliste = os.listdir(self.verzeichnis_trash)
        if not dateiliste:
            return
        bilddatei_trash = None
        for i in dateiliste:
            if os.path.splitext(i)[0] == "pypordb_bildalt":
                bilddatei_trash = os.path.join(self.verzeichnis_trash, i)
                break
        bilddatei_neu = os.path.join(self.verzeichnis_thumbs, "cd" +str(cd), bild.rstrip())
        if not os.path.exists(bilddatei_neu):
            bilddatei_neu = os.path.join(self.verzeichnis_cover, bild.rstrip())
        if bilddatei_trash and os.path.exists(bilddatei_neu):
            messageBox = QtWidgets.QMessageBox()
            messageBox.addButton(self.tr("Image restore"), QtWidgets.QMessageBox.AcceptRole)
            messageBox.addButton(self.tr("Cancel"), QtWidgets.QMessageBox.RejectRole)
            messageBox.setWindowTitle(self.tr("Image restore ") +os.path.basename(bilddatei_neu))
            messageBox.setIcon(QtWidgets.QMessageBox.Question)
            messageBox.setText(self.tr("Do you want to restore the image?"))
            message = messageBox.exec_()
            if message == 0:
                os.rename(bilddatei_trash, bilddatei_neu)
            
        self.ausgabe_in_table()
        self.bilder_aktuell()
        self.suchfeld.setFocus()
        
    def onOriginalIntoClipboard(self):
        item = self.tableWidgetBilder.currentItem()
        if not item:
            return
        column = self.tableWidgetBilder.column(item)
        row = self.tableWidgetBilder.row(item)
        index = int(row * self.columns + column + self.start_bilder)
        if self.aktuelles_res[index][5]:
            original = self.aktuelles_res[index][5]
        else:
            original = ""
        if item:
            werte = []
            werte.append(original)
            zu_erfassen = []
            zu_erfassen.append(["UPDATE pordb_vid_neu SET original = %s", werte])
            update_func = DBUpdate(self, zu_erfassen)
            DBUpdate.update_data(update_func)
            self.statusBar.showMessage('"' +original +'"' +self.tr(" transferred into clipboard"))
        self.suchfeld.setFocus()
        
    def onCovergross(self):
        item = self.tableWidgetBilder.currentItem()
        column = self.tableWidgetBilder.column(item)
        row = self.tableWidgetBilder.row(item)
        index = int(row * self.columns + column + self.start_bilder)
        cover = os.path.join(self.verzeichnis_cover, self.aktuelles_res[index][3].strip())
        if os.path.exists(cover):
            bilddialog = DarstellerAnzeigeGross(cover)
            bilddialog.exec_()
        self.suchfeld.setFocus()
        
    def onBildLoeschen(self):
        items = self.tableWidgetBilderAktuell.selectedItems()
        self.updatetimer.stop()
        for i in items:
            text = str(i.text().split("\n")[0])
            bilddatei = os.path.join(self.verzeichnis, text) 
            try:
                os.remove(bilddatei)
            except:
                pass
        self.bilder_aktuell()
        self.suchfeld.setFocus()
        self.updatetimer.start(self.updatefrequenz)
        
    def onCover(self, datei = None):
        cover = []
        j = 0
        if not datei:
            dateiliste = os.listdir(self.verzeichnis_original)
            for i in dateiliste:
                if os.path.splitext(i)[-1].lower() in IMAGE_FILES:
                    cover.append(os.path.join(self.verzeichnis_original, i))
                    j += 1
                    if j == 2:    # es werden nur 2 Bilddateien akzeptiert
                        break
        else:
            cover = datei
        if cover:
            dialog = Cover(cover, self.verzeichnis_original)
            dialog.exec_()
            datei, originaldatei = dialog.datei()
            if datei:
                self.onNeueingabe(dateien = datei, cover_anlegen = 1, original = originaldatei)
            else:
                self.file = None
        self.suchfeld.setFocus()
        
    def onDrucken(self):
        def paint_action():
            painter = QtGui.QPainter(self.printer)
            x = 30
            y = 0
            seite = 1
            if self.tabWidget.currentIndex() == 0:
                if self.partner:
                    painter.drawText(x + 300, y, "- " +str(seite) +" -")
                    y += 15
                    verzeichnis_m = os.path.join(self.verzeichnis_thumbs, "darsteller_m")
                    verzeichnis_w = os.path.join(self.verzeichnis_thumbs, "darsteller_w")
                    randunten = 50
                    for i in self.aktuelles_res:
                        if i[-1] == ")":
                            anfang = i.rfind("(")
                        else:
                            anfang = len(i)
                        name = i[0 : anfang]
                        filename = os.path.join(verzeichnis_w, name.strip().lower().replace(" ", "_").replace("'", "_apostroph_") + ".jpg")
                        if not os.path.exists(filename):
                            filename = os.path.join(verzeichnis_m, name.strip().lower().replace(" ", "_").replace("'", "_apostroph_") + ".jpg")
                        if not os.path.exists(filename):
                            filename = os.path.join(self.verzeichnis_thumbs, "nichtvorhanden", "nicht_vorhanden.jpg")
                        bild = QtGui.QPixmap(filename).scaled(size, QtCore.Qt.KeepAspectRatio)
                        if y + bild.height() + randunten > self.printer.pageRect().height():
                            y = 0
                            self.printer.newPage()
                            seite += 1
                            painter.drawText(x + 300, y, "- " +str(seite) +" -")
                            y += 15
                        painter.drawPixmap(x, y, bild)
                        y += 12 + bild.height()
                        painter.drawText(x, y, i)
                        y += 15
                    app.restoreOverrideCursor()
                    return
                else:
                    res = self.aktuelles_res
                    if self.actionCheckBoxDVDCover.isChecked():
                        zw_res = []
                        for i in res:
                            dateiname = os.path.join(self.verzeichnis_cover, i[3].strip())
                            if os.path.exists(dateiname):
                                zw_res.append(i)
                        res = zw_res
                painter.drawText(x + 300, y, "- " +str(seite) +" -")
                y += 15
                for i in res:
                    if self.aktuelle_ausgabe == "Darsteller":
                        sex = str(self.letzter_select_komplett)[str(self.letzter_select_komplett).find("sex") + 7]
                        filename = os.path.join(self.verzeichnis_thumbs, "darsteller_" + sex, i[0].strip().lower().replace(" ", "_") + ".jpg")
                    else:
                        filename = os.path.join(self.verzeichnis_thumbs, "cd" + str(i[2]), i[3].strip())
                        if not os.path.exists(filename):
                            filename = os.path.join(self.verzeichnis_cover, + i[3].strip())
                    bild = QtGui.QPixmap(filename)
                    if bild.height() > self.printer.pageRect().height() - 60 or bild.width() > self.printer.pageRect().width() - 60:
                        bild = QtGui.QPixmap(bild).scaled(self.printer.pageRect().width() - 60, self.printer.pageRect().height() - 60, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
                    if bild.width() > 270:
                        randunten = 220
                    else:
                        randunten = 50
                    if y + bild.height() + randunten > self.printer.pageRect().height():
                        y = 0
                        self.printer.newPage()
                        seite += 1
                        painter.drawText(x + 300, y, "- " +str(seite) +" -")
                        y += 15
                    painter.drawPixmap(x, y, bild)
                    y += 12 + bild.height()
                    if self.aktuelle_ausgabe == "Darsteller":
                        painter.drawText(x, y, i[0])
                        y += 15
                        painter.drawText(x, y, self.tr("Count: ") +str(i[2]))
                        y += 15
                        if i[5]:
                            painter.drawText(x, y, "Nation: " +i[5])
                        else:
                            painter.drawText(x, y, "Nation: n.a." )
                        y += 15
                        if i[6]:
                            for j in range(round(len(i[6]) / 90 + 1), 0):
                                if j == 0:
                                    painter.drawText(x, y, "Tattoo: " + i[6][0 : 90])
                                else:
                                    y += 15
                                    painter.drawText(x, y, i[6][j * 90 : j * 90 + 90])
                        else:
                            painter.drawText(x, y, "Tattoo: -" )
                        y += 15
                        painter.drawText(x, y, "Partner: " +str(i[8]))
                    else:
                        painter.drawText(x, y, self.tr("Title: ") +i[0])
                        y += 15
                        painter.drawText(x, y, self.tr("Actor: ") +i[1])
                        y += 15
                        painter.drawText(x, y, "CD: " +str(i[2]))
                        y += 15
                        painter.drawText(x, y, self.tr("Image: ") +i[3])
                        y += 15
                        painter.drawText(x, y, self.tr("watched: ") +i[4])
                        y += 15
                        if i[5]:
                            painter.drawText(x, y, "Original: " +i[5])
                        else:
                            painter.drawText(x, y, "Original: ")
                        y += 15
                        painter.drawText(x, y, "CS: ")
                        x += 25
                        if i[9]:
                            painter.drawText(x, y, str(i[9]) + "f")
                            x += 25
                        if i[10]:
                            painter.drawText(x, y, str(i[10]) + "h")
                            x += 25
                        if i[11]:
                            painter.drawText(x, y, str(i[11]) + "t")
                            x += 25
                        if i[12]:
                            painter.drawText(x, y, str(i[12]) + "c")
                            x += 25
                        if i[13]:
                            painter.drawText(x, y, str(i[13]) + "x")
                            x += 25
                        if i[14]:
                            painter.drawText(x, y, str(i[14]) + "o")
                            x += 25
                        if i[15]:
                            painter.drawText(x, y, str(i[15]) + "v")
                            x += 25
                        if i[16]:
                            painter.drawText(x, y, str(i[16]) + "b")
                            x += 25
                        if i[17]:
                            painter.drawText(x, y, str(i[17]) + "a")
                            x += 25
                        if i[18]:
                            painter.drawText(x, y, str(i[18]) + "s")
                            x += 25                            
                        x = 30
                        y += 15
                        if i[7]:
                            painter.drawText(x, y, self.tr("available: ") +i[7])
                        else:
                            painter.drawText(x, y, self.tr("available: "))
                        if i[21]:
                            y += 15
                            painter.drawText(x, y, self.tr("Remarks: ") + i[21])
                        if i[22]:
                            y += 15
                            painter.drawText(x, y, self.tr("Rating: ") + i[22] * "*")                            
                    y += 20
                    painter.drawLine(x, y, x + 600, y)
                    y += 20
                app.restoreOverrideCursor()
                painter.end()
            elif self.tabWidget.currentIndex() == 1:
                name = str(self.labelDarsteller.text()).strip().lstrip("=")
                if name:
                    painter.drawText(x + 300, y, "- " +str(seite) +" -")
                    y += 15
                    painter.drawText(x, y, name)
                    y += 15
                    filename = os.path.join(self.verzeichnis_thumbs, "darsteller_w", name.strip().lower().replace(" ", "_").replace("'", "_apostroph_") + ".jpg")
                    if not os.path.exists(filename):
                        filename = os.path.join(self.verzeichnis_thumbs, "darsteller_m", name.strip().lower().replace(" ", "_").replace("'", "_apostroph_") + ".jpg")
                    bild = QtGui.QPixmap(filename)
                    if bild.height() > self.printer.pageRect().height() - 60 or bild.width() > self.printer.pageRect().width() - 60:
                        bild = QtGui.QPixmap(bild).scaled(self.printer.pageRect().width() - 60, self.printer.pageRect().height() - 60, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
                    painter.drawPixmap(x, y, bild)
                    y += 15 + bild.height()
                    if y > self.printer.pageRect().height():
                        y = 0
                        self.printer.newPage()
                        seite += 1
                        painter.drawText(x + 300, y, "- " +str(seite) +" -")
                        y += 15
                    painter.drawLine(x, y, x + 600, y)
                    y += 15
                    if y + 15 > self.printer.pageRect().height():
                        y = 0
                        self.printer.newPage()
                        seite += 1
                        painter.drawText(x + 300, y, "- " +str(seite) +" -")
                        y += 15
                        
                    painter.drawText(x, y, self.tr("Statistics"))
                    y += 10
                    painter.drawLine(x, y, x + 60, y)
                    for i in range(self.listWidgetStatistik.count()):
                        y += 15
                        if y > self.printer.pageRect().height():
                            y = 0
                            self.printer.newPage()
                            seite += 1
                            painter.drawText(x + 300, y, "- " +str(seite) +" -")
                            y += 15
                        texte = str(self.listWidgetStatistik.item(i).text()).split()
                        if len(texte) == 3:
                          painter.drawText(x, y, texte[0].strip())
                          x += 100
                          painter.drawText(x, y, texte[1].strip())
                          x += 30
                          painter.drawText(x, y, texte[2].strip())
                          x = 30
                        else:
                          painter.drawText(x, y, str(self.listWidgetStatistik.item(i).text()).strip())
                    y += 15
                    if y > self.printer.pageRect().height():
                        y = 0
                        self.printer.newPage()
                        seite += 1
                        painter.drawText(x + 300, y, "- " +str(seite) +" -")
                        y += 15
                    painter.drawLine(x, y, x + 600, y)
                    y += 15
                    if y + 15 > self.printer.pageRect().height():
                        y = 0
                        self.printer.newPage()
                        seite += 1
                        painter.drawText(x + 300, y, "- " +str(seite) +" -")
                        y += 15
                        
                    painter.drawText(x, y, "Partner (" +str(len(self.paarung)) +")")
                    y += 10
                    painter.drawLine(x, y, x + 60, y)
                    for i in range(self.listWidgetDarsteller.count()):
                        y += 15
                        if y > self.printer.pageRect().height():
                            y = 0
                            self.printer.newPage()
                            seite += 1
                            painter.drawText(x + 300, y, "- " +str(seite) +" -")
                            y += 15
                        painter.drawText(x, y, str(self.listWidgetDarsteller.item(i).text()).strip())
                    y += 15
                    if y > self.printer.pageRect().height():
                        y = 0
                        self.printer.newPage()
                        seite += 1
                        painter.drawText(x + 300, y, "- " +str(seite) +" -")
                        y += 15
                    painter.drawLine(x, y, x + 600, y)
                    y += 15
                    if y + 15 > self.printer.pageRect().height():
                        y = 0
                        self.printer.newPage()
                        seite += 1
                        painter.drawText(x + 300, y, "- " +str(seite) +" -")
                        y += 15
                        
                    painter.drawText(x, y, self.tr("Movies (") +str(self.listWidgetFilme.count()) +")")
                    y += 10
                    painter.drawLine(x, y, x + 60, y)
                    for i in range(self.listWidgetFilme.count()):
                        y += 15
                        if y > self.printer.pageRect().height():
                            y = 0
                            self.printer.newPage()
                            seite += 1
                            painter.drawText(x + 300, y, "- " +str(seite) +" -")
                            y += 15
                        painter.drawText(x, y, str(self.listWidgetFilme.item(i).text()).strip())
                    app.restoreOverrideCursor()
                    painter.end()
            elif self.tabWidget.currentIndex() == 2:
                painter.drawText(x + 100, y, "- " +str(seite) +" -")
                y += 15
                painter.drawText(x, y, self.tr("Search term: ") +self.lineEditSuchen.text())
                y += 15
                painter.drawText(x, y, "In mpg_katalog: " +"_" *90)
                y += 15
                columns = self.tableWidget.columnCount()
                rows = self.tableWidget.rowCount()
                for i in range(rows):
                    for j in range(columns):
                        y += 15
                        if y > self.printer.pageRect().height():
                            y = 0
                            self.printer.newPage()
                            seite += 1
                            painter.drawText(x + 100, y, "- " +str(seite) +" -")
                            y += 15
                        try:
                            text = self.tableWidget.item(i, j).text()
                        except:
                            text = " "
                        painter.drawText(x, y, text)
                        
                y += 15
                painter.drawText(x, y, "In vid: " +"_" *90)
                y += 15
                        
                columns = self.tableWidget1.columnCount()
                rows = self.tableWidget1.rowCount()
                for i in range(rows):
                    for j in range(columns):
                        y += 15
                        if y > self.printer.pageRect().height():
                            y = 0
                            self.printer.newPage()
                            seite += 1
                            painter.drawText(x + 100, y, "- " +str(seite) +" -")
                            y += 15
                        try:
                            text = self.tableWidget1.item(i, j).text()
                        except:
                            pass
                        painter.drawText(x, y, text)
                        
                app.restoreOverrideCursor()
                self.suchfeld.setFocus()
                painter.end()
                return
            elif self.tabWidget.currentIndex() == 3:
                painter.end()
                self.webView.print_(self.printer)
                app.restoreOverrideCursor()
            else:
                app.restoreOverrideCursor()
                self.suchfeld.setFocus()
                return
        # end of paint_action
        
        app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        
        self.preview = QtPrintSupport.QPrintPreviewDialog(self.printer)
        self.preview.paintRequested.connect(paint_action)
        self.suchfeld.setFocus()
        if not self.preview.exec_():
            app.restoreOverrideCursor()
            return
        
    def onDarstellerGross(self):
        if self.tabWidget.currentIndex() == 0:
            self.onDarstellerUebernehmen()
            ein = self.eingabe_auswerten().lstrip("=")
        else:
            if self.context_actor_image:
                ein = str(self.labelDarsteller.text()).strip().title()
            else:
                selected = self.listWidgetDarsteller.selectedItems()
                if selected:
                    ein = str(selected[0].text()).strip()
                    ein = ein.split("(")[0]
                else:
                    ein = str(self.labelDarsteller.text()).strip().title()
        
        self.listWidgetDarsteller.clearSelection()
        if ein:
            bildname = ein.lower().strip().replace(" ", "_").replace("'", "_apostroph_")
            self.bilddarsteller = os.path.join(self.verzeichnis_thumbs, "darsteller_w", bildname + ".jpg")
            if not os.path.isfile(self.bilddarsteller):
                self.bilddarsteller = os.path.join(self.verzeichnis_thumbs, "darsteller_w", bildname + ".png")
                if not os.path.isfile(self.bilddarsteller):
                    self.bilddarsteller = os.path.join(self.verzeichnis_thumbs, "darsteller_m", bildname + ".jpg")
                    if not os.path.isfile(self.bilddarsteller):
                        self.bilddarsteller = os.path.join(self.verzeichnis_thumbs, "darsteller_m", bildname + ".png")
                        if not os.path.isfile(self.bilddarsteller):
                            self.bilddarsteller = os.path.join(self.verzeichnis_thumbs, "nichtvorhanden", "nicht_vorhanden.jpg")
            bilddialog = DarstellerAnzeigeGross(self.bilddarsteller)
            bilddialog.exec_()
        self.suchfeld.setFocus()
        
    def onShowDetails(self):
        ein = str(self.labelDarsteller.text()).strip().title()
        dialog = ActorDetails(ein, self.verzeichnis_thumbs)
        dialog.exec_()
        self.onbildAnzeige()
        self.suchfeld.setFocus()
        
    def onGetUrl(self):
        ein = str(self.labelDarsteller.text()).strip().title()
        if ein:
            zu_lesen = "SELECT url FROM pordb_darsteller WHERE darsteller = %s"
            lese_func = DBLesen(self, zu_lesen, ein)
            res = DBLesen.get_data(lese_func)
            if res[0][0]:
                clipboard = QtWidgets.QApplication.clipboard()
                clipboard.setText(res[0][0])
        self.suchfeld.setFocus()
        
    def onGoToUrl(self):
        ein = str(self.labelDarsteller.text()).strip().title()
        if ein:
            zu_lesen = "SELECT url FROM pordb_darsteller WHERE darsteller = %s"
            lese_func = DBLesen(self, zu_lesen, ein)
            res = DBLesen.get_data(lese_func)
            if res[0][0] and res[0][0] != "0":
                self.lineEditURL.setText(res[0][0])
                self.GetWebsite()
                self.tabWidget.setCurrentIndex(3)
            else:
                clipboard = QtWidgets.QApplication.clipboard()
                clipboard.setText(ein.lstrip("="))
                self.tabWidget.setCurrentIndex(3)
        self.suchfeld.setFocus()
        
    def video_anzeigen(self, titel):
        suchendialog = SucheVideo(app, titel)
        suchendialog.exec_()
        app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        zu_lesen, werte = suchendialog.zu_lesen, suchendialog.werte
        if zu_lesen:
            self.start_bilder = 0
            self.partner = 0
            self.ausgabe(zu_lesen, zu_lesen, werte)
            self.letzter_select_komplett = zu_lesen
            self.letzter_select_komplett_werte = werte
        app.restoreOverrideCursor()
        self.suchfeld.setFocus()
        
    def onDarsteller(self):
        # Darsteller in pordb_vid suchen und anzeigen
        self.start_bilder = 0
        try:
            ein = str(self.suchfeld.currentText()).title().strip()
        except:
            QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("Seems to be an invalid character in the search field"))
            return
        if not ein or ein == "=":
            return
        app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        vorname = False
        if ein.find("=") == 0:
            vorname = True
            eingabe = ein.lstrip("=")
        else:
            eingabe = ein
        werte = []
        if vorname:
            zu_lesen = "SELECT * FROM pordb_vid WHERE (darsteller = %s OR darsteller LIKE %s OR darsteller LIKE %s OR darsteller LIKE %s)"
            werte.append(eingabe)
            werte.append(eingabe + ",%")
            werte.append("%, " + eingabe + ",%")
            werte.append("%, " + eingabe)
        else:
            zu_lesen = "SELECT * FROM pordb_vid WHERE darsteller LIKE %s"
            werte.append("%" + eingabe + "%")
        if self.actionVid.isChecked():
            zu_lesen += " AND vorhanden = %s"
            werte.append("x")
            self.actionVid.toggle()
        self.letzter_select = zu_lesen
        zu_lesen += " ORDER BY cd, lower(bild), darsteller"
        self.letzter_select_komplett = zu_lesen
        self.letzter_select_komplett_werte = werte
        self.partner = 0
        self.ausgabe(ein, zu_lesen, werte)
        app.restoreOverrideCursor()

    def onCD(self):
        # CD in pordb_vid suchen und anzeigen
        self.start_bilder = 0
        try:
            ein = int(self.suchfeld.currentText())
        except:
            QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("CD is not a number"))
            return
        app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        werte = []
        zu_lesen = "SELECT * FROM pordb_vid WHERE cd = %s"
        werte.append(str(ein))
        if self.actionVid.isChecked():
            zu_lesen += " AND vorhanden = %s"
            werte.append("x")
            self.actionVid.toggle()
        self.letzter_select = zu_lesen
        zu_lesen += " ORDER BY lower(bild), darsteller"
        self.letzter_select_komplett = zu_lesen
        self.letzter_select_komplett_werte = werte
        self.partner = 0
        self.ausgabe(str(ein), zu_lesen, werte)
        app.restoreOverrideCursor()
            
    def onTitel(self):
        # nach Titel in pordb_vid suchen und anzeigen
        self.start_bilder = 0
        try:
            ein = str(self.suchfeld.currentText()).lower().strip()
        except:
            QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("Seems to be an invalid character in the search field"))
            return
        if not ein:
            return
        app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        werte = []
        zu_lesen = "SELECT * FROM pordb_vid WHERE LOWER(titel) LIKE %s"
        werte.append("%" + ein.replace(" ", "%") +"%")
        if self.actionVid.isChecked():
            zu_lesen += " AND vorhanden = %s"
            werte.append("x")
            self.actionVid.toggle()
        self.letzter_select = zu_lesen
        zu_lesen += " ORDER BY cd, lower(bild), darsteller"
        self.letzter_select_komplett = zu_lesen
        self.letzter_select_komplett_werte = werte
        self.partner = 0
        self.ausgabe(ein, zu_lesen, werte)
        app.restoreOverrideCursor()
            
    def onOriginal(self):
        # nach Originaltitel in pordb_vid suchen und anzeigen
        self.start_bilder = 0
        try:
            ein = str(self.suchfeld.currentText()).replace("#","").lower().strip()
        except:
            QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("Seems to be an invalid character in the search field"))
            return
        if not ein or ein == "=":
            return
        ein2 = str(self.suchfeld.currentText()).replace("#","").title().strip()
        ein3 = str(self.suchfeld.currentText()).replace("#","").lower().strip()
        app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        werte = []
        if ein[0] == "=":
            zu_lesen = "SELECT * FROM pordb_original WHERE (LOWER(original) LIKE %s OR original LIKE %s)"
            werte.append(ein3[1:] + " %")
            werte.append(ein2[1:] + " %")
        else:
            zu_lesen = "SELECT * FROM pordb_original WHERE (LOWER(original) LIKE %s OR original LIKE %s)"
            werte.append("%" + ein3.replace(" ", "%") + "%")
            werte.append("%" + ein2.replace(" ", "%") + "%")
        lese_func = DBLesen(self, zu_lesen, werte)
        res = DBLesen.get_data(lese_func)
        werte = []
        if ein[0] == "=":
            zu_lesen = "SELECT * FROM pordb_vid WHERE (LOWER(original) = %s OR original LIKE %s"
            werte.append(ein3[1:])
            werte.append(ein2[1:] + " %")
        else:
            zu_lesen = "SELECT * FROM pordb_vid WHERE (LOWER(original) LIKE %s OR original LIKE %s"
            werte.append("%" + ein3.replace(" ", "%") + "%")
            werte.append("%" + ein2.replace(" ", "%") + "%")
        for i in self.suchbegriffe:
                suchbegriff = i.lower().strip()
                if suchbegriff:
                    for j, wert in enumerate(werte):
                        wert_lower = wert.lower()
                        if suchbegriff in wert_lower:
                            if suchbegriff == "-":
                                neuer_wert = wert_lower.replace(suchbegriff, " ").title()
                            else:
                                neuer_wert = wert_lower.replace(suchbegriff, self.suchbegriffe[i].lower().strip()).title()
                            if neuer_wert not in werte:
                                werte.append(neuer_wert)
                                zu_lesen += " OR original LIKE %s"
        zu_lesen += ")"                        
        original_erweiterung = ""
        for i in res:
            original_erweiterung += " OR primkey = %s"
            werte.append(str(i[2]))
        if original_erweiterung:
            zu_lesen += original_erweiterung
        if self.actionVid.isChecked():
            zu_lesen += " AND vorhanden = %s"
            werte.append("x")
            self.actionVid.toggle()
        self.letzter_select = zu_lesen
        zu_lesen += " ORDER BY original, cd, lower(bild), darsteller"
        self.letzter_select_komplett = zu_lesen
        self.letzter_select_komplett_werte = werte
        self.partner = 0
        self.ausgabe(ein3, zu_lesen, werte)
        app.restoreOverrideCursor()
        
    def onHelp(self):
        QtWidgets.QMessageBox.about(self, "About PorDB3", """<b>PorDB3</b> v %s <p>Copyright &copy; 2012-2018 HWM</p> <p>GNU GENERAL PUBLIC LICENSE Version 3</p> <p>This is PorDB3.</p> <p>Python %s - Qt %s - PyQt %s on %s""" % (__version__, platform.python_version(), QtCore.QT_VERSION_STR, QtCore.PYQT_VERSION_STR, platform.system()))
        self.suchfeld.setFocus()
        
    def ausgabe(self, ein, zu_lesen, werte = None):
        lese_func = DBLesen(self, zu_lesen, werte)
        self.aktuelles_res = DBLesen.get_data(lese_func)
        zw_res = []
        if "SELECT * FROM pordb_vid WHERE (LOWER(original)" in zu_lesen:
            if self.actionCheckBoxDVDCover.isChecked():
                for i in self.aktuelles_res:
                    dateiname = os.path.join(self.verzeichnis_thumbs, "cd" + str(i[2]), i[3].strip())
                    if not os.path.exists(dateiname):
                        dateiname = os.path.join(self.verzeichnis_cover, i[3].strip())
                        if os.path.exists(dateiname):
                            zw_res.append(i)
                self.aktuelles_res = zw_res
        if "ORDER BY original" in zu_lesen:
            original_liste = []
            for i in self.aktuelles_res:
                teile = i[5].split()
                folge = 0
                try:
                    folge = int(teile[-1])
                    original_liste.append([" ".join(teile[0 : -1]), folge, i])
                except:
                    try:
                        folge = int(teile[-2])
                        original_liste.append([" ".join(teile[0 : -2]), folge, i])
                    except:
                        original_liste.append([i[5], folge, i])
            #1. sort serial number
            getcount = itemgetter(1)
            original_liste = sorted(original_liste, key=getcount)
            #2. sort original title
            getcount = itemgetter(0)
            original_liste = sorted(original_liste, key=getcount)
            self.aktuelles_res = []
            for i in original_liste:
                self.aktuelles_res.append(i[2])
            
        # Delete duplicates which are created through table suchbegriffe
        liste_neu = []
        for i in self.aktuelles_res:
            if not i in liste_neu:
                liste_neu.append(i)
        self.aktuelles_res[:] = liste_neu
        
        # Ignore the year in the original title
        ignore_year = True
        if ein != "":
            index1 = ein.rfind("(") + 1
            index2 = ein.rfind(")")
            if index1 > 0:
                if len(ein[index1 : index2]) == 4:
                    try:
                        jahr = int(ein[index1 : index2])
                    except:
                        ignore_year = True
        if ignore_year == False and "SELECT * FROM pordb_vid WHERE (LOWER(original)" in zu_lesen:
            liste_neu = []
            for i in self.aktuelles_res:
                index1 = i[5].rfind("(") + 1
                index2 = i[5].rfind(")")
                jahr = -1
                if index1 > 0:
                    suchtext = i[5][: index1].lower().strip()
                else:
                    suchtext = i[5].lower().strip()
                if index1 > 0:
                    if len(i[5][index1 : index2]) == 4:
                        try:
                            jahr = int(i[5][index1 : index2])
                            suchtext = i[5][: index1 - 1].lower().strip()
                        except:
                            pass
                if jahr < 0 or ein.lower().strip().lstrip("=") == suchtext:
                    liste_neu.append(i)
            self.aktuelles_res[:] = liste_neu            
        
        self.ausgabe_in_table()
        befehl = zu_lesen[:] + " (" +  ";".join(werte) + ")"
        if befehl and len(befehl) < 5001:
            zu_erfassen = []
            werte = []
            werte.append(befehl)
            zu_erfassen.append(["DELETE FROM pordb_history WHERE sql = %s", werte])
            werte = []
            werte.append(befehl)
            werte.append(datetime.datetime.now().isoformat(" "))
            zu_erfassen.append(["INSERT INTO pordb_history VALUES (%s, %s)", werte])
            update_func = DBUpdate(self, zu_erfassen)
            DBUpdate.update_data(update_func)
        
        if ein.startswith("SELECT "):
            pass
        else:
            self.statusBar.showMessage(self.tr("Search was: ") +ein)
            self.suchhistorie(ein)
        self.suchfeld.setCurrentIndex(-1)
        self.tabWidget.setCurrentIndex(0)
        self.suchfeld.setFocus()
    # end of ausgabe
    
    def ausgabe_in_table(self):
        self.tableWidgetBilder.clear()
        zeile = 0
        spalte = -1
        res = self.aktuelles_res[int(self.start_bilder):int(self.start_bilder) + int(self.anzahl_bilder)]
        self.tableWidgetBilder.setRowCount(round(len(res) / self.columns + 0.4))
        if len(res) < self.columns:
            self.tableWidgetBilder.setColumnCount(len(res))
        else:
            self.tableWidgetBilder.setColumnCount(self.columns)
        for i in res:
            cover = ""
            dateiname = os.path.join(self.verzeichnis_thumbs, "cd" + str(i[2]), i[3])
            if not os.path.exists(dateiname) or self.actionCheckBoxDVDCover.isChecked():
                dateiname = os.path.join(self.verzeichnis_cover, i[3].strip())
                if os.path.exists(dateiname):
                    cover = "x"
            if os.path.exists(dateiname):
                bild = QtGui.QPixmap(dateiname)
                groesse = bild.size()
                bild = QtGui.QIcon(dateiname)
            else:
                bild = QtGui.QPixmap(os.path.join(self.verzeichnis_thumbs, "nichtvorhanden", "nicht_vorhanden.jpg"))
                groesse = bild.size()
                bild = QtGui.QIcon(os.path.join(self.verzeichnis_thumbs, "nichtvorhanden", "nicht_vorhanden.jpg"))
            cs = ""
            if i[9] != 0:
                cs += str(i[9]) +"f"
            if i[10] != 0:
                cs += str(i[10]) +"h"
            if i[11] != 0:
                cs += str(i[11]) +"t"
            if i[12] != 0:
                cs += str(i[12]) +"c"
            if i[13] != 0:
                cs += str(i[13]) +"x"
            if i[14] != 0:
                cs += str(i[14]) +"o"
            if i[15] != 0:
                cs += str(i[15]) +"v"
            if i[16] != 0:
                cs += str(i[16]) +"b"
            if i[17] != 0:
                cs += str(i[17]) +"a"
            if i[18] != 0:
                cs += str(i[18]) +"s"
            if i[19] != 0:
                cs += str(i[19]) +"k"
            ort = str(i[2]) +" " +cs
            if i[5] == None:
                original = ""
            else:
                original = i[5]
            text = ""
            if cover:
                text = "Cover (" +str(groesse.width()) +", " +str(groesse.height()) +")\n" 
                text += "------------------------------\n"
            darsteller = i[1].split(", ")
            geschlecht_alt = ""
            darsteller_ausgabe = ""
            for j in darsteller:
                if j:
                    zu_lesen = "SELECT sex FROM pordb_darsteller WHERE darsteller = %s"
                    lese_func = DBLesen(self, zu_lesen, j)
                    res = DBLesen.get_data(lese_func)
                    if res:
                        if geschlecht_alt != res[0][0]:
                            if geschlecht_alt == "":
                                darsteller_ausgabe += j
                            else:
                                darsteller_ausgabe += "\n--\n" + j 
                            geschlecht_alt = res[0][0]
                        else:
                            darsteller_ausgabe += "\n" +j
            if len(original) > 30:
                original_liste = original.split()
                original = ""
                multiplikator = 1
            else:
                original_liste = []
            k = 0
            for j in original_liste:
                k += 1
                original += j +" "
                if len(original.strip()) > multiplikator * 30 and len(original_liste) > k:
                    original = original.strip() + "\n"
                    multiplikator += 1
            if original:
                text += original +"\n------------------------------\n"
            if self.anzeige_komplett:
                titel_liste = []
                titel = i[0]
                if len(titel) > 30:
                    for j in range(int(len(titel) / 30 + 1)):
                        titel_liste.append(titel[j * 30 : (j + 1) * 30])
                else:
                    titel_liste.append(titel)
                titel = "\n".join(titel_liste)
                bild_liste = []
                bild_element = i[3]
                if len(bild_element) > 30:
                    for j in range(int(len(bild_element) / 30 + 1)):
                        bild_liste.append(bild_element[j * 30 : (j + 1) * 30])
                else:
                    bild_liste.append(bild_element)
                bild_element = "\n".join(bild_liste)
                text += self.tr("Title: ") +"\n" +titel +"\n" +self.tr("Image: ") +"\n" +bild_element +"\n------------------------------\n"
                self.angezeigt_komplett = True
            else:
                self.angezeigt_komplett = False
            if darsteller_ausgabe:
                text += darsteller_ausgabe +"\n------------------------------\n" 
            text += "CD=" +ort +" "
            if i[4] == 'x':
                text += self.tr("\nwatched")
            elif i[7] == 'x':
                text += self.tr("\nin stock")
            if i[20] == '0':
                text += " SD"
            elif i[20] == '1':
                text += " HD 720p"
            elif i[20] == '2':
                text += " HD 1080p"
            elif i[20] == '3':
                text += " UltraHD"
            elif i[20] == '9':
                text += self.tr(" unknown")
            zu_lesen = "SELECT * FROM pordb_original WHERE foreign_key_pordb_vid = %s"
            lese_func = DBLesen(self, zu_lesen, str(i[8]))
            res2 = DBLesen.get_data(lese_func)
            if len(res2) > 0:
                text += "\n>>>>>"
            if i[21]:
                text += "\n!!!"
            if i[22]:
                text += "\n\n" + i[22] * "* "
            newitem = QtWidgets.QTableWidgetItem(bild, text)
            if i[4] != " " and i[7] != " " and i[7] != None: # clip is present and watched
                newitem.setForeground(QtGui.QColor("green"))
            elif i[7] == " " or i[7] == None:
                newitem.setForeground(QtGui.QColor("red"))
            spalte += 1
            if spalte == self.columns:
                spalte = 0
                zeile += 1
            self.tableWidgetBilder.setItem(zeile, spalte, newitem)
        self.restarbeiten_bilder()
        self.aktuelle_ausgabe = "Bilder"
        self.anzeige_komplett = False

    # end of ausgabe_in_table    
        
    def suchhistorie(self, e):
        if not e or e == " ":
            return
        zu_lesen = "SELECT * FROM pordb_suche ORDER BY nr"
        lese_func = DBLesen(self, zu_lesen)
        res = DBLesen.get_data(lese_func)
        zu_erfassen = []
        for i in res:
            if i[1].strip() == e.strip():
                werte = []
                werte.append(e)
                zu_erfassen.append(["DELETE FROM pordb_suche WHERE suche = %s", werte])
                break
        werte = []
        werte.append(e)
        zu_erfassen.append(["INSERT INTO pordb_suche (suche) VALUES (%s)", werte])
        if len(res) >= 20:
            werte = []
            werte.append(str(res[0][0]))
            zu_erfassen.append(["DELETE FROM pordb_suche WHERE nr = %s", werte])
            
        update_func = DBUpdate(self, zu_erfassen)
        DBUpdate.update_data(update_func)
    
        self.historie()
        
    # end of suchhistorie

    def historie(self):
        self.suchfeld.clear()
        zu_lesen = "SELECT * FROM pordb_suche ORDER BY nr DESC"
        lese_func = DBLesen(self, zu_lesen)
        res = DBLesen.get_data(lese_func)
        if res:
            for i in res:
                j = i[1].rstrip()
                self.suchfeld.addItem(j.replace("''", "'"))

    def onSuche(self):
        suche = Suchen(self)
        suche.lineEditDarsteller.setText(self.suche_darsteller)
        suche.lineEditDarsteller.setFocus()
        suche.lineEditCD.setText(self.suche_cd)
        suche.lineEditTitel.setText(self.suche_titel)
        suche.lineEditOriginal.setText(self.suche_original)
        suche.checkBoxVid.setChecked(self.present)
        suche.checkBoxWatched.setChecked(self.watched)
        suche.checkBoxNotVid.setChecked(self.notpresent)
        suche.checkBoxNotWatched.setChecked(self.notwatched)
        try:
            suche.comboBoxCS.setCurrentIndex(suche.comboBoxCS.findText(self.suche_cs))
        except:
            pass
        if self.suche_stars == 1:
            suche.onStar1()
        elif self.suche_stars == 2:
            suche.onStar2()
        elif self.suche_stars == 3:
            suche.onStar3()
        elif self.suche_stars == 4:
            suche.onStar4()
        elif self.suche_stars == 5:
            suche.onStar5()
        suche.lineEditRemarks.setText(self.suche_remarks)
        if suche.exec_():
            self.suche_darsteller = suche.lineEditDarsteller.text()
            self.suche_cd = suche.lineEditCD.text()
            self.suche_titel = suche.lineEditTitel.text()
            self.suche_original = suche.lineEditOriginal.text()
            self.present = suche.checkBoxVid.isChecked()
            self.watched = suche.checkBoxWatched.isChecked()
            self.notpresent = suche.checkBoxNotVid.isChecked()
            self.notwatched = suche.checkBoxNotWatched.isChecked()
            self.suche_cs = suche.comboBoxCS.currentText()
            self.suche_stars = suche.set_stars
            self.suche_remarks = suche.lineEditRemarks.text()
            
            # select-Anweisung aufbauen
            zu_lesen = "SELECT * FROM pordb_vid WHERE "
            argument = 0
            werte = []
            # Darsteller
            if self.suche_darsteller:
                argument = 1
                zu_lesen += "darsteller LIKE %s"
                werte.append("%" + str(self.suche_darsteller).title() + "%")
        
            # CD
            if self.suche_cd:
                try:
                    cd = int(self.suche_cd)
                except:
                    QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("CD is not a number"))
                    return
                if argument == 1:
                    zu_lesen += " AND "
                argument = 1
                zu_lesen += "cd = %s"
                werte.append(str(cd))
    
            # Titel
            if self.suche_titel:
                if argument == 1:
                    zu_lesen += " AND "
                argument = 1
                zu_lesen += "titel LIKE %s"
                werte.append("%" + str(self.suche_titel) + "%")
    
            # Original 
            if self.suche_original:
                if argument == 1:
                    zu_lesen += " AND "    
                argument = 1
                zu_lesen += "original LIKE %s"
                werte.append("%" + str(self.suche_original).title() + "%")
                
            # CS
            if self.suche_cs:
                if argument == 1:
                    zu_lesen += " AND "
                argument = 1
                zu_lesen += "cs" +str(self.suche_cs).split()[0] +"<> %s"
                werte.append("0")
            
            # Present Button gesetzt
            if argument == 1 and self.present and not self.notpresent:
                zu_lesen += " AND vorhanden = %s"
                werte.append("x")
                
            # NotPresent Button gesetzt
            if argument == 1 and self.notpresent and not self.present:
                zu_lesen += " AND vorhanden = %s"
                werte.append(" ")
                
            # Watched Button gesetzt
            if argument == 1 and self.watched and not self.notwatched:
                zu_lesen += " AND gesehen = %s"
                werte.append("x")
                
            # NotWatched Button gesetzt
            if argument == 1 and self.notwatched and not self.watched:
                zu_lesen += " AND gesehen = %s"
                werte.append(" ")
                
            # Rating
            if self.suche_stars:
                if argument == 1:
                    zu_lesen += " AND "    
                argument = 1
                zu_lesen += "stars = %s"
                werte.append(str(self.suche_stars))
                
            # Remarks 
            if self.suche_remarks:
                if argument == 1:
                    zu_lesen += " AND "    
                argument = 1
                zu_lesen += "remarks LIKE %s"
                werte.append("%" + str(self.suche_remarks) + "%")
            
            zu_lesen += " ORDER BY cd, lower(titel)"
            app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
            self.letzter_select_komplett = zu_lesen
            self.letzter_select_komplett_werte = werte
            self.letzter_select = zu_lesen
            if argument != 0:
                self.start_bilder = 0
                self.partner = 0
                self.ausgabe(zu_lesen, zu_lesen, werte)
            app.restoreOverrideCursor()
        self.suchfeld.setFocus()
    # end of onSuche
                
    def onbildAnzeige(self, ignorelist=False):
        self.onDarstellerspeichern(refresh=False)
        if type(ignorelist) != bool:
            ignorelist = False
        ein = self.eingabe_auswerten(ignorelist)
        if not ein:
            return
        res = self.darsteller_lesen(ein)
        if not res: 
            self.clear_actor_tab(False)
            return
        elif len(res) > 1:
            self.clear_actor_tab(True)
            return            
        self.pushButtonIAFDholen.setEnabled(True)
        self.pushButtonDarstellerLoeschen.setEnabled(True)
        self.pushButtonDarstellerspeichern.setEnabled(True)
        self.pushButtonPartnerZeigen.setEnabled(True)
        self.pushButtonPseudo.setEnabled(True)       
        for i in res:
            if i[1] == "m" or i[1] == "w": # not from pseudo_table
                name = i[0]
                bildname = i[0].lower().strip().replace(" ", "_").replace("'", "_apostroph_")
                self.bilddarsteller = os.path.join(self.verzeichnis_thumbs, "darsteller_" +i[1], bildname + ".jpg")
                if not os.path.isfile(self.bilddarsteller):
                    self.bilddarsteller = os.path.join(self.verzeichnis_thumbs, "darsteller_" +i[1], bildname + ".png")
                    if not os.path.isfile(self.bilddarsteller):
                        self.bilddarsteller = os.path.join(self.verzeichnis_thumbs, "nichtvorhanden", "nicht_vorhanden.jpg")
                if i[11] and i[11] != "0": # URL vorhanden
                    self.pushButtonIAFDBackground.setEnabled(True)
                else:
                    self.pushButtonIAFDBackground.setEnabled(False)
        self.bildSetzen()
        try:
            self.suchhistorie("=" +name)
        except:
            pass
        
        app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        zu_erfassen = []
        werte = []
        werte.append(name)
        zu_erfassen.append(["DELETE FROM pordb_darsteller100 WHERE darsteller = %s", werte])
        zu_erfassen.append(["INSERT INTO pordb_darsteller100 (darsteller) VALUES (%s)", werte])
        update_func = DBUpdate(self, zu_erfassen)
        DBUpdate.update_data(update_func)
        self.onStatistik()
        self.onDarstellerFilme(res)
        self.onpaareSuchen(res)
        self.suchfeld.setCurrentIndex(-1)
        self.suchfeld.setFocus()
        self.listWidgetDarsteller.clearSelection()
        self.pushButtonSortPartner.setText(QtWidgets.QApplication.translate("Dialog", "Quantity", None))
        self.pushButtonSort.setText(QtWidgets.QApplication.translate("Dialog", "Year", None))
        app.restoreOverrideCursor()
    # end of onbildAnzeige
    
    def bildSetzen(self):
        if self.bilddarsteller:
            # Multiplikation mit 0.05, da es eine Wechselwirkung mit dem Parent Frame gibt
            bild = QtGui.QPixmap(self.bilddarsteller).scaled(self.labelBildanzeige.parentWidget().width() - self.labelBildanzeige.parentWidget().width() * 0.05, self.labelBildanzeige.parentWidget().height() - self.labelBildanzeige.parentWidget().height() * 0.05, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            self.labelBildanzeige.setPixmap(bild)
            
    def clear_actor_tab(self, actor_found):
        self.labelDarsteller.clear()
        self.labelAlter.clear()
        self.pushButtonIAFDBackground.setEnabled(False)
        self.bilddarsteller = os.path.join(self.verzeichnis_thumbs, "nichtvorhanden", "nicht_vorhanden.jpg")
        self.bildSetzen()
        self.listWidgetStatistik.clear()
        self.listWidgetFilme.clear()
        self.labelFilme.clear()
        self.labelAlter.clear()
        self.labelAktiv.clear()
        self.lineEditAnzahl.clear()
        self.lineEditGeboren.clear()
        self.lineEditTattoo.clear()
        if actor_found == True:
            self.labelFehler.clear()
            self.pushButtonPartnerZeigen.setEnabled(True)
        else:
            self.labelText.clear()
            self.listWidgetDarsteller.clear()
            self.pushButtonPartnerZeigen.setEnabled(False)
        self.pushButtonIAFDholen.setEnabled(False)
        self.pushButtonDarstellerLoeschen.setEnabled(False)
        self.pushButtonDarstellerspeichern.setEnabled(False)
        self.pushButtonPseudo.setEnabled(False)
            
    def onTabwechsel(self, tab):
        if tab == 4 or tab == 5:
            self.actionDrucken.setEnabled(False)
        else:
            self.actionDrucken.setEnabled(True)
        
    def onpaareSuchen(self, res):
        if not res:
            return
        gesucht = res[0][0].strip()
        # Get the complete list of partners of the actor
        zu_lesen = "SELECT partner, cd, bild FROM pordb_partner WHERE darsteller = %s ORDER BY partner"
        lese_func = DBLesen(self, zu_lesen, gesucht)
        res_komplett = DBLesen.get_data(lese_func)
        partner_komplett = []
        for i in res_komplett:
            partner_komplett.append(i[0])
        # Get the distinct list of partners of the actor
        zu_lesen = "SELECT DISTINCT ON (partner) partner, cd, bild FROM pordb_partner WHERE darsteller = %s ORDER BY partner"
        lese_func = DBLesen(self, zu_lesen, gesucht)
        res = DBLesen.get_data(lese_func)
        res2 = res[:]
        ethnic = None
        cs = None
        mengeEthnic = set()
        menge = set()
        for i in res2:
            menge.add(i[0])
        if self.comboBoxEthnicFilter.currentText():
            ethnic = str(self.comboBoxEthnicFilter.currentText())
            for i in res:
                zu_lesen = "SELECT ethnic FROM pordb_darsteller WHERE darsteller = %s"
                lese_func = DBLesen(self, zu_lesen, i[0].strip())
                res1 = DBLesen.get_data(lese_func)
                if res1[0][0] == ethnic:
                    mengeEthnic.add(i[0])
            self.comboBoxEthnicFilter.setCurrentIndex(-1)
            menge = mengeEthnic
            
        res = res_komplett[:]
        mengeCs = set()
        if self.comboBoxCSFilter.currentText():
            cs = str(self.comboBoxCSFilter.currentText())[0:1]
            for i in res:
                zu_lesen = "SELECT cs" + cs + " FROM pordb_vid WHERE cd = %s AND bild = %s"
                lese_func = DBLesen(self, zu_lesen, (str(i[1]), i[2]))
                res1 = DBLesen.get_data(lese_func)
                try:
                    if res1[0][0] != 0:
                        mengeCs.add(i[0])
                except: 
                    QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("There is something wrong with partners: ") + zu_lesen + "(" + str(i[1]) + ", " + i[2] + ")")
                    return
            if ethnic:
                menge = mengeEthnic & mengeCs
            else:
                menge = mengeCs
            self.comboBoxCSFilter.setCurrentIndex(-1)
        
        self.paarung = []
        for i in menge:
            anzahl = partner_komplett.count(i)
            self.paarung.append(i.strip() +" (" +str(anzahl) +")")
                    
        self.paarung.sort()
        self.listWidgetDarsteller.clear()
        self.listWidgetDarsteller.addItems(self.paarung)
        self.labelText.setText(self.tr("Partner: ") +str(len(self.paarung)))
        if not ethnic and not cs:
            werte = []
            werte.append(len(self.paarung))
            werte.append(gesucht)
            zu_erfassen = []
            zu_erfassen.append(["UPDATE pordb_darsteller SET partner = %s WHERE darsteller = %s", werte])
            update_func = DBUpdate(self, zu_erfassen)
            DBUpdate.update_data(update_func)
    # end of onpaareSuchen
        
    def eingabe_auswerten(self, ignorelist = False):
        ein = None
        try:
            ein = str(self.suchfeld.currentText()).strip().title()
        except:
            QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("Illegal characters in search field"))
            return
        if not ein and not ignorelist:
            selected = self.listWidgetDarsteller.selectedItems()
            if selected:
                ein = str(selected[0].text())
                ein = "=" +ein[0 : ein.rfind("(")].strip()
        if not ein:
            ein = "=" + str(self.labelDarsteller.text()).strip().title()
        return ein
    
    def darsteller_lesen(self, ein):
        werte = []
        if ein[0] == '=':
            eingabe=ein.lstrip('=')
            zu_lesen = "SELECT * FROM pordb_darsteller WHERE darsteller = %s"
            werte.append(eingabe)
            if self.comboBoxSex.currentText() == "Mann" or self.comboBoxSex.currentText() == "Male":
                zu_lesen += " AND sex = %s"
                werte.append("m")
            elif self.comboBoxSex.currentText() == "Frau" or self.comboBoxSex.currentText() == "Female":
                zu_lesen += " AND sex = %s"
                werte.append("w")
            zu_lesen += " ORDER BY darsteller"
            lese_func = DBLesen(self, zu_lesen, werte)
            res = DBLesen.get_data(lese_func)
        else:
            eingabe = ein
            zu_lesen = "SELECT * FROM pordb_darsteller WHERE darsteller LIKE %s"
            werte.append("%" + eingabe + "%")
            if self.comboBoxSex.currentText() == "Mann" or self.comboBoxSex.currentText() == "Male":
                zu_lesen += " AND sex = %s"
                werte.append("m")
            elif self.comboBoxSex.currentText() == "Frau" or self.comboBoxSex.currentText() == "Female":
                zu_lesen += " AND sex = %s"
                werte.append("w")
            zu_lesen += " ORDER BY darsteller"
            lese_func = DBLesen(self, zu_lesen, werte)
            res = DBLesen.get_data(lese_func)
            
            zu_lesen = "SELECT pseudo, darsteller FROM pordb_pseudo WHERE pseudo LIKE %s"
            zu_lesen += " ORDER BY darsteller"
            lese_func = DBLesen(self, zu_lesen, "%" + eingabe + "%")
            res1 = DBLesen.get_data(lese_func)
            if len(res) == 0 and len(res1) > 0:
                QtWidgets.QMessageBox.warning(self, self.tr("Caution! "), self.tr("Actor has been found as pseudonym only!"))
            if res1:
                for i in res1:
                    werte = []
                    zu_lesen = "SELECT * FROM pordb_darsteller WHERE darsteller = %s"
                    werte.append(i[1])
                    if self.comboBoxSex.currentText() == "Mann" or self.comboBoxSex.currentText() == "Male":
                        zu_lesen += " AND sex = %s"
                        werte.append("m")
                    elif self.comboBoxSex.currentText() == "Frau" or self.comboBoxSex.currentText() == "Female":
                        zu_lesen += " AND sex = %s"
                        werte.append("w")

                    lese_func = DBLesen(self, zu_lesen, werte)
                    res2 = DBLesen.get_data(lese_func)
                    vorhanden = 0
                    if res2:
                        for j in res:
                            if res2[0][0] == j[0]:
                                vorhanden = 1
                        if not vorhanden:
                            res.extend(res2)
                res.sort()
                
        self.comboBoxSex.setCurrentIndex(0)
        if len(res) > 1:
            self.listWidgetDarsteller.clear()
            for i in res:
                self.listWidgetDarsteller.addItem(i[0])
            self.labelText.setText("<font color=red>" +self.tr("Please select:") +"</font>")
            self.suchfeld.setCurrentIndex(-1)
        elif len(res) == 1:
            self.labelDarsteller.setText(res[0][0])
            if res[0][1] == "w":
                self.comboBoxGeschlecht.setCurrentIndex(0)
            else:
                self.comboBoxGeschlecht.setCurrentIndex(1)
            self.lineEditAnzahl.setText(str(res[0][2]))
            if res[0][4] != None:
                self.comboBoxHaarfarbe.setCurrentIndex(self.comboBoxHaarfarbe.findText(res[0][4].strip()))
            self.labelFehler.clear()
            if res[0][5] != None and res[0][5] != " " and res[0][5][0:1] != "-":
                if len(self.nationen) == 0:
                    self.nation_fuellen()
                try:
                    i = self.nationen.index(res[0][5])
                    self.comboBoxNation.setCurrentIndex(i)
                except:
                    self.comboBoxNation.setCurrentIndex(-1)
                    self.labelFehler.setText("<font color=red>" +self.tr("Data collection of actor seems to be not complete, nation: ") +res[0][5]  +"</font>")
            else:
                if res[0][5] and res[0][5][0:1] != "-":
                    nation = res[0][5]
                else:
                    nation = ""
                    self.labelFehler.setText("<font color=red>" +self.tr("Data collection of actor seems to be not complete, nation: ") +nation  +"</font>")
            if res[0][6] != None:
                self.lineEditTattoo.setText(res[0][6].strip())
            else:
                self.lineEditTattoo.setText("")
            if res[0][7] != None:
                self.comboBoxEthnic.setCurrentIndex(self.comboBoxEthnic.findText(res[0][7].strip()))
            if res[0][9] != None:
                geburtstag = (str(res[0][9])[0:10])
                self.lineEditGeboren.setText(str(res[0][9])[0:10])
                self.lineEditGeboren.setCursorPosition(0)
                if geburtstag != "0001-01-01":
                    geboren = (str(res[0][9])[0:10]).split("-")
                    jahr = int(geboren[0])
                    monat = int(geboren[1])
                    tag = int(geboren[2])
                    alter = age(datetime.date(jahr, monat, tag))
                    self.labelAlter.setText(str(alter))
                else:
                    self.labelAlter.clear()
            else:
                self.lineEditGeboren.setText("")
                self.labelAlter.clear()
            if res[0][10] != None:
                self.labelFilme.setText(str(res[0][10]))
            else:
                self.labelFilme.clear()
            aktiv = ""
            if res[0][12] != None:
                aktiv = str(res[0][12])
            if res[0][13] != None and res[0][13] != 0:
                aktiv += "-" +str(res[0][13])
            besucht = 0
            if res[0][14] != None:
                aktiv += " (" +str(res[0][14])[0:10] +")"
                besuch = (str(res[0][14])[0:10]).split("-")
                jahr = int(besuch[0])
                monat = int(besuch[1])
                tag = int(besuch[2])
                besucht = age(datetime.date(jahr, monat, tag))
            if aktiv:
                if besucht > 0:
                    farbe = "<font color=red>"
                else:
                    farbe = "<font color=black>"
                self.labelAktiv.setText(farbe +self.tr("active : ") +aktiv +"</font>")
            else:
                self.labelAktiv.clear()
        else:
            werte = []
            zu_lesen = "SELECT * FROM pordb_pseudo WHERE pseudo = %s"
            werte.append(eingabe)
            zu_lesen += " ORDER BY darsteller"
            lese_func = DBLesen(self, zu_lesen, werte)
            res1 = DBLesen.get_data(lese_func)
            if res1:
                ein = "=" + res1[0][1].strip()
                res = self.darsteller_lesen(ein)
            else:
                self.labelFehler.setText("<font color=red>" +self.tr("Actor not available") +"</font>")
        self.suchfeld.setFocus()
        return res
    # end of darsteller_lesen
    
    def onDarstellerspeichern(self, refresh=True):
        name = str(self.labelDarsteller.text()).replace("'", "''")
        if not name:
            return
        try:
            ein = int(self.lineEditAnzahl.text())
        except:
            QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("Quantity is not a number"))
            self.lineEditAnzahl.setSelection(0, len(self.lineEditAnzahl.text()))
            return
        # update-Anweisung aufbauen
        if str(self.lineEditGeboren.text()):
            geboren = self.lineEditGeboren.text().split("-")
            try:
                geboren = datetime.date(int(geboren[0]), int(geboren[1]),int(geboren[2]))
            except ValueError:
                QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("Invalid birthday"))
                return
            geboren = str(self.lineEditGeboren.text())
        else:
            geboren = "0001-01-01"
        werte = []
        werte.append(str(ein))
        werte.append(str(self.comboBoxHaarfarbe.currentText()))
        werte.append(str(self.comboBoxGeschlecht.currentText()))
        werte.append(str(self.comboBoxNation.currentText())[0:2])
        werte.append(self.lineEditTattoo.text())
        werte.append(geboren)
        werte.append(str(self.comboBoxEthnic.currentText()))
        werte.append(name)
        zu_erfassen = []
        zu_erfassen.append(["UPDATE pordb_darsteller SET anzahl = %s, haarfarbe = %s, sex = %s, nation = %s, tattoo = %s, geboren = %s, ethnic = %s WHERE darsteller = %s", werte])
        update_func = DBUpdate(self, zu_erfassen)
        DBUpdate.update_data(update_func)
        
        filename = os.path.join(self.verzeichnis_thumbs, "darsteller_" +str(self.comboBoxGeschlecht.currentText()),  name.strip().lower().replace(" ", "_") + ".jpg")
        if not os.path.exists(filename):
            filename = os.path.join(self.verzeichnis_thumbs, "darsteller_" +str(self.comboBoxGeschlecht.currentText()), name.strip().lower().replace(" ", "_") + ".png")
            extension = ".png"
        else:
            extension = ".jpg"
        if os.path.exists(filename):
            pass
        else:
            if str(self.comboBoxGeschlecht.currentText()) == "w":
                sex_alt = "m"
            else:
                sex_alt = "w"
            oldfilename = os.path.join(self.verzeichnis_thumbs, "darsteller_" + sex_alt, name.strip().lower().replace(" ", "_") + extension)
            if os.path.exists(oldfilename):
                os.rename(oldfilename, filename)
        
        if refresh:
            self.onbildAnzeige()
            self.labelFehler.clear()
            self.suchfeld.setFocus()
    # end of onDarstellerspeichern
    
    def onIAFD(self):
        ein = self.eingabe_auswerten()
        if ein == "=":
            return
        res = self.darsteller_lesen(ein)
        if res and res[0][11] and res[0][11] != "0":
            app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
            try:
                seite = urllib.request.urlopen(res[0][11], timeout=10).read().decode("utf-8")
            except (urllib.error.URLError, socket.timeout) as e:
                app.restoreOverrideCursor()
                QtWidgets.QMessageBox.critical(self, self.tr("Error "), str(e))
                return
            app.restoreOverrideCursor()
            bilddialog = DarstellerdatenAnzeigen(app, res[0][11], seite, self.verzeichnis_thumbs, name = res[0][0])
            bilddialog.exec_()
        else:
            clipboard = QtWidgets.QApplication.clipboard()
            clipboard.setText(ein.lstrip("="), mode=clipboard.Clipboard)
            self.tabWidget.setCurrentIndex(3)
        
        self.darsteller_lesen(ein)
        self.onbildAnzeige()
            
    def onIAFDBackground(self):
        # ignorelist is added because very often a list entry is selected
        ein = self.eingabe_auswerten(ignorelist=True)
        res = self.darsteller_lesen(ein)
        if res[0][11]:
            monate = {"January":"01", "February":"02", "March":"03", "April":"04", "May":"05", "June":"06", "July":"07", "August":"08", "September":"09", "October":"10", "November":"11", "December":"12", }
            haarfarben = {"Brown":"br", "Brown/Light Brown":"br", "Dark Brown":"br", "Light Brown":"br", "Black":"s", "Red":"r", "Blond":"bl", "Honey Blond":"bl", "Dark Blond":"bl", "Dirty Blond":"bl", "Sandy Blond":"bl", "Strawberry Blond":"bl", "Auburn":"r"}
            app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
            try:
                seite = urllib.request.urlopen(res[0][11], timeout=10).read().decode("utf-8")
            except (urllib.error.URLError, socket.timeout) as e:
                app.restoreOverrideCursor()
                QtWidgets.QMessageBox.critical(self, self.tr("Error "), str(e))
                return
            
            actordata = ActorData(seite)
            
            # Check if actors name has changed in IAFD
            actor_name = ActorData.actor_name(actordata)
            if not actor_name:
                app.restoreOverrideCursor()
                QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("Seems IAFD site is offline"))
                return
            if res[0][0].lower().strip() != actor_name.lower():
                app.restoreOverrideCursor()
                QtWidgets.QMessageBox.warning(self, self.tr("Warning "), self.tr("Actors name in \nPorDB --> ({0}) \ndiffers from actors name in the \nIAFD --> ({1}).\nMaybe you should rename the actor in PorDB.").format(res[0][0].strip(), actor_name))
            
            # Darsteller Geboren
            geboren = ActorData.actor_born(actordata)
            monat = monate.get(geboren[0:geboren.find(" ")], self.tr("not available"))
            if monat != self.tr("not available"):
                tag = geboren[geboren.find(" ")+1:geboren.find(",")]
                jahr = geboren[geboren.find(", ")+2:]
                geboren = jahr +"-" + monat + "-" + tag
            else:
                geboren = 0
            
            zu_erfassen = []
            if geboren == 0:
                if not res[0][9]:
                    werte = []
                    werte.append(res[0][0])
                    zu_erfassen.append(["UPDATE pordb_darsteller SET geboren = '0001-01-01' WHERE darsteller = %s", werte])
            else:
                werte = []
                werte.append(str(geboren))
                werte.append(res[0][0])
                zu_erfassen.append(["UPDATE pordb_darsteller SET geboren = %s WHERE darsteller = %s", werte])
                
            # Check if actors country differs from that in IAFD
            actor_country = ActorData.actor_country(actordata)
            zu_lesen = "SELECT iso FROM pordb_iso_land WHERE national = %s"
            lese_func = DBLesen(self, zu_lesen, actor_country)
            res_iso_land = DBLesen.get_data(lese_func)
            if res_iso_land and res[0][5] != res_iso_land[0][0]:
                actor_birthplace = ActorData.actor_birthplace(actordata)
                if actor_birthplace == "No data":
                    actor_birthplace = "-"
                app.restoreOverrideCursor()
                QtWidgets.QMessageBox.warning(self, self.tr("Warning "), self.tr("Actors country in \nPorDB --> ({0}) \ndiffers from actors country in the \nIAFD --> ({1}, birthplace: {2}).\nMaybe you should check the actor in PorDB.").format(res[0][5].strip(), res_iso_land[0][0], actor_birthplace))
            
            # Darsteller Anzahl Filme
            filme = ActorData.actor_movies(actordata)
            if int(filme) > 0:
                werte = []
                werte.append(filme)
                werte.append(res[0][0])
                zu_erfassen.append(["UPDATE pordb_darsteller SET filme = %s WHERE darsteller = %s", werte])
                
            # Actors hair color
            hair = ActorData.actor_hair(actordata)
            haarfarbe = haarfarben.get(hair, self.tr("not available"))
            if haarfarbe != self.tr("not available"):
                werte = []
                werte.append(haarfarbe)
                werte.append(res[0][0])
                zu_erfassen.append(["UPDATE pordb_darsteller SET haarfarbe = %s WHERE darsteller = %s", werte])
                
            # Darsteller aktiv von / bis
            aktiv_von, aktiv_bis = ActorData.actor_activ(actordata)

            if aktiv_von != 0:
                werte = []
                werte.append(str(aktiv_von))
                werte.append(res[0][0])
                zu_erfassen.append(["UPDATE pordb_darsteller SET aktivvon = %s WHERE darsteller = %s", werte])
            if aktiv_bis != 0:
                werte = []
                werte.append(str(aktiv_bis))
                werte.append(res[0][0])
                zu_erfassen.append(["UPDATE pordb_darsteller SET aktivbis = %s WHERE darsteller = %s", werte])
                
            # Darsteller Tattoos
            tattoos = ActorData.actor_tattoos(actordata)
            if tattoos.lower() == "none":
                tats = "-"
            elif tattoos.lower() == "no data":
                tats = ""
            else:
                tats = tattoos.replace("'", "''").replace('\\', "")
            if tats:
                werte = []
                werte.append(tats)
                werte.append(res[0][0])
                zu_erfassen.append(["UPDATE pordb_darsteller SET tattoo = %s WHERE darsteller = %s", werte])
                    
            datum = str(time.localtime()[0]) + '-' + str(time.localtime()[1]) + '-' + str(time.localtime()[2])
            werte = []
            werte.append(datum)
            werte.append(res[0][0])
            zu_erfassen.append(["UPDATE pordb_darsteller SET besuch = %s WHERE darsteller = %s", werte])
            update_func = DBUpdate(self, zu_erfassen)
            DBUpdate.update_data(update_func)
                
            self.darsteller_lesen(ein)
            self.onbildAnzeige(ignorelist=True)
                
            app.restoreOverrideCursor()
            
    # end of onIAFDBackground
    
    def onDarstellerloeschen(self):
        name = str(self.labelDarsteller.text())
        if not name:
            return
        messageBox = QtWidgets.QMessageBox()
        messageBox.addButton(self.tr("Yes"), QtWidgets.QMessageBox.AcceptRole)
        messageBox.addButton(self.tr("No"), QtWidgets.QMessageBox.RejectRole)
        messageBox.setWindowTitle(self.tr("Actor ") +name.strip() +self.tr(" will be deleted now"))
        messageBox.setIcon(QtWidgets.QMessageBox.Question)
        messageBox.setText(self.tr("Should the actor really be deleted?"))
        message = messageBox.exec_()
        if message == 0:
            zu_erfassen = []
            # delete-Anweisung aufbauen
            werte = []
            werte.append(name)
            zu_erfassen.append(["DELETE FROM pordb_pseudo WHERE darsteller = %s", werte])
            zu_erfassen.append(["DELETE FROM pordb_darsteller WHERE darsteller = %s", werte])
            zu_erfassen.append(["DELETE FROM pordb_partner WHERE darsteller = %s", werte])
            zu_erfassen.append(["DELETE FROM pordb_partner WHERE partner = %s", werte])
            update_func = DBUpdate(self, zu_erfassen)
            DBUpdate.update_data(update_func)
            bildname = name.strip().lower().replace(" ", "_").replace("'", "_apostroph_")
            datei_alt = os.path.join(self.verzeichnis_thumbs, "darsteller_" +str(self.comboBoxGeschlecht.currentText()), bildname +".jpg")
            try:
                os.remove(datei_alt)
            except:
                pass
            self.statusBar.showMessage(self.tr("Actor ") +name.strip() +self.tr(" deleted"))
        self.labelFehler.clear()
        self.suchfeld.setFocus()
    # end of onDarstellerloeschen
    
    def onNeueingabe(self, undo = None, cover_anlegen = None, dateien = None, original = None):
        self.suchfeld.setFocus()
        if undo:
            dateiliste = os.listdir(self.verzeichnis_trash)
            if not dateiliste:
                return
            j = 0
            for i in dateiliste:
                if os.path.splitext(i)[-1] == ".txt":
                    datei = open(os.path.join(self.verzeichnis_trash, i), "r")
                    text = datei.readlines()
                    datei.close()
                elif (os.path.splitext(i)[-1].lower() in IMAGE_FILES) and os.path.splitext(i)[0] != "pypordb_bildalt":
                    j += 1
                    self.file = os.path.join(self.verzeichnis_trash, i)
            titel = text[0].strip()
            darsteller = text[1].strip()
            cd = text[2].strip()
            bild = text[3].strip()
            gesehen = text[4].strip()
            original = text[5].strip()
            cs = []
            cs.append(text[9].strip() +'f')
            cs.append(text[10].strip() +'h')
            cs.append(text[11].strip() +'t')
            cs.append(text[12].strip() +'c')
            cs.append(text[13].strip() +'x')
            cs.append(text[14].strip() +'o')
            cs.append(text[15].strip() +'v')
            cs.append(text[16].strip() +'b')
            cs.append(text[17].strip() +'a')
            cs.append(text[18].strip() +'s')
            cs.append(text[19].strip() +'k')
            vorhanden = text[7].strip()
            if len(text) > 21 and text[21].strip() == "COVER":
                trash_cover = "x"
            else:
                trash_cover = None
            definition = text[20].strip()
            if not definition:
                definition = "0"
            remarks = text[21].strip()
            try:
                stars = int(text[22].strip())
            except:
                stars = 0
            if j != 1:
                self.file, _ = QtWidgets.QFileDialog.getOpenFileName(self, self.tr("Image files"), self.verzeichnis_trash, self.tr("Image files (*.jpg *.jpeg *.png);;all files (*.*)"))
            eingabedialog = Neueingabe(self.verzeichnis, self.verzeichnis_original, self.verzeichnis_thumbs, self.verzeichnis_trash, self.verzeichnis_cover, self.file, titel, darsteller, cd, bild, gesehen, original, cs, vorhanden, remarks, stars, "", undo, original_cover=trash_cover, high_definition = definition)
        else:
            if not cover_anlegen:
                if len(self.tableWidgetBilderAktuell.selectedItems()) == 1 or len(self.tableWidgetBilderAktuell.selectedItems()) == 2:
                    items = self.tableWidgetBilderAktuell.selectedItems()
                    dateien = []
                    for i in items:
                        dateien.append(os.path.join(self.verzeichnis, i.text().split("\n")[0]))
            if dateien:
                if type(dateien) == str:
                    self.file = dateien
                else:
                    self.file = dateien[0]
                if len(dateien) == 2:
                    self.onCover(datei = dateien)
            else:
                try:
                    dateiliste = os.listdir(self.verzeichnis)
                except:
                    self.verzeichnis = self.verzeichnis_original
                    dateiliste = os.listdir(self.verzeichnis)
                j = 0
                for i in dateiliste:
                    if os.path.splitext(i)[-1].lower() in IMAGE_FILES:
                        j += 1
                        self.file = os.path.join(self.verzeichnis, i)
                if j != 1:
                    self.file, _ = QtWidgets.QFileDialog.getOpenFileName(self, self.tr("Image files"), self.verzeichnis, self.tr("Image files (*.jpg *.jpeg *.png);;all files (*.*)"))
                    if self.file:
                        self.verzeichnis = os.path.dirname(str(self.file))
            # In case we have just stored a cover, this part of program is already done
            if self.file and os.path.exists(self.file):
                eingabedialog = Neueingabe(self.verzeichnis, self.verzeichnis_original, self.verzeichnis_thumbs, self.verzeichnis_trash, self.verzeichnis_cover, self.file, cover_anlegen = cover_anlegen, original = original)
        if not self.file:
            return
        
        if not undo:
            self.verzeichnis = os.path.dirname(str(self.file))
        
        # In case we have just stored a cover, this part of program is already done
        datei = self.file
        if os.path.exists(datei):
            eingabedialog.exec_()
            self.bilderliste = []
            self.bilder_aktuell()
            zu_lesen = "SELECT * FROM pordb_vid_neu"
            lese_func = DBLesen(self, zu_lesen)
            res = DBLesen.get_data(lese_func)
            self.spinBoxAktuell.setValue(res[0][2])
            self.statusBar.showMessage("ins:CD" +str(res[0][2]) +" Title:" +res[0][0].strip() +" Act:" +res[0][1].strip())
            if str(self.labelDarsteller.text()) != "":
                self.darsteller_lesen("=" +str(self.labelDarsteller.text()).strip().title())
                self.onbildAnzeige()
                
        # next block is necessary in case a new entry should be created without any search action before
        if not self.aktuelles_res:
            self.letzter_select_komplett_werte = []
            self.letzter_select_komplett_werte.append(str(self.spinBoxAktuell.value()))
            self.letzter_select_komplett_werte.append(os.path.basename(self.file))
            self.letzter_select_komplett = "SELECT * FROM pordb_vid WHERE cd = %s AND bild = %s"
            
        if self.tabWidget.currentIndex() == 0:
            self.ausgabe("", self.letzter_select_komplett, self.letzter_select_komplett_werte)
        
    # end of onNeueingabe
        
    def onKorrektur(self, zeile, spalte):
        item = self.tableWidgetBilder.currentItem()
        column = self.tableWidgetBilder.column(item)
        row = self.tableWidgetBilder.row(item)
        index = int(row * self.columns + column + self.start_bilder)
        if item:
            if self.aktuelle_ausgabe == "Darsteller":
                self.onDarstellerUebernehmen()
                self.onbildAnzeige()
                self.changeTab("F3")
                return
            cd = self.aktuelles_res[index][2]
            bild = self.aktuelles_res[index][3]
            titel = self.aktuelles_res[index][0]
            darsteller = self.aktuelles_res[index][1]
            gesehen = self.aktuelles_res[index][4]
            if self.aktuelles_res[index][5]:
                original = self.aktuelles_res[index][5]
            else:
                original = ""
            cs = []
            cs.append(str(self.aktuelles_res[index][9]) +'f')
            cs.append(str(self.aktuelles_res[index][10]) +'h')
            cs.append(str(self.aktuelles_res[index][11]) +'t')
            cs.append(str(self.aktuelles_res[index][12]) +'c')
            cs.append(str(self.aktuelles_res[index][13]) +'x')
            cs.append(str(self.aktuelles_res[index][14]) +'o')
            cs.append(str(self.aktuelles_res[index][15]) +'v')
            cs.append(str(self.aktuelles_res[index][16]) +'b')
            cs.append(str(self.aktuelles_res[index][17]) +'a')
            cs.append(str(self.aktuelles_res[index][18]) +'s')
            cs.append(str(self.aktuelles_res[index][19]) +'k')
            if self.aktuelles_res[index][7]:
                vorhanden = self.aktuelles_res[index][7]
            else:
                vorhanden = ""
            definition = self.aktuelles_res[index][20]
            remarks = self.aktuelles_res[index][21]
            stars = self.aktuelles_res[index][22]
            self.file = os.path.join(self.verzeichnis_thumbs, "cd" +str(cd), self.aktuelles_res[index][3].strip())
            cover = False
            if not os.path.exists(self.file):
                self.file = os.path.join(self.verzeichnis_cover, self.aktuelles_res[index][3].strip())
                cover = True
            zu_lesen = "SELECT * FROM pordb_original WHERE foreign_key_pordb_vid = %s"
            werte = []
            werte.append(str(self.aktuelles_res[index][8]))
            lese_func = DBLesen(self, zu_lesen, werte)
            res2 = DBLesen.get_data(lese_func)
            original_weitere = []
            for i in res2:
                original_weitere.append(i[1])
            eingabedialog = Neueingabe(self.verzeichnis, self.verzeichnis_original, self.verzeichnis_thumbs, self.verzeichnis_trash, self.verzeichnis_cover, self.file, titel, darsteller, cd, bild, gesehen, original, cs, vorhanden, remarks, stars, cover, None, None, original_weitere, high_definition = definition)
            change_flag = None
            res_alt = self.aktuelles_res
            if eingabedialog.exec_():
                change_flag = True
            self.ausgabe("", self.letzter_select_komplett, self.letzter_select_komplett_werte)
            if change_flag:
                self.statusBar.showMessage("upd:CD" +str(res_alt[index][2]) +" Title:" +res_alt[index][0].strip() +" Act:" +res_alt[index][1].strip())
            if str(self.labelDarsteller.text()) != "":
                self.darsteller_lesen("=" +str(self.labelDarsteller.text()).strip().title())
                self.onbildAnzeige()
        self.suchfeld.setFocus()
    # end of onKorrektur
        
    def onDarstellerSuchen(self):
        def partner_reduzieren(zu_lesen, werte):
            lese_func = DBLesen(self, zu_lesen, werte)
            res = DBLesen.get_data(lese_func)
            darsteller = []
            for i in res:
                darsteller.append(i[0])
            for i in aktuelles_res:
                if i[0] in darsteller:
                    self.aktuelles_res.append(i)

        self.partner = None
        suche = DarstellerSuchen()
        suche.lineEditDarstellerSuche.setText(self.sucheD_darsteller)
        suche.lineEditDarstellerSuche.setFocus()
        suche.comboBoxDarstellerSucheGeschlecht.setCurrentIndex(suche.comboBoxDarstellerSucheGeschlecht.findText(self.sucheD_geschlecht))
        suche.lineEditActor1.setText(self.sucheD_actor1)
        suche.lineEditActor2.setText(self.sucheD_actor2)
        suche.lineEditActor3.setText(self.sucheD_actor3)
        suche.dateEditDarstellerSucheAb.setDate(QtCore.QDate.fromString(self.sucheD_ab, "yyyyMMdd"))
        suche.dateEditDarstellerSucheBis.setDate(QtCore.QDate.fromString(self.sucheD_bis, "yyyyMMdd"))
        suche.comboBoxDarstellerSucheHaar.setCurrentIndex(suche.comboBoxDarstellerSucheHaar.findText(self.sucheD_haar))
        suche.comboBoxDarstellerSucheNation.setCurrentIndex(suche.comboBoxDarstellerSucheNation.findText(self.sucheD_nation))
        suche.comboBoxDarstellerSucheTattoo.setCurrentIndex(suche.comboBoxDarstellerSucheTattoo.findText(self.sucheD_tattoo))
        suche.lineEditDarstellerSucheTattoo.setText(self.sucheD_etattoo)
        suche.comboBoxDarstellerSucheEthnic.setCurrentIndex(suche.comboBoxDarstellerSucheEthnic.findText(self.sucheD_ethnic))
        
        if suche.exec_():
            app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
            self.sucheD_darsteller = suche.lineEditDarstellerSuche.text()
            self.sucheD_geschlecht = suche.comboBoxDarstellerSucheGeschlecht.currentText()
            self.sucheD_actor1 = suche.lineEditActor1.text()
            self.sucheD_actor2 = suche.lineEditActor2.text()
            self.sucheD_actor3 = suche.lineEditActor3.text()
            self.sucheD_ab = suche.dateEditDarstellerSucheAb.date().toString("yyyyMMdd")
            self.sucheD_bis = suche.dateEditDarstellerSucheBis.date().toString("yyyyMMdd")
            self.sucheD_haar = suche.comboBoxDarstellerSucheHaar.currentText()
            self.sucheD_nation = suche.comboBoxDarstellerSucheNation.currentText()
            self.sucheD_tattoo = suche.comboBoxDarstellerSucheTattoo.currentText()
            self.sucheD_etattoo = suche.lineEditDarstellerSucheTattoo.text()
            self.sucheD_ethnic = suche.comboBoxDarstellerSucheEthnic.currentText()
        # select-Anweisung aufbauen
            zu_lesen = "SELECT * FROM pordb_darsteller WHERE "
            argument = 0
            werte = []
            #Name
            if self.sucheD_darsteller:
                argument = 1
                zu_lesen2 = "SELECT DISTINCT ON (darsteller) darsteller FROM pordb_pseudo WHERE pseudo LIKE %s"
                lese_func = DBLesen(self, zu_lesen2, "%" + self.sucheD_darsteller + "%")
                res = DBLesen.get_data(lese_func)
                if res:
                    zu_lesen += "(darsteller LIKE %s"
                    werte.append("%" + self.sucheD_darsteller + "%")
                    for i in res:
                        zu_lesen += " OR darsteller = %s"
                        werte.append(i[0].strip())
                    zu_lesen += ")"
                else:
                    zu_lesen += "darsteller LIKE %s"
                    werte.append("%" + self.sucheD_darsteller + "%")
    
            # Geschlecht
            if self.sucheD_geschlecht:
                if argument == 1:
                    zu_lesen += " AND "
                argument = 1
                zu_lesen += "sex = %s"
                werte.append(self.sucheD_geschlecht)
                
            # Datum >=
            if argument == 1:
                zu_lesen += " AND "
            argument = 1
            zu_lesen += "datum >= %s"
            werte.append(self.sucheD_ab)
    
            # Datum_bis <=
            if argument == 1:
                zu_lesen += " AND "
            argument = 1
            zu_lesen += "datum <= %s"
            werte.append(self.sucheD_bis)
    
            # Haarfarbe
            if self.sucheD_haar:
                if argument == 1:
                    zu_lesen += " AND "
                argument = 1
                zu_lesen += "haarfarbe = %s"
                werte.append(self.sucheD_haar)
    
            # Nation
            if self.sucheD_nation:
                if argument == 1:
                    zu_lesen += " AND "
                argument = 1
                zu_lesen += "nation = %s"
                werte.append(self.sucheD_nation[0:2])
    
            # Tattoo
            if self.sucheD_tattoo == self.tr("yes"):
                if argument == 1:
                    zu_lesen += " AND "
                argument = 1
                zu_lesen += "tattoo IS NOT NULL AND tattoo != %s AND tattoo != %s AND tattoo != %s"
                werte.append("-")
                werte.append(" ")
                werte.append("")
            elif self.sucheD_tattoo == self.tr("no"):
                if argument == 1:
                    zu_lesen += " AND "
                argument = 1
                zu_lesen += "(tattoo = %s or tattoo = %s)"
                werte.append("-")
                werte.append("")
            if self.sucheD_etattoo:
                if argument == 1:
                    zu_lesen += " AND "
                argument = 1
                zu_lesen += "tattoo LIKE %s"
                werte.append("%" + self.sucheD_etattoo + "%")
    
            # Ethnic
            if self.sucheD_ethnic:
                if argument == 1:
                    zu_lesen += " AND "
                argument = 1
                zu_lesen += "ethnic = %s"
                werte.append(self.sucheD_ethnic)
    
            zu_lesen += " ORDER BY darsteller"
            
            self.letzter_select_komplett = zu_lesen
            self.letzter_select_komplett_werte = werte
            self.letzter_select = zu_lesen
    
            self.aktuelles_res = []
            if argument != 0:
                lese_func = DBLesen(self, zu_lesen, werte)
                aktuelles_res = DBLesen.get_data(lese_func)
                self.aktuelles_res = aktuelles_res[:]
                if suche.lineEditActor1.text() != "":
                    self.aktuelles_res = []
                    zu_lesen = "SELECT DISTINCT ON (partner) partner FROM pordb_partner WHERE darsteller = %s"
                    werte = str(suche.lineEditActor1.text()).title()
                    partner_reduzieren(zu_lesen, werte)
                if suche.lineEditActor2.text() != "":
                    aktuelles_res = self.aktuelles_res[:]
                    self.aktuelles_res = []
                    zu_lesen = "SELECT DISTINCT ON (partner) partner FROM pordb_partner WHERE darsteller = %s"
                    werte = str(suche.lineEditActor2.text()).title()
                    partner_reduzieren(zu_lesen, werte)
                if suche.lineEditActor3.text() != "":
                    aktuelles_res = self.aktuelles_res[:]
                    self.aktuelles_res = []
                    zu_lesen = "SELECT DISTINCT ON (partner) partner FROM pordb_partner WHERE darsteller = %s"
                    werte = str(suche.lineEditActor3.text()).title()
                    partner_reduzieren(zu_lesen, werte)

                self.start_bilder = 0
                self.ausgabedarsteller()
            app.restoreOverrideCursor()
        else:
            self.suchfeld.setFocus()
    # end of onDarstellerSuchen

    def ausgabedarsteller(self):
        self.tableWidgetBilder.clear()
        res = self.aktuelles_res[int(self.start_bilder):int(self.start_bilder) + int(self.anzahl_bilder)]
        self.tableWidgetBilder.setRowCount(round(len(res) / self.columns + 0.4))
        if len(res) < self.columns:
            self.tableWidgetBilder.setColumnCount(len(res))
        else:
            self.tableWidgetBilder.setColumnCount(self.columns)
        zeile = 0
        spalte = -1
        for i in res:
            if len(i[0]) == 1:
                if i.rfind("(") > 0:
                    name = i[0 : i.rfind("(") - 1]
                else:
                    name = i.strip()
                bildname = name.lower().replace(" ", "_").replace("'", "_apostroph_")
                zu_lesen = "SELECT * FROM pordb_darsteller WHERE darsteller = %s"
                lese_func = DBLesen(self, zu_lesen, name)
                res2 = DBLesen.get_data(lese_func)
                if res2[0][5]: 
                    nationality = res2[0][5]
                else:
                    nationality = ""
                if res2[0][12]: 
                    active = str(res2[0][12])
                    if res2[0][13] and res2[0][13] > 0:
                        active += "-" + str(res2[0][13])
                else:
                    active = ""
                text = name + "\n" + nationality + "\n" + active
                if os.path.exists(os.path.join(self.verzeichnis_thumbs, "darsteller_w", bildname + ".jpg")):
                    dateiname = os.path.join(self.verzeichnis_thumbs, "darsteller_w",  bildname + ".jpg")
                elif os.path.exists(os.path.join(self.verzeichnis_thumbs, "darsteller_w", bildname + ".png")):
                    dateiname = os.path.join(self.verzeichnis_thumbs, "darsteller_w", bildname + ".png")
                elif os.path.exists(os.path.join(self.verzeichnis_thumbs, "darsteller_m", bildname + ".jpg")):
                    dateiname = os.path.join(self.verzeichnis_thumbs, "darsteller_m", bildname + ".jpg")
                else:
                    dateiname = os.path.join(self.verzeichnis_thumbs, "darsteller_m", bildname + ".png")
            else:
                bildname = i[0].lower().strip().replace(" ", "_").replace("'", "_apostroph_")
                if i[5]: 
                    nationality = i[5]
                else:
                    nationality = ""
                if i[12]: 
                    active = str(i[12])
                    if i[13] and i[13] > 0:
                        active += "-" + str(i[13])
                else:
                    active = ""
                text = i[0] + "\n" + nationality + "\n" + active
                if os.path.exists(os.path.join(self.verzeichnis_thumbs, "darsteller_" + i[1], bildname + ".jpg")):
                    dateiname = os.path.join(self.verzeichnis_thumbs, "darsteller_" + i[1], bildname +".jpg")
                else:
                    dateiname = os.path.join(self.verzeichnis_thumbs, "darsteller_" + i[1], bildname + ".png")
            if not os.path.isfile(dateiname):
                dateiname = os.path.join(self.verzeichnis_thumbs, "nichtvorhanden", "nicht_vorhanden.jpg")
            bild = QtGui.QIcon(dateiname)
            newitem = QtWidgets.QTableWidgetItem(bild, text)
            spalte += 1
            if spalte == self.columns:
                spalte = 0
                zeile += 1
            self.tableWidgetBilder.setItem(zeile, spalte, newitem)
        self.restarbeiten_bilder()
        self.suchfeld.setCurrentIndex(-1)
        self.suchfeld.setFocus()
        self.tabWidget.setCurrentIndex(0)
        self.aktuelle_ausgabe = "Darsteller"
    # end of ausgabedarsteller
    
    def restarbeiten_bilder(self):
        self.tableWidgetBilder.scrollToTop()
        vertical_header = list(range(int(round(self.start_bilder / self.columns + 0.4)), int(round((self.start_bilder + self.anzahl_bilder) / self.columns + 0.4)))) 
        for i in range(len(vertical_header)):
            vertical_header[i] = str(vertical_header[i] + 1)
        self.tableWidgetBilder.setVerticalHeaderLabels(vertical_header)
        self.tableWidgetBilder.resizeRowsToContents()
        self.tableWidgetBilder.resizeColumnsToContents()
        self.anzahl.setText(self.tr("Quantity: ") +str(len(self.aktuelles_res)))
        seite_von = int(round(self.start_bilder / self.anzahl_bilder + 1))
        seite_bis = int(round(len(self.aktuelles_res) / float(self.anzahl_bilder) + 0.499999))
        self.labelSeite.setText(self.tr("Page ") +str(seite_von) + self.tr(" of ") +str(seite_bis))
        if seite_von == 1:
            self.actionFirst.setEnabled(False)
            self.actionPrev.setEnabled(False)
        else:
            self.actionFirst.setEnabled(True)
            self.actionPrev.setEnabled(True)
            self.suchfeld.setFocus()
        if seite_von == seite_bis:
            self.actionLast.setEnabled(False)
            self.actionNext.setEnabled(False)
        else:
            self.actionLast.setEnabled(True)
            self.actionNext.setEnabled(True)
            self.suchfeld.setFocus()
            
        if seite_von < seite_bis:
            horizontal_header = list(range(int(self.columns)))
            for i in range(len(horizontal_header)):
                horizontal_header[i] = str(horizontal_header[i] + 1) +"  >>>>>>>>>>>>>>>>>"
            self.tableWidgetBilder.setHorizontalHeaderLabels(horizontal_header)
    
    def onUndo(self):
        self.onNeueingabe(undo = 1)
        
    def onStatistik(self):
        ein = self.eingabe_auswerten()
        if not ein:
            return
        werte = []
        if ein[0] == '=':
            zu_lesen = "SELECT * FROM pordb_vid WHERE darsteller = %s OR darsteller LIKE %s OR darsteller LIKE %s OR darsteller LIKE %s"
            werte.append(ein.strip("="))
            werte.append(ein.strip("=") + ",%")
            werte.append("%, " + ein.strip("=") + ",%")
            werte.append("%, " + ein.strip("="))
        else:
            zu_lesen = "SELECT * FROM pordb_vid WHERE darsteller LIKE %s"
            werte.append("%" + ein + "%")
        lese_func = DBLesen(self, zu_lesen, werte)
        res = DBLesen.get_data(lese_func)
        sum_f = sum_h = sum_t = sum_c = sum_x = sum_o = sum_v = sum_b = sum_a = sum_s = 0
        cs = []
        for i in res:
            sum_f += i[9]
            sum_h += i[10]
            sum_t += i[11]
            sum_c += i[12]
            sum_x += i[13]
            sum_o += i[14]
            sum_v += i[15]
            sum_b += i[16]
            sum_a += i[17]
            sum_s += i[18]
        cs.append(sum_f)
        cs.append(sum_h)
        cs.append(sum_t)
        cs.append(sum_c)
        cs.append(sum_x)
        cs.append(sum_o)
        cs.append(sum_v)
        cs.append(sum_b)
        cs.append(sum_a)
        cs.append(sum_s)
        cs_summe = sum_f + sum_h + sum_t + sum_c + sum_x + sum_o + sum_v + sum_b + sum_a + sum_s
        cs.append(cs_summe)
        stats = []
        k = -1
        for i in ["Facial......", "Handjob.....", self.tr("Tits........"), "Creampie....", "Analcreampie", "Oralcreampie", self.tr("Cunt........"), self.tr("Belly......."), self.tr("Ass........."), self.tr("Others......"), self.tr("Summary.....")]:
            k += 1
            if i == self.tr("Summary....."):
                stats.append("________________________")
                stats.append("")
            try:
                prozent = cs[k] * 100.0 / cs_summe
            except:
                prozent = 0
            stats.append(("%-13.28s %3.4s %6.2f") % (i, cs[k], prozent))
        self.listWidgetStatistik.clear()
        self.listWidgetStatistik.addItems(stats)
    # end of onStatistik
        
    def onDarstellerUmbenennen(self):
        ein = self.eingabe_auswerten()
        if ein == "=":
            return
        vorname = False
        if ein[0] == "=":
            vorname = True
            eingabe = ein.lstrip('=').title()
        else:
            eingabe = ein.title()
        if not ein:
            return
        umbenennen = DarstellerUmbenennen(ein)
        neuer_name = None
        if umbenennen.exec_():
            app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
            neuer_name = str(umbenennen.lineEditNeuerName.text())
            if neuer_name:
                neuer_name = neuer_name.strip().title()
                zu_lesen = "SELECT * FROM pordb_pseudo WHERE darsteller = %s and pseudo = %s"
                lese_func = DBLesen(self, zu_lesen, (eingabe, neuer_name))
                res = DBLesen.get_data(lese_func)
                if res:
                    app.restoreOverrideCursor()
                    QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("New name already exists as alias, please first edit/delete the aliases"))
                    return
                werte = []
                if vorname:
                    zu_lesen = "SELECT * FROM pordb_vid WHERE (darsteller = %s OR darsteller LIKE %s OR darsteller LIKE %s OR darsteller LIKE %s)"
                    werte.append(eingabe)
                    werte.append(eingabe + ",%")
                    werte.append("%, " + eingabe + ",%")
                    werte.append("%, " + eingabe)
                else:
                    zu_lesen = "SELECT * FROM pordb_vid WHERE darsteller LIKE %s"
                    werte.append("%" + eingabe + "%")
                lese_func = DBLesen(self, zu_lesen, werte)
                res = DBLesen.get_data(lese_func)
                res1 = []
                darsteller_liste = []
                for i in res:
                    darsteller_liste = i[1].split(',')
                    for j in range(len(darsteller_liste)):
                        darsteller_liste[j] = darsteller_liste[j].strip()
                    res1.append([i[2], i[3], darsteller_liste])
                k = -1
                res2 = res1[:]
                for i in res1:
                    k += 1
                    if eingabe not in i[2]:
                        del res2[k]
                        k -=1
                zu_lesen = "SELECT * FROM pordb_darsteller WHERE darsteller = %s"
                lese_func = DBLesen(self, zu_lesen, eingabe)
                res = DBLesen.get_data(lese_func)
                if res[0][3] == None:
                    res[0][3] = '2000-01-01'
                if res[0][9]:
                    geboren = str(res[0][9])
                else:
                    geboren = "0001-01-01"
                if res[0][11]:
                    url = res[0][11]
                else:
                    url = "0"
                if res[0][12]:
                    aktivvon = res[0][12]
                else:
                    aktivvon = 0
                if res[0][13]:
                    aktivbis = res[0][13]
                else:
                    aktivbis = 0
                if res[0][14]:
                    besucht = str(res[0][14])
                else:
                    besucht = "0001-01-01"
                    
                zu_erfassen = []
                zu_lesen = "SELECT darsteller FROM pordb_darsteller WHERE darsteller = %s"
                lese_func = DBLesen(self, zu_lesen, neuer_name)
                res3 = DBLesen.get_data(lese_func)
                if res3:
                    werte = []
                    werte.append(len(res2))
                    werte.append(neuer_name)
                    zu_erfassen.append(["UPDATE pordb_darsteller SET anzahl = anzahl + %s WHERE darsteller = %s", werte])
                else:
                    werte = []
                    werte.append(neuer_name.title().lstrip("="))
                    werte.append(res[0][1])
                    werte.append(res[0][2])
                    werte.append(str(res[0][3]))
                    werte.append(res[0][4])
                    werte.append(res[0][5])
                    werte.append(res[0][6])
                    werte.append(res[0][7])
                    werte.append(res[0][8])
                    werte.append(str(geboren))
                    werte.append(res[0][10])
                    werte.append(url)
                    werte.append(aktivvon)
                    werte.append(aktivbis)
                    werte.append(str(besucht))
                    zu_erfassen.append(["INSERT INTO pordb_darsteller VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", werte])
                
                werte = []
                werte.append(neuer_name.title().lstrip("="))
                werte.append(eingabe)
                zu_erfassen.append(["UPDATE pordb_pseudo SET darsteller = %s WHERE darsteller = %s", werte])
                werte = []
                werte.append(eingabe)
                zu_erfassen.append(["DELETE FROM pordb_darsteller WHERE darsteller = %s", werte])
                l = -1
                bildname = eingabe.lower().replace(" ", "_").replace("'", "_apostroph_")
                datei_alt = os.path.join(self.verzeichnis_thumbs, "darsteller_" + res[0][1], bildname + ".jpg")
                bildname = neuer_name.lower().strip().replace("'", "''").lstrip("=").replace(" ", "_").replace("''", "_apostroph_")
                datei_neu = os.path.join(self.verzeichnis_thumbs, "darsteller_" + res[0][1], bildname + ".jpg")
                sortier = Neueingabe(self.verzeichnis, self.verzeichnis_original, self.verzeichnis_thumbs, self.verzeichnis_trash, self.verzeichnis_cover, datei_alt)
                for i in res2:
                    l += 1
                    k = -1
                    for j in i[2]:
                        k += 1
                        if j == eingabe:
                            res2[l][2][k] = eingabe.title().lstrip("=").replace("''", "'")
                    darsteller_liste = sortier.darsteller_sortieren(res2[l][2])
                    darsteller_liste2 = [neuer_name.title() if x==eingabe.title().lstrip("=") else x for x in darsteller_liste]
                    werte = []
                    werte.append(", ".join(darsteller_liste2))
                    werte.append(i[0])
                    werte.append(i[1])
                    zu_erfassen.append(["UPDATE pordb_vid SET darsteller = %s WHERE cd = %s AND bild = %s", werte])

                self.statusBar.showMessage(str(len(res2)) + self.tr(" lines changed"))
                
                zu_lesen = "SELECT * FROM pordb_partner WHERE darsteller = %s"
                lese_func = DBLesen(self, zu_lesen, eingabe)
                res = DBLesen.get_data(lese_func)
                werte = []
                werte.append(eingabe)
                zu_erfassen.append(["DELETE FROM pordb_partner WHERE darsteller = %s", werte])
                for i in res:
                    werte = []
                    werte.append(neuer_name.title())
                    werte.append(str(i[1]))
                    werte.append(i[2])
                    werte.append(str(i[3]))
                    zu_erfassen.append(["INSERT INTO pordb_partner VALUES (%s, %s, %s,%s)", werte])
                    
                zu_lesen = "SELECT * FROM pordb_partner WHERE partner = %s"
                lese_func = DBLesen(self, zu_lesen, eingabe)
                res = DBLesen.get_data(lese_func)
                werte = []
                werte.append(eingabe)
                zu_erfassen.append(["DELETE FROM pordb_partner WHERE partner = %s", werte])
                for i in res:
                    werte = []
                    werte.append(str(i[0]))
                    werte.append(neuer_name.title())
                    werte.append(i[2])
                    werte.append(str(i[3]))
                    zu_erfassen.append(["INSERT INTO pordb_partner VALUES (%s, %s, %s, %s)", werte])
                    
                update_func = DBUpdate(self, zu_erfassen)
                DBUpdate.update_data(update_func)
                
                if ein.strip("=") in self.aktuelles_res:
                    self.aktuelles_res.remove(ein.strip("="))
                    self.aktuelles_res.append(neuer_name.title())
                    self.aktuelles_res.sort()
                    
                if os.path.exists(datei_alt) and os.path.exists(datei_neu) and datei_alt != datei_neu:
                    dialog = ShowTwoImages(datei_alt, datei_neu)
                    app.restoreOverrideCursor()
                    dialog.exec_()
                    datei = dialog.datei()
                    if datei == 1:
                        try:
                            os.remove(datei_neu)
                            os.rename(datei_alt, datei_neu)
                        except:
                            QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("Image file could not be renamed"))
                    elif datei == 2:
                        try:
                            os.remove(datei_alt)
                        except:
                            QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("Image file could not be renamed"))
                    else:
                        QtWidgets.QMessageBox.information(self, self.tr("Information "), self.tr("Renaming canceled"))
                        self.suchfeld.setCurrentIndex(-1)
                        self.suchfeld.setFocus()
                        return
                else:
                    try:
                        os.rename(datei_alt, datei_neu)
                    except:
                        QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("Image file could not be renamed"))
                        
        if neuer_name:
            self.labelDarsteller.setText(neuer_name.replace("''", "'").title())
            self.darsteller_lesen("=" + neuer_name)
            self.onbildAnzeige()
        app.restoreOverrideCursor()
        self.suchfeld.setCurrentIndex(-1)
        self.suchfeld.setFocus()
    # end of onDarstellerUmbenennen
    
    def onDarstellerFilme(self, res):
        ein = self.eingabe_auswerten()
        if not ein:
            return
        if not res:
            return
        werte = []
        if ein[0] == '=':
            zu_lesen = "SELECT DISTINCT ON (original) original FROM pordb_vid WHERE darsteller = %s OR darsteller LIKE %s OR darsteller LIKE %s OR darsteller LIKE %s"
            werte.append(ein.strip("="))
            werte.append(ein.strip("=") + ",%")
            werte.append("%, " + ein.strip("=") + ",%")
            werte.append("%, " + ein.strip("="))
        else:
            zu_lesen = "SELECT DISTINCT ON (original) original FROM pordb_vid WHERE darsteller LIKE %s"
            werte.append("%" + ein + "%")
        lese_func = DBLesen(self, zu_lesen, werte)
        res = DBLesen.get_data(lese_func)
        filme = []
        for i in res:
            if i[0] and i[0].strip() > " ":
                filme.append(i[0].strip())
        self.listWidgetFilme.clear()
        self.listWidgetFilme.addItems(filme)
        self.pushButtonSort.setText(QtWidgets.QApplication.translate("Dialog", "Year", None))
    # end of onDarstellerFilme
    
    def onPartnerSortieren(self):
        def vergleich(a):
            wert1 = a[a.rfind("(") + 1 : a.rfind(")")]
            return int(wert1)
                
        text = self.pushButtonSortPartner.text()
        if text == self.tr("Quantity"):
            items = []
            for i in range(self.listWidgetDarsteller.count()):
                items.append(str(self.listWidgetDarsteller.item(i).text()).strip())
            items.sort(key = vergleich, reverse=True)
            self.listWidgetDarsteller.clear()
            self.listWidgetDarsteller.addItems(items)
            self.pushButtonSortPartner.setText(QtWidgets.QApplication.translate("Dialog", "Partner", None))
        else:
            self.listWidgetDarsteller.sortItems()
            self.pushButtonSortPartner.setText(QtWidgets.QApplication.translate("Dialog", "Quantity", None))
        self.suchfeld.setFocus()
    # end of onPartnerSortieren
        
    def onFilmeSortieren(self):
        def vergleich(a):
            try:
                return a.split()[-1]
            except:
                return 0
                
        text = self.pushButtonSort.text()
        if text == self.tr("Year"):
            items = []
            for i in range(self.listWidgetFilme.count()):
                items.append(str(self.listWidgetFilme.item(i).text()).strip())
            items.sort(key = vergleich)
            self.listWidgetFilme.clear()
            self.listWidgetFilme.addItems(items)
            self.pushButtonSort.setText(QtWidgets.QApplication.translate("Dialog", "Title", None))
        else:
            self.listWidgetFilme.sortItems()
            self.pushButtonSort.setText(QtWidgets.QApplication.translate("Dialog", "Year", None))
        self.suchfeld.setFocus()
    # end of onFilmeSortieren
    
    def onFilmeFilter(self, text):
        if text == "":
            ein = self.eingabe_auswerten()
            res = self.darsteller_lesen(ein)
            self.onDarstellerFilme(res)
        else:
            liste = self.listWidgetFilme.findItems(text, QtCore.Qt.MatchContains)
            items = []
            for i in liste:
                items.append(i.text())
            self.listWidgetFilme.clear()
            self.listWidgetFilme.addItems(items)

    def onPartnerZeigen(self):
        app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.start_bilder = 0
        self.aktuelles_res = []
        for i in range(self.listWidgetDarsteller.count()):
            self.aktuelles_res.append(str(self.listWidgetDarsteller.item(i).text()).strip())
        
        if not self.aktuelles_res:
            app.restoreOverrideCursor()
            return
        self.ausgabedarsteller()
        app.restoreOverrideCursor()
        self.suchfeld.setFocus()
        self.partner = 1
    # end of onPartnerZeigen
    
    def onPseudo(self):
        ein = self.eingabe_auswerten()
        if ein == "=":
            return
        zu_lesen = "SELECT pseudo FROM pordb_pseudo WHERE darsteller = %s ORDER BY pseudo"
        lese_func = DBLesen(self, zu_lesen, ein.lstrip('='))
        res = DBLesen.get_data(lese_func)
        pseudos = []
        for i in res:
            pseudos.append(i[0].strip())
        bilddialog = PseudonymeBearbeiten(ein, pseudos)
        bilddialog.exec_()
        self.suchfeld.setFocus()
    # end of onPseudo
    
    def onSuchen(self, suchfilterMpg=None, suchfilterVid=None):
        import locale
        locale.setlocale(locale.LC_ALL, '')
        ein = str(self.lineEditSuchen.text()).strip().replace(".", " ")
        
        filesizefrom = 0
        filesizeto = 0
        if self.lineEditFilesizeFrom.text():
            try:
                filesizefrom = float(self.lineEditFilesizeFrom.text().replace(",", "."))
            except:
                self.lineEditFilesizeFrom.setFocus()
                self.lineEditFilesizeFrom.selectAll()
                QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("Only digits allowed as filesize"))
                return
        if self.lineEditFilesizeTo.text():
            try:
                filesizeto = float(self.lineEditFilesizeTo.text().replace(",", "."))
            except:
                self.lineEditFilesizeTo.setFocus()
                self.lineEditFilesizeTo.selectAll()
                QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("Only digits allowed as filesize"))
                return
        
        if not ein and not filesizefrom and not filesizeto:
            self.lineEditSuchen.setFocus()
            return
            
        werte = []
        if ein:
            zu_lesen = "SELECT * FROM pordb_mpg_katalog WHERE LOWER(file) LIKE %s" 
            werte.append("%" + ein.lower().replace(" ", "%") + "%")
            if suchfilterMpg:
                zu_lesen += " AND LOWER(file) LIKE %s"
                werte.append("%" + suchfilterMpg + "%")
        else:
            zu_lesen = "SELECT * FROM pordb_mpg_katalog WHERE "
        if filesizefrom:
            if self.comboBoxFilesizeUnit.currentText() == "MB":
                faktor = 1048576
            elif self.comboBoxFilesizeUnit.currentText() == "GB":
                faktor = 1073741824    
            else:
                faktor = 1
            groesse1 = (filesizefrom - 0.005) * faktor
            if filesizeto:
                groesse2 = (filesizeto + 0.005) * faktor
                if groesse2 <= groesse1:
                    self.lineEditFilesizeTo.setFocus()
                    self.lineEditFilesizeTo.selectAll()
                    QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("Filesize to must be bigger than filesize from"))
                    return
                    
            else:
                groesse2 = (filesizefrom + 0.005) * faktor
            if ein:
                zu_lesen += " AND "
            zu_lesen += "groesse >= %s AND groesse < %s"
            werte.append(groesse1)
            werte.append(groesse2)
            if suchfilterMpg:
                zu_lesen += " AND LOWER(file) LIKE %s"
                werte.append("%" + suchfilterMpg + "%")
        zu_lesen += " ORDER BY file"
        if len(ein) < 3 and not filesizefrom:
            self.lineEditSuchen.setFocus()
            QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("Please enter at least 3 characters in the searchfield"))
            return
            
        app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        lese_func = DBLesen(self, zu_lesen, werte)
        rows = DBLesen.get_data(lese_func)
        self.searchResultsMpg = rows
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.clear()
        self.tableWidget.setRowCount(len(rows))
        zeilen = []
        if len(rows) == 0:
            self.tableWidget.setColumnCount(0)
        else:
            self.tableWidget.setColumnCount(len(rows[0]) + 2)
            for i in range(len(rows)):
                zeile = list(rows[i])
                if rows[i][4]:
                    zeile.append(round(rows[i][4] / 1024.0 / 1024.0, 2))
                    zeile.append(round(rows[i][4] / 1024.0 / 1024.0 / 1024.0, 2))
                zeilen.append(zeile)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setHorizontalHeaderLabels(self.fieldnames_mpg)
        for i in range(len(zeilen)):
            for j in range(len(zeilen[i])):
                try:    # fieldtype is char
                    newitem = QtWidgets.QTableWidgetItem(zeilen[i][j].strip())
                except:
                    try:    # fieldtype is int
                        newitem = QtWidgets.QTableWidgetItem()
                        if type(zeilen[i][j]) == int:
                            wert = locale.format("%d", zeilen[i][j], grouping=True)
                            newitem.setData(0, wert)
                        elif type(zeilen[i][j]) == float:
                            wert = locale.format("%.2f", zeilen[i][j], grouping=True)
                            newitem.setData(0, wert)
                        else:
                            newitem.setData(0, str(int(zeilen[i][j])))
                    except:    # fieldtype is None
                        newitem = QtWidgets.QTableWidgetItem(" ")
                self.tableWidget.setItem(i, j, newitem)
        try:
            self.tableWidget.setSortingEnabled(True)
            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.resizeRowsToContents()
        except:
            pass
        self.tableWidget.scrollToTop()
        zeilen = len(rows)
        self.labelMpgGefunden.setText(str(zeilen) +self.tr(" found"))
        self.labelMpgFound.clear()
            
        self.tableWidget1.clearContents()
        if ein:
            werte = []
            werte_erweiterung = []
            zu_lesen = "SELECT * FROM pordb_original WHERE LOWER(original) LIKE %s"
            werte.append("%" + ein.lower().replace(" ", "%") + "%")
            if suchfilterVid:
                zu_lesen += " AND LOWER(original) LIKE %s"
                werte.append("%" + suchfilterVid + "%")
            lese_func = DBLesen(self, zu_lesen, werte)
            res = DBLesen.get_data(lese_func)
            original_erweiterung = ""
            for i in res:
                original_erweiterung += " OR primkey = %s"
                werte_erweiterung.append(str(i[2]))
            
            werte = []
            zu_lesen = "SELECT * FROM pordb_vid WHERE (LOWER(original) LIKE %s OR LOWER(titel) LIKE %s)"
            werte.append("%" + ein.lower() + "%")
            werte.append("%" + ein.lower().replace(" ", "%") + "%")
            if suchfilterVid:
                zu_lesen += " AND (LOWER(original) LIKE %s OR LOWER(titel) LIKE %s)"
                werte.append("%" + suchfilterVid + "%")
                werte.append("%" + suchfilterVid + "%")
            if original_erweiterung:
                zu_lesen += original_erweiterung
                werte.extend(werte_erweiterung)
            lese_func = DBLesen(self, zu_lesen, werte)
            res = DBLesen.get_data(lese_func)
            self.searchResultsVid = res
            
            self.tableWidget1.setSortingEnabled(False)
            self.tableWidget1.setRowCount(len(res))
            if len(res) == 0:
                self.tableWidget1.setColumnCount(0)
            else:
                self.tableWidget1.setColumnCount(len(res[0]))
            self.tableWidget1.setAlternatingRowColors(True)
            self.tableWidget1.setHorizontalHeaderLabels(self.fieldnames_vid)
            for i in range(len(res)):
                for j in range(len(res[0])):
                    try:    # fieldtype is char
                        newitem = QtWidgets.QTableWidgetItem(res[i][j].strip())
                    except:
                        try:    # fieldtype is int
                            newitem = QtWidgets.QTableWidgetItem(str(res[i][j]))
                        except:    # fieldtype is None
                            newitem = QtWidgets.QTableWidgetItem(" ")
                    self.tableWidget1.setItem(i, j, newitem)
            try:
                self.tableWidget1.setSortingEnabled(True)
                self.tableWidget1.resizeColumnsToContents()
                self.tableWidget1.resizeRowsToContents()
            except:
                pass
            self.tableWidget1.scrollToTop()
            zeilen = len(res)
            self.labelVidGefunden.setText(str(zeilen) +self.tr(" found"))
        else:
            self.labelVidGefunden.clear()
            self.tableWidget1.setColumnCount(0)
            self.tableWidget1.setRowCount(0)
        self.labelVidFound.clear()
        app.restoreOverrideCursor()
        self.suchfeld.setFocus()
    # end of onSuchen
    
    def onSearchMpg(self):
        if self.searchResultsMpg:
            anzahl = self.searchResults(self.lineEditSearchMpg, self.tableWidget, self.searchResultsMpg, (2,))
            self.labelMpgFound.setText(self.tr("found: ") + str(anzahl))
        
    def onSearchVid(self):
        if self.searchResultsVid:
            anzahl = self.searchResults(self.lineEditSearchVid, self.tableWidget1, self.searchResultsVid, (0, 5))
            self.labelVidFound.setText(self.tr("found: ") + str(anzahl))
            
    def onFilterMpg(self):
        self.onSuchen(str(self.lineEditSearchMpg.text()).lower(), str(self.lineEditSearchVid.text()).lower())
        
    def onFilterVid(self):
        self.onSuchen(str(self.lineEditSearchMpg.text()).lower(), str(self.lineEditSearchVid.text()).lower())
            
    def onDeleteMpgKatalog(self):
        items = self.tableWidget.selectedItems()
        zu_erfassen = []
        anzahl_werte = int(len(items) / len(self.fieldnames_mpg))
        for i in range(anzahl_werte):
            werte = []
            werte.append(items[i * len(self.fieldnames_mpg)].text().strip())
            werte.append(items[i * len(self.fieldnames_mpg) + 1].text().strip())
            werte.append(items[i * len(self.fieldnames_mpg) + 2].text().strip())
            zu_erfassen.append(["DELETE FROM pordb_mpg_katalog WHERE device = %s and dir = %s and file = %s", werte])
        if zu_erfassen:
            update_func = DBUpdate(self, zu_erfassen)
            DBUpdate.update_data(update_func)
            QtWidgets.QMessageBox.critical(self, self.tr("Information "), str(anzahl_werte) + self.tr(" line(s) deleted"))
        app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.onSuchen()
        app.restoreOverrideCursor()
        
    def searchResults(self, lineEdit, tableWidget, rows, column):
        tableWidget.clearSelection()
        tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        suchbegriff = str(lineEdit.text()).lower()
        item_scroll = None
        row_scroll = 0
        selected_items = []
        zaehler = 0
        for j in column:
            row_zaehler = 0
            for i in range(len(rows)):
                row_zaehler += 1
                item = tableWidget.item(i, j)
                text = str(item.text()).lower()
                if suchbegriff in text:
                    zaehler += 1
                    if zaehler == 1:
                        if row_scroll == 0 or row_zaehler < row_scroll:
                            item_scroll = item
                            row_scroll = row_zaehler
                    if not i in selected_items:
                        tableWidget.selectRow(i)
                        selected_items.append(i)
        if item_scroll:
            tableWidget.scrollToItem(item_scroll)
        tableWidget.setFocus()
        return zaehler
    
    def onClear(self):
        self.lineEditSuchen.clear()
        self.lineEditFilesizeFrom.clear()
        self.lineEditFilesizeTo.clear()
        self.lineEditSuchen.setFocus()
        self.comboBoxFilesizeUnit.setCurrentIndex(0)
        self.lineEditSearchMpg.clear()
        self.lineEditSearchVid.clear()
        
    def onDateinamenUebernehmen(self):
        self.suchfeld.insertItem(0, self.lineEditSuchen.text())
        self.suchfeld.setCurrentIndex(0)
        self.suchfeld.setFocus()
        
    def onClearURL(self):
        self.lineEditURL.clear()
        self.lineEditURL.setFocus()
        
    def onLoadStarted(self):
        app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        
    def onLoadFinished(self, arg):
        app.restoreOverrideCursor()
        self.suchfeld.setFocus()
        
    def onVideoSuchen(self):
        text = str(self.webView.page().mainFrame().toHtml())
        actordata = ActorData(text)
        titel = ActorData.actor_list_of_movies(actordata)
        if titel:
            self.video_anzeigen(titel)
            
    def onIAFDSeite(self):
        self.webView.load(QtCore.QUrl("http://www.iafd.com/"))
        
    def onSearchWebsite(self):
        searchstring = self.lineEditSearchWebsite.text()
        self.webView.page().findText(searchstring)
        
    def onDarstellerdatenAbholen(self):
        url = self.webView.url().toString()
        ende = url.find("gender=") + 8
        url = url[0:ende]
        text = str(self.webView.page().mainFrame().toHtml())
        bilddialog = DarstellerdatenAnzeigen(app, url, text, self.verzeichnis_thumbs)
        fehler = False
        try:
            bilddialog.geschlecht
        except:
            fehler = True
        if fehler:
            QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("Seems IAFD site is offline"))
            return

        bilddialog.exec_()
        self.suchfeld.setFocus()
        
        self.darsteller_lesen("=" +bilddialog.name)
        self.onbildAnzeige()
        
    def onMovieData(self):
        url = self.webView.url().toString()
        text = str(self.webView.page().mainFrame().toHtml())
        movie_data = SaveMovieData(app, url, text)
        res = SaveMovieData.get_data(movie_data)
        if res and res[2]:
            show_iafd_data = ShowIafdData(self.verzeichnis, self.verzeichnis_original, self.verzeichnis_thumbs, self.verzeichnis_trash, self.verzeichnis_cover, res)
            show_iafd_data.exec_()
        if str(self.labelDarsteller.text()) != "":
            self.darsteller_lesen("=" +str(self.labelDarsteller.text()).strip().title())
            self.onbildAnzeige()
        self.suchfeld.setFocus()
        
    def onLinkClicked(self, url):
        self.webView.load(QtCore.QUrl(url))
        
    def onUrlChanged(self, url):
        self.url = url.toString()
        self.statusBar.showMessage(self.url)
        
    def GetWebsite(self):
        if str(self.lineEditURL.text()).startswith("http://") or str(self.lineEditURL.text()).startswith("https://"):
            url = self.lineEditURL.text()
        else:
            url = "http://" + self.lineEditURL.text()
        self.webView.load(QtCore.QUrl(url))
        self.statusBar.showMessage(url)
        
    def onUrlVerwalten(self):
        if self.url:
            url = str(self.url)
        else:
            url = "http://www.iafd.com/"
        bookmarks = Bookmarks(url)
        bookmarks.exec_()
        neue_url = None
        try:
            neue_url = bookmarks.neue_url
        except:
            pass
        if neue_url:
            self.lineEditURL.setText(neue_url)
            self.lineEditURL.setFocus()
            self.webView.load(QtCore.QUrl(self.lineEditURL.text()))
        
        self.suchfeld.setFocus()
            
    def onStatistikCS(self):
        self.tableWidgetStatistik.setSortingEnabled(False)
        self.tableWidgetStatistik.clear()
        self.tableWidgetStatistik.setRowCount(len(self.cumshots) + 1)
        self.tableWidgetStatistik.setColumnCount(2)
        self.tableWidgetStatistik.setAlternatingRowColors(True)
        j = -1
        gesamt = 0
        for i in list(self.cumshots.keys()):
            zu_lesen = "SELECT sum(cs" +i +") FROM pordb_vid" 
            lese_func = DBLesen(self, zu_lesen)
            res = DBLesen.get_data(lese_func)
            if res[0][0]:
                gesamt += res[0][0]
            newitem = QtWidgets.QTableWidgetItem(self.cumshots[i])
            j += 1
            self.tableWidgetStatistik.setItem(j, 0, newitem)
            newitem = QtWidgets.QTableWidgetItem()
            if res[0][0]:
                newitem.setData(0, res[0][0])
            else:
                newitem.setData(0, 0)
            newitem.setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
            self.tableWidgetStatistik.setItem(j, 1, newitem)
        newitem = QtWidgets.QTableWidgetItem(self.tr("Summary"))
        j += 1
        self.tableWidgetStatistik.setItem(j, 0, newitem)
        newitem = QtWidgets.QTableWidgetItem()
        newitem.setData(0, gesamt)
        newitem.setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.tableWidgetStatistik.setItem(j, 1, newitem)
        self.tableWidgetStatistik.resizeColumnsToContents()
        self.tableWidgetStatistik.resizeRowsToContents()
        self.tableWidgetStatistik.setSortingEnabled(True)
        self.tableWidgetStatistik.sortItems(1)
        self.suchfeld.setFocus()
        
    def onStatistikDarstellerW(self):
        try:
            anzahl = int(self.lineEditAnzahlW.text())
        except:
            QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("Quantity is not a number"))
            return
        werte = []
        werte.append(anzahl)
        zu_erfassen = []
        zu_erfassen.append(["UPDATE pordb_vid_neu SET partnerw = %s", werte])
        update_func = DBUpdate(self, zu_erfassen)
        DBUpdate.update_data(update_func)
        self.onStatistikDarsteller("w", anzahl)
        
    def onStatistikDarstellerM(self):
        try:
            anzahl = int(self.lineEditAnzahlM.text())
        except:
            QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("Quantity is not a number"))
            return
        werte = []
        werte.append(anzahl)
        zu_erfassen = []
        zu_erfassen.append(["UPDATE pordb_vid_neu SET partnerm = %s", werte])
        update_func = DBUpdate(self, zu_erfassen)
        DBUpdate.update_data(update_func)
        self.onStatistikDarsteller("m", anzahl)
        
    def onStatistikDarsteller(self, sex, anzahl):
        zu_lesen = "SELECT darsteller, anzahl, partner, nation, geboren, filme FROM pordb_darsteller WHERE sex = %s AND partner > %s ORDER BY partner, darsteller"
        lese_func = DBLesen(self, zu_lesen, (sex, str(anzahl)))
        res = DBLesen.get_data(lese_func)
        self.tableWidgetStatistik.setSortingEnabled(False)
        self.tableWidgetStatistik.clear()
        self.tableWidgetStatistik.setRowCount(len(res))
        self.tableWidgetStatistik.setColumnCount(6)
        self.tableWidgetStatistik.setAlternatingRowColors(True)
        j = -1
        for i in res:
            newitem = QtWidgets.QTableWidgetItem(i[0])
            j += 1
            self.tableWidgetStatistik.setItem(j, 0, newitem)
            newitem = QtWidgets.QTableWidgetItem()
            newitem.setData(0, i[1])
            newitem.setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
            self.tableWidgetStatistik.setItem(j, 1, newitem)
            newitem = QtWidgets.QTableWidgetItem()
            newitem.setData(0, i[2])
            newitem.setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
            self.tableWidgetStatistik.setItem(j, 2, newitem)
            if i[3]:
                newitem = QtWidgets.QTableWidgetItem(i[3])
            else:
                newitem = QtWidgets.QTableWidgetItem("")
            self.tableWidgetStatistik.setItem(j, 3, newitem)
            try:
                geboren = (str(i[4])[0:10]).split("-")
                jahr = int(geboren[0])
                monat = int(geboren[1])
                tag = int(geboren[2])
                if jahr != 1:
                    alter = age(datetime.date(jahr, monat, tag))
                    newitem = QtWidgets.QTableWidgetItem(str(alter))
                else:
                    newitem = QtWidgets.QTableWidgetItem()
            except:
                newitem = QtWidgets.QTableWidgetItem()
            self.tableWidgetStatistik.setItem(j, 4, newitem)
            newitem = QtWidgets.QTableWidgetItem()
            if i[5]:
                newitem.setData(0, i[5])
            else:
                newitem.setData(0, 0)
            newitem.setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
            self.tableWidgetStatistik.setItem(j, 5, newitem)
        self.tableWidgetStatistik.setHorizontalHeaderLabels([self.tr("Actor"), self.tr("Quantity"), self.tr("Partner"), self.tr("Nation"), self.tr("Age"), self.tr("Movies")])
        self.tableWidgetStatistik.setSortingEnabled(True)
        self.tableWidgetStatistik.sortItems(2, 1)
        self.tableWidgetStatistik.resizeColumnsToContents()
        self.tableWidgetStatistik.resizeRowsToContents()
        self.tableWidgetStatistik.scrollToTop()
        self.suchfeld.setFocus()
        
    def onStatistikAnzahlClips(self):
        zu_lesen = "SELECT COUNT (*) FROM pordb_vid"
        lese_func = DBLesen(self, zu_lesen)
        res = DBLesen.get_data(lese_func)
        try:
            QtWidgets.QMessageBox.information(self, "PorDB", self.tr("Quantity of movies: ") +str(res[0][0]))
        except:
            pass
        self.suchfeld.setFocus()
        
    def onStatistikAnzahlClipsJahr(self):
        app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        zu_lesen = "SELECT DISTINCT original FROM pordb_vid"
        lese_func = DBLesen(self, zu_lesen)
        res = DBLesen.get_data(lese_func)
        
        jahre = {}
        gesamt = 0
        for i in res:
            if i[0] and i[0].strip() and i[0].strip()[-1] == ")":
                original = i[0].strip()
                jahr = original[-5:-1]
                if jahr.isdigit():
                    if jahr in jahre:
                        jahre[jahr] = jahre[jahr] +1
                    else:
                        jahre[jahr] = 1
                    gesamt += 1
                    
        s = list(jahre.keys())
        if not s:
            app.restoreOverrideCursor()
            return
        s.sort()
        jahr_min = s[0]
        jahr_max = s[-1]
        jahre_titel = list(range(int(jahr_min), int(jahr_max) +1))
        j = -1
        for i in jahre_titel:
            j += 1
            jahre_titel[j] = str(i)

        #datum_akt = str(time.localtime()[0]) + '-' + str(time.localtime()[1]) + '-' + str(time.localtime()[2])
        
        self.tableWidgetStatistik.setSortingEnabled(False)
        self.tableWidgetStatistik.clear()
        self.tableWidgetStatistik.setRowCount(len(jahre_titel))
        self.tableWidgetStatistik.setColumnCount(2)
        self.tableWidgetStatistik.setAlternatingRowColors(True)
        j = -1
        datum_alt = "1900-01-01"
        gesamt = 0
        for i in jahre_titel:
            j += 1
            k = 0
            newitem = QtWidgets.QTableWidgetItem()
            newitem.setData(0, i)
            newitem.setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
            self.tableWidgetStatistik.setItem(j, k, newitem)
            k = 1
            newitem = QtWidgets.QTableWidgetItem()
            try:
                newitem.setData(0, jahre[i])
            except:
                newitem.setData(0, 0)
            newitem.setTextAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
            self.tableWidgetStatistik.setItem(j, k, newitem)
            try:
                gesamt += jahre[i]
            except:
                pass
        if datum_alt != "1900-01-01":
            k += 1
            newitem = QtWidgets.QTableWidgetItem()
            newitem.setData(0, gesamt)
            newitem.setTextAlignment(QtCore.Qt.AlignRight)
            self.tableWidgetStatistik.setItem(j, k, newitem)
        self.tableWidgetStatistik.setHorizontalHeaderLabels([self.tr("Year"), self.tr("Quantity")])
        self.tableWidgetStatistik.resizeColumnsToContents()
        self.tableWidgetStatistik.resizeRowsToContents()
        self.tableWidgetStatistik.setSortingEnabled(True)
        self.tableWidgetStatistik.sortItems(0)
        self.tableWidgetStatistik.scrollToBottom()
        
        app.restoreOverrideCursor()
        self.suchfeld.setFocus()
        
    def onCheckNewVersion(self, initial=True):
        def change_tables_definition():
            zu_erfassen = []
            werte = []
            zu_lesen = "SELECT Column_Name from information_schema.columns where table_name = 'pordb_vid' and Column_Name = 'remarks'"
            lese_func = DBLesen(self, zu_lesen)
            res = DBLesen.get_data(lese_func)
            if not res:
                zu_erfassen.append(["ALTER TABLE pordb_vid ADD COLUMN remarks VARCHAR(256)", werte])
            zu_lesen = "SELECT Column_Name from information_schema.columns where table_name = 'pordb_vid' and Column_Name = 'stars'"
            lese_func = DBLesen(self, zu_lesen)
            res = DBLesen.get_data(lese_func)
            if not res:
                zu_erfassen.append(["ALTER TABLE pordb_vid ADD COLUMN stars INTEGER", werte])
            if zu_erfassen:
                update_func = DBUpdate(self, zu_erfassen)
                DBUpdate.update_data(update_func)
            
        app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        version = None
        whatsnew = None
        seite = None
        try:
            seite = urllib.request.urlopen(FILE_VERSION).read()
        except (urllib.error.URLError, socket.timeout) as e:
            app.restoreOverrideCursor()
            message = QtWidgets.QMessageBox.critical(self, self.tr("Error "), str(e))
            return            
    
        if seite:
            begin = str(seite).find("pordbversion")
            version = str(seite)[begin + 21 : begin + 21 + str(seite)[begin + 21 :].find("&")]
            if version != __version__:
                begin = str(seite).find("whatsnew")
                whatsnew = str(seite)[begin + 17 : begin + 17 + str(seite)[begin + 17 :].find("&")]
                dialog = UpdateVersion(version, whatsnew)
                if dialog.exec_():
                    change_tables_definition()
                    desktop_directory = os.path.join(os.path.expanduser("~"), ".local", "share", "applications")
                    desktop_datei = os.path.join(desktop_directory, "PorDB.desktop")
                    if not os.path.exists(desktop_directory):
                        os.makedirs(desktop_directory)
                    messageBox = QtWidgets.QMessageBox()
                    messageBox.addButton(self.tr("Yes"), QtWidgets.QMessageBox.AcceptRole)
                    messageBox.addButton(self.tr("No"), QtWidgets.QMessageBox.RejectRole)
                    messageBox.setWindowTitle(self.tr("Menu entry"))
                    messageBox.setIcon(QtWidgets.QMessageBox.Question)
                    messageBox.setText(self.tr("Should I create a menu entry?"))
                    message = messageBox.exec_()
                    if message == 0:
                        try:
                            datei = open(desktop_datei, "w")
                            datei.write("[Desktop Entry]" + "\n")
                            datei.write("Comment=PorDB" + "\n")
                            datei.write("Exec=python3 " + os.path.join(os.getcwd(), "pordb.py") + "\n")
                            datei.write("Icon=" + os.path.join(os.getcwd(), "pypordb", "8027068_splash.png") + "\n")
                            datei.write("Name=PorDB" + "\n")
                            datei.write("NoDisplay=false" + "\n")
                            datei.write("Path[$e]=" + os.getcwd() + "\n")
                            datei.write("StartupNotify=true" + "\n")
                            datei.write("Terminal=0" + "\n")
                            datei.write("TerminalOptions=" + "\n")
                            datei.write("Type=Application" + "\n")
                            datei.write("Categories=Graphics;" + "\n")
                            datei.write("X-KDE-SubstituteUID=false" + "\n")
                            datei.write("X-KDE-Username=" + "\n")
                            datei.close()
                            message = QtWidgets.QMessageBox.information(self, self.tr("Information "), self.tr("Menu entry added under graphics"))
                        except:
                            message = QtWidgets.QMessageBox.critical(self, self.tr("Error "), self.tr("Adding of menu entry failed"))
                            
                    python = sys.executable
                    os.execl(python, python, * sys.argv)
            else:
                if not self.initial_run:
                    app.restoreOverrideCursor()
                    message = QtWidgets.QMessageBox.information(self, self.tr("Information "), self.tr("You have the latest version"))
                    self.suchfeld.setFocus()
        app.restoreOverrideCursor()
        
    def onSuchbegriffe(self):
        bilddialog = SuchbegriffeBearbeiten()
        bilddialog.exec_()
        self.suchbegriffe_lesen()
        self.suchfeld.setFocus()
        
    def onLand(self):
        bilddialog = LandBearbeiten(self.comboBoxNation, self.nation_fuellen)
        bilddialog.exec_()
        self.suchfeld.setFocus()
        
    def onBackup(self):
        app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        import tarfile
        # Backup database
        if self.checkBoxDatabase.isChecked():
            subprocess.check_output(["pg_dump", DBNAME, "-f", os.path.join(self.verzeichnis_original, DBNAME + ".sql")], universal_newlines=True)
                
        # Backup picture directory
        if self.checkBoxPictures.isChecked():
            tar = tarfile.open(os.path.join(self.verzeichnis_original, "archive.tar.gz"), "w:gz")
            tar.add(self.verzeichnis_thumbs)
            tar.close()
            
            datei = open(os.path.join(self.verzeichnis_original, "archive.tar.gz"), "rb")
            partnum = 0
            while True:
                chunk = datei.read(100000000)
                if not chunk:
                    break
                partnum += 1
                filename = os.path.join(self.verzeichnis_original, ("pordb_part%04d" % partnum))
                fileobj = open(filename, "wb")
                fileobj.write(chunk)
                fileobj.close()
            
            datei.close()
            os.remove(os.path.join(self.verzeichnis_original, "archive.tar.gz"))
        
        app.restoreOverrideCursor()
        self.suchfeld.setFocus()
        message = QtWidgets.QMessageBox(self)
        message.setText(self.tr("Backup in directory ") +self.verzeichnis_original + self.tr(" created"))
        message.exec_()
        
    def onRestore(self):
        app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        import tarfile
        nachricht = self.tr("No files found for restoring")
        
        # Restore the database
        datei = os.path.join(self.verzeichnis_original, DBNAME + ".sql")
        if os.path.exists(datei):
            conn.close()
            subprocess.check_output(["dropdb", DBNAME], universal_newlines=True)
            subprocess.check_output(["createdb", "-O", "postgres", "-E", "UTF8", "-T", "template0", DBNAME], universal_newlines=True)
            subprocess.check_output(["psql", "-d", DBNAME, "-f", os.path.join(self.verzeichnis_original, DBNAME + ".sql")], universal_newlines=True)
            #os.remove(datei)
        else:
            app.restoreOverrideCursor()
            message = QtWidgets.QMessageBox(self)
            message.setText(self.tr("No backup file in directory ") +self.verzeichnis_original + self.tr(" found"))
            message.exec_()
            return
        
        nachricht = self.tr("Database restore was successful, you can now delete your backup file")

        # Restore the picture directory
        parts = os.listdir(self.verzeichnis)
        parts.sort()
        output = open(os.path.join(self.verzeichnis, "archive.tar.gz"), "wb")
        bilddatei_gefunden = False
        for filename in parts:
            if filename.startswith("pordb_part"):
                bilddatei_gefunden = True
                filepath = os.path.join(self.verzeichnis, filename)
                fileobj = open(filepath, "rb")
                while True:
                    filebytes = fileobj.read(100000000)
                    if not filebytes:
                        break
                    output.write(filebytes)
                fileobj.close()
        output.close()
        if os.path.isfile(os.path.join(self.verzeichnis, "archive.tar.gz")) and os.path.getsize(os.path.join(self.verzeichnis, "archive.tar.gz")) == 0:
            os.remove(os.path.join(self.verzeichnis, "archive.tar.gz"))
        if bilddatei_gefunden:
            if os.path.isfile(os.path.join(self.verzeichnis, "archive.tar.gz")):
                tar = tarfile.open(os.path.join(self.verzeichnis, "archive.tar.gz"))
                try:
                    tar.extractall(path=self.verzeichnis)
                except:
                    self.suchfeld.setFocus()
                    message = QtWidgets.QMessageBox(self)
                    message.setText(self.tr("Restore from directory ") + self.verzeichnis + self.tr(" failed. In most cases there is a file with an invalid creation/change date."))
                    message.exec_()
                    app.restoreOverrideCursor()
                    return
                tar.close()
            else:
                self.suchfeld.setFocus()
                app.restoreOverrideCursor()
                message = QtWidgets.QMessageBox(self)
                message.setText(self.tr("Restore from directory ") + self.verzeichnis + self.tr(" failed. No backup files found."))
                message.exec_()
                return
            
            nachricht += "; " + self.tr("Backup in directory ") + self.verzeichnis + self.tr(" restored. You can now copy the complete directory to its origin place.")

        app.restoreOverrideCursor()
        self.suchfeld.setFocus()
        message = QtWidgets.QMessageBox(self)
        message.setText(nachricht)
        message.exec_()
        
    def onWartung(self):
        app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        os.system("vacuumdb" + " --analyze " + DBNAME)
        app.restoreOverrideCursor()
        self.suchfeld.setFocus()
        message = QtWidgets.QMessageBox(self)
        message.setText(self.tr("Maintenance executed"))
        message.exec_()
        
    def device_fuellen(self):
        zu_lesen = "SELECT * FROM pordb_mpg_verzeichnisse ORDER BY dir"
        lese_func = DBLesen(self, zu_lesen)
        res = DBLesen.get_data(lese_func)
        self.comboBoxDevice.clear()
        if res:
            for i in res:
                self.comboBoxDevice.addItem(i[0])
        self.comboBoxDevice.setCurrentIndex(-1)
        self.suchfeld.setFocus()
        
    def onDevicesVerwalten(self):
        bilddialog = Devices(self.device_fuellen)
        bilddialog.exec_()
        self.suchfeld.setFocus()
            
    def onStartScan(self):
        if not self.comboBoxDevice.currentText():
            message = QtWidgets.QMessageBox(self)
            message.setText(self.tr("Select device"))
            message.exec_()
            return
            
        self.verzeichnis_tools = str(QtWidgets.QFileDialog.getExistingDirectory(self, self.tr("Select directory"), "/"))
        if self.verzeichnis_tools:
            if self.checkBoxSubdirectories.isChecked():
                self.dateien = []
                liste = os.walk(self.verzeichnis_tools)
                for root, dirs, files in liste:
                    for file_ in files:
                        self.dateien.append([root, file_])
            else:
                self.dateien = os.listdir(self.verzeichnis_tools)
            self.dateien.sort()
        else:
            return
        
        for i in self.dateien:
            if len(i) > 256:
                message = QtWidgets.QMessageBox(self)
                message.setText(self.tr("Error, filename ") +i +self.tr(" to long"))
                message.exec_()
                return
            
        #self.threadPool = []
        
        # generic thread using signal
        #self.threadPool.append(GenericThread(self.addFiles))
        # signal for updating current file
        #self.disconnect(self, QtCore.SIGNAL("add(QString)"), self.updateFileLabel)
        #self.connect(self, QtCore.SIGNAL("add(QString)"), self.updateFileLabel)
        # signal for finished
        #self.disconnect(self, QtCore.SIGNAL("finished"), self.output_result)
        #self.connect(self, QtCore.SIGNAL("finished"), self.output_result)
        # start thread
        #self.threadPool[len(self.threadPool)-1].start()
        
        app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.addFiles()
        self.output_result()
        app.restoreOverrideCursor()
        
    # end of onStartScan
    
    def addFiles(self):
        self.res_duplicates = []
        zu_erfassen = []
        
        for i in self.dateien:
            if type(i) == str:
                filepath = os.path.join(self.verzeichnis_tools, i)
                directory = self.verzeichnis_tools
                file_ = i
            else:
                filepath = os.path.join(i[0], i[1].strip())
                directory = i[0]
                file_ = i[1]
            if os.path.isfile(filepath):
                #self.emit(QtCore.SIGNAL("add(QString)"), i)
                zu_lesen = "SELECT * FROM pordb_mpg_katalog WHERE file = %s OR groesse = %s"
                lese_func = DBLesen(self, zu_lesen, (file_, str(os.path.getsize(filepath))))
                res = DBLesen.get_data(lese_func)
                in_datenbank = True
                for j in res:
                    if j[0].strip() == str(self.comboBoxDevice.currentText()).strip() and j[1].strip() == os.path.basename(directory) and j[2].replace("'", "''").strip() == file_.replace("'", "''").strip():
                        in_datenbank = False
                    
                if in_datenbank:
                    for j in res:
                        # put only in duplicate list, when actual directory is another one than that in database
                        if j[1].strip() != directory.strip(): 
                            a = list(j)
                            a.append(file_)
                            a.append(int(os.path.getsize(os.path.join(filepath))))
                            self.res_duplicates.append(a)
                    werte = []
                    werte.append(str(self.comboBoxDevice.currentText()))
                    werte.append(os.path.basename(directory))
                    werte.append(file_)
                    werte.append(None)
                    werte.append(os.path.getsize(filepath))
                    zu_erfassen.append(["INSERT INTO pordb_mpg_katalog VALUES (%s, %s, %s, %s, %s)", werte])
                    
        update_func = DBUpdate(self, zu_erfassen)
        DBUpdate.update_data(update_func)
        self.files_added = str(len(zu_erfassen))
        #self.emit(QtCore.SIGNAL("finished"))
        
    # end of addFiles
    
    def output_result(self):
        # jetzt die Dubletten in Tabelle ausgeben
        self.row = 0
        self.column = 0
        self.tableWidgetDubletten.clear()
        self.tableWidgetDubletten.setAlternatingRowColors(True)
        self.tableWidgetDubletten.setColumnCount(7)
        self.tableWidgetDubletten.setRowCount(len(self.res_duplicates))
        counter = 0
        for j in self.res_duplicates:
            # Checkbox
            newitem = QtWidgets.QTableWidgetItem()
            newitem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable)
            if os.path.join(self.verzeichnis_tools, j[5].strip()) == j[2].strip() and str(j[4]) == str(os.path.getsize(os.path.join(self.verzeichnis_tools, j[5].strip()))):
                newitem.setCheckState(QtCore.Qt.Checked)
                counter += 1
            else:
                newitem.setCheckState(QtCore.Qt.Unchecked)
            self.tableWidgetDubletten.setItem(self.row, self.column, newitem)
            self.column += 1
            newitem = QtWidgets.QTableWidgetItem(j[2].strip())     # Filename
            self.tableWidgetDubletten.setItem(self.row, self.column, newitem)
            self.column += 1
            newitem = QtWidgets.QTableWidgetItem(j[0].strip())        # Device
            self.tableWidgetDubletten.setItem(self.row, self.column, newitem)
            self.column += 1
            newitem = QtWidgets.QTableWidgetItem(j[1].strip())        # Directory
            self.tableWidgetDubletten.setItem(self.row, self.column, newitem)
            self.column += 1
            newitem = QtWidgets.QTableWidgetItem(str(j[4]))    # Size in database
            self.tableWidgetDubletten.setItem(self.row, self.column, newitem)
            self.column += 1
            newitem = QtWidgets.QTableWidgetItem(j[5].strip())     # new Filename
            self.tableWidgetDubletten.setItem(self.row, self.column, newitem)
            self.column += 1
            newitem = QtWidgets.QTableWidgetItem(str(j[6]))    # Size of new file
            self.tableWidgetDubletten.setItem(self.row, self.column, newitem)
            self.row += 1
            self.column = 0
            
        self.tableWidgetDubletten.setHorizontalHeaderLabels([self.tr("delete"), self.tr("File in database"), self.tr("Device"), self.tr("Directory"), self.tr("Size in database"), self.tr("new file"), self.tr("Size of new file")])
        self.tableWidgetDubletten.resizeColumnsToContents()
        self.tableWidgetDubletten.resizeRowsToContents()
        
        message = self.files_added + self.tr(" File(s) collected")
        if len(self.res_duplicates) > 0:
            self.pushButtonDeleteDuplicates.setEnabled(True)
            self.pushButtonDeselect.setEnabled(True)
            if counter > 0:
                message += ", " +str(counter) +self.tr(" Duplicate(s) found") 
            else:
                message += ", " +str(len(self.res_duplicates)) +self.tr(" Duplicate(s) found, but some of them only in relation to file size")
        
        self.labelMessage.setText(message)
        self.suchfeld.setFocus()
    # end of output_result
        
    def updateFileLabel(self, text):
        self.labelCurrentFile.setText(text)
        
    def onDeleteDuplicates(self):
        app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        zu_erfassen = []
        counter = 0
        for i in range(self.tableWidgetDubletten.rowCount()):
            if self.tableWidgetDubletten.item(i, 0).checkState():
                werte = []
                werte.append(str(self.comboBoxDevice.currentText()).strip())
                werte.append(os.path.basename(self.verzeichnis_tools))
                werte.append(str(self.tableWidgetDubletten.item(i, 5).text()).strip())
                zu_erfassen.append(["DELETE FROM pordb_mpg_katalog WHERE device = %s AND dir = %s AND file = %s", werte])
                try:
                    os.remove(os.path.join(self.verzeichnis_tools, str(self.tableWidgetDubletten.item(i, 5).text()).strip()))
                    counter += 1
                except:
                    pass
        if counter > 0:
            update_func = DBUpdate(self, zu_erfassen)
            DBUpdate.update_data(update_func)
            message = str(counter) +self.tr(" File(s) deleted")
        else:
            message = ""
        self.statusBar.showMessage(message)
        app.restoreOverrideCursor()
        self.suchfeld.setFocus()
        
    def onDeselect(self):
        for i in range(self.tableWidgetDubletten.rowCount()):
            self.tableWidgetDubletten.item(i, 0).setCheckState(QtCore.Qt.Unchecked)
        self.suchfeld.setFocus()
        
app = QtWidgets.QApplication(sys.argv)
app.setOrganizationName("pypordb")
app.setOrganizationDomain("pypordb")
locale = QtCore.QLocale.system().name()
#locale = "en_EN"
appTranslator = QtCore.QTranslator()
if appTranslator.load("pordb_" + locale, os.getcwd()):
    app.installTranslator(appTranslator)
dialog = MeinDialog()
dialog.show()
sys.exit(app.exec_())
