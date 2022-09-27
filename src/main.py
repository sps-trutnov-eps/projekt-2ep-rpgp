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

screen = pg.display.set_mode(resolution)
pg.display.set_caption("Generic Game")

active_screen = main_menu

dev_shortcut = None
devmode = False

bt_acc = True
pt_acc = True

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
        ### TEXTURE PREVIEW TOOL ###
        # Zde se do podprogramu zadá cesta textury, kterou chceme vidět ve hře
        pt.get_texture(DATA_ROOT + "/data/textures/weapons/warrior/swords/3.png")
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
    
    #item_texture = pg.image.load(DATA_ROOT + "/data/textures/weapons/stick.png").convert_alpha()
    #item_surface = pg.transform.scale(item_texture, (64, 64))
    #item_surface_large = pg.transform.scale(item_texture, (128, 128))
    #item_rect = item_surface.get_rect(center = (resolution[0]/2 + 100, resolution[1]/2))
    #item_rect_large = item_surface_large.get_rect(center = (resolution[0]/2 - 100, resolution[1]/2))
    #screen.blit(item_surface, item_rect)
    #screen.blit(item_surface_large, item_rect_large)
    
    pg.display.update()