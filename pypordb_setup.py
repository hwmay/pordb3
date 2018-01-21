#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
from PyQt4 import QtGui, QtCore
from pordb_setup import Ui_Dialog as Dialog
import zipfile

class Dialog(QtGui.QDialog, Dialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)   
        
        self.connect(self.pushButtonNext, QtCore.SIGNAL("clicked()"), self.onNext)
        self.connect(self.pushButtonBack, QtCore.SIGNAL("clicked()"), self.onBack)
        self.connect(self.pushButtonDir, QtCore.SIGNAL("clicked()"), self.onDirectory)
        self.connect(self.pushButtonZip, QtCore.SIGNAL("clicked()"), self.onZipFile)
        
        self.neuer_tab = 0
        self.verzeichnis = os.path.expanduser("~")
        self.file = None
        self.pushButtonBack.setEnabled(False)
        self.pushButtonNext.setEnabled(True)
        self.error = False

    def onNext(self):
        if self.neuer_tab == 0:
            self.init_db()
        elif self.neuer_tab == 3:
            self.install()
        elif self.neuer_tab == 4:
            self.close()
        self.neuer_tab = min(self.tabWidget.currentIndex() + 1, 4)
        self.tabWidget.setCurrentIndex(self.neuer_tab)
        self.pushButtonBack.setEnabled(True)
        if self.neuer_tab == 0:
            self.pushButtonNext.setEnabled(True)
        elif self.neuer_tab == 2:
            self.pushButtonNext.setEnabled(False)
        elif self.neuer_tab == 4:
            self.pushButtonNext.setText(self.tr("Finish"))
        else:
            self.pushButtonNext.setText(self.tr("Next"))
        
    def onBack(self):
        self.neuer_tab = self.tabWidget.currentIndex() - 1
        self.tabWidget.setCurrentIndex(self.neuer_tab)
        if self.neuer_tab == 0:
            self.pushButtonBack.setEnabled(False)
            self.pushButtonNext.setEnabled(True)
        elif self.neuer_tab == 1:
            self.pushButtonNext.setEnabled(True)
        elif self.neuer_tab == 4:
            self.pushButtonNext.setText(self.tr("Finish"))
        else:
            self.pushButtonNext.setText(self.tr("Next"))
            
    def onDirectory(self):
        datei = QtGui.QFileDialog.getExistingDirectory(self, self.tr("Select directory or create a new one"), self.verzeichnis)
        if datei:
            self.verzeichnis = str(datei)
            self.labelDirectory.setText(self.tr("Directory: ") +self.verzeichnis)
            
    def onZipFile(self):
        datei = QtGui.QFileDialog.getOpenFileName(self, self.tr("Zip file"), os.path.expanduser("~"), self.tr("Zip files (*.zip *.ZIP);;all files (*.*)"))
        if datei:
            self.file = str(datei)
            self.labelFile.setText(self.tr("File: ") +self.file)
            self.pushButtonNext.setEnabled(True)
            
    def install(self):
        # Create all directories
        directory = os.path.join(os.path.expanduser("~"), "mpg")
        self.create_directory(directory)
        if self.error:
            pass
        
        directory = os.path.join(os.path.expanduser("~"), "thumbs_sammlung")
        self.create_directory(directory)
        if self.error:
            pass
        
        directory_new = os.path.join(directory, "cover")
        self.create_directory(directory)
        if self.error:
            pass
        
        directory_new = os.path.join(directory, "darsteller_m")
        self.create_directory(directory_new)
        if self.error:
            pass
        
        directory_new = os.path.join(directory, "darsteller_w")
        self.create_directory(directory_new)
        if self.error:
            pass
        
        directory_new = os.path.join(directory, "nichtvorhanden")
        self.create_directory(directory_new)
        if self.error:
            pass
        
        directory_new = os.path.join(directory, "trash")
        self.create_directory(directory_new)
        if self.error:
            pass
        
        # Unzip and move all files to installation directory
        file = zipfile.ZipFile(self.file, "r")
        zipfile.ZipFile.extractall(file, self.verzeichnis)
        self.listWidget.addItem(self.tr("Congratulations, PorDB3 installation was successful!"))
        self.listWidget.addItem("")
        self.listWidget.addItem(self.tr("How to start?"))
        self.listWidget.addItem(self.tr("Postgresql database server must be running!"))
        self.listWidget.addItem(self.tr("Go to install directory ") + os.path.join(self.verzeichnis, "pordb-master"))
        self.listWidget.addItem(self.tr("Start the PorDB3 with command 'python3 pordb.py &'"))
        
    def create_directory(self, directory):
        try:
            os.mkdir(directory)
        except:
            message = QtGui.QMessageBox.information(self, self.tr("Warning "), self.tr("Directory ") +directory +self.tr(" already exists, nothing changed"))
            self.error = True
            return
        self.listWidget.addItem(self.tr("Directory ") +directory +self.tr(" created"))
        
    def init_db(self):
        app.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        try:
            import psycopg2
            import psycopg2.extensions
        except:
            app.restoreOverrideCursor()
            message = QtGui.QMessageBox.critical(self, self.tr("Fatal error "), self.tr("Package psycopg2 not found. You have to install this package first."))
            self.error = True
            return
        db_host='localhost'
        # Create database
        database = "por"
        conn = psycopg2.connect(database="postgres", host=db_host)
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        try:
            cur.execute("CREATE DATABASE " +database  +" ENCODING='UTF8' TEMPLATE=template0 OWNER=postgres TABLESPACE=pg_default LC_COLLATE = 'C' LC_CTYPE = 'C' CONNECTION LIMIT = -1")
        except Exception as e:
            messageBox = QtGui.QMessageBox()
            messageBox.addButton(self.tr("Yes, delete database and all data in it"), QtGui.QMessageBox.AcceptRole)
            messageBox.addButton(self.tr("No, abort installation"), QtGui.QMessageBox.RejectRole)
            button_No = messageBox.addButton(self.tr("No, only software installation"), QtGui.QMessageBox.YesRole)
            messageBox.setDefaultButton(button_No)
            messageBox.setWindowTitle(self.tr("Database already exists"))
            messageBox.setIcon(QtGui.QMessageBox.Warning)
            messageBox.setText(self.tr("Should I drop the existing database and create a new one?"))
            message = messageBox.exec_()
            if message == 2: # Only software will be installed
                cur.close()
                conn.close()
                self.listWidgetDB.addItem(self.tr("Database has not been changed"))
                app.restoreOverrideCursor()
                return
            elif message == 0:
                try:
                    cur.execute("DROP DATABASE " +database +";")
                    cur.execute("CREATE DATABASE " +database +" ENCODING='UTF8' TEMPLATE=template0 OWNER=postgres TABLESPACE=pg_default LC_COLLATE = 'C' LC_CTYPE = 'C' CONNECTION LIMIT = -1")
                except Exception as e:
                    sys.exit()
            else:
                cur.close()
                conn.close()
                sys.exit()
        conn.commit()
        cur.close()
        conn.close()
        
        # Create tables
        conn = psycopg2.connect(database=database, host=db_host)
        cur = conn.cursor()
        cur.execute('CREATE TABLE pordb_mpg_verzeichnisse (dir character(10) NOT NULL, CONSTRAINT "key" PRIMARY KEY (dir)) WITH (OIDS=FALSE)')
        cur.execute("ALTER TABLE pordb_mpg_verzeichnisse OWNER TO postgres;")
        
        cur.execute('''CREATE TABLE pordb_darsteller (
    darsteller character(50) NOT NULL,
    sex character(1),
    anzahl integer NOT NULL,
    datum date,
    haarfarbe character(2),
    nation character(2),
    tattoo character varying(500),
    ethnic character(1),
    partner integer DEFAULT 0,
    geboren date,
    filme integer DEFAULT 0,
    url character varying,
    aktivvon integer,
    aktivbis integer,
    besuch date
);''')
        cur.execute("ALTER TABLE public.pordb_darsteller OWNER TO postgres;")
        
        cur.execute('''CREATE TABLE pordb_darsteller100 (
    nr integer NOT NULL,
    darsteller character(200) NOT NULL
);''')
        cur.execute("ALTER TABLE public.pordb_darsteller100 OWNER TO postgres;")
        
        cur.execute('''CREATE SEQUENCE pordb_darsteller100_nr_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;''')
        cur.execute("ALTER TABLE public.pordb_darsteller100_nr_seq OWNER TO postgres;")
        cur.execute("ALTER SEQUENCE pordb_darsteller100_nr_seq OWNED BY pordb_darsteller100.nr;")
        cur.execute("SELECT pg_catalog.setval('pordb_darsteller100_nr_seq', 1, true);")
        
        cur.execute('''CREATE TABLE pordb_iso_land (
    iso character(2) NOT NULL,
    land character(100),
    aktiv character(1),
    "national" character(100)
);''')
        cur.execute("ALTER TABLE public.pordb_iso_land OWNER TO postgres;")
        
        cur.execute('''CREATE TABLE pordb_mpg_katalog (
    device character(256) NOT NULL,
    dir character(256) NOT NULL,
    file character(256) NOT NULL,
    verarbeitet character(1),
    groesse bigint
);''')
        cur.execute("ALTER TABLE public.pordb_mpg_katalog OWNER TO postgres;")
        cur.execute("SET default_with_oids = true;")
        
        cur.execute('''CREATE TABLE pordb_partner (
    darsteller character(50) NOT NULL,
    partner character(50) NOT NULL,
    cd integer NOT NULL,
    bild character varying(256) NOT NULL
);''')
        cur.execute("ALTER TABLE public.pordb_partner OWNER TO postgres;")
        
        cur.execute('''CREATE TABLE pordb_bookmarks (
    url character varying(255) NOT NULL,
    z integer NOT NULL
);''')
        cur.execute("ALTER TABLE public.pordb_bookmarks OWNER TO postgres;")
        cur.execute('''CREATE SEQUENCE pordb_bookmarks_z_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;''')
        cur.execute("ALTER TABLE public.pordb_bookmarks_z_seq OWNER TO postgres;")
        cur.execute("ALTER SEQUENCE pordb_bookmarks_z_seq OWNED BY pordb_bookmarks.z;")
        cur.execute("SELECT pg_catalog.setval('pordb_bookmarks_z_seq', 1, true);")
        cur.execute("SET default_with_oids = false;")
        
        cur.execute('''CREATE TABLE pordb_history (
    "sql" character varying(5000) NOT NULL,
    "time" timestamp without time zone DEFAULT ('now'::text)::timestamp without time zone NOT NULL
);''')
        cur.execute("ALTER TABLE public.pordb_history OWNER TO postgres;")
        cur.execute("SET default_with_oids = true;")
        
        cur.execute('''CREATE TABLE pordb_original (
    pordb_original_key integer NOT NULL,
    original character(256) NOT NULL,
    foreign_key_pordb_vid integer NOT NULL
);''')
        cur.execute("ALTER TABLE public.pordb_original OWNER TO postgres;")
        cur.execute('''CREATE SEQUENCE pordb_original_pordb_original_key_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;''')
        cur.execute("ALTER TABLE public.pordb_original_pordb_original_key_seq OWNER TO postgres;")
        cur.execute("ALTER SEQUENCE pordb_original_pordb_original_key_seq OWNED BY pordb_original.pordb_original_key;")
        cur.execute("SELECT pg_catalog.setval('pordb_original_pordb_original_key_seq', 1, true);")
        
        cur.execute('''CREATE TABLE pordb_pseudo (
    pseudo character(256) NOT NULL,
    darsteller character(256) NOT NULL
);''')
        cur.execute("ALTER TABLE public.pordb_pseudo OWNER TO postgres;")
        cur.execute("SET default_with_oids = true;")
        
        cur.execute('''CREATE TABLE pordb_suchbegriffe (
    suchbegriff character(256) NOT NULL,
    alternative character(256) NOT NULL
);''')
        cur.execute("ALTER TABLE public.pordb_suchbegriffe OWNER TO postgres;")
        
        cur.execute('''CREATE TABLE pordb_suche (
    nr integer NOT NULL,
    suche character(200) NOT NULL
);''')
        cur.execute("ALTER TABLE public.pordb_suche OWNER TO postgres;")
        cur.execute('''CREATE SEQUENCE pordb_suche_nr_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;''')
        cur.execute("ALTER TABLE public.pordb_suche_nr_seq OWNER TO postgres;")
        cur.execute("ALTER SEQUENCE pordb_suche_nr_seq OWNED BY pordb_suche.nr;")
        cur.execute("SELECT pg_catalog.setval('pordb_suche_nr_seq', 1, true);")
        
        cur.execute('''CREATE TABLE pordb_vid (
    titel character varying(256) NOT NULL,
    darsteller character varying(256),
    cd integer NOT NULL,
    bild character varying(256) NOT NULL,
    gesehen character(1),
    original character varying(256),
    cs character(1),
    vorhanden character(1),
    primkey integer NOT NULL,
    csf integer DEFAULT 0,
    csh integer DEFAULT 0,
    cst integer DEFAULT 0,
    csc integer DEFAULT 0,
    csx integer DEFAULT 0,
    cso integer DEFAULT 0,
    csv integer DEFAULT 0,
    csb integer DEFAULT 0,
    csa integer DEFAULT 0,
    css integer DEFAULT 0,
    csk integer DEFAULT 0,
    hd  character(1),
    remarks VARCHAR(256),
    stars INTEGER
);''')
        cur.execute("ALTER TABLE public.pordb_vid OWNER TO postgres;")
        
        cur.execute('''CREATE TABLE pordb_vid_neu (
    titel character varying(256) NOT NULL,
    darsteller character varying(256),
    cd integer NOT NULL,
    original character varying(256),
    partnerw integer,
    partnerm integer,
    anzahl_bilder integer, 
    anzahl_spalten integer
);''')
        cur.execute("ALTER TABLE public.pordb_vid_neu OWNER TO postgres;")
        cur.execute('''CREATE SEQUENCE pordb_vid_primkey_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;''')
        cur.execute("ALTER TABLE public.pordb_vid_primkey_seq OWNER TO postgres;")
        cur.execute("ALTER SEQUENCE pordb_vid_primkey_seq OWNED BY pordb_vid.primkey;")
        cur.execute("SELECT pg_catalog.setval('pordb_vid_primkey_seq', 1, true);")
        cur.execute("ALTER TABLE pordb_darsteller100 ALTER COLUMN nr SET DEFAULT nextval('pordb_darsteller100_nr_seq'::regclass);")
        cur.execute("ALTER TABLE pordb_bookmarks ALTER COLUMN z SET DEFAULT nextval('pordb_bookmarks_z_seq'::regclass);")
        cur.execute("ALTER TABLE pordb_original ALTER COLUMN pordb_original_key SET DEFAULT nextval('pordb_original_pordb_original_key_seq'::regclass);")
        cur.execute("ALTER TABLE pordb_suche ALTER COLUMN nr SET DEFAULT nextval('pordb_suche_nr_seq'::regclass);")
        cur.execute("ALTER TABLE pordb_vid ALTER COLUMN primkey SET DEFAULT nextval('pordb_vid_primkey_seq'::regclass);")
        cur.execute("ALTER TABLE ONLY pordb_darsteller ADD CONSTRAINT pordb_darsteller_pkey PRIMARY KEY (darsteller);")
        cur.execute("ALTER TABLE ONLY pordb_iso_land ADD CONSTRAINT pordb_iso_land_pkey PRIMARY KEY (iso);")
        cur.execute("ALTER TABLE ONLY pordb_original ADD CONSTRAINT original_key PRIMARY KEY (pordb_original_key);")
        cur.execute("ALTER TABLE ONLY pordb_partner ADD CONSTRAINT pordb_partner_pkey PRIMARY KEY (darsteller, partner, cd, bild);")
        cur.execute('ALTER TABLE ONLY pordb_history ADD CONSTRAINT pordb_history_pkey PRIMARY KEY ("sql", "time");')
        cur.execute("ALTER TABLE ONLY pordb_mpg_katalog ADD CONSTRAINT prim PRIMARY KEY (device, dir, file);")
        cur.execute("ALTER TABLE ONLY pordb_suchbegriffe ADD CONSTRAINT primary_key PRIMARY KEY (suchbegriff, alternative);")
        cur.execute("ALTER TABLE ONLY pordb_pseudo ADD CONSTRAINT pseudodar PRIMARY KEY (pseudo, darsteller);")
        cur.execute("ALTER TABLE ONLY pordb_suche ADD CONSTRAINT pordb_suche_pkey PRIMARY KEY (nr);")
        cur.execute("ALTER TABLE ONLY pordb_vid ADD CONSTRAINT pordb_vid_key PRIMARY KEY (primkey);")
        cur.execute('CREATE INDEX "public.pordb_vid_cd" ON pordb_vid USING btree (cd);')
        cur.execute('CREATE INDEX "public.pordb_vid_darsteller" ON pordb_vid USING btree (darsteller);')
        cur.execute("ALTER TABLE ONLY pordb_pseudo ADD CONSTRAINT darsteller FOREIGN KEY (darsteller) REFERENCES pordb_darsteller(darsteller);")
        cur.execute("ALTER TABLE ONLY pordb_original ADD CONSTRAINT pordb_vid_id FOREIGN KEY (foreign_key_pordb_vid) REFERENCES pordb_vid(primkey) MATCH FULL ON DELETE CASCADE;")
        
        cur.execute("REVOKE ALL ON SCHEMA public FROM PUBLIC;")
        cur.execute("REVOKE ALL ON SCHEMA public FROM postgres;")
        cur.execute("GRANT ALL ON SCHEMA public TO postgres;")
        cur.execute("GRANT ALL ON SCHEMA public TO PUBLIC;")
        
        cur.execute("REVOKE ALL ON TABLE pordb_darsteller FROM PUBLIC;")
        cur.execute("REVOKE ALL ON TABLE pordb_darsteller FROM postgres;")
        cur.execute("GRANT ALL ON TABLE pordb_darsteller TO postgres;")
        cur.execute("GRANT ALL ON TABLE pordb_darsteller TO PUBLIC;")
        
        cur.execute("REVOKE ALL ON TABLE pordb_darsteller100 FROM PUBLIC;")
        cur.execute("REVOKE ALL ON TABLE pordb_darsteller100 FROM postgres;")
        cur.execute("GRANT ALL ON TABLE pordb_darsteller100 TO postgres;")
        cur.execute("GRANT ALL ON TABLE pordb_darsteller100 TO PUBLIC;")
        
        cur.execute("REVOKE ALL ON TABLE pordb_iso_land FROM PUBLIC;")
        cur.execute("REVOKE ALL ON TABLE pordb_iso_land FROM postgres;")
        cur.execute("GRANT ALL ON TABLE pordb_iso_land TO postgres;")
        cur.execute("GRANT ALL ON TABLE pordb_iso_land TO PUBLIC;")
        
        cur.execute("REVOKE ALL ON TABLE pordb_mpg_katalog FROM PUBLIC;")
        cur.execute("REVOKE ALL ON TABLE pordb_mpg_katalog FROM postgres;")
        cur.execute("GRANT ALL ON TABLE pordb_mpg_katalog TO postgres;")
        cur.execute("GRANT ALL ON TABLE pordb_mpg_katalog TO PUBLIC;")
        
        cur.execute("REVOKE ALL ON TABLE pordb_partner FROM PUBLIC;")
        cur.execute("REVOKE ALL ON TABLE pordb_partner FROM postgres;")
        cur.execute("GRANT ALL ON TABLE pordb_partner TO postgres;")
        cur.execute("GRANT ALL ON TABLE pordb_partner TO PUBLIC;")
        
        cur.execute("REVOKE ALL ON TABLE pordb_suche FROM PUBLIC;")
        cur.execute("REVOKE ALL ON TABLE pordb_suche FROM postgres;")
        cur.execute("GRANT ALL ON TABLE pordb_suche TO postgres;")
        cur.execute("GRANT ALL ON TABLE pordb_suche TO PUBLIC;")
        
        cur.execute("REVOKE ALL ON TABLE pordb_vid FROM PUBLIC;")
        cur.execute("REVOKE ALL ON TABLE pordb_vid FROM postgres;")
        cur.execute("GRANT ALL ON TABLE pordb_vid TO postgres;")
        cur.execute("GRANT ALL ON TABLE pordb_vid TO PUBLIC;")
        
        cur.execute("REVOKE ALL ON TABLE pordb_vid_neu FROM PUBLIC;")
        cur.execute("REVOKE ALL ON TABLE pordb_vid_neu FROM postgres;")
        cur.execute("GRANT ALL ON TABLE pordb_vid_neu TO postgres;")
        cur.execute("GRANT ALL ON TABLE pordb_vid_neu TO PUBLIC;")
        
        cur.execute('''INSERT INTO pordb_vid_neu(
            titel, darsteller, cd, original, partnerw, partnerm, anzahl_bilder, anzahl_spalten)
    VALUES ('', '', 1, '', 0, 0, 4, 4);''')
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('AF', 'AFGHANISTAN', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('AX', 'ALAND ISLANDS', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('AL', 'ALBANIA', 'x', 'Albanian')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('DZ', 'ALGERIA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('AS', 'AMERICAN SAMOA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('AD', 'ANDORRA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('AO', 'ANGOLA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('AI', 'ANGUILLA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('AQ', 'ANTARCTICA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('AG', 'ANTIGUA AND BARBUDA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('AR', 'ARGENTINA', 'x', 'Argentinian')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('AM', 'ARMENIA', 'x', 'Armenian')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('AW', 'ARUBA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('AU', 'AUSTRALIA', 'x', 'Australian')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('AT', 'AUSTRIA', 'x', 'Austrian')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('AZ', 'AZERBAIJAN', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('BS', 'BAHAMAS', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('BH', 'BAHRAIN', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('BD', 'BANGLADESH', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('BB', 'BARBADOS', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('BY', 'BELARUS', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('BE', 'BELGIUM', 'x', 'Belgian')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('BZ', 'BELIZE', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('BJ', 'BENIN', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('BM', 'BERMUDA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('BT', 'BHUTAN', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('BO', 'BOLIVIA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('BA', 'BOSNIA AND HERZEGOVINA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('BW', 'BOTSWANA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('BV', 'BOUVET ISLAND', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('BR', 'BRAZIL', 'x', 'Brazilian')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('IO', 'BRITISH INDIAN OCEAN TERRITORY', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('BN', 'BRUNEI DARUSSALAM', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('BG', 'BULGARIA', 'x', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('BF', 'BURKINA FASO', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('BI', 'BURUNDI', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('KH', 'CAMBODIA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('CM', 'CAMEROON', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('CA', 'CANADA', 'x', 'Canadian')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('CV', 'CAPE VERDE', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('KY', 'CAYMAN ISLANDS', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('CF', 'CENTRAL AFRICAN REPUBLIC', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('TD', 'CHAD', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('CL', 'CHILE', 'x', 'Chilean')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('CN', 'CHINA', 'x', 'Chinese')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('CX', 'CHRISTMAS ISLAND', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('CC', 'COCOS (KEELING) ISLANDS', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('CO', 'COLOMBIA', 'x', 'Colombian')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('KM', 'COMOROS', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('CG', 'CONGO', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('CK', 'COOK ISLANDS', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('CR', 'COSTA RICA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('CI', 'COTE D IVOIRE', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('HR', 'CROATIA', 'x', 'Croatian')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('CU', 'CUBA', 'x', 'Cuban')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('CY', 'CYPRUS', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('CZ', 'CZECH REPUBLIC', 'x', 'Czech')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('DK', 'DENMARK', 'x', 'Danish')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('DJ', 'DJIBOUTI', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('DM', 'DOMINICA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('DO', 'DOMINICAN REPUBLIC', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('EC', 'ECUADOR', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('EG', 'EGYPT', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('SV', 'EL SALVADOR', 'x', 'Salvadorean')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('GQ', 'EQUATORIAL GUINEA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('ER', 'ERITREA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('EE', 'ESTONIA', 'x', 'Estonian')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('ET', 'ETHIOPIA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('FK', 'FALKLAND ISLANDS (MALVINAS)', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('FO', 'FAROE ISLANDS', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('FJ', 'FIJI', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('FI', 'FINLAND', 'x', 'Finnish')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('FR', 'FRANCE', 'x', 'French')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('GF', 'FRENCH GUIANA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('PF', 'FRENCH POLYNESIA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('TF', 'FRENCH SOUTHERN TERRITORIES', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('GA', 'GABON', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('GM', 'GAMBIA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('GE', 'GEORGIA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('DE', 'GERMANY', 'x', 'German')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('GH', 'GHANA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('GI', 'GIBRALTAR', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('GR', 'GREECE', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('GL', 'GREENLAND', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('GD', 'GRENADA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('GP', 'GUADELOUPE', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('GU', 'GUAM', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('GT', 'GUATEMALA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('GG', 'GUERNSEY', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('GN', 'GUINEA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('GW', 'GUINEA-BISSAU', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('GY', 'GUYANA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('HT', 'HAITI', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('HM', 'HEARD ISLAND AND MCDONALD ISLANDS', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('VA', 'HOLY SEE (VATICAN CITY STATE)', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('HN', 'HONDURAS', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('HK', 'HONG KONG', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('HU', 'HUNGARY', 'x', 'Hungarian')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('IS', 'ICELAND', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('IN', 'INDIA', 'x', 'Indian')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('ID', 'INDONESIA', 'x', 'Indonesian')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('IR', 'IRAN', 'x', 'Persian')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('IQ', 'IRAQ', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('IE', 'IRELAND', 'x', 'Irish')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('IM', 'ISLE OF MAN', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('IL', 'ISRAEL', 'x', 'Israeli')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('IT', 'ITALY', 'x', 'Italian')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('JM', 'JAMAICA', 'x', 'Jamaican')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('JP', 'JAPAN', 'x', 'Japanese')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('JE', 'JERSEY', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('JO', 'JORDAN', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('KZ', 'KAZAKHSTAN', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('KE', 'KENYA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('KI', 'KIRIBATI', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('KR', 'KOREA', 'x', 'Korean')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('KW', 'KUWAIT', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('KG', 'KYRGYZSTAN', 'x', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('LA', 'LAO PEOPLES DEMOCRATIC REPUBLIC', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('LV', 'LATVIA', 'x', 'Latvian')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('LB', 'LEBANON', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('LS', 'LESOTHO', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('LR', 'LIBERIA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('LY', 'LIBYAN ARAB JAMAHIRIYA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('LI', 'LIECHTENSTEIN', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('LT', 'LITHUANIA', 'x', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('LU', 'LUXEMBOURG', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('MO', 'MACAO', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('MK', 'MACEDONIA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('MY', 'MALAYSIA', 'x', 'Malaysian')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('MV', 'MALDIVES', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('ML', 'MALI', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('MT', 'MALTA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('MH', 'MARSHALL ISLANDS', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('MQ', 'MARTINIQUE', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('MR', 'MAURITANIA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('MU', 'MAURITIUS', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('YT', 'MAYOTTE', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('MX', 'MEXICO', 'x', 'Mexican')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('FM', 'MICRONESIA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('MD', 'MOLDOVA', 'x', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('MC', 'MONACO', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('MN', 'MONGOLIA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('MS', 'MONTSERRAT', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('MA', 'MOROCCO', 'x', 'Moroccan')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('MZ', 'MOZAMBIQUE', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('MM', 'MYANMAR', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('NA', 'NAMIBIA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('NR', 'NAURU', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('NP', 'NEPAL', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('NL', 'NETHERLANDS', 'x', 'Dutch')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('AN', 'NETHERLANDS ANTILLES', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('NC', 'NEW CALEDONIA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('NZ', 'NEW ZEALAND', 'x', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('NI', 'NICARAGUA', 'x', 'Nicaraguan')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('NE', 'NIGER', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('NG', 'NIGERIA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('NU', 'NIUE', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('NF', 'NORFOLK ISLAND', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('MP', 'NORTHERN MARIANA ISLANDS', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('NO', 'NORWAY', 'x', 'Norwegian')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('OM', 'OMAN', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('PK', 'PAKISTAN', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('PW', 'PALAU', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('PS', 'PALESTINIAN TERRITORY', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('PA', 'PANAMA', 'x', 'Panamanian')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('PG', 'PAPUA NEW GUINEA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('PY', 'PARAGUAY', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('PE', 'PERU', 'x', 'Peruvian')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('PH', 'PHILIPPINES', 'x', 'Filipino')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('PN', 'PITCAIRN', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('PL', 'POLAND', 'x', 'Polish')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('PT', 'PORTUGAL', 'x', 'Portugese')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('PR', 'PUERTO RICO', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('QA', 'QATAR', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('RE', 'REUNION', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('RO', 'ROMANIA', 'x', 'Romanian')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('RU', 'RUSSIAN FEDERATION', 'x', 'Russian')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('RW', 'RWANDA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('SH', 'SAINT HELENA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('KN', 'SAINT KITTS AND NEVIS', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('LC', 'SAINT LUCIA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('PM', 'SAINT PIERRE AND MIQUELON', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('VC', 'SAINT VINCENT AND THE GRENADINES', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('WS', 'SAMOA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('SM', 'SAN MARINO', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('ST', 'SAO TOME AND PRINCIPE', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('SA', 'SAUDI ARABIA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('SN', 'SENEGAL', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('CS', 'SERBIA AND MONTENEGRO', 'x', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('SC', 'SEYCHELLES', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('SL', 'SIERRA LEONE', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('SG', 'SINGAPORE', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('SK', 'SLOVAKIA', 'x', 'Slovak')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('SI', 'SLOVENIA', 'x', 'Slovenian')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('SB', 'SOLOMON ISLANDS', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('SO', 'SOMALIA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('ZA', 'SOUTH AFRICA', 'x', 'South African')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('GS', 'SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('ES', 'SPAIN', 'x', 'Spanish')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('LK', 'SRI LANKA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('SD', 'SUDAN', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('SR', 'SURINAME', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('SJ', 'SVALBARD AND JAN MAYEN', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('SZ', 'SWAZILAND', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('SE', 'SWEDEN', 'x', 'Swedish')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('CH', 'SWITZERLAND', 'x', 'Swiss')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('SY', 'SYRIAN ARAB REPUBLIC', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('TW', 'TAIWAN', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('TJ', 'TAJIKISTAN', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('TZ', 'TANZANIA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('TH', 'THAILAND', 'x', 'Thai')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('TL', 'TIMOR-LESTE', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('TG', 'TOGO', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('TK', 'TOKELAU', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('TO', 'TONGA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('TT', 'TRINIDAD AND TOBAGO', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('TN', 'TUNISIA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('TR', 'TURKEY', 'x', 'Turkish')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('TM', 'TURKMENISTAN', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('TC', 'TURKS AND CAICOS ISLANDS', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('TV', 'TUVALU', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('UG', 'UGANDA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('UA', 'UKRAINE', 'x', 'Ukranian')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('AE', 'UNITED ARAB EMIRATES', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('GB', 'UNITED KINGDOM', 'x', 'English')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('US', 'UNITED STATES', 'x', 'American')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('UM', 'UNITED STATES MINOR OUTLYING ISLANDS', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('UY', 'URUGUAY', 'x', 'Uruguayan')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('UZ', 'UZBEKISTAN', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('VU', 'VANUATU', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('VE', 'VENEZUELA', 'x', 'Venezuelan')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('VN', 'VIET NAM', 'x', 'Vietnamese')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('VI', 'VIRGIN ISLANDS', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('VG', 'VIRGIN ISLANDS', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('WF', 'WALLIS AND FUTUNA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('EH', 'WESTERN SAHARA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('YE', 'YEMEN', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('ZM', 'ZAMBIA', '', '')")
        cur.execute("INSERT INTO pordb_iso_land (iso, land, aktiv, national) VALUES ('ZW', 'ZIMBABWE', '', '')")
        cur.execute("INSERT INTO pordb_suchbegriffe (suchbegriff, alternative) VALUES ('&', 'and')")
        cur.execute("INSERT INTO pordb_suchbegriffe (suchbegriff, alternative) VALUES ('-', '')")
        cur.execute("INSERT INTO pordb_suchbegriffe (suchbegriff, alternative) VALUES ('17', 'seventeen')")
        cur.execute("INSERT INTO pordb_suchbegriffe (suchbegriff, alternative) VALUES ('18', 'eighteen')")
        cur.execute("INSERT INTO pordb_suchbegriffe (suchbegriff, alternative) VALUES ('8', 'eight')")
        cur.execute("INSERT INTO pordb_suchbegriffe (suchbegriff, alternative) VALUES ('Bombshell', 'Bomb shell')")
        cur.execute("INSERT INTO pordb_suchbegriffe (suchbegriff, alternative) VALUES ('buttfuck', 'butt fuck')")
        cur.execute("INSERT INTO pordb_suchbegriffe (suchbegriff, alternative) VALUES ('five', '5')")
        cur.execute("INSERT INTO pordb_suchbegriffe (suchbegriff, alternative) VALUES ('for', '4')")
        cur.execute("INSERT INTO pordb_suchbegriffe (suchbegriff, alternative) VALUES ('gang bang', 'gangbang')")
        cur.execute("INSERT INTO pordb_suchbegriffe (suchbegriff, alternative) VALUES ('schoolgirl', 'school girl')")
        cur.execute("INSERT INTO pordb_suchbegriffe (suchbegriff, alternative) VALUES ('two', '2')")
        
        try:
            conn.commit()
            self.listWidgetDB.addItem(self.tr("Database created"))
            self.listWidgetDB.addItem(self.tr("Database tables created"))
        except Exception as e:
            message = QtGui.QMessageBox.critical(self, self.tr("Error "), self.tr("Errors occured"))
            sys.exit()
        cur.close()
        conn.close()
        app.restoreOverrideCursor()
        
app = QtGui.QApplication(sys.argv)
locale = QtCore.QLocale.system().name()
locale = 'en_EN'
appTranslator = QtCore.QTranslator()
if appTranslator.load("pordb_setup_" + locale, os.getcwd()):
    app.installTranslator(appTranslator)
dialog = Dialog()
dialog.show()
sys.exit(app.exec_())
