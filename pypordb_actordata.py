# -*- coding: utf-8 -*-

'''
    Copyright 2012-2024 HWM
    
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
    along with Foobar.  If not, see <http://www.gnu.org/licenses >.
'''

class ActorData():
    def __init__(self, seite):
        self.seite = seite
        
    def actor_name(self):
        # Darsteller Name
        anfang = self.seite.find("Vital Stats")
        if anfang < 0:
            return False
        anfang = self.seite.find('<h1>')
        ende = self.seite.find('</h1>')
        return self.seite[anfang+4:ende].strip()
    
    def actor_image(self):
        anfang = self.seite.find('id="headshot"')
        if anfang < 0:
            return False
        anfang = self.seite.find('src="', anfang)
        ende = self.seite.find('"></div>', anfang)
        return self.seite[anfang+5:ende].replace(" ", "%20")
    
    def actor_sex(self):
        anfang = self.seite.find('name="Gender" value="')
        ende = self.seite.find('">', anfang)
        geschlecht = self.seite[anfang+21:ende]
        if geschlecht == "f":
            geschlecht = "w"
        elif geschlecht != "m":
            return False
        return geschlecht
    
    def actor_alias(self):
        anfang = self.seite.find('AKA</p><div class="biodata">')
        ende = self.seite.find('</div>', anfang)
        pseudonyme = self.seite[anfang+28:ende].strip()
        if pseudonyme == "No known aliases":
            return ""
        else:
            return pseudonyme
    
    def actor_country(self):
        anfang = self.seite.find('Nationality</p><p class="biodata">')
        ende = self.seite.find('</p><p', anfang+15)
        return self.seite[anfang+34:ende]
    
    def actor_birthplace(self):
        anfang = self.seite.find('Birthplace</p><p class="biodata">')
        if anfang < 0:
            return False
        ende = self.seite.find(';</p><p', anfang)
        return self.seite[anfang+33:ende].strip("&nbsp;")
    
    def actor_ethnic(self):
        anfang = self.seite.find('Ethnicity</p><p class="biodata">')
        ende = self.seite.find('</p><p', anfang+15)
        return self.seite[anfang+32:ende]
    
    def actor_hair(self):
        anfang = self.seite.find('Hair Colors</p><p class="biodata">')
        offset = 34
        if anfang < 0:
            anfang = self.seite.find('Hair Color</p><p class="biodata">')
            offset = 33
        ende = self.seite.find('</p>', anfang+15)
        return self.seite[anfang+offset:ende]
    
    def actor_tattoos(self):
        anfang = self.seite.find('Tattoos</p><p class="biodata">')
        ende = self.seite.find('</p><p', anfang+30)
        if ende - anfang > 500:
            ende = anfang + 500
        return self.seite[anfang+30:ende]
    
    def actor_born(self):
        anfang = self.seite.find('Birthday</p><p class="biodata">')
        ende = self.seite.find('</a>', anfang+15)
        born = self.seite[anfang+31:ende]
        if born.startswith('<a href'):
            anfang = self.seite.find('">', anfang+31)
            return self.seite[anfang+2:ende]
        else:
            return self.seite[anfang+31:ende]
    
    def actor_movies(self):
        anfang = self.seite.find('Performer Credits (')
        if anfang > 0:
            ende = self.seite.find(')', anfang)
            return self.seite[anfang+19:ende]
        else:
            return 0
        
    def actor_activ(self):
        anfang = self.seite.find('Years Active</p><p class="biodata">')
        if anfang == -1:
            anfang = self.seite.find('Years Active as Performer') 
            if anfang == -1:
                anfang = self.seite.find('Year Active</p><p class="biodata">') + 34
            else:
                anfang = self.seite.find('"biodata">', anfang)
                if anfang > -1:
                    anfang += 10
        else:
            anfang += 35
        aktiv_von = self.seite[anfang:anfang+4]
        try:
            aktiv_von = int(aktiv_von)
        except:
            aktiv_von = 0
        aktiv_bis = self.seite[anfang + 5:anfang + 9]
        try:
            aktiv_bis = int(aktiv_bis)
        except:
            aktiv_bis = 0
        return (aktiv_von, aktiv_bis)
    
    def actor_list_of_movies(self):
        titel = []
        anfang = 0
        while True:
            anfang = self.seite.find('title.rme', anfang)
            if anfang > -1:
                anfang = self.seite.find('">', anfang)
                if anfang > -1:
                    ende = self.seite.find('</a></td><td>', anfang)
                    titel.append(self.seite[anfang+2:ende].strip())
            else:
                break
        return titel
        
