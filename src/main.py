# --- Projekt Role-playing parodie Vojtěcha Nepimacha a Pavla Kotka ---
import sys
import pygame as pg
from Screens import *
from dev_tools import *

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'

resolution = 1200, 900

pg.init()

clock = pg.time.Clock()
screen = pg.display.set_mode(resolution)
pg.display.set_caption("Generic Game")

active_screen = main_menu
active_table = "Close"

dev_shortcut = None
devmode = False

bt_acc = True
pt_acc = True

while True:
    # Získání infa o akcích
    events = pg.event.get()
    pressed = pg.key.get_pressed()
    m_pressed = pg.mouse.get_pressed()
    
    # Možnosti vypnutí
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    
    if active_screen == "Exit":
        pg.quit()
        sys.exit()
    
    # Vykreslení obrazovky/tabulky
    screen.blit(active_screen.background,(0,0))
    if not active_table == "Close":
        table = pg.Surface(active_table.size)
        table.set_alpha(active_table.alpha)
        screen.blit(table, (active_table.position))
    
    ### Kontrola stisku tlačítek ###
    
    if active_table == "Close" and not active_screen == "Exit":
        for button in active_screen.t_buttons:
            if button.draw:
                pg.draw.rect(screen, button.colour, (button.position, (button.width, button.height)), 3)
            result = button.check(m_pressed)
            if not result == None:
                active_table = result
        for button in active_screen.l_buttons:
            if button.draw:
                pg.draw.rect(screen, button.colour, (button.position, (button.width, button.height)), 3)
            result = button.check(m_pressed)
            if not result == None:
                active_screen = result
                
    elif not active_table == "Close" and not active_screen == "Exit":
        for button in active_table.l_buttons:
            if button.draw:
                pg.draw.rect(screen, button.colour, (button.position, (button.width, button.height)), 3)
            result = button.check(m_pressed)
            if not result == None:
                active_screen = result
                active_table = "Close"
        if not active_table == "Close":
            for button in active_table.t_buttons:
                if button.draw:
                    pg.draw.rect(screen, button.colour, (button.position, (button.width, button.height)), 3)
                result = button.check(m_pressed)
                if not result == None:
                    active_table = result
    
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
        pt.get_texture(DATA_ROOT + "/data/textures/weapons/warrior/swords/4.png")
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
    clock.tick(144)