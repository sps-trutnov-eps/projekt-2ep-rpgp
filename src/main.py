# --- Projekt Role-playing parodie Vojtěcha Nepimacha a Pavla Kotka ---
import sys
import pygame as pg
from screens import *
from button_tool import *

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
    pressed = pg.key.get_pressed()
    screen.blit(active_screen.background,(0,0))
    for event in events:
        if event.type == pg.QUIT:
            running = False
            pg.quit()
            sys.exit()
    
    # Práce Button_tool
    if pg.mouse.get_pressed()[0]:
        bt.find_l()
    if pg.mouse.get_pressed()[2]:
        bt.find_r()
        
    corner1, corner2, width, height = bt.calculate()
    
    # Vypisování výsledků Button_tool
    if pg.key.get_pressed()[pg.K_SPACE]:
        print("Šířka: ", width)
        print("Výška: ", height)
        print("1. Roh: ", corner1[0], ", ", corner1[1])
        print("2. Roh: ", corner2[0], ", ", corner2[1])
    if not width == 0 and not height == 0:
        pg.draw.rect(screen, (0,255,0), (corner1[0], corner1[1], width, height), 2)
    
    pg.display.update()