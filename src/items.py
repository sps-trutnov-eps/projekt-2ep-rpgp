import pygame as pg
import sys
from Screens import *

pg.font.init()
resolution = 1200, 900

class item():
    def __init__(self, name, description, texture, position, belonging):
        self.name = name
        self.description = description
        self.texture = texture
        self.position = position
        self.screen = screen
        self.name_size = 100
        self.desc_size = 50
        self.belonging = belonging
        
    def draw(self, font, screen, on_screen):
        if self.belonging == on_screen.active_screen.name:
            texture_scaled = pg.transform.scale(self.texture, (192, 192))
            
            self.name_font = pg.font.Font(font, self.name_size)
            self.desc_font = pg.font.Font(font, self.desc_size)
            
            name_text = self.name_font.render(self.name, True, (0,0,0))
            name_text_rect = name_text.get_rect()
            name_text_rect.midtop = self.position[0] + 96, self.position[1] + 192
            
            text_list = []
            pos_list = []
            i = 0
            
            for line in self.description.split('\n'):
                text_line = self.desc_font.render(line, True, (75,75,75))
                text_list.append(text_line)
                pos = text_line.get_rect(midtop=(self.position[0] + 96, self.position[1] + 192 + self.name_size + (self.desc_size * i)))
                pos_list.append(pos)
                i = i + 1
            
            for j in range(i):
                screen.blit(text_list[j], pos_list[j])
            
            screen.blit(texture_scaled, self.position)
            screen.blit(name_text, name_text_rect)
        
item = item("Stick", "Nothing but a very\ngeneric stick.", pg.image.load(DATA_ROOT + "/data/textures/weapons/stick.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board")
        