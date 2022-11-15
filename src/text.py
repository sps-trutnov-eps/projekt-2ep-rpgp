import sys
import pygame as pg
from data import *

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'
    
pg.font.init()
    
class text_cl():
    def __init__(self):
        self.texts = []
        self.messages = []
        
    def texts_bundling(self):
        self.all = self.texts + self.messages
        
text_class = text_cl()
    
class text():
    def __init__(self, belonging, text, position, font, colour):
        text_class.texts.append(self)
        self.belonging = belonging
        self.text = text
        self.position = position
        self.font = font
        self.colour = colour
        self.size = self.font.size(self.text)
        
    def blit_self(self, screen, on__screen):
        if not on__screen.active_screen == "Exit":
            if not on__screen.active_table == "Close":
                if on__screen.active_table.name in self.belonging:
                    surf = self.font.render(self.text, True, self.colour)
                    width, height = self.font.size(self.text)[0], self.font.size(self.text)[1]
                    screen.blit(surf, ((self.position[0] - (width / 2)), (self.position[1] - (height / 2))))
            elif on__screen.active_screen.name in self.belonging:
                surf = self.font.render(self.text, True, self.colour)
                width, height = self.font.size(self.text)[0], self.font.size(self.text)[1]
                screen.blit(surf, ((self.position[0] - (width / 2)), (self.position[1] - (height / 2))))
            
        
    def update(self, new_text, new_pos):
        self.text = new_text
        if not new_pos == None:
            self.position = new_pos
            
class message():
    def __init__(self, belonging, text, pos):
        self.belonging = belonging
        self.text = text
        self.position = pos
        self.font = font
        self.colour = colour
        
heading0_size  = 80
heading1_size = 66
settings_size = 45
regular_size = 30

def_link = DATA_ROOT + "/data/fonts/VeniceClassic.ttf"
def_colour = (200,200,200)
dark_colour = (30,30,30)

coin_level_font = pg.font.Font(def_link, 54)

# Texty v tabulce nové hry
tn1 = text(["New game table"], "Choose your role:", (600,200), pg.font.Font(def_link, heading0_size), def_colour) 

# Texty v tabulce nastavení
ts1 = text(["Settings table"], "Settings", (600,200), pg.font.Font(def_link, heading1_size), def_colour)
texts_settings = [ts1]

# Texty v tabulce credits
tc1 = text(["Credits table"], "Credits", (600, 200), pg.font.Font(def_link, heading1_size), def_colour)
texts_credits = [tc1]

# Texty v obchodě
tsh_buy = text(["Weapon board", "Armor board", "Item board"], "Buy", (162, 810), pg.font.Font(def_link, heading1_size), dark_colour)
tsh_equip = text(["Weapon board", "Armor board", "Item board"], "Equip", (437, 810), pg.font.Font(def_link, heading1_size), dark_colour)
texts_shop = [tsh_buy, tsh_equip]

# Texty v nastavení ve hře
caption = text(["Game table"], "Settings", (600,200), pg.font.Font(def_link, heading1_size), def_colour)
save = text(["Game table"], "Save", (600,500), pg.font.Font(def_link, settings_size), def_colour)
texts_gsettings = [caption, save]

# Texty v bitvě
texts_battle = []

# Peníze a level
golds = text(["Game menu", "Shop", "Campaign", "Profile", "Weapon board", "Armor board", "Item board"], str(player.gold), (1110 - (coin_level_font.size(str(player.gold))[0] / 2),30 + (coin_level_font.size(str(player.gold))[1] / 2)), coin_level_font, dark_colour)
level = text(["Game menu", "Shop", "Campaign", "Profile", "Weapon board", "Armor board", "Item board"], str(player.level), (1110 - (coin_level_font.size(str(player.level))[0] / 2),85 + (coin_level_font.size(str(player.gold))[1] / 2)), coin_level_font, dark_colour)
texts_g_l = [golds, level]

text_class.texts_bundling()
