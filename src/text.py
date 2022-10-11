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
        
heading_size = 66
regular_size = 30

# Texty v tabulce nastavení
ts1 = text("Settings", (499,130), pg.font.Font(DATA_ROOT + "/data/fonts/VeniceClassic.ttf", heading_size), (200,200,200))
texts_settings = [ts1]

# Texty v tabulce credits
tc1 = text("Credits", (512, 130), pg.font.Font(DATA_ROOT + "/data/fonts/VeniceClassic.ttf", heading_size), (200,200,200))
texts_credits = [tc1]
