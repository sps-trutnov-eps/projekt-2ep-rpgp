import sys
import pygame as pg

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

### Nástroj pro získání místa a rozměrů textu ###

# LMB = určení rohu
# ARROW UP = zvětšení textu
# ARROW DOWN = zmenšení textu
# LEFT CTRL = kurzor neurčuje střed, ale centr

class text_tool():
    def __init__(self, font):
        self.activity = False
        self.colour = (200,200,200)
        self.corner = [0,0]
        self.width = 0
        self.height = 0
        self.center = 0
        self.center_acc = False
        self.text = None
        self.size = 30
        self.font = font
        self.list_acc = True
        self.change_acc = True
        
    def on_off(self):
        self.activity = not self.activity
        if self.activity:
            print("Text tool byl zapnut")
        else:
            print("Text tool byl vypnut")
        
    def find(self, m_pressed):
        if self.activity:
            if m_pressed[0]:
                self.corner = [round(pg.mouse.get_pos()[0]), round(pg.mouse.get_pos()[1])]
        else:
            pass
    
    def show(self, text, pressed, screen):
        if self.activity:
            if self.size > 0:
                font = pg.font.Font(self.font, self.size)
                writing = font.render(text, False, self.colour)
                text_rect = (self.corner, font.size(text))
                if self.center_acc:
                    text_rect = ((self.corner[0] - (font.size(text)[0]/2), self.corner[1] - (font.size(text)[1])/2), font.size(text))
                screen.blit(writing, text_rect)
                if pressed[pg.K_SPACE] and self.list_acc:
                    print("Šířka: ", font.size(text)[0])
                    print("Výška: ", font.size(text)[1])
                    print("Střed: ", (self.corner[0] + (font.size(text)[0]/2), self.corner[1] + (font.size(text)[1])/2))
                    print("Veliksot: ", self.size)
                    print("Roh: ", self.corner[0], ", ", self.corner[1])
                    self.list_acc = False
                elif pressed[pg.K_SPACE] and not self.list_acc:
                    pass
                else:
                    self.list_acc = True
        else:
            pass
    
    def change(self, pressed):
        if self.activity:
            if pressed[pg.K_UP] and self.change_acc:
                self.size += 1
            elif pressed[pg.K_DOWN] and self.change_acc:
                self.size -= 1
            elif pressed[pg.K_LCTRL] and self.change_acc:
                self.center_acc = not self.center_acc
                self.change_acc = False
            elif (pressed[pg.K_UP] or pressed[pg.K_DOWN] or pressed[pg.K_LCTRL]) and not self.change_acc:
                pass
            else:
                self.change_acc = True
        else:
            pass
    
bt = button_tool()
tt = text_tool(DATA_ROOT + "/data/fonts/VeniceClassic.ttf")
pt = texture_preview_tool()
