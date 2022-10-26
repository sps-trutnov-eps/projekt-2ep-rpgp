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

weapons = []

def init_items(weapons, role):
    if role == "warrior":
        weapon_name_1_type_1 = "Wooden Sword"
        weapon_name_2_type_1 = "Copper Sword"
        weapon_name_3_type_1 = "Iron Dagger"
        weapon_name_4_type_1 = "Fencing Sword"
        weapon_name_5_type_1 = "Yankov Avenger"
        
        weapon_desc_1_type_1 = "A slight upgrade to your stick.\nStill not much to look at but\natleast its sword shaped."
        weapon_desc_2_type_1 = "A crooked poorly crafted\ncopper sword."
        weapon_desc_3_type_1 = "A small iron dagger. It doesn't\nhave much range but it won't break."
        weapon_desc_4_type_1 = "A long, quality fencing sword.\nMuch better than anything\n you've hanled before."
        weapon_desc_5_type_1 = "The Legendary sword of the demon\nslayer Ivanovic Yankov. It is imbued\nwith the essence of fire and originality."
        
        
        weapon_name_1_type_2 = "Primitive Axe"
        weapon_name_2_type_2 = "Copper Hatchet"
        weapon_name_3_type_2 = "Lumberjack Axe"
        weapon_name_4_type_2 = "Steel Waraxe"
        weapon_name_5_type_2 = "Vorneag's Waraxe"
        
        weapon_desc_1_type_2 = "A sharpened stone\ntied to a branch."
        weapon_desc_2_type_2 = "A chipped copper hatchet.\nIt has seen better days\nbut it still holds up."
        weapon_desc_3_type_2 = "An axe of a lumberjack\n by profession."
        weapon_desc_4_type_2 = "A large, hefty but\nproper waraxe."
        weapon_desc_5_type_2 = "The Waraxe of the\nlegendary dwarf warrior\nVorneag Grimbow."
        
        
        weapon_name_1_type_3 = "Wooden Mallet"
        weapon_name_2_type_3 = "Steel Hammer"
        weapon_name_3_type_3 = "Spiked Mace"
        weapon_name_4_type_3 = "Metal Flail"
        weapon_name_5_type_3 = "Thor's Mjölnir"
        
        weapon_desc_1_type_3 = "A wooden simple wooden\nmallet made from a stick\nand a piece of wood."
        weapon_desc_2_type_3 = "A solid hammer made\nof cast steel."
        weapon_desc_3_type_3 = "A spiked mace on a stick."
        weapon_desc_4_type_3 = "A spiky metal ball\non a chain."
        weapon_desc_5_type_3 = "The mythical hammer\nof the norse god\nof thunder, Thor."

    starter_weapon = item("Stick", "Nothing but a very\ngeneric stick.", pg.image.load(DATA_ROOT + "/data/textures/weapons/stick.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board")
    starter_weapon.shown = True
    weapon_1_type_1 = item(weapon_name_1_type_1, weapon_desc_1_type_1, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_1/1.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board")
    weapon_2_type_1 = item(weapon_name_2_type_1, weapon_desc_2_type_1, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_1/2.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board")
    weapon_3_type_1 = item(weapon_name_3_type_1, weapon_desc_3_type_1, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_1/3.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board")
    weapon_4_type_1 = item(weapon_name_4_type_1, weapon_desc_4_type_1, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_1/4.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board")
    weapon_5_type_1 = item(weapon_name_5_type_1, weapon_desc_5_type_1, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_1/5.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board")

    weapon_1_type_2 = item(weapon_name_1_type_2, weapon_desc_1_type_2, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_2/1.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board")
    weapon_2_type_2 = item(weapon_name_2_type_2, weapon_desc_2_type_2, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_2/2.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board")
    weapon_3_type_2 = item(weapon_name_3_type_2, weapon_desc_3_type_2, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_2/3.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board")
    weapon_4_type_2 = item(weapon_name_4_type_2, weapon_desc_4_type_2, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_2/4.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board")
    weapon_5_type_2 = item(weapon_name_5_type_2, weapon_desc_5_type_2, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_2/5.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board")
        
    weapon_1_type_3 = item(weapon_name_1_type_3, weapon_desc_1_type_3, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_3/1.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board")
    weapon_2_type_3 = item(weapon_name_2_type_3, weapon_desc_2_type_3, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_3/2.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board")
    weapon_3_type_3 = item(weapon_name_3_type_3, weapon_desc_3_type_3, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_3/3.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board")
    weapon_4_type_3 = item(weapon_name_4_type_3, weapon_desc_4_type_3, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_3/4.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board")
    weapon_5_type_3 = item(weapon_name_5_type_3, weapon_desc_5_type_3, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_3/5.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board")
    
    weapons = [
            starter_weapon,
            weapon_1_type_1,
            weapon_2_type_1,
            weapon_3_type_1,
            weapon_4_type_1,
            weapon_5_type_1,
            weapon_1_type_2,
            weapon_2_type_2,
            weapon_3_type_2,
            weapon_4_type_2,
            weapon_5_type_2,
            weapon_1_type_3,
            weapon_2_type_3,
            weapon_3_type_3,
            weapon_4_type_3,
            weapon_5_type_3
            ]
    
    weapon_class.weapons = weapons
    
class item():
    def __init__(self, name, description, texture, position, belonging):
        self.name = name
        self.description = description
        self.texture = texture
        self.position = position
        self.name_size = 75
        self.desc_size = 35
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
    
class weapon_cl():
    def __init__(self, weapons):
        self.weapons = weapons
        
weapon_class = weapon_cl(weapons)
