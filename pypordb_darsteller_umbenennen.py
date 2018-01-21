# -*- coding: utf-8 -*-

'''
    Copyright 2012-2018 HWM
    
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
from pordb_darsteller_umbenennen import Ui_Dialog as pordb_darsteller_umbenennen

class DarstellerUmbenennen(QtWidgets.QDialog, pordb_darsteller_umbenennen):
    def __init__(self, alter_name, parent=None):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        
        self.pushButtonUmbenennen.clicked.connect(self.accept)
        self.pushButtonCancel.clicked.connect(self.close)
        
        self.lineEditNeuerName.setText(alter_name.strip("=").replace("''", "'"))
