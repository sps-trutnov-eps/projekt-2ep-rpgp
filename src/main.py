# --- Projekt Role-playing parodie Vojtěcha Nepimacha a Pavla Kotka ---
import sys
import pygame as pg
from Screens import *
from button_generator import *

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'

resolution = 1200, 900

pg.init()

screen = pg.display.set_mode(resolution)
pg.display.set_caption("Generic Game")

active_screen = main_menu

while True:
    events = pg.event.get()
    pressed = pg.key.get_pressed()
    screen.blit(active_screen.background,(0,0))
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    
        if pressed[pg.K_p]:
            new_button_coordinates = area_select(screen)
            print(new_button_coordinates)
    
    pg.display.update()