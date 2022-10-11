import sys
import pygame as pg

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'
    
pg.font.init()
    
class text():
    def __init__(self, text, position, font, colour):
        self.text = text
        self.position = position
        self.font = font
        self.colour = colour
        self.size = self.font.size(self.text)
        
    def blit_self(self, active_screen):
        text = self.font.render(self.text, True, self.colour)
        text_rect = text.get_rect()
        text_rect.topleft = self.position
        active_screen.blit(text, text_rect)
        
heading0_size  = 80
heading1_size = 66
regular_size = 30

def_link = DATA_ROOT + "/data/fonts/VeniceClassic.ttf"
def_colour = (200,200,200)

# Texty v tabulce nové hry
tn1 = text("Choose your role:", (342,330), pg.font.Font(def_link, heading0_size), def_colour) 
texts_new_game = [tn1]

# Texty v tabulce nastavení
ts1 = text("Settings", (499,130), pg.font.Font(def_link, heading1_size), def_colour)
texts_settings = [ts1]

# Texty v tabulce credits
tc1 = text("Credits", (512, 130), pg.font.Font(def_link, heading1_size), def_colour)
texts_credits = [tc1]
