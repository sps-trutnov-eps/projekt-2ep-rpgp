# --- Projekt Role-playing parodie Vojtěcha Nepimacha a Pavla Kotka ---
import sys
import pygame as pg

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'

resolution = 1200, 900

pg.init()

screen = pg.display.set_mode(resolution)
pg.display.set_caption("Generic Game")


while True:
    event = pg.event.get()
    screen.fill((50,200,50))
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    
    pg.display.update()