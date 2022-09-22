import sys
import pygame as pg

def area_select(surface):
    area_selection = True
    point_1 = None
    point_2 = None
    
    #while area_selection == True:
    while point_1 == None or point_2 == None:
        if point_1 == None and pg.mouse.get_pressed()[0]:
            point_1 = round(pg.mouse.get_pos()[0]), round(pg.mouse.get_pos()[1]) 
            
        if point_2 == None and pg.mouse.get_pressed()[2]:
            point_2 = round(pg.mouse.get_pos()[0]), round(pg.mouse.get_pos()[1]) 
        
        events = pg.event.get()
        pressed = pg.key.get_pressed()
        
        #for event in events:
        #    if pressed[pg.K_o]:
        #        area_selection = False
        
        #if not point_1 == None:
         #   if not point_2 == None:
          #      pg.draw.rect(surface, (0,255,0), point_1, point_2)
        
    return point_1, point_2