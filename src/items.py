import pygame as pg
import sys
from Screens import *

pg.font.init()

class item():
    def __init__(self, name, description, texture, position, screen):
        self.name = name
        self.description = description
        self.texture = texture
        self.position = position
        self.screen = screen
        self.name_size = 100
        self.desc_size = 50
        
    def draw(self, font):
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
            self.screen.blit(text_list[j], pos_list[j])
        
        self.screen.blit(texture_scaled, self.position)
        self.screen.blit(name_text, name_text_rect)
        