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
bt_acc = True

pg.init()

screen = pg.display.set_mode(resolution)
pg.display.set_caption("Generic Game")

active_screen = main_menu

while True:
    pressed = pg.key.get_pressed()
    m_pressed = pg.mouse.get_pressed()
    events = pg.event.get()
    screen.blit(active_screen.background,(0,0))
    for event in events:
        if event.type == pg.QUIT:
            running = False
            pg.quit()
            sys.exit()
    
    # Práce Button_tool -> třeba aktivovat
    bt.find(m_pressed)
    bt.calculate()
    
    # Vypisování výsledků Button_tool
    bt.list(pressed, screen)
    
    # Aktivace/Deaktivace Button_tool
    if pressed[pg.K_s] and bt_acc:
        bt.on_off()
        bt_acc = False
    elif pressed[pg.K_s] and not bt_acc:
        pass
    else:
        bt_acc = True
    
    pg.display.update()