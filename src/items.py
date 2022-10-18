import pygame as pg
import sys
from data import *

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'

pg.init()
pg.font.init()
resolution = 1200, 900

if player.role == "warrior":
    weapon_name_1_type_1 = "Wooden Sword"
    weapon_name_2_type_1 = "Copper Sword"
    weapon_name_3_type_1 = "Iron Dagger"
    weapon_name_4_type_1 = "Fencing Sword"
    weapon_name_5_type_1 = "Yankov Avenger"
    
    weapon_desc_1_type_1 = "A slight upgrade to your stick.\nStill not much to look at but\natleast its sword shaped."
    weapon_desc_2_type_1 = "A crooked poorly crafted\ncopper sword."
    weapon_desc_3_type_1 = "A small iron dagger. It doesn't\nhave much range but it won't break."
    weapon_desc_4_type_1 = "A long, quality fencing sword. Much better\nthan anything you've hanled before."
    weapon_desc_5_type_1 = "The Legendary sword of the demon\nslayer Ivanovic Yankov. It is imbued with\nthe essence of fire and originality."
    
    
    weapon_name_1_type_2 = ""
    weapon_name_2_type_2 = ""
    weapon_name_3_type_2 = ""
    weapon_name_4_type_2 = ""
    weapon_name_5_type_2 = ""
    
    weapon_desc_1_type_2 = ""
    weapon_desc_2_type_2 = ""
    weapon_desc_3_type_2 = ""
    weapon_desc_4_type_2 = ""
    weapon_desc_5_type_2 = ""
    
    
    weapon_name_1_type_3 = ""
    weapon_name_2_type_3 = ""
    weapon_name_3_type_3 = ""
    weapon_name_4_type_3 = ""
    weapon_name_5_type_3 = ""
    
    weapon_desc_1_type_3 = ""
    weapon_desc_2_type_3 = ""
    weapon_desc_3_type_3 = ""
    weapon_desc_4_type_3 = ""
    weapon_desc_5_type_3 = ""

class item():
    def __init__(self, name, description, texture, position, belonging):
        self.name = name
        self.description = description
        self.texture = texture
        self.position = position
        self.name_size = 100
        self.desc_size = 50
        self.belonging = belonging
        self.shown = False
        
    def draw(self, font, screen, on_screen):
        if self.belonging == on_screen.active_screen.name and self.shown:
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
        
starter_weapon = item("Stick", "Nothing but a very\ngeneric stick.", pg.image.load(DATA_ROOT + "/data/textures/weapons/stick.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board")
starter_weapon.shown = True
weapon_1_type_1 = item(weapon_name_1_type_1, weapon_desc_1_type_1, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_1/1.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board")
weapon_2_type_1 = item(weapon_name_2_type_1, weapon_desc_2_type_1, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_1/2.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board")
weapon_3_type_1 = item(weapon_name_3_type_1, weapon_desc_3_type_1, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_1/3.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board")
weapon_4_type_1 = item(weapon_name_4_type_1, weapon_desc_4_type_1, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_1/4.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board")
weapon_5_type_1 = item(weapon_name_5_type_1, weapon_desc_5_type_1, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_1/5.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board")
    
weapons = [
            starter_weapon,
            weapon_1_type_1,
            weapon_2_type_1,
            weapon_3_type_1,
            weapon_4_type_1,
            weapon_5_type_1
            ]
    