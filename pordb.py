#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import time
import datetime
import platform
import urllib.request, urllib.error, urllib.parse
from operator import itemgetter, attrgetter
import psycopg2
from PyQt4 import QtGui, QtCore
from PyQt4.QtWebKit import QWebPage
from PyQt4.QtWebKit import QWebFrame
import PyQt4.QtWebKit as webkit
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

size = QtCore.QSize(260, 260)
sizeneu = QtCore.QSize(500, 400)
size_neu = QtCore.QSize(130, 130)
size_darsteller = QtCore.QSize(1920, 1080)

dbname = "por"
initial_run = True

__version__ = "1.9.1"
file_version = "https://github.com/hwmay/pordb3/blob/master/version"

# Make a connection to the database and check to see if it succeeded.
db_host = "localhost"
try:
    conn = psycopg2.connect(database=dbname, host=db_host)
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

class MeinDialog(QtGui.QMainWindow, MainWindow):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        
        # Slot für Splitter zum Re-Scalen des Darstellerbildes
        self.connect(self.splitter, QtCore.SIGNAL("splitterMoved(int, int)"), self.bildSetzen)
        
        # Slot für Aktivieren von Buttons bei Wechsel des Tabs
        self.connect(self.tabWidget, QtCore.SIGNAL("currentChanged(int)"), self.onTabwechsel)
        
        # Slots einrichten für Bilder
        self.connect(self.actionNeueingabe, QtCore.SIGNAL("triggered()"), self.onNeueingabe)
        self.connect(self.actionDarsteller, QtCore.SIGNAL("triggered()"), self.onDarsteller)
        self.connect(self.actionCd, QtCore.SIGNAL("triggered()"), self.onCD)
        self.connect(self.actionTitel, QtCore.SIGNAL("triggered()"), self.onTitel)
        self.connect(self.actionOriginal, QtCore.SIGNAL("triggered()"), self.onOriginal)
        self.connect(self.actionSuche, QtCore.SIGNAL("triggered()"), self.onSuche)
        self.connect(self.actionDrucken, QtCore.SIGNAL("triggered()"), self.onDrucken)
        self.connect(self.tableWidgetBilder, QtCore.SIGNAL("cellDoubleClicked(int, int)"), self.onKorrektur)
        self.connect(self.tableWidgetBilderAktuell, QtCore.SIGNAL("cellDoubleClicked(int, int)"), self.onNeuDoubleClick)
        self.connect(self.tableWidgetBilder, QtCore.SIGNAL("customContextMenuRequested(QPoint)"), self.onContexttableWidgetBilder)
        self.tableWidgetBilderAktuell.__class__.dragEnterEvent = self.tableWidgetBilderAktuelldragEnterEvent
        self.tableWidgetBilder.__class__.dropEvent = self.tableWidgetBilderdropEvent
        self.connect(self.actionDarstellerUebernehmen, QtCore.SIGNAL("triggered()"), self.onDarstellerUebernehmen)
        self.connect(self.actionAnzeigenOriginal, QtCore.SIGNAL("triggered()"), self.onAnzeigenOriginal)
        self.connect(self.actionAnzeigenTitle, QtCore.SIGNAL("triggered()"), self.onAnzeigenTitle)
        self.connect(self.actionMassChange, QtCore.SIGNAL("triggered()"), self.onMassChange)
        self.connect(self.actionSortieren_nach_Darsteller, QtCore.SIGNAL("triggered()"), self.onSortieren_nach_Darsteller)
        self.connect(self.actionSortieren_nach_CD, QtCore.SIGNAL("triggered()"), self.onSortieren_nach_CD)
        self.connect(self.actionSortieren_nach_Titel, QtCore.SIGNAL("triggered()"), self.onSortieren_nach_Titel)
        self.connect(self.actionOriginal_umbenennen, QtCore.SIGNAL("triggered()"), self.onOriginal_umbenennen)
        self.connect(self.actionOriginal_weitere, QtCore.SIGNAL("triggered()"), self.onOriginal_weitere)
        self.connect(self.actionRedoImageChange, QtCore.SIGNAL("triggered()"), self.onRedoImageChange)
        self.connect(self.actionSortieren_nach_Original, QtCore.SIGNAL("triggered()"), self.onSortieren_nach_Original)
        self.connect(self.actionOriginalIntoClipboard, QtCore.SIGNAL("triggered()"), self.onOriginalIntoClipboard)
        self.connect(self.actionCovergross, QtCore.SIGNAL("triggered()"), self.onCovergross)
        self.connect(self.tableWidgetBilderAktuell, QtCore.SIGNAL("customContextMenuRequested(QPoint)"), self.onContexttableWidgetBilderAktuell)
        self.connect(self.actionBildLoeschen, QtCore.SIGNAL("triggered()"), self.onBildLoeschen)
        self.connect(self.actionFirst, QtCore.SIGNAL("triggered()"), self.onPageFirst)
        self.connect(self.actionPrev, QtCore.SIGNAL("triggered()"), self.onPageUp)
        self.connect(self.actionNext, QtCore.SIGNAL("triggered()"), self.onPageDown)
        self.connect(self.actionLast, QtCore.SIGNAL("triggered()"), self.onPageLast)
        self.connect(self.actionUndo, QtCore.SIGNAL("triggered()"), self.onUndo)
        self.connect(self.actionOnHelp, QtCore.SIGNAL("triggered()"), self.onHelp)
        self.connect(self.pushButtonDir, QtCore.SIGNAL("clicked()"), self.onDirectoryChange)
        self.connect(self.pushButtonRefresh, QtCore.SIGNAL("clicked()"), self.onDirectoryRefresh)
        
        # Slots einrichten für Darsteller
        self.connect(self.bildAnzeige, QtCore.SIGNAL("clicked()"), self.onbildAnzeige)
        self.connect(self.comboBoxSex, QtCore.SIGNAL("currentIndexChanged(int)"), self.setFocus)
        self.connect(self.pushButtonDarstellerspeichern, QtCore.SIGNAL("clicked()"), self.onDarstellerspeichern)
        self.connect(self.pushButtonIAFDholen, QtCore.SIGNAL("clicked()"), self.onIAFD)
        self.connect(self.pushButtonIAFDBackground, QtCore.SIGNAL("clicked()"), self.onIAFDBackground)
        self.connect(self.pushButtonDarstellerLoeschen, QtCore.SIGNAL("clicked()"), self.onDarstellerloeschen)
        self.connect(self.listWidgetDarsteller, QtCore.SIGNAL("customContextMenuRequested(QPoint)"), self.onContextDarsteller)
        self.connect(self.listWidgetDarsteller, QtCore.SIGNAL("itemDoubleClicked(QListWidgetItem*)"), self.onbildAnzeige)
        self.connect(self.actionAnzeigenPaar, QtCore.SIGNAL("triggered()"), self.onAnzeigenPaar)
        self.connect(self.labelBildanzeige, QtCore.SIGNAL("customContextMenuRequested(QPoint)"), self.onBildgross)
        self.labelBildanzeige.__class__.dragEnterEvent = self.tableWidgetBilderAktuelldragEnterEvent
        self.labelBildanzeige.__class__.dropEvent = self.labelBildanzeigedropEvent
        self.connect(self.actionGetUrl, QtCore.SIGNAL("triggered()"), self.onGetUrl)
        self.connect(self.actionGoToUrl, QtCore.SIGNAL("triggered()"), self.onGoToUrl)
        self.connect(self.actionShowDetails, QtCore.SIGNAL("triggered()"), self.onShowDetails)
        self.connect(self.actionBildanzeigegross, QtCore.SIGNAL("triggered()"), self.onDarstellerGross)
        self.connect(self.listWidgetFilme, QtCore.SIGNAL("customContextMenuRequested(QPoint)"), self.onContextFilm)
        self.connect(self.actionFilm_zeigen, QtCore.SIGNAL("triggered()"), self.onFilm_zeigen)
        self.connect(self.listWidgetStatistik, QtCore.SIGNAL("customContextMenuRequested(QPoint)"), self.onContextCS)
        self.connect(self.actionCSZeigen, QtCore.SIGNAL("triggered()"), self.onCSZeigen)
        self.connect(self.pushButtonDarstellerSuchen, QtCore.SIGNAL("clicked()"), self.onDarstellerSuchen)
        self.connect(self.pushButtonUmbenennen, QtCore.SIGNAL("clicked()"), self.onDarstellerUmbenennen)
        self.connect(self.pushButtonSortPartner, QtCore.SIGNAL("clicked()"), self.onPartnerSortieren)
        self.connect(self.pushButtonSort, QtCore.SIGNAL("clicked()"), self.onFilmeSortieren)
        self.connect(self.pushButtonPartnerZeigen, QtCore.SIGNAL("clicked()"), self.onPartnerZeigen)
        self.connect(self.pushButtonPseudo, QtCore.SIGNAL("clicked()"), self.onPseudo)
        
        # Slots einrichten für Dateien suchen
        self.connect(self.pushButtonSuchen, QtCore.SIGNAL("clicked()"), self.onSuchen)
        self.connect(self.pushButtonClear, QtCore.SIGNAL("clicked()"), self.onClear)
        self.connect(self.pushButtonUebernehmen, QtCore.SIGNAL("clicked()"), self.onDateinamenUebernehmen)
        self.connect(self.pushButtonSearchMpg, QtCore.SIGNAL("clicked()"), self.onSearchMpg)
        self.connect(self.pushButtonSearchVid, QtCore.SIGNAL("clicked()"), self.onSearchVid)
        
        # Slots einrichten für Web
        self.connect(self.webView, QtCore.SIGNAL("loadStarted()"), self.onLoadStarted)
        self.connect(self.webView, QtCore.SIGNAL("loadFinished (bool)"), self.onLoadFinished)
        self.connect(self.pushButtonVideo, QtCore.SIGNAL("clicked()"), self.onVideoSuchen)
        self.connect(self.pushButtonBack, QtCore.SIGNAL("clicked()"), self.webView.back)
        self.connect(self.pushButtonForward, QtCore.SIGNAL("clicked()"), self.webView.forward)
        self.connect(self.pushButtonIAFD, QtCore.SIGNAL("clicked()"), self.onIAFDSeite)
        self.connect(self.pushButtonAbholen, QtCore.SIGNAL("clicked()"), self.onDarstellerdatenAbholen)
        self.connect(self.pushButtonMovie, QtCore.SIGNAL("clicked()"), self.onMovieData)
        self.connect(self.pushButtonClearURL, QtCore.SIGNAL("clicked()"), self.onClearURL)
        self.connect(self.pushButtonUrl, QtCore.SIGNAL("clicked()"), self.onUrlVerwalten)
        self.connect(self.pushButtonSearchWebsite, QtCore.SIGNAL("clicked()"), self.onSearchWebsite)
        self.connect(self.webView, QtCore.SIGNAL("linkClicked (const QUrl&)"), self.onLinkClicked)
        self.connect(self.webView, QtCore.SIGNAL("urlChanged (const QUrl&)"), self.onUrlChanged)
        
        # Slots einrichten für Statistiken
        self.connect(self.pushButtonCS, QtCore.SIGNAL("clicked()"), self.onStatistikCS)
        self.connect(self.pushButtonDarstellerW, QtCore.SIGNAL("clicked()"), self.onStatistikDarstellerW)
        self.connect(self.pushButtonDarstellerM, QtCore.SIGNAL("clicked()"), self.onStatistikDarstellerM)
        self.connect(self.pushButtonAnzahlClips, QtCore.SIGNAL("clicked()"), self.onStatistikAnzahlClips)
        self.connect(self.pushButtonClipsJahr, QtCore.SIGNAL("clicked()"), self.onStatistikAnzahlClipsJahr)
        
        # Slots einrichten für Tools
        self.connect(self.pushButtonCheckNewVersion, QtCore.SIGNAL("clicked()"), self.onCheckNewVersion)
        self.connect(self.pushButtonSuchbegriffe, QtCore.SIGNAL("clicked()"), self.onSuchbegriffe)
        self.connect(self.pushButtonLand, QtCore.SIGNAL("clicked()"), self.onLand)
        self.connect(self.pushButtonBackup, QtCore.SIGNAL("clicked()"), self.onBackup)
        self.connect(self.pushButtonRestore, QtCore.SIGNAL("clicked()"), self.onRestore)
        self.connect(self.pushButtonWartung, QtCore.SIGNAL("clicked()"), self.onWartung)
        self.connect(self.pushButtonDateikatalog, QtCore.SIGNAL("toggled(bool)"), self.frame_Dateikatalog, QtCore.SLOT("setVisible(bool)"))
        self.frame_Dateikatalog.hide()
        self.connect(self.pushButtonVerwalten, QtCore.SIGNAL("clicked()"), self.onDevicesVerwalten)
        self.connect(self.pushButtonStart, QtCore.SIGNAL("clicked()"), self.onStartScan)
        self.connect(self.pushButtonDeleteDuplicates, QtCore.SIGNAL("clicked()"), self.onDeleteDuplicates)
        self.connect(self.pushButtonDeselect, QtCore.SIGNAL("clicked()"), self.onDeselect)
        self.pushButtonDeleteDuplicates.setEnabled(False)
        self.pushButtonDeselect.setEnabled(False)
        
        global initial_run
        if initial_run:
            bild = QtGui.QPixmap(os.getcwd() +os.sep +"pypordb" +os.sep +"8027068_splash.png").scaled(276, 246, QtCore.Qt.KeepAspectRatio)
            splash = QtGui.QSplashScreen(bild)
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
            self.verzeichnis = str(os.path.expanduser("~") +os.sep +"mpg")
            self.verzeichnis_original = self.verzeichnis
            self.verzeichnis_thumbs = str(os.path.expanduser("~") +os.sep +"thumbs_sammlung")
            self.verzeichnis_trash = str(self.verzeichnis_thumbs +os.sep +"trash")
            self.verzeichnis_cover = str(self.verzeichnis_thumbs +os.sep +"cover")
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
        self.anzahl = QtGui.QLabel()
        self.statusBar.addPermanentWidget(self.anzahl)
        
        self.mpg_aktuell = QtGui.QLabel()
        self.mpg_aktuell.setText(self.trUtf8("Actual volume: "))
        self.statusBar.addPermanentWidget(self.mpg_aktuell)
        
        self.spinBoxAktuell = QtGui.QSpinBox()
        self.spinBoxAktuell.setRange(1, 9999)
        self.statusBar.addPermanentWidget(self.spinBoxAktuell)
        self.connect(self.spinBoxAktuell, QtCore.SIGNAL("valueChanged(int)"), self.onVidNeuAktualisieren)
        
        self.pushButtonHistorie = QtGui.QPushButton()
        self.pushButtonHistorie.setText(QtGui.QApplication.translate("Dialog", "Historie", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonHistorie.setToolTip(self.trUtf8("Open search history"))
        self.statusBar.addPermanentWidget(self.pushButtonHistorie)
        self.connect(self.pushButtonHistorie, QtCore.SIGNAL("clicked()"), self.onHistorie)
        
        self.labelSeite = QtGui.QLabel()
        self.statusBar.addPermanentWidget(self.labelSeite)
        
        # populate toolbar
        self.suchfeld = QtGui.QComboBox()
        self.suchfeld.setMinimumWidth(250)
        self.suchfeld.setEditable(True)
        self.suchfeld.setWhatsThis(self.trUtf8("Searching field. By pressing the escape key it will be cleared and gets the focus."))
        self.toolBar.insertWidget(self.actionSuchfeld, self.suchfeld)
        self.toolBar.removeAction(self.actionSuchfeld)
        
        self.toolBar.removeAction(self.actionAnzahlBilder)
        
        self.setWindowTitle("PorDB3")
        self.screen = QtGui.QDesktopWidget().screenGeometry()
        #print self.screen.width(), self.screen.height()
        if initial_run:
            splash.showMessage("Loading history", color = QtGui.QColor("red"))
            app.processEvents()
        self.historie()
        if initial_run:
            splash.showMessage("Initializing ...", color = QtGui.QColor("red"))
            for i in os.listdir(os.path.expanduser("~" +os.sep +"tmp")):
                os.remove(os.path.expanduser("~" +os.sep +"tmp" +os.sep +i))
            app.processEvents()
        
        self.aktuelle_ausgabe = " "
        self.suche_darsteller = self.suche_cd = self.suche_titel = self.suche_original = self.suche_cs = ""
        self.sucheD_darsteller = self.sucheD_geschlecht = self.sucheD_haar = self.sucheD_nation = self.sucheD_tattoo = self.sucheD_etattoo = self.sucheD_ethnic = ""
        self.sucheD_actor1 = self.sucheD_actor2 = self.sucheD_actor3 = ""
        self.sucheD_ab = ""
        self.sucheD_bis = ""
        
        self.tabWidget.setCurrentIndex(0)
        self.video = False
        self.watched = False
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
        self.last_search_entry_for_original = ""
        
        self.pushButtonIAFDBackground.setEnabled(False)
        
        self.updatetimer = QtCore.QTimer()
        QtCore.QObject.connect(self.updatetimer, QtCore.SIGNAL("timeout()"), self.bilder_aktuell)
        self.connect(self.tableWidgetBilderAktuell, QtCore.SIGNAL("cellPressed(int, int)"), self.onTimerStop)
        self.updatefrequenz = 1000
        self.updatetimer.start(self.updatefrequenz)
        
        self.tableWidgetBilderAktuell.setColumnCount(1)
        self.tableWidgetBilderAktuell.setIconSize(size_neu)

        self.printer = QtGui.QPrinter(QtGui.QPrinter.ScreenResolution)
        self.printer.setOutputFileName(self.verzeichnis_original + os.sep + "print.pdf")
        
        zu_lesen = "SELECT cd, partnerw, partnerm, anzahl_bilder, anzahl_spalten FROM pordb_vid_neu"
        lese_func = DBLesen(self, zu_lesen)
        res = DBLesen.get_data(lese_func)
        self.spinBoxAktuell.setValue(res[0][0])
        self.lineEditAnzahlM.setText(str(res[0][2]))
        self.lineEditAnzahlW.setText(str(res[0][1]))
        
        self.spinBoxZeilen = QtGui.QSpinBox()
        self.spinBoxZeilen.setRange(1, 99)
        try:
            self.spinBoxZeilen.setValue(res[0][3])
        except:
            self.spinBoxZeilen.setValue(12)
        self.spinBoxZeilen.setToolTip(self.trUtf8("Images per page"))
        self.toolBar.insertWidget(self.actionAnzahlBilder, self.spinBoxZeilen)
        self.connect(self.spinBoxZeilen, QtCore.SIGNAL("valueChanged(int)"), self.onAnzahlZeilen)
        
        self.spinBoxSpalten = QtGui.QSpinBox()
        self.spinBoxSpalten.setRange(1, 10)
        try:
            self.spinBoxSpalten.setValue(res[0][4])
        except:
            self.spinBoxSpalten.setValue(3)
        self.spinBoxSpalten.setToolTip(self.trUtf8("Columns"))
        self.toolBar.insertWidget(self.actionAnzahlBilder, self.spinBoxSpalten)
        self.connect(self.spinBoxSpalten, QtCore.SIGNAL("valueChanged(int)"), self.onAnzahlSpalten)
        
        self.anzahl_bilder = self.spinBoxZeilen.value()
        self.onAnzahlZeilen()
        self.onAnzahlSpalten()
        
        if initial_run:
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
        self.cumshots = {"f":"Facial", "h":"Handjob", "t":str(self.trUtf8("Tits")), "c":"Creampie", "x":"Analcreampie", "o":"Oralcreampie", "v":str(self.trUtf8("Cunt")), "b":str(self.trUtf8("Belly")), "a":str(self.trUtf8("Ass")), "s":str(self.trUtf8("Others"))}
        self.cumshots_reverse = {"Facial":"f", "Handjob":"h", str(self.trUtf8("Tits")):"t", "Creampie":"c", "Analcreampie":"x", "Oralcreampie":"o", str(self.trUtf8("Cunt")):"v", str(self.trUtf8("Belly")):"b", str(self.trUtf8("Ass")):"a", str(self.trUtf8("Others")):"s"}
        
        if initial_run:
            splash.showMessage("Getting device names", color = QtGui.QColor("red"))
            app.processEvents()
            self.device_fuellen()
        
        if initial_run: 
            splash.showMessage("Loading IAFD", color = QtGui.QColor("red"))
            app.processEvents()
            zaehler = 0
            while True:
                zaehler += 1
                try:
                    seite = urllib.request.urlopen("http://www.iafd.com/").read()
                    if seite:
                        self.webView.load(QtCore.QUrl("http://www.iafd.com/"))
                        break
                    else:
                        pass
                except:
                    pass
                if zaehler > 1:
                    break
            self.webView.page().setLinkDelegationPolicy(QWebPage.DelegateAllLinks)
            if zaehler > 1:
                self.statusBar.showMessage(self.trUtf8("Either your computer is not online or the IAFD is not reachable"))
                
        if initial_run:
            splash.showMessage("Ready", color = QtGui.QColor("green"))
            app.processEvents()
            splash.finish(self)
        
        # Get version file from github
        if initial_run: 
            self.onCheckNewVersion()
            initial_run = False
            
    def setFocus(self, i):
        self.suchfeld.setFocus()
    
    def closeEvent(self, event):
        settings = QtCore.QSettings()
        settings.setValue("MeinDialog/Size", self.size())
        settings.setValue("MeinDialog/Position", self.pos())
        settings.setValue("MeinDialog/State", self.saveState())
        settings.setValue("splitter", self.splitter.saveState())
        
    def bilder_aktuell(self):
        self.label_akt_verzeichnis.setText(self.verzeichnis)
        dateiliste = os.listdir(self.verzeichnis)
        zeile = -1
        dateiliste_bereinigt = dateiliste[:]
        for i in dateiliste:
            zeile += 1
            if os.path.splitext(i)[-1].lower() == ".jpg" or os.path.splitext(i)[-1].lower() == ".jpeg" or os.path.splitext(i)[-1].lower() == ".png":
                pass
            else:
                del dateiliste_bereinigt[zeile]
                zeile -= 1
        self.tableWidgetBilderAktuell.setRowCount(len(dateiliste_bereinigt))
        zeile = -2
        dateiliste_bereinigt.sort()
        if self.bilderliste != dateiliste_bereinigt:
            for i in dateiliste_bereinigt:
                bild = QtGui.QPixmap(self.verzeichnis +os.sep +i)
                text = i + "\n" + str(QtGui.QPixmap(bild).width()) +"x" +str(QtGui.QPixmap(bild).height())
                bild = QtGui.QPixmap(self.verzeichnis +os.sep +i).scaled(size, QtCore.Qt.KeepAspectRatio)
                bild = QtGui.QIcon(bild)
                newitem = QtGui.QTableWidgetItem(bild, text)
                zeile += 1
                self.tableWidgetBilderAktuell.setItem(zeile, 1, newitem)
            self.tableWidgetBilderAktuell.resizeColumnsToContents()
            self.tableWidgetBilderAktuell.resizeRowsToContents()
            self.tableWidgetBilderAktuell.scrollToTop()
            self.tableWidgetBilderAktuell.setCurrentCell(0, 0)
            self.bilderliste = dateiliste_bereinigt[:]
        if not self.updatetimer.isActive():
            if len(dateiliste_bereinigt) > 10000:
                self.updatefrequenz = 10000000
            elif len(dateiliste_bereinigt) > 1000:
                self.updatefrequenz = 1000000
            elif len(dateiliste_bereinigt) > 100:
                self.updatefrequenz = 100000
            elif len(dateiliste_bereinigt) > 10:
                self.updatefrequenz = 10000
            else:
                self.updatefrequenz = 1000
            self.updatetimer.start(self.updatefrequenz)
        #print "Anzahl Bilder:", len(dateiliste_bereinigt), str(time.localtime()[3]) +":" +str(time.localtime()[4]) +":" +str(time.localtime()[5])
    # end of bilder_aktuell
    
    def onTimerStop(self, zeile, spalte):
        self.updatetimer.stop()
    
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
            self.comboBoxNation.addItem(text)
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
            dateien.append(str(self.verzeichnis +os.sep +i.text().split("\n")[0]))
        if len(dateien) > 2:
            message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("You can only drag 1 or 2 pictures"))
            return    
        else:
            bilddatei_alt = self.verzeichnis_thumbs +os.sep +"cd" +str(cd) +os.sep +bild.rstrip()
            if len(dateien) == 2:
                if os.path.exists(bilddatei_alt):
                    message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("You can only drag 1 picture"))
                    return    
                original = self.aktuelles_res[index][5]
                dialog = Cover(dateien, self.verzeichnis_original, original)
                dialog.exec_()
                datei, original = dialog.datei()
                bilddatei = QtGui.QImage(datei)
                bilddatei_alt = self.verzeichnis_cover +os.sep +bild.rstrip()
                ext = os.path.splitext(bilddatei_alt)[-1].lower()
                if ext == ".jpeg":
                    ext = "jpg"
                if not os.path.exists(bilddatei_alt):
                    message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Image to replace does not exist"))
                    return
                os.rename(bilddatei_alt, self.verzeichnis_trash +os.sep +"pypordb_bildalt" +ext)
            else:
                if os.path.exists(bilddatei_alt):
                    try:
                        os.remove(self.verzeichnis_trash +os.sep +"pypordb_bildalt.*")
                    except:
                        pass
                    ext = os.path.splitext(bilddatei_alt)[-1].lower()
                    if ext == ".jpeg":
                        ext = "jpg"
                    os.rename(bilddatei_alt, self.verzeichnis_trash +os.sep +"pypordb_bildalt" +ext)
                    bilddatei = QtGui.QImage(dateien[0]).scaled(size, QtCore.Qt.KeepAspectRatio)
                else:
                    bilddatei = QtGui.QImage(dateien[0])
                    bilddatei_alt = self.verzeichnis_cover +os.sep +bild.rstrip()
            
        if bilddatei.save(bilddatei_alt):
            if len(dateien) == 1:
                os.remove(dateien[0])
            else:
                os.remove(datei)
        else:
            message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Error saving image file"))
            return
            
        self.ausgabe_in_table()
        self.bilder_aktuell()
        self.suchfeld.setFocus()
    # end of tableWidgetBilderdropEvent
    
    def labelBildanzeigedropEvent(self, event):
        items = self.tableWidgetBilderAktuell.selectedItems()
        dateien = []
        for i in items:
            dateien.append(str(self.verzeichnis +os.sep +i.text().split("\n")[0]))
        if len(dateien) > 1:
            message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("You can only drag 1 picture"))
            return    
        else:
            name = str(self.labelDarsteller.text()).strip().lstrip("=")
            if not name:
                return
            bild = QtGui.QImage(dateien[0])
            if bild.width() > size_darsteller.width() or bild.height() > size_darsteller.height():
                message = QtGui.QMessageBox.warning(self, self.trUtf8("Caution! "), self.trUtf8("Image of the actor is very big"))
            zu_lesen = "SELECT sex FROM pordb_darsteller WHERE darsteller = %s"
            lese_func = DBLesen(self, zu_lesen, name)
            res = DBLesen.get_data(lese_func)
            extension_new = os.path.splitext(str(dateien[0]))[-1].lower()
            if extension_new == '.jpeg':
                extension_new = '.jpg'
            sex = res[0][0]
            if sex:
                oldfilename = self.verzeichnis_thumbs +os.sep +"darsteller_" +sex +os.sep +name.replace(" ", "_").replace("'", "_apostroph_").lower() + ".jpg"
                extension_old = None
                if not os.path.isfile(oldfilename):
                    oldfilename = self.verzeichnis_thumbs +os.sep +"darsteller_" +sex +os.sep +name.replace(" ", "_").replace("'", "_apostroph_").lower() + ".png"
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
            dateien.append(self.verzeichnis +os.sep +i.text().split("\n")[0])
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
        datei = QtGui.QFileDialog.getExistingDirectory(self, self.trUtf8("Select directory"), self.verzeichnis)
        if datei:
            self.verzeichnis = str(datei)
            app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
            self.bilder_aktuell()
            app.restoreOverrideCursor()
        self.suchfeld.setFocus()
            
    def onDirectoryRefresh(self):
        self.bilder_aktuell()
        
    def onHistorie(self):
        historiedialog = Historie()
        historiedialog.exec_()
        zu_lesen = str(historiedialog.zu_lesen)
        werte = str(historiedialog.werte).lstrip("(").rstrip(")").split(";")
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
        menu = QtGui.QMenu(self.listWidgetDarsteller)
        menu.addAction(self.actionAnzeigenPaar)
        menu.addAction(self.actionBildanzeigegross)
        self.context_actor_image = False
        menu.exec_(self.listWidgetDarsteller.mapToGlobal(event))
            
    def onContextCS(self, event):
        menu = QtGui.QMenu(self.listWidgetStatistik)
        menu.addAction(self.actionCSZeigen)
        menu.exec_(self.listWidgetStatistik.mapToGlobal(event))
        
    def onContextFilm(self, event):
        menu = QtGui.QMenu(self.listWidgetFilme)
        menu.addAction(self.actionFilm_zeigen)
        menu.exec_(self.listWidgetFilme.mapToGlobal(event))
        
    def onContexttableWidgetBilder(self, event):
        item = self.tableWidgetBilder.currentItem()
        if not item:
            return
        menu = QtGui.QMenu(self.tableWidgetBilder)
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
            menu = QtGui.QMenu(self.tableWidgetBilderAktuell)
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
        menu = QtGui.QMenu(self.labelBildanzeige)
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
                zu_lesen += " ORDER BY cd, bild, darsteller"
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
        zu_lesen = self.letzter_select_komplett[0:finde] + " ORDER BY darsteller, cd, bild"
        self.letzter_select_komplett = zu_lesen
        self.ausgabe(zu_lesen, zu_lesen, self.letzter_select_komplett_werte)
        app.restoreOverrideCursor()
        
    def onSortieren_nach_CD(self):
        app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        finde = self.letzter_select_komplett.find("ORDER BY")
        zu_lesen = self.letzter_select_komplett[0:finde] + " ORDER BY cd, darsteller, bild"
        self.letzter_select_komplett = zu_lesen
        self.ausgabe(zu_lesen, zu_lesen, self.letzter_select_komplett_werte)
        app.restoreOverrideCursor()
        
    def onSortieren_nach_Original(self):
        app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        finde = self.letzter_select_komplett.find("ORDER BY")
        zu_lesen = self.letzter_select_komplett[0:finde] + " ORDER BY original, cd, darsteller, bild"
        self.letzter_select_komplett = zu_lesen
        self.ausgabe(zu_lesen, zu_lesen, self.letzter_select_komplett_werte)
        app.restoreOverrideCursor()
        
    def onSortieren_nach_Titel(self):
        app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        finde = self.letzter_select_komplett.find("ORDER BY")
        zu_lesen = self.letzter_select_komplett[0:finde] + " ORDER BY titel, cd, darsteller, bild"
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
            message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("There is no original title: cannot be renamed"))
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
                zu_lesen = "SELECT * FROM pordb_vid WHERE original = %s ORDER BY original, cd, bild, darsteller"
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
        items = self.tableWidgetBilder.selectedItems()
        zu_erfassen = []
        for i in items:
            column = self.tableWidgetBilder.column(i)
            row = self.tableWidgetBilder.row(i)
            index = int(row * self.columns + column + self.start_bilder)
            werte = []
            werte.append(vorhanden)
            if masschangedialog.resolution:
                werte.append(masschangedialog.resolution)
            else:
                werte.append(None)            
            werte.append(str(self.aktuelles_res[index][2]))
            werte.append(self.aktuelles_res[index][3])
            zu_erfassen.append(["UPDATE pordb_vid SET vorhanden = %s, hd = %s WHERE cd = %s AND bild = %s", werte])
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
            message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Movie has no original title"))
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
        j = 0
        bilddatei_trash = None
        for i in dateiliste:
            if os.path.splitext(i)[0] == "pypordb_bildalt":
                bilddatei_trash = self.verzeichnis_trash +os.sep +i
                break
        bilddatei_neu = self.verzeichnis_thumbs +os.sep +"cd" +str(cd) +os.sep +bild.rstrip()
        if not os.path.exists(bilddatei_neu):
            bilddatei_neu = self.verzeichnis_cover +os.sep +os.sep +bild.rstrip()
        if bilddatei_trash and os.path.exists(bilddatei_neu):
            messageBox = QtGui.QMessageBox()
            messageBox.addButton(self.trUtf8("Image restore"), QtGui.QMessageBox.AcceptRole)
            messageBox.addButton(self.trUtf8("Cancel"), QtGui.QMessageBox.RejectRole)
            messageBox.setWindowTitle(self.trUtf8("Image restore ") +os.path.basename(bilddatei_neu))
            messageBox.setIcon(QtGui.QMessageBox.Question)
            messageBox.setText(self.trUtf8("Do you want to restore the image?"))
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
            self.statusBar.showMessage('"' +original +'"' +self.trUtf8(" transferred into clipboard"))
        self.suchfeld.setFocus()
        
    def onCovergross(self):
        item = self.tableWidgetBilder.currentItem()
        column = self.tableWidgetBilder.column(item)
        row = self.tableWidgetBilder.row(item)
        index = int(row * self.columns + column + self.start_bilder)
        if self.aktuelles_res[index][5]:
            original = self.aktuelles_res[index][5]
        else:
            original = ""
        cover = self.verzeichnis_cover + os.sep + self.aktuelles_res[index][3].strip()
        if os.path.exists(cover):
            bilddialog = DarstellerAnzeigeGross(cover)
            bilddialog.exec_()
        self.suchfeld.setFocus()
        
    def onBildLoeschen(self):
        items = self.tableWidgetBilderAktuell.selectedItems()
        for i in items:
            text = str(i.text().split("\n")[0])
            bilddatei = self.verzeichnis +os.sep +text 
            try:
                os.remove(bilddatei)
            except:
                pass
        self.bilder_aktuell()
        self.suchfeld.setFocus()
        
    def onCover(self, datei = None):
        cover = []
        j = 0
        if not datei:
            dateiliste = os.listdir(self.verzeichnis_original)
            for i in dateiliste:
                if os.path.splitext(i)[-1].lower() == ".jpg" or os.path.splitext(i)[-1].lower() == ".jpeg" or os.path.splitext(i)[-1].lower() == ".png":
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
                    darsteller = str(self.labelDarsteller.text()).strip()
                    verzeichnis_m = self.verzeichnis_thumbs + os.sep + "darsteller_m"
                    verzeichnis_w = self.verzeichnis_thumbs + os.sep + "darsteller_w"
                    randunten = 50
                    for i in self.aktuelles_res:
                        if i[-1] == ")":
                            anfang = i.rfind("(")
                        else:
                            anfang = len(i)
                        name = i[0 : anfang]
                        filename = verzeichnis_w + os.sep + name.strip().lower().replace(" ", "_").replace("'", "_apostroph_") + ".jpg"
                        if not os.path.exists(filename):
                            filename = verzeichnis_m + os.sep + name.strip().lower().replace(" ", "_").replace("'", "_apostroph_") + ".jpg"
                        if not os.path.exists(filename):
                            filename = self.verzeichnis_thumbs + os.sep + "nichtvorhanden" + os.sep + "nicht_vorhanden.jpg"
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
                            dateiname = self.verzeichnis_cover +"/" +i[3].strip()
                            if os.path.exists(dateiname):
                                zw_res.append(i)
                        res = zw_res
                painter.drawText(x + 300, y, "- " +str(seite) +" -")
                y += 15
                for i in res:
                    if self.aktuelle_ausgabe == "Darsteller":
                        sex = str(self.letzter_select_komplett)[str(self.letzter_select_komplett).find("sex") + 7]
                        filename = self.verzeichnis_thumbs + os.sep + "darsteller_" + sex + os.sep + i[0].strip().lower().replace(" ", "_") + ".jpg"
                    else:
                        filename = self.verzeichnis_thumbs + os.sep + "cd" +str(i[2]) +os.sep +i[3].strip()
                        if not os.path.exists(filename):
                            filename = self.verzeichnis_cover +os.sep +i[3].strip()
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
                        painter.drawText(x, y, self.trUtf8("Count: ") +str(i[2]))
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
                        painter.drawText(x, y, self.trUtf8("Title: ") +i[0])
                        y += 15
                        painter.drawText(x, y, self.trUtf8("Actor: ") +i[1])
                        y += 15
                        painter.drawText(x, y, "CD: " +str(i[2]))
                        y += 15
                        painter.drawText(x, y, self.trUtf8("Image: ") +i[3])
                        y += 15
                        painter.drawText(x, y, self.trUtf8("only image: ") +i[4])
                        y += 15
                        if i[5]:
                            painter.drawText(x, y, "Original: " +i[5])
                        else:
                            painter.drawText(x, y, "Original: ")
                        y += 15
                        if i[6]:
                            painter.drawText(x, y, "CS: " +i[6])
                        else:
                            painter.drawText(x, y, "CS: ")
                        y += 15
                        if i[7]:
                            painter.drawText(x, y, self.trUtf8("available: ") +i[7])
                        else:
                            painter.drawText(x, y, self.trUtf8("available: "))
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
                    filename = self.verzeichnis_thumbs + os.sep + "darsteller_w" + os.sep + name.strip().lower().replace(" ", "_").replace("'", "_apostroph_") + ".jpg"
                    if not os.path.exists(filename):
                        filename = self.verzeichnis_thumbs + os.sep + "darsteller_m" + os.sep + name.strip().lower().replace(" ", "_").replace("'", "_apostroph_") + ".jpg"
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
                        
                    painter.drawText(x, y, self.trUtf8("Statistics"))
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
                        
                    painter.drawText(x, y, self.trUtf8("Movies (") +str(self.listWidgetFilme.count()) +")")
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
                painter.drawText(x, y, self.trUtf8("Search term: ") +self.lineEditSuchen.text())
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
        
        self.preview = QtGui.QPrintPreviewDialog(self.printer)
        self.connect(self.preview, QtCore.SIGNAL("paintRequested (QPrinter *)"), paint_action)
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
            self.bilddarsteller = self.verzeichnis_thumbs + os.sep + "darsteller_w" + os.sep + bildname + ".jpg"
            if not os.path.isfile(self.bilddarsteller):
                self.bilddarsteller = self.verzeichnis_thumbs + os.sep + "darsteller_w" + os.sep + bildname + ".png"
                if not os.path.isfile(self.bilddarsteller):
                    self.bilddarsteller = self.verzeichnis_thumbs + os.sep + "darsteller_m" + os.sep + bildname + ".jpg"
                    if not os.path.isfile(self.bilddarsteller):
                        self.bilddarsteller = self.verzeichnis_thumbs + os.sep + "darsteller_m" + os.sep + bildname + ".png"
                        if not os.path.isfile(self.bilddarsteller):
                            self.bilddarsteller = self.verzeichnis_thumbs + os.sep + "nichtvorhanden" + os.sep + "nicht_vorhanden.jpg"
            bilddialog = DarstellerAnzeigeGross(self.bilddarsteller)
            bilddialog.exec_()
        self.suchfeld.setFocus()
        
    def onShowDetails(self):
        ein = str(self.labelDarsteller.text()).strip().title()
        dialog = ActorDetails(ein, self.verzeichnis_thumbs)
        dialog.exec_()
        self.suchfeld.setFocus()
        
    def onGetUrl(self):
        ein = str(self.labelDarsteller.text()).strip().title()
        if ein:
            zu_lesen = "SELECT url FROM pordb_darsteller WHERE darsteller = %s"
            lese_func = DBLesen(self, zu_lesen, ein)
            res = DBLesen.get_data(lese_func)
            if res[0][0]:
                clipboard = QtGui.QApplication.clipboard()
                clipboard.setText(res[0][0], mode=QtGui.QClipboard.Clipboard)
        self.suchfeld.setFocus()
        
    def onGoToUrl(self):
        ein = str(self.labelDarsteller.text()).strip().title()
        if ein:
            zu_lesen = "SELECT url FROM pordb_darsteller WHERE darsteller = %s"
            lese_func = DBLesen(self, zu_lesen, ein)
            res = DBLesen.get_data(lese_func)
            if res[0][0]:
                self.lineEditURL.setText(res[0][0])
                self.GetWebsite()
                self.tabWidget.setCurrentIndex(3)
            else:
                clipboard = QtGui.QApplication.clipboard()
                clipboard.setText(ein.lstrip("="), mode=QtGui.QClipboard.Clipboard)
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
            message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Seems to be an invalid character in the search field"))
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
        zu_lesen += " ORDER BY cd, bild, darsteller"
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
            message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("CD is not a number"))
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
        zu_lesen += " ORDER BY bild, darsteller"
        self.letzter_select_komplett = zu_lesen
        self.letzter_select_komplett_werte = werte
        self.partner = 0
        self.ausgabe(str(ein), zu_lesen, werte)
        app.restoreOverrideCursor()
            
    def onTitel(self):
        # nach Titel in pordb_vid suchen und anzeigen
        self.start_bilder = 0
        try:
            ein = str(self.suchfeld.currentText()).replace("'", "''").lower()
            ein = str(self.suchfeld.currentText()).replace("'", "''").lower().strip()
        except:
            message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Seems to be an invalid character in the search field"))
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
        zu_lesen += " ORDER BY cd, bild, darsteller"
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
            message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Seems to be an invalid character in the search field"))
            return
        if not ein or ein == "=":
            return
        self.last_search_entry_for_original = ein
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
            zu_lesen = "SELECT * FROM pordb_vid WHERE (LOWER(original) = %s OR original LIKE %s)"
            werte.append(ein3[1:])
            werte.append(ein2[1:] + " %")
        else:
            zu_lesen = "SELECT * FROM pordb_vid WHERE (LOWER(original) LIKE %s OR original LIKE %s)"
            werte.append("%" + ein3.replace(" ", "%") + "%")
            werte.append("%" + ein2.replace(" ", "%") + "%")
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
        zu_lesen += " ORDER BY original, cd, bild, darsteller"
        self.letzter_select_komplett = zu_lesen
        self.letzter_select_komplett_werte = werte
        self.partner = 0
        self.ausgabe(ein3, zu_lesen, werte)
        app.restoreOverrideCursor()
        
    def onHelp(self):
        QtGui.QMessageBox.about(self, "About PorDB3", """<b>PorDB3</b> v %s <p>Copyright &copy; 2012-2014 HWM</p> <p>GNU GENERAL PUBLIC LICENSE Version 3</p> <p>This is PorDB3.</p> <p>Python %s - Qt %s - PyQt %s on %s""" % (__version__, platform.python_version(), QtCore.QT_VERSION_STR, QtCore.PYQT_VERSION_STR, platform.system()))
        self.suchfeld.setFocus()
        
    def ausgabe(self, ein, zu_lesen, werte = None):
        if ein == "":
            ein = self.last_search_entry_for_original
        lese_func = DBLesen(self, zu_lesen, werte)
        self.aktuelles_res = DBLesen.get_data(lese_func)
        zw_res = []
        if "SELECT * FROM pordb_vid WHERE (LOWER(original)" in zu_lesen:
            ende = zu_lesen.find("primkey")
            if ende < 0:
                ende1 = zu_lesen.find("gesehen") - 6 # damit das "and" nicht in der where-Bedingung durch "&" ersetzt wird
                ende2 = zu_lesen.find("vorhanden") - 6 # damit das "and" nicht in der where-Bedingung durch "&" ersetzt wird
                if ende1 > 0 and ende2 > 0:
                    ende = min(ende1, ende2)
                else:
                    ende = max(ende1, ende2)
            for i in self.suchbegriffe:
                suchbegriff = i.lower().strip()
                if suchbegriff and suchbegriff in zu_lesen[0:ende]:
                    if ende > 0:
                        zu_lesen2 = zu_lesen[0:ende - 3]
                        zu_lesen3 = zu_lesen[ende - 3 :]
                    else:
                        zu_lesen2 = zu_lesen
                        zu_lesen3 = ""
                    if suchbegriff == "-":
                        zu_lesen2.replace(suchbegriff, " ")
                    else:
                        zu_lesen2 = zu_lesen2.replace(suchbegriff, self.suchbegriffe[i].lower().strip()) + zu_lesen3
                    if zu_lesen != zu_lesen2:
                        lese_func = DBLesen(self, zu_lesen2)
                        res2 = DBLesen.get_data(lese_func)
                        if res2:
                            self.aktuelles_res.extend(res2)
            if self.actionCheckBoxDVDCover.isChecked():
                for i in self.aktuelles_res:
                    dateiname = self.verzeichnis_thumbs +"/cd" +str(i[2]) +"/" +i[3].strip()
                    if not os.path.exists(dateiname):
                        dateiname = self.verzeichnis_cover +"/" +i[3].strip()
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
        if "SELECT * FROM pordb_vid WHERE (LOWER(original)" in zu_lesen:
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
        befehl = befehl.replace("'", "''")
        if len(befehl) < 5001:
            zu_erfassen = []
            werte = []
            werte.append(befehl)
            zu_erfassen.append(["DELETE FROM pordb_history WHERE sql = %s", werte])
            werte = []
            werte.append(befehl)
            werte.append(datetime.datetime.now().isoformat(' '))
            zu_erfassen.append(["INSERT INTO pordb_history VALUES (%s, %s)", werte])
            update_func = DBUpdate(self, zu_erfassen)
            DBUpdate.update_data(update_func)
        
        if ein.startswith("SELECT "):
            pass
        else:
            self.statusBar.showMessage(self.trUtf8("Search was: ") +ein)
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
            dateiname = self.verzeichnis_thumbs +"/cd" +str(i[2]) +"/" +i[3].strip()
            if not os.path.exists(dateiname) or self.actionCheckBoxDVDCover.isChecked():
                dateiname = self.verzeichnis_cover +"/" +i[3].strip()
                if os.path.exists(dateiname):
                    cover = "x"
            if os.path.exists(dateiname):
                bild = QtGui.QPixmap(dateiname)
                groesse = bild.size()
                bild = QtGui.QIcon(dateiname)
            else:
                bild = QtGui.QPixmap(self.verzeichnis_thumbs +"/nichtvorhanden/nicht_vorhanden.jpg")
                groesse = bild.size()
                bild = QtGui.QIcon(self.verzeichnis_thumbs +"/nichtvorhanden/nicht_vorhanden.jpg")
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
                text += self.trUtf8("Title: ") +"\n" +titel +"\n" +self.trUtf8("Image: ") +"\n" +bild_element +"\n------------------------------\n"
                self.angezeigt_komplett = True
            else:
                self.angezeigt_komplett = False
            if darsteller_ausgabe:
                text += darsteller_ausgabe +"\n------------------------------\n" 
            text += "CD=" +ort +" "
            if i[4] == 'x':
                text += self.trUtf8("\nwatched")
            elif i[7] == 'x':
                text += self.trUtf8("\nin stock")
            if i[20] == '0':
                text += " SD"
            elif i[20] == '1':
                text += " HD 720p"
            elif i[20] == '2':
                text += " HD 1080p"
            elif i[20] == '3':
                text += " UltraHD"
            elif i[20] == '9':
                text += self.trUtf8(" unknown")
            zu_lesen = "SELECT * FROM pordb_original WHERE foreign_key_pordb_vid = %s"
            lese_func = DBLesen(self, zu_lesen, str(i[8]))
            res2 = DBLesen.get_data(lese_func)
            if len(res2) > 0:
                text += "\n>>>>>"
            newitem = QtGui.QTableWidgetItem(bild, text)
            if i[4] != " " and i[7] != " " and i[7] != None: # clip is present and watched
                newitem.setTextColor(QtGui.QColor("green"))
            elif i[7] == " " or i[7] == None:
                newitem.setTextColor(QtGui.QColor("red"))
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
        suche.checkBoxVid.setChecked(self.video)
        suche.checkBoxWatched.setChecked(self.watched)
        try:
            suche.comboBoxCS.setCurrentIndex(suche.comboBoxCS.findText(self.suche_cs))
        except:
            pass
        if suche.exec_():
            self.suche_darsteller = suche.lineEditDarsteller.text()
            self.suche_cd = suche.lineEditCD.text()
            self.suche_titel = suche.lineEditTitel.text()
            self.suche_original = suche.lineEditOriginal.text()
            self.video = suche.checkBoxVid.isChecked()
            self.watched = suche.checkBoxWatched.isChecked()
            self.suche_cs = suche.comboBoxCS.currentText()
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
                    message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("CD is not a number"))
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
            
            # Vid Button gesetzt
            if argument == 1 and self.video:
                zu_lesen += " AND (vorhanden != %s)"
                werte.append(" ")
                
            # Watched Button gesetzt
            if argument == 1 and self.watched:
                zu_lesen += " AND (gesehen = %s)"
                werte.append("x")
            
            zu_lesen += " ORDER BY cd, titel"
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
                
    def onbildAnzeige(self):
        ein = self.eingabe_auswerten()
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
                self.bilddarsteller = self.verzeichnis_thumbs +os.sep +"darsteller_" +i[1] +os.sep +bildname +".jpg"
                if not os.path.isfile(self.bilddarsteller):
                    self.bilddarsteller = self.verzeichnis_thumbs +os.sep +"darsteller_" +i[1] +os.sep +bildname +".png"
                    if not os.path.isfile(self.bilddarsteller):
                        self.bilddarsteller = self.verzeichnis_thumbs +os.sep +"nichtvorhanden" +os.sep +"nicht_vorhanden.jpg"
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
        self.onStatistik()
        self.onDarstellerFilme(res)
        self.onpaareSuchen(res)
        self.suchfeld.setCurrentIndex(-1)
        self.suchfeld.setFocus()
        self.listWidgetDarsteller.clearSelection()
        self.pushButtonSortPartner.setText(QtGui.QApplication.translate("Dialog", "Quantity", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSort.setText(QtGui.QApplication.translate("Dialog", "Year", None, QtGui.QApplication.UnicodeUTF8))
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
        self.bilddarsteller = self.verzeichnis_thumbs +os.sep +"nichtvorhanden" +os.sep +"nicht_vorhanden.jpg"
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
        geschlecht = res[0][1]
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
                zu_lesen = "SELECT cs" +cs +" FROM pordb_vid WHERE cd = %s AND bild = %s"
                lese_func = DBLesen(self, zu_lesen, (str(i[1]), i[2]))
                res1 = DBLesen.get_data(lese_func)
                try:
                    if res1[0][0] != 0:
                        mengeCs.add(i[0])
                except: 
                    message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("There is something wrong with partners: ") +zu_lesen)
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
        self.labelText.setText(self.trUtf8("Partner: ") +str(len(self.paarung)))
        if not ethnic and not cs:
            werte = []
            werte.append(len(self.paarung))
            werte.append(gesucht)
            zu_erfassen = []
            zu_erfassen.append(["UPDATE pordb_darsteller SET partner = %s WHERE darsteller = %s", werte])
            update_func = DBUpdate(self, zu_erfassen)
            DBUpdate.update_data(update_func)
    # end of onpaareSuchen
        
    def eingabe_auswerten(self):
        try:
            ein = str(self.suchfeld.currentText()).strip().title()
        except:
            message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Illegal characters in search field"))
            return
        if not ein:
            selected = self.listWidgetDarsteller.selectedItems()
            if selected:
                ein = str(selected[0].text())
                ein = "=" +ein[0 : ein.rfind("(")].strip()
        if not ein:
            ein = "=" +str(self.labelDarsteller.text()).strip().title()
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
                message = QtGui.QMessageBox.warning(self, self.trUtf8("Caution! "), self.trUtf8("Actor has been found as pseudonym only!"))
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
            self.labelText.setText("<font color=red>" +self.trUtf8("Please select:") +"</font>")
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
                    self.labelFehler.setText("<font color=red>" +self.trUtf8("Data collection of actor seems to be not complete, nation: ") +res[0][5]  +"</font>")
            else:
                if res[0][5] and res[0][5][0:1] != "-":
                    nation = res[0][5]
                else:
                    nation = ""
                    self.labelFehler.setText("<font color=red>" +self.trUtf8("Data collection of actor seems to be not complete, nation: ") +nation  +"</font>")
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
                    alter = age((datetime.date(jahr, monat, tag)))
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
                besucht = age((datetime.date(jahr, monat, tag)))
            if aktiv:
                if besucht > 0:
                    farbe = "<font color=red>"
                else:
                    farbe = "<font color=black>"
                self.labelAktiv.setText(farbe +self.trUtf8("active : ") +aktiv +"</font>")
            else:
                self.labelAktiv.clear()
        else:
            werte = []
            zu_lesen = "SELECT * FROM pordb_pseudo WHERE pseudo = %s"
            werte.append(eingabe)
            if self.comboBoxSex.currentText() == self.trUtf8("Male"):
                zu_lesen += " AND sex = %s"
                werte.append("m")
            elif self.comboBoxSex.currentText() == self.trUtf8("Female"):
                zu_lesen += " AND sex = %s"
                werte.append("m")
            zu_lesen += " ORDER BY darsteller"
            lese_func = DBLesen(self, zu_lesen, werte)
            res1 = DBLesen.get_data(lese_func)
            if res1:
                ein = "=" + res1[0][1].strip()
                res = self.darsteller_lesen(ein)
            else:
                self.labelFehler.setText("<font color=red>" +self.trUtf8("Actor not available") +"</font>")
        self.suchfeld.setFocus()
        return res
    # end of darsteller_lesen
    
    def onDarstellerspeichern(self):
        name = str(self.labelDarsteller.text()).replace("'", "''")
        if not name:
            return
        try:
            ein = int(self.lineEditAnzahl.text())
        except:
            message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Quantity is not a number"))
            self.lineEditAnzahl.setSelection(0, len(self.lineEditAnzahl.text()))
            return
        # update-Anweisung aufbauen
        if str(self.lineEditGeboren.text()):
            geboren = str(self.lineEditGeboren.text())
        else:
            geboren = "0001-01-01"
        datum = str(time.localtime()[0]) + '-' + str(time.localtime()[1]) + '-' + str(time.localtime()[2])
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
        
        filename = self.verzeichnis_thumbs + os.sep + "darsteller_" +str(self.comboBoxGeschlecht.currentText()) + os.sep + name.strip().lower().replace(" ", "_") + ".jpg"
        if not os.path.exists(filename):
            filename = self.verzeichnis_thumbs + os.sep + "darsteller_" +str(self.comboBoxGeschlecht.currentText()) + os.sep + name.strip().lower().replace(" ", "_") + ".png"
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
            oldfilename = self.verzeichnis_thumbs + os.sep + "darsteller_" +sex_alt + os.sep + name.strip().lower().replace(" ", "_") + extension
            if os.path.exists(oldfilename):
                os.rename(oldfilename, filename)
        
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
            zaehler = 0
            while True:
                zaehler += 1
                try:
                    seite = urllib.request.urlopen(res[0][11]).read().decode("iso-8859-1")
                    break
                except:
                    pass
                if zaehler > 10:
                    break
            app.restoreOverrideCursor()
            if zaehler > 10:
                message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Site of actor could not be found"))
                return
            else:
                bilddialog = DarstellerdatenAnzeigen(app, res[0][11], seite, self.verzeichnis_thumbs, name = res[0][0])
                app.restoreOverrideCursor()
                bilddialog.exec_()
        else:
            clipboard = QtGui.QApplication.clipboard()
            clipboard.setText(ein.lstrip("="), mode=QtGui.QClipboard.Clipboard)
            self.tabWidget.setCurrentIndex(3)
        
        self.onbildAnzeige()
            
    def onIAFDBackground(self):
        ein = self.eingabe_auswerten()
        res = self.darsteller_lesen(ein)
        if res[0][11]:
            monate = {"January":"01", "February":"02", "March":"03", "April":"04", "May":"05", "June":"06", "July":"07", "August":"08", "September":"09", "October":"10", "November":"11", "December":"12", }
            app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
            zaehler = 0
            while True:
                zaehler += 1
                try:
                    seite = str(urllib.request.urlopen(res[0][11]).read())
                    break
                except:
                    pass
                if zaehler > 10:
                    break
            if zaehler > 10:
                app.restoreOverrideCursor()
                message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Site of actor could not be found"))
                return
            
            actordata = ActorData(seite)
                
            # Darsteller Geboren
            geboren = ActorData.actor_born(actordata)
            monat = monate.get(geboren[0:geboren.find(" ")], self.trUtf8("not available"))
            if monat != self.trUtf8("not available"):
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
            
            # Darsteller Anzahl Filme
            filme = ActorData.actor_movies(actordata)
            if int(filme) > 0:
                werte = []
                werte.append(filme)
                werte.append(res[0][0])
                zu_erfassen.append(["UPDATE pordb_darsteller SET filme = %s WHERE darsteller = %s", werte])
                
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
            if tattoos == "None" or tattoos == "none":
                tats = "-"
            elif tattoos == "No data" or tattoos == "No Data":
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
                
            self.onbildAnzeige()
                
            app.restoreOverrideCursor()
            
    # end of onIAFDBackground
    
    def onDarstellerloeschen(self):
        name = str(self.labelDarsteller.text())
        if not name:
            return
        messageBox = QtGui.QMessageBox()
        messageBox.addButton(self.trUtf8("Yes"), QtGui.QMessageBox.AcceptRole)
        messageBox.addButton(self.trUtf8("No"), QtGui.QMessageBox.RejectRole)
        messageBox.setWindowTitle(self.trUtf8("Actor ") +name.strip() +self.trUtf8(" will be deleted now"))
        messageBox.setIcon(QtGui.QMessageBox.Question)
        messageBox.setText(self.trUtf8("Should the actor really be deleted?"))
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
            datei_alt = self.verzeichnis_thumbs +os.sep +"darsteller_" +str(self.comboBoxGeschlecht.currentText()) +os.sep +bildname +".jpg"
            try:
                os.remove(datei_alt)
            except:
                pass
            self.statusBar.showMessage(self.trUtf8("Actor ") +name.strip() +self.trUtf8(" deleted"))
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
                    datei = open(self.verzeichnis_trash +os.sep +i, "r")
                    text = datei.readlines()
                    datei.close()
                elif (os.path.splitext(i)[-1].lower() == ".jpg" or os.path.splitext(i)[-1].lower() == ".jpeg" or os.path.splitext(i)[-1].lower() == ".png") and os.path.splitext(i)[0] != "pypordb_bildalt":
                    j += 1
                    self.file = str(self.verzeichnis_trash +os.sep +i)
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
            if j != 1:
                self.file = QtGui.QFileDialog.getOpenFileName(self, self.trUtf8("Image files"), self.verzeichnis_trash, self.trUtf8("Image files (*.jpg *.jpeg *.png);;all files (*.*)"))
            eingabedialog = Neueingabe(self.verzeichnis, self.verzeichnis_original, self.verzeichnis_thumbs, self.verzeichnis_trash, self.verzeichnis_cover, self.file, titel, darsteller, cd, bild, gesehen, original, cs, vorhanden, "", undo, original_cover=trash_cover, high_definition = definition)
        else:
            if not cover_anlegen:
                if len(self.tableWidgetBilderAktuell.selectedItems()) == 1 or len(self.tableWidgetBilderAktuell.selectedItems()) == 2:
                    items = self.tableWidgetBilderAktuell.selectedItems()
                    dateien = []
                    for i in items:
                        dateien.append(str(self.verzeichnis +os.sep +i.text().split("\n")[0]))
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
                    if os.path.splitext(i)[-1].lower() == ".jpg" or os.path.splitext(i)[-1].lower() == ".jpeg" or os.path.splitext(i)[-1].lower() == ".png":
                        j += 1
                        self.file = self.verzeichnis +os.sep +i
                if j != 1:
                    self.file = QtGui.QFileDialog.getOpenFileName(self, self.trUtf8("Image files"), self.verzeichnis, self.trUtf8("Image files (*.jpg *.jpeg *.png);;all files (*.*)"))
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
            self.file = self.verzeichnis_thumbs +os.sep +"cd" +str(cd) +os.sep +self.aktuelles_res[index][3].strip()
            cover = False
            if not os.path.exists(self.file):
                self.file = self.verzeichnis_cover +os.sep +self.aktuelles_res[index][3].strip()
                cover = True
            zu_lesen = "SELECT * FROM pordb_original WHERE foreign_key_pordb_vid = %s"
            werte = []
            werte.append(str(self.aktuelles_res[index][8]))
            lese_func = DBLesen(self, zu_lesen, werte)
            res2 = DBLesen.get_data(lese_func)
            original_weitere = []
            for i in res2:
                original_weitere.append(i[1])
            eingabedialog = Neueingabe(self.verzeichnis, self.verzeichnis_original, self.verzeichnis_thumbs, self.verzeichnis_trash, self.verzeichnis_cover, self.file, titel, darsteller, cd, bild, gesehen, original, cs, vorhanden, cover, None, None, original_weitere, high_definition = definition)
            change_flag = None
            res_alt = self.aktuelles_res
            if eingabedialog.exec_():
                change_flag = True
            self.ausgabe("", self.letzter_select_komplett, self.letzter_select_komplett_werte)
            if change_flag:
                self.statusBar.showMessage("upd:CD" +str(res_alt[index][2]) +" Title:" +res_alt[index][0].strip() +" Act:" +res_alt[index][1].strip())
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
            if self.sucheD_tattoo == self.trUtf8("yes"):
                if argument == 1:
                    zu_lesen += " AND "
                argument = 1
                zu_lesen += "tattoo IS NOT NULL AND tattoo != %s AND tattoo != %s AND tattoo != %s"
                werte.append("-")
                werte.append(" ")
                werte.append("")
            elif self.sucheD_tattoo == self.trUtf8("no"):
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
                if os.path.exists(self.verzeichnis_thumbs + os.sep +"darsteller_w" + os.sep + bildname +".jpg"):
                    dateiname = self.verzeichnis_thumbs + os.sep +"darsteller_w" + os.sep + bildname +".jpg"
                elif os.path.exists(self.verzeichnis_thumbs + os.sep +"darsteller_w" + os.sep + bildname +".png"):
                    dateiname = self.verzeichnis_thumbs + os.sep +"darsteller_w" + os.sep + bildname +".png"
                elif os.path.exists(self.verzeichnis_thumbs + os.sep +"darsteller_m" + os.sep + bildname +".jpg"):
                    dateiname = self.verzeichnis_thumbs + os.sep +"darsteller_m" + os.sep + bildname +".jpg"
                else:
                    dateiname = self.verzeichnis_thumbs + os.sep +"darsteller_m" + os.sep + bildname +".png"
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
                if os.path.exists(self.verzeichnis_thumbs +"/darsteller_" +i[1] + os.sep +bildname +".jpg"):
                    dateiname = self.verzeichnis_thumbs +"/darsteller_" +i[1] + os.sep +bildname +".jpg"
                else:
                    dateiname = self.verzeichnis_thumbs +"/darsteller_" +i[1] + os.sep +bildname +".png"
            if not os.path.isfile(dateiname):
                dateiname = self.verzeichnis_thumbs +"/nichtvorhanden/nicht_vorhanden.jpg"
            bild = QtGui.QIcon(dateiname)
            newitem = QtGui.QTableWidgetItem(bild, text)
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
        self.anzahl.setText(self.trUtf8("Quantity: ") +str(len(self.aktuelles_res)))
        seite_von = int(round(self.start_bilder / self.anzahl_bilder + 1))
        seite_bis = int(round(len(self.aktuelles_res) / float(self.anzahl_bilder) + 0.499999))
        self.labelSeite.setText(self.trUtf8("Page ") +str(seite_von) + self.trUtf8(" of ") +str(seite_bis))
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
        for i in ["Facial......", "Handjob.....", self.trUtf8("Tits........"), "Creampie....", "Analcreampie", "Oralcreampie", self.trUtf8("Cunt........"), self.trUtf8("Belly......."), self.trUtf8("Ass........."), self.trUtf8("Others......"), self.trUtf8("Summary.....")]:
            k += 1
            if i == self.trUtf8("Summary....."):
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
        vorname = ""
        if ein.find('=') == 0:
            vorname = "X"
            eingabe = ein.lstrip('=').title()
        else:
            eingabe = ein.title()
        if not ein:
            return
        umbenennen = DarstellerUmbenennen(ein)
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
                    message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("New name already exists as alias, please first edit/delete the aliases"))
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
                        darsteller_liste[j] = darsteller_liste[j].strip().replace("'", "''")
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
                bildname = eingabe.lower().replace(" ", "_").replace("''", "_apostroph_")
                datei_alt = self.verzeichnis_thumbs +"/darsteller_" +res[0][1] +os.sep +bildname +".jpg"
                bildname = neuer_name.lower().strip().replace("'", "''").lstrip("=").replace(" ", "_").replace("''", "_apostroph_")
                datei_neu = self.verzeichnis_thumbs +"/darsteller_" +res[0][1] +os.sep +bildname +".jpg"
                sortier = Neueingabe(self.verzeichnis, self.verzeichnis_original, self.verzeichnis_thumbs, self.verzeichnis_trash, self.verzeichnis_cover, datei_alt)
                for i in res2:
                    l += 1
                    k = -1
                    for j in i[2]:
                        k += 1
                        if j == eingabe:
                            res2[l][2][k] = eingabe.title().lstrip("=").replace("''", "'")
                    darsteller_liste = sortier.darsteller_sortieren(res2[l][2])
                    darsteller_liste2 = [neuer_name.title().replace("'", "''") if x==eingabe.title().lstrip("=").replace("''", "'") else x for x in darsteller_liste]
                    werte = []
                    werte.append(", ".join(darsteller_liste2))
                    werte.append(i[0])
                    werte.append(i[1])
                    zu_erfassen.append(["UPDATE pordb_vid SET darsteller = %s WHERE cd = %s AND bild = %s", werte])

                self.statusBar.showMessage(str(len(res2)) + self.trUtf8(" lines changed"))
                
                zu_lesen = "SELECT * FROM pordb_partner WHERE darsteller = %s"
                lese_func = DBLesen(self, zu_lesen, eingabe)
                res = DBLesen.get_data(lese_func)
                for i in res:
                    werte = []
                    werte.append(neuer_name.title())
                    werte.append(str(i[1]))
                    werte.append(i[2])
                    werte.append(str(i[3]))
                    zu_erfassen.append(["INSERT INTO pordb_partner VALUES (%s, %s, %s,%s)", werte])
                    werte = []
                    werte.append(eingabe)
                    zu_erfassen.append(["DELETE FROM pordb_partner WHERE darsteller = %s", werte])
                    
                zu_lesen = "SELECT * FROM pordb_partner WHERE partner = %s"
                lese_func = DBLesen(self, zu_lesen, eingabe)
                res = DBLesen.get_data(lese_func)
                for i in res:
                    werte = []
                    werte.append(str(i[0]))
                    werte.append(neuer_name.title())
                    werte.append(i[2])
                    werte.append(str(i[3]))
                    zu_erfassen.append(["INSERT INTO pordb_partner VALUES (%s, %s, %s, %s)", werte])
                    werte = []
                    werte.append(eingabe)
                    zu_erfassen.append(["DELETE FROM pordb_partner WHERE partner = %s", werte])
                    
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
                            message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Image file could not be renamed"))
                    elif datei == 2:
                        try:
                            os.remove(datei_alt)
                        except:
                            message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Image file could not be renamed"))
                    else:
                        message = QtGui.QMessageBox.information(self, self.trUtf8("Information "), self.trUtf8("Renaming canceled"))
                        self.suchfeld.setCurrentIndex(-1)
                        self.suchfeld.setFocus()
                        return
                else:
                    try:
                        os.rename(datei_alt, datei_neu)
                    except:
                        message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Image file could not be renamed"))
                    
        try:
            self.labelDarsteller.setText(neuer_name.replace("''", "'").title())
        except:
            pass
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
        geschlecht = res[0][1]
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
        self.pushButtonSort.setText(QtGui.QApplication.translate("Dialog", "Year", None, QtGui.QApplication.UnicodeUTF8))
    # end of onDarstellerFilme
    
    def onPartnerSortieren(self):
        def vergleich(a):
            wert1 = a[a.rfind("(") + 1 : a.rfind(")")]
            return int(wert1)
                
        text = self.pushButtonSortPartner.text()
        if text == self.trUtf8("Quantity"):
            items = []
            for i in range(self.listWidgetDarsteller.count()):
                items.append(str(self.listWidgetDarsteller.item(i).text()).strip())
            items.sort(key = vergleich)
            items.reverse()
            self.listWidgetDarsteller.clear()
            self.listWidgetDarsteller.addItems(items)
            self.pushButtonSortPartner.setText(QtGui.QApplication.translate("Dialog", "Partner", None, QtGui.QApplication.UnicodeUTF8))
        else:
            self.listWidgetDarsteller.sortItems()
            self.pushButtonSortPartner.setText(QtGui.QApplication.translate("Dialog", "Quantity", None, QtGui.QApplication.UnicodeUTF8))
        self.suchfeld.setFocus()
    # end of onPartnerSortieren
        
    def onFilmeSortieren(self):
        def vergleich(a):
            try:
                return a.split()[-1]
            except:
                return 0
                
        text = self.pushButtonSort.text()
        if text == self.trUtf8("Year"):
            items = []
            for i in range(self.listWidgetFilme.count()):
                items.append(str(self.listWidgetFilme.item(i).text()).strip())
            items.sort(key = vergleich)
            self.listWidgetFilme.clear()
            self.listWidgetFilme.addItems(items)
            self.pushButtonSort.setText(QtGui.QApplication.translate("Dialog", "Title", None, QtGui.QApplication.UnicodeUTF8))
        else:
            self.listWidgetFilme.sortItems()
            self.pushButtonSort.setText(QtGui.QApplication.translate("Dialog", "Year", None, QtGui.QApplication.UnicodeUTF8))
        self.suchfeld.setFocus()
    # end of onFilmeSortieren

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
    
    def onSuchen(self):
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
                message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Only digits allowed as filesize"))
                return
        if self.lineEditFilesizeTo.text():
            try:
                filesizeto = float(self.lineEditFilesizeTo.text().replace(",", "."))
            except:
                self.lineEditFilesizeTo.setFocus()
                self.lineEditFilesizeTo.selectAll()
                message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Only digits allowed as filesize"))
                return
        
        if not ein and not filesizefrom and not filesizeto:
            self.lineEditSuchen.setFocus()
            return
            
        werte = []
        if ein:
            zu_lesen = "SELECT * FROM pordb_mpg_katalog WHERE LOWER(file) LIKE %s" 
            werte.append("%" + ein.lower().replace(" ", "%") + "%")
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
                    message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Filesize to must be bigger than filesize from"))
                    return
                    
            else:
                groesse2 = (filesizefrom + 0.005) * faktor
            if ein:
                zu_lesen += " AND "
            zu_lesen += "groesse >= %s AND groesse < %s"
            werte.append(groesse1)
            werte.append(groesse2)
        zu_lesen += " ORDER BY file"
        if len(ein) < 3 and not filesizefrom:
            self.lineEditSuchen.setFocus()
            message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Please enter at least 3 characters in the searchfield"))
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
                mb = 0
                try:    # fieldtype is char
                    newitem = QtGui.QTableWidgetItem(zeilen[i][j].strip())
                except:
                    try:    # fieldtype is int
                        newitem = QtGui.QTableWidgetItem()
                        if type(zeilen[i][j]) == int:
                            wert = locale.format("%d", zeilen[i][j], grouping=True)
                            newitem.setData(0, wert)
                        elif type(zeilen[i][j]) == float:
                            wert = locale.format("%.2f", zeilen[i][j], grouping=True)
                            newitem.setData(0, wert)
                        else:
                            newitem.setData(0, str(int(zeilen[i][j])))
                    except:    # fieldtype is None
                        newitem = QtGui.QTableWidgetItem(" ")
                self.tableWidget.setItem(i, j, newitem)
        try:
            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.resizeRowsToContents()
            self.tableWidget.setSortingEnabled(True)
        except:
            pass
        self.tableWidget.scrollToTop()
        zeilen = len(rows)
        self.labelMpgGefunden.setText(str(zeilen) +self.trUtf8(" found"))
        self.labelMpgFound.clear()
            
        self.tableWidget1.clearContents()
        if ein:
            werte = []
            werte_erweiterung = []
            zu_lesen = "SELECT * FROM pordb_original WHERE LOWER(original) LIKE %s"
            werte.append("%" + ein.lower().replace(" ", "%") + "%")
            lese_func = DBLesen(self, zu_lesen, werte)
            res = DBLesen.get_data(lese_func)
            original_erweiterung = ""
            for i in res:
                original_erweiterung += " OR primkey = %s"
                werte_erweiterung.append(str(i[2]))
            
            werte = []
            zu_lesen = "SELECT * FROM pordb_vid WHERE LOWER(original) LIKE %s OR LOWER(titel) LIKE %s"
            werte.append("%" + ein.lower() + "%")
            werte.append("%" + ein.lower().replace(" ", "%") + "%")
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
                        newitem = QtGui.QTableWidgetItem(res[i][j].strip())
                    except:
                        try:    # fieldtype is int
                            newitem = QtGui.QTableWidgetItem(str(res[i][j]))
                        except:    # fieldtype is None
                            newitem = QtGui.QTableWidgetItem(" ")
                    self.tableWidget1.setItem(i, j, newitem)
            try:
                self.tableWidget1.resizeColumnsToContents()
                self.tableWidget1.resizeRowsToContents()
                self.tableWidget1.setSortingEnabled(True)
            except:
                pass
            self.tableWidget1.scrollToTop()
            zeilen = len(res)
            self.labelVidGefunden.setText(str(zeilen) +self.trUtf8(" found"))
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
            self.labelMpgFound.setText(self.trUtf8("found: ") + str(anzahl))
        
    def onSearchVid(self):
        if self.searchResultsVid:
            anzahl = self.searchResults(self.lineEditSearchVid, self.tableWidget1, self.searchResultsVid, (0, 5))
            self.labelVidFound.setText(self.trUtf8("found: ") + str(anzahl))
        
    def searchResults(self, lineEdit, tableWidget, rows, column):
        tableWidget.clearSelection()
        tableWidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
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
        #Logik:
        #1. Suchen nach 'class="moviecount">'
        #2. dann bis zum nächsten Blank: dazwischen ist Anzahl Movies
        #3. Suchen nach "tr class"
        #4. dann Suchen nach '.htm">'
        #5. dann Suchen nach dem nächsten "<": dazwischen ist der Titel
        #6. weiter bei 3.
        
        text = str(self.webView.page().mainFrame().toHtml())
        anfang = text.find('class="moviecount">')
        ende = text.find(' ', anfang)
        anzahl = 0
        try:
            anzahl = int(text[anfang+19:ende])
        except:
            pass
        titel = []
        if anzahl:
            for i in range(anzahl):
                anfang = text.find("tr class", ende)
                anfang2 = text.find('.htm">', anfang)
                ende = text.find("<", anfang2)
                titel.append(text[anfang2+6:ende].strip())
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
            geschlecht = bilddialog.ethnic
        except:
            fehler = True
        if not fehler:
            bilddialog.exec_()
        self.suchfeld.setFocus()
        
    def onMovieData(self):
        url = self.webView.url().toString()
        text = str(self.webView.page().mainFrame().toHtml())
        movie_data = SaveMovieData(app, url, text)
        res = SaveMovieData.get_data(movie_data)
        if res:
            show_iafd_data = ShowIafdData(self.verzeichnis, self.verzeichnis_original, self.verzeichnis_thumbs, self.verzeichnis_trash, self.verzeichnis_cover, res)
            show_iafd_data.exec_()
        self.suchfeld.setFocus()
        
    def onLinkClicked(self, url):
        self.webView.load(QtCore.QUrl(url))
        
    def onUrlChanged(self, url):
        self.url = url.toString()
        self.statusBar.showMessage(self.url)
        
    def GetWebsite(self):
        if str(self.lineEditURL.text()).startswith("http://"):
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
            newitem = QtGui.QTableWidgetItem(self.cumshots[i])
            j += 1
            self.tableWidgetStatistik.setItem(j, 0, newitem)
            newitem = QtGui.QTableWidgetItem()
            if res[0][0]:
                newitem.setData(0, res[0][0])
            else:
                newitem.setData(0, 0)
            newitem.setTextAlignment(QtCore.Qt.AlignRight)
            self.tableWidgetStatistik.setItem(j, 1, newitem)
        newitem = QtGui.QTableWidgetItem(self.trUtf8("Summary"))
        j += 1
        self.tableWidgetStatistik.setItem(j, 0, newitem)
        newitem = QtGui.QTableWidgetItem()
        newitem.setData(0, gesamt)
        newitem.setTextAlignment(QtCore.Qt.AlignRight)
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
            message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Quantity is not a number"))
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
            message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Quantity is not a number"))
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
            newitem = QtGui.QTableWidgetItem(i[0])
            j += 1
            self.tableWidgetStatistik.setItem(j, 0, newitem)
            newitem = QtGui.QTableWidgetItem()
            newitem.setData(0, i[1])
            newitem.setTextAlignment(QtCore.Qt.AlignRight)
            self.tableWidgetStatistik.setItem(j, 1, newitem)
            newitem = QtGui.QTableWidgetItem()
            newitem.setData(0, i[2])
            newitem.setTextAlignment(QtCore.Qt.AlignRight)
            self.tableWidgetStatistik.setItem(j, 2, newitem)
            if i[3]:
                newitem = QtGui.QTableWidgetItem(i[3])
            else:
                newitem = QtGui.QTableWidgetItem("")
            self.tableWidgetStatistik.setItem(j, 3, newitem)
            try:
                geboren = (str(i[4])[0:10]).split("-")
                jahr = int(geboren[0])
                monat = int(geboren[1])
                tag = int(geboren[2])
                if jahr != 1:
                    alter = age((datetime.date(jahr, monat, tag)))
                    newitem = QtGui.QTableWidgetItem(str(alter))
                else:
                    newitem = QtGui.QTableWidgetItem()
            except:
                newitem = QtGui.QTableWidgetItem()
            self.tableWidgetStatistik.setItem(j, 4, newitem)
            newitem = QtGui.QTableWidgetItem()
            if i[5]:
                newitem.setData(0, i[5])
            else:
                newitem.setData(0, 0)
            newitem.setTextAlignment(QtCore.Qt.AlignRight)
            self.tableWidgetStatistik.setItem(j, 5, newitem)
        self.tableWidgetStatistik.setHorizontalHeaderLabels([self.trUtf8("Actor"), self.trUtf8("Quantity"), self.trUtf8("Partner"), self.trUtf8("Nation"), self.trUtf8("Age"), self.trUtf8("Movies")])
        self.tableWidgetStatistik.resizeColumnsToContents()
        self.tableWidgetStatistik.resizeRowsToContents()
        self.tableWidgetStatistik.setSortingEnabled(True)
        self.tableWidgetStatistik.sortItems(2, 1)
        self.tableWidgetStatistik.scrollToTop()
        self.suchfeld.setFocus()
        
    def onStatistikAnzahlClips(self):
        zu_lesen = "SELECT COUNT (*) FROM pordb_vid"
        lese_func = DBLesen(self, zu_lesen)
        res = DBLesen.get_data(lese_func)
        try:
            QtGui.QMessageBox.information(self, "PorDB", self.trUtf8("Quantity of movies: ") +str(res[0][0]))
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

        datum_akt = str(time.localtime()[0]) + '-' + str(time.localtime()[1]) + '-' + str(time.localtime()[2])
        akt_jahr = datum_akt[0:4]
        
        self.tableWidgetStatistik.setSortingEnabled(False)
        self.tableWidgetStatistik.clear()
        self.tableWidgetStatistik.setRowCount(len(jahre_titel))
        self.tableWidgetStatistik.setColumnCount(2)
        self.tableWidgetStatistik.setAlternatingRowColors(True)
        j = -1
        datum_alt = "1900-01-01"
        gesamt = 0
        datum = []
        for i in jahre_titel:
            j += 1
            k = 0
            newitem = QtGui.QTableWidgetItem()
            newitem.setData(0, i)
            newitem.setTextAlignment(QtCore.Qt.AlignRight)
            self.tableWidgetStatistik.setItem(j, k, newitem)
            k = 1
            newitem = QtGui.QTableWidgetItem()
            try:
                newitem.setData(0, jahre[i])
            except:
                newitem.setData(0, 0)
            newitem.setTextAlignment(QtCore.Qt.AlignRight)
            self.tableWidgetStatistik.setItem(j, k, newitem)
            try:
                gesamt += jahre[i]
            except:
                pass
        if datum_alt != "1900-01-01":
            k += 1
            newitem = QtGui.QTableWidgetItem()
            newitem.setData(0, gesamt)
            newitem.setTextAlignment(QtCore.Qt.AlignRight)
            self.tableWidgetStatistik.setItem(j, k, newitem)
        self.tableWidgetStatistik.setHorizontalHeaderLabels([self.trUtf8("Year"), self.trUtf8("Quantity")])
        self.tableWidgetStatistik.resizeColumnsToContents()
        self.tableWidgetStatistik.resizeRowsToContents()
        self.tableWidgetStatistik.setSortingEnabled(True)
        self.tableWidgetStatistik.sortItems(0)
        self.tableWidgetStatistik.scrollToBottom()
        
        app.restoreOverrideCursor()
        self.suchfeld.setFocus()
        
    def onCheckNewVersion(self, initial=True):
        global initial_run
        version = None
        whatsnew = None
        seite = None
        zaehler = 0
        while True:
            zaehler += 1
            try:
                seite = urllib.request.urlopen(file_version).read()
                if seite:
                    break
                else:
                    pass
            except:
                pass
            if zaehler > 1:
                break
    
        if seite:
            begin = str(seite).find("pordbversion")
            version = str(seite)[begin + 21 : begin + 21 + str(seite)[begin + 21 :].find("&")]
            if version != __version__:
                begin = str(seite).find("whatsnew")
                whatsnew = str(seite)[begin + 17 : begin + 17 + str(seite)[begin + 17 :].find("&")]
                dialog = UpdateVersion(version, whatsnew)
                if dialog.exec_():
                    desktop_directory = str(os.path.expanduser("~") +os.sep +".local/share/applications")
                    desktop_datei = desktop_directory + os.sep + "PorDB.desktop"
                    if not os.path.exists(desktop_directory):
                        os.makedirs(desktop_directory)
                    messageBox = QtGui.QMessageBox()
                    messageBox.addButton(self.trUtf8("Yes"), QtGui.QMessageBox.AcceptRole)
                    messageBox.addButton(self.trUtf8("No"), QtGui.QMessageBox.RejectRole)
                    messageBox.setWindowTitle(self.trUtf8("Menu entry"))
                    messageBox.setIcon(QtGui.QMessageBox.Question)
                    messageBox.setText(self.trUtf8("Should I create a menu entry?"))
                    message = messageBox.exec_()
                    if message == 0:
                        try:
                            datei = open(desktop_datei, "w")
                            datei.write("[Desktop Entry]" + "\n")
                            datei.write("Comment=PorDB" + "\n")
                            datei.write("Exec=python3 " + os.getcwd() + os.sep + "pordb.py" + "\n")
                            datei.write("Icon=" + os.getcwd() + os.sep + "pypordb/8027068_splash.png" + "\n")
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
                            message = QtGui.QMessageBox.information(self, self.trUtf8("Information "), self.trUtf8("Menu entry added under graphics"))
                        except:
                            message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Adding of menu entry failed"))
                            
                    python = sys.executable
                    os.execl(python, python, * sys.argv)
            else:
                if not initial_run:
                    message = QtGui.QMessageBox.information(self, self.trUtf8("Information "), self.trUtf8("You have the latest version"))
                    self.suchfeld.setFocus()
        
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
            zu_lesen = "SELECT * FROM information_schema.tables WHERE table_schema = %s AND table_name NOT LIKE %s AND table_name LIKE %s ORDER BY table_name"
            lese_func = DBLesen(self, zu_lesen, ("public", "pga_%", "pordb%"))
            res = DBLesen.get_data(lese_func)
            db_host = "localhost"
            try:
                self.conn = psycopg2.connect(database=dbname, host=db_host)
            except Exception as e:
                message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Connection to database failed"))
                return
            self.cur = self.conn.cursor()
            for i in res:
                datei = open(self.verzeichnis_original +os.sep +i[2] +".txt", "w")
                try:
                    self.cur.copy_to(datei, i[2], sep='|')
                except Exception as e:
                    message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Copy to file failed"))
                    return
                datei.close()
                
        # Backup picture directory
        if self.checkBoxPictures.isChecked():
            tar = tarfile.open(self.verzeichnis_original +os.sep +"archive.tar.gz", "w:gz")
            tar.add(self.verzeichnis_thumbs)
            tar.close()
            
            datei = open(self.verzeichnis_original +os.sep +"archive.tar.gz", "rb")
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
            os.remove(self.verzeichnis_original +os.sep +"archive.tar.gz")
        
        app.restoreOverrideCursor()
        self.suchfeld.setFocus()
        message = QtGui.QMessageBox(self)
        message.setText(self.trUtf8("Backup in directory ") +self.verzeichnis_original + self.trUtf8(" created"))
        message.exec_()
        
    def onRestore(self):
        app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        import tarfile
        nachricht = self.trUtf8("No files found for restoring")
        
        # Restore the database
        db_host="localhost"
        try:
            self.conn = psycopg2.connect(database=dbname, host=db_host)
        except Exception as e:
            message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Connection to database failed"))
            return
        self.cur = self.conn.cursor()
        dateiliste = os.listdir(self.verzeichnis)
        # caused by foreign keys, the following tables has to be processed first
        try:
            dateiliste.remove("pordb_vid.txt")
            dateiliste.remove("pordb_darsteller.txt")
            dateiliste.insert(0, "pordb_darsteller.txt")
            dateiliste.insert(0, "pordb_vid.txt")
        except:
            pass
        dateien_gefunden = False
        for i in dateiliste:
            if i.startswith("pordb_") and i.endswith(".txt"):
                tabelle = i.rstrip(".txt")
                datei = open(self.verzeichnis +os.sep +i, "r")
                delete = "truncate " +tabelle +" CASCADE"                
                try:
                    self.cur.execute(delete)
                except Exception as e:
                    app.restoreOverrideCursor()
                    message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Truncate for table " +i +" failed: " +str(e)))
                    datei.close()
                    return
                try:
                    self.cur.copy_from(datei, tabelle, sep='|')
                    dateien_gefunden = True
                except Exception as e:
                    app.restoreOverrideCursor()
                    message = QtGui.QMessageBox.critical(self, self.trUtf8("Error "), self.trUtf8("Copy from file " +i +" failed: " +str(e)))
                    datei.close()
                    return
                datei.close()
                
        self.conn.commit()
        
        if dateien_gefunden:
            for i in dateiliste:
                if i.startswith("pordb_") and i.endswith(".txt"):
                    os.remove(self.verzeichnis +os.sep +i)
            nachricht = self.trUtf8("Database restore was successful")

        # Restore the picture directory
        parts = os.listdir(self.verzeichnis)
        parts.sort()
        output = open(self.verzeichnis +os.sep +"archive.tar.gz", "wb")
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
        if os.path.isfile(self.verzeichnis +os.sep +"archive.tar.gz") and os.path.getsize(self.verzeichnis +os.sep +"archive.tar.gz") == 0:
            os.remove(self.verzeichnis +os.sep +"archive.tar.gz")
        if bilddatei_gefunden:
            if os.path.isfile(self.verzeichnis +os.sep +"archive.tar.gz"):
                tar = tarfile.open(self.verzeichnis +os.sep +"archive.tar.gz")
                try:
                    tar.extractall(path=self.verzeichnis)
                except:
                    self.suchfeld.setFocus()
                    message = QtGui.QMessageBox(self)
                    message.setText(self.trUtf8("Restore from directory ") +self.verzeichnis + self.trUtf8(" failed. In most cases there is a file with an invalid creation/change date."))
                    message.exec_()
                    app.restoreOverrideCursor()
                    return
                tar.close()
            else:
                self.suchfeld.setFocus()
                app.restoreOverrideCursor()
                message = QtGui.QMessageBox(self)
                message.setText(self.trUtf8("Restore from directory ") +self.verzeichnis + self.trUtf8(" failed. No backup files found."))
                message.exec_()
                return
            if dateien_gefunden:
                nachricht += "; "
            nachricht += self.trUtf8("Backup in directory ") +self.verzeichnis + self.trUtf8(" restored. You can now copy the complete directory to its origin place.")

        app.restoreOverrideCursor()
        self.suchfeld.setFocus()
        message = QtGui.QMessageBox(self)
        message.setText(nachricht)
        message.exec_()
        
    def onWartung(self):
        app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        befehl = "/usr/bin/vacuumdb --analyze por"
        os.system(befehl)
        app.restoreOverrideCursor()
        self.suchfeld.setFocus()
        message = QtGui.QMessageBox(self)
        message.setText(self.trUtf8("Maintenance executed"))
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
        from pypordb_genericthread import GenericThread
        
        if not self.comboBoxDevice.currentText():
            message = QtGui.QMessageBox(self)
            message.setText(self.trUtf8("Select device"))
            message.exec_()
            return
            
        self.verzeichnis_tools = str(QtGui.QFileDialog.getExistingDirectory(self, self.trUtf8("Select directory"), "/"))
        if self.verzeichnis_tools:
            self.dateien = os.listdir(self.verzeichnis_tools)
            self.dateien.sort()
        else:
            return
        
        for i in self.dateien:
            if len(i) > 256:
                message = QtGui.QMessageBox(self)
                message.setText(self.trUtf8("Error, filename ") +i +self.trUtf8(" to long"))
                message.exec_()
                return
            
        self.threadPool = []
        
        # generic thread using signal
        self.threadPool.append(GenericThread(self.addFiles))
        # signal for updating current file
        self.disconnect(self, QtCore.SIGNAL("add(QString)"), self.updateFileLabel)
        self.connect(self, QtCore.SIGNAL("add(QString)"), self.updateFileLabel)
        # signal for finished
        self.connect(self, QtCore.SIGNAL("finished"), self.output_result)
        # start thread
        self.threadPool[len(self.threadPool)-1].start()
        
    # end of onStartScan
    
    def addFiles(self):
        self.res_duplicates = []
        zu_erfassen = []
        
        for i in self.dateien:
            self.emit(QtCore.SIGNAL("add(QString)"), i)
            zu_lesen = "SELECT * FROM pordb_mpg_katalog WHERE file = %s OR groesse = %s"
            lese_func = DBLesen(self, zu_lesen, (i, str(os.path.getsize(self.verzeichnis_tools +os.sep +i.strip()))))
            res = DBLesen.get_data(lese_func)
            in_datenbank = True
            for j in res:
                if j[0].strip() == str(self.comboBoxDevice.currentText()).strip() and j[1].strip() == os.path.basename(self.verzeichnis_tools) and j[2].replace("'", "''").strip() == i.replace("'", "''").strip():
                    in_datenbank = False
                
            if in_datenbank:
                for j in res:
                    # put only in duplicate list, when actual directory is another one than that in database
                    if j[1].strip() != os.path.basename(self.verzeichnis_tools).strip(): 
                        a = list(j)
                        a.append(i)
                        a.append(int(os.path.getsize(self.verzeichnis_tools +os.sep +i.strip())))
                        self.res_duplicates.append(a)
                werte = []
                werte.append(str(self.comboBoxDevice.currentText()))
                werte.append(os.path.basename(self.verzeichnis_tools))
                werte.append(i)
                werte.append(None)
                werte.append(os.path.getsize(self.verzeichnis_tools + os.sep + i))
                zu_erfassen.append(["INSERT INTO pordb_mpg_katalog VALUES (%s, %s, %s, %s, %s)", werte])
                    
        update_func = DBUpdate(self, zu_erfassen)
        DBUpdate.update_data(update_func)
        self.files_added = str(len(zu_erfassen))
        self.emit(QtCore.SIGNAL("finished"))
        
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
            newitem = QtGui.QTableWidgetItem()
            newitem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable)
            if self.verzeichnis_tools +os.sep +j[5].strip() == j[2].strip() and str(j[4]) == str(os.path.getsize(self.verzeichnis_tools +os.sep +j[5].strip())):
                newitem.setCheckState(QtCore.Qt.Checked)
                counter += 1
            else:
                newitem.setCheckState(QtCore.Qt.Unchecked)
            self.tableWidgetDubletten.setItem(self.row, self.column, newitem)
            self.column += 1
            newitem = QtGui.QTableWidgetItem(j[2].strip())     # Filename
            self.tableWidgetDubletten.setItem(self.row, self.column, newitem)
            self.column += 1
            newitem = QtGui.QTableWidgetItem(j[0].strip())        # Device
            self.tableWidgetDubletten.setItem(self.row, self.column, newitem)
            self.column += 1
            newitem = QtGui.QTableWidgetItem(j[1].strip())        # Directory
            self.tableWidgetDubletten.setItem(self.row, self.column, newitem)
            self.column += 1
            newitem = QtGui.QTableWidgetItem(str(j[4]))    # Size in database
            self.tableWidgetDubletten.setItem(self.row, self.column, newitem)
            self.column += 1
            newitem = QtGui.QTableWidgetItem(j[5].strip())     # new Filename
            self.tableWidgetDubletten.setItem(self.row, self.column, newitem)
            self.column += 1
            newitem = QtGui.QTableWidgetItem(str(j[6]))    # Size of new file
            self.tableWidgetDubletten.setItem(self.row, self.column, newitem)
            self.row += 1
            self.column = 0
            
        self.tableWidgetDubletten.setHorizontalHeaderLabels([self.trUtf8("delete"), self.trUtf8("File in database"), self.trUtf8("Device"), self.trUtf8("Directory"), self.trUtf8("Size in database"), self.trUtf8("new file"), self.trUtf8("Size of new file")])
        self.tableWidgetDubletten.resizeColumnsToContents()
        self.tableWidgetDubletten.resizeRowsToContents()
        
        message = self.files_added + self.trUtf8(" File(s) collected")
        if len(self.res_duplicates) > 0:
            self.pushButtonDeleteDuplicates.setEnabled(True)
            self.pushButtonDeselect.setEnabled(True)
            if counter > 0:
                message += ", " +str(counter) +self.trUtf8(" Duplicate(s) found") 
            else:
                message += ", " +str(len(self.res_duplicates)) +self.trUtf8(" Duplicate(s) found, but some of them only in relation to file size")
        
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
                    os.remove(self.verzeichnis_tools +os.sep +str(self.tableWidgetDubletten.item(i, 5).text()).strip())
                    counter += 1
                except:
                    pass
        if counter > 0:
            update_func = DBUpdate(self, zu_erfassen)
            DBUpdate.update_data(update_func)
            message = str(counter) +self.trUtf8(" File(s) deleted")
        else:
            message = ""
        self.statusBar.showMessage(message)
        app.restoreOverrideCursor()
        self.suchfeld.setFocus()
        
    def onDeselect(self):
        for i in range(self.tableWidgetDubletten.rowCount()):
            self.tableWidgetDubletten.item(i, 0).setCheckState(QtCore.Qt.Unchecked)
        self.suchfeld.setFocus()
        
app = QtGui.QApplication(sys.argv)
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
