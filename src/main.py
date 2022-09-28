# --- Projekt Role-playing parodie Vojtěcha Nepimacha a Pavla Kotka ---
import sys
import pygame as pg
from screens import *
from dev_tools import *

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'

resolution = 1200, 900
table_colour = (30,30,30)
button_colour = (200,200,200)

pg.init()

screen = pg.display.set_mode(resolution)
pg.display.set_caption("Generic Game")

active_screen = main_menu
active_table = "Close"

dev_shortcut = None
devmode = False

bt_acc = True
pt_acc = True

while True:
    pressed = pg.key.get_pressed()
    m_pressed = pg.mouse.get_pressed()
    events = pg.event.get()
    screen.blit(active_screen.background,(0,0))
    if not active_table == "Close":
        pg.draw.rect(screen, table_colour, (active_table.position, (active_table.size[0], active_table.size[1])))
        
    for event in events:
        if event.type == pg.QUIT:
            running = False
            pg.quit()
            sys.exit()
    
    ### Kontrola stisku tlačítek ###
    
    if active_table == "Close":
        for button in active_screen.l_buttons:
            result = button.check(m_pressed)
            if not result == None:
                active_screen = result
                
    else:
        for button in active_table.t_buttons:
            pg.draw.rect(screen, button_colour, (button.position, (button.width, button.height)), 3)
            result = button.check(m_pressed)
            if not result == None:
                active_table = result
                
    if active_table == "Close":
        for button in active_screen.t_buttons:
            result = button.check(m_pressed)
            if not result == None:
                active_table = result
            
    else:    
        for button in active_table.l_buttons:
            pg.draw.rect(screen, button_colour, (button.position, (button.width, button.height)), 3)
            result = button.check(m_pressed)
            if not result == None:
                active_screen = result
                active_table = "Close"
    
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
        ### TEXTURE PREVIEW TOOL ###
        # Zde se do podprogramu zadá cesta textury, kterou chceme vidět ve hře
        pt.get_texture(DATA_ROOT + "/data/textures/weapons/warrior/swords/1.png")
        # Zde se textury zobrazují
        pt.render_preview(screen, resolution)
        
        # Aktivace a deaktivate Texture Preview Toolu
        if pressed[pg.K_r] and pt_acc:
            pt.on_off()
            pt_acc = False
            
        elif pressed[pg.K_r] and not pt_acc:
            pass
        else:
            pt_acc = True
        
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