# -*- coding: utf-8 -*-

class ActorData():
    def __init__(self, seite):
        self.seite = seite
        
    def actor_name(self):
        # Darsteller Name
        anfang = self.seite.find("personal biography")
        if anfang < 0:
            return False
        anfang = self.seite.find('<h1>', anfang)
        ende = self.seite.find('</h1>', anfang)
        return self.seite[anfang+4:ende].strip()
    
    def actor_image(self):
        anfang = self.seite.find('headshots/')
        if anfang < 0:
            return False
        ende = self.seite.find('"></div>', anfang)
        return self.seite[anfang+10:ende].replace(" ", "%20")
    
    def actor_sex(self):
        anfang = self.seite.find('&amp;gender=')
        ende = self.seite.find('"', anfang)
        geschlecht = self.seite[anfang+12:ende]
        if geschlecht == "f":
            geschlecht = "w"
        elif geschlecht != "m":
            return False
        return geschlecht
    
    def actor_alias(self):
        anfang = self.seite.find('AKA</b>')
        anfang = self.seite.find('</td><td>', anfang)
        ende = self.seite.find('</td>', anfang+1)
        pseudonyme = self.seite[anfang+9:ende]
        if pseudonyme == "No known aliases":
            return ""
        else:
            return pseudonyme
    
    def actor_country(self):
        anfang = self.seite.find('Nationality/Heritage</b></td><td>')
        ende = self.seite.find('</td></tr>', anfang)
        return self.seite[anfang+33:ende]
    
    def actor_birthplace(self):
        anfang = self.seite.find('Birthplace</b></td><td>')
        if anfang < 0:
            return False
        ende = self.seite.find('</td></tr>', anfang)
        return self.seite[anfang+23:ende].strip("&nbsp;")
    
    def actor_ethnic(self):
        anfang = self.seite.find('Ethnicity</b></td><td>')
        ende = self.seite.find('</td></tr>', anfang)
        return self.seite[anfang+22:ende]
    
    def actor_hair(self):
        anfang = self.seite.find('Hair Colors</b></td><td>')
        offset = 24
        if anfang < 0:
            anfang = self.seite.find('Hair Color</b></td><td>')
            offset = 23
        ende = self.seite.find('</td></tr>', anfang)
        return self.seite[anfang+offset:ende]
    
    def actor_tattoos(self):
        anfang = self.seite.find('Tattoos</b></td><td>')
        ende = self.seite.find('</td>', anfang+20)
        if ende - anfang > 500:
            ende = anfang + 500
        return self.seite[anfang+20:ende]
    
    def actor_born(self):
        anfang = self.seite.find('<b>Birthday')
        anfang = self.seite.find('">', anfang)
        ende = self.seite.find('</a>', anfang)
        return self.seite[anfang+2:ende]
    
    def actor_movies(self):
        anfang = self.seite.find('moviecount">')
        if anfang > 0:
            ende = self.seite.find(' Title', anfang+1)
            return self.seite[anfang+12:ende]
        else:
            return 0
        
    def actor_activ(self):
        anfang = self.seite.find('Years Active</b></td><td>')
        if anfang == -1:
            anfang = self.seite.find('Years Active as Performer</b></td><td>') 
            if anfang == -1:
                anfang = self.seite.find('Year Active</b></td><td>') + 24
            else:
                anfang += 38
        else:
            anfang += 25
        aktiv_von = self.seite[anfang:anfang + 4]
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
