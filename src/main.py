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

new_button_coordinates = None
final_coords = 0, 0, 0, 0

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
            tuple1 = new_button_coordinates[0]
            tuple2 = new_button_coordinates[1]
            coord1 = int(tuple1[0])
            coord2 = int(tuple1[1])
            coord3 = int(tuple2[0])
            coord4 = int(tuple2[1])
            final_coords = coord1, coord2, coord3, coord4
            print(new_button_coordinates)
            print(final_coords)
            
    pg.draw.rect(screen, (0,255,0), final_coords)
    
    
    pg.display.update()