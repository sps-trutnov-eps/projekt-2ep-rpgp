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

dev_shortcut = None
devmode = False

bt_acc = True

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
    
    ### Kontrola stisku tlačítek ###
    for button in link_buttons:
        result = button.check(m_pressed)
        if not result == None:
            active_screen = result
    
    ### DEVELOPER MODE ###
    if pressed[pg.K_d]:
        dev_shortcut = 1
    
    if pressed[pg.K_e] and dev_shortcut == 1:
        dev_shortcut = 2
    
    if pressed[pg.K_v] and dev_shortcut == 2:
        if devmode == False:
            devmode = True
            dev_shortcut = None
        else:
            devmode = False
            dev_shortcut = None

    ### DEVELOPER MODE ###
    if devmode:
        ### BUTTON TOOL ###
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