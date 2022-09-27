import pygame as pg
import sys

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'

### Nástroj pro náhled textur previewů ###

class texture_preview_tool():
    def __init__(self):
        self.activity = False
        
    def get_texture(self, texture):
        self.texture = texture
        
    def render_preview(self, screen, resolution):
        self.preview_texture = pg.image.load(self.texture).convert_alpha()
        self.preview_surface = pg.transform.scale(self.preview_texture, (64, 64))
        self.preview_surface_large = pg.transform.scale(self.preview_texture, (128, 128))
        self.preview_rect = self.preview_surface.get_rect(center = (resolution[0]/2 + 100, resolution[1]/2))
        self.preview_rect_large = self.preview_surface_large.get_rect(center = (resolution[0]/2 - 100, resolution[1]/2))
        if self.activity:
            rect_w = 400
            rect_h = 200
            pg.draw.rect(screen,(0,0,0),(resolution[0]/2 - rect_w/2, resolution[1]/2 - rect_h/2, rect_w, rect_h))
            pg.draw.rect(screen,(255,255,255),(resolution[0]/2 - rect_w/2, resolution[1]/2 - rect_h/2, rect_w, rect_h),10)
            screen.blit(self.preview_surface, self.preview_rect)
            screen.blit(self.preview_surface_large, self.preview_rect_large)

    def on_off(self):
        self.activity = not self.activity
        
    def texture_queue(self):
        pass
    
### Nástroj pro získání místa a rozměrů tlačítek ###

# LMB = určení prvního rohu
# RMB = určení druhého rohu
# SPACE = výpis hodnot

class button_tool():
    def __init__(self):
        self.activity = False
        self.corner1 = [0,0]
        self.corner2 = [0,0]
        self.width = 0
        self.height = 0
        self.list_acc = True
        
    def on_off(self):
        self.activity = not self.activity
        if self.activity:
            print("Button tool byl zapnut")
        else:
            print("Button tool byl vypnut")
        
    def find(self, m_pressed):
        if self.activity:
            if m_pressed[0]:
                self.corner1 = [round(pg.mouse.get_pos()[0]), round(pg.mouse.get_pos()[1])]
            if m_pressed[2]:
                self.corner2 = [round(pg.mouse.get_pos()[0]), round(pg.mouse.get_pos()[1])]
        else:
            pass
            
    def calculate(self):
        if self.activity:
            if not self.corner1 == [] and not self.corner2 == []:
                self.width = (abs(self.corner1[0] - self.corner2[0]))
                self.height = (abs(self.corner1[1] - self.corner2[1]))
        else:
            pass

    def list(self, pressed, screen):
        if self.activity:
            if pressed[pg.K_SPACE] and self.list_acc:
                print("Šířka: ", self.width)
                print("Výška: ", self.height)
                print("1. Roh: ", self.corner1[0], ", ", self.corner1[1])
                print("2. Roh: ", self.corner2[0], ", ", self.corner2[1])
                self.list_acc = False
            elif pressed[pg.K_SPACE] and not self.list_acc:
                pass
            else:
                self.list_acc = True
                
            if not self.width == 0 and not self.height == 0:
                pg.draw.rect(screen, (0,255,0), (self.corner1[0], self.corner1[1], self.width, self.height), 3)
        else:
            pass

bt = button_tool()
pt = texture_preview_tool()
