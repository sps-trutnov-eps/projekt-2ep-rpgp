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
        
    def draw(self, active_screen):
        text = self.font.render(self.text, True, self.colour)
        text_rect = text.get_rect()
        text_rect.topleft = self.position
        active_screen.blit(text, text_rect)
        
# Texty v tabulce nastavení
settings_size = 26
ts1 = text("Something", (150,150), pg.font.Font(DATA_ROOT + "/data/fonts/VeniceClassic.ttf", settings_size), (200,120,100))
texts_settings = [ts1]
