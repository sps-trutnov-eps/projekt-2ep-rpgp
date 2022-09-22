import sys
import pygame as pg

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'

class screen():
    def __init__(self, name, background, buttons):
        self.name = name
        self.background = background
        self.buttons = buttons

class button():
    def __init__(self, position, link):
        self.position = position
        self.link = link
        
main_menu = screen("Main menu", pg.image.load(DATA_ROOT + "/data/textures/screens/main_menu.png"), [])
