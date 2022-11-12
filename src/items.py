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
armors = []
misc_items = []

def init_items(weapons, role, armors, misc_items):
    ### ZBRANĚ ###
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
        
    if role == "mage":
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
        
    if role == "ranger":
        weapon_name_1_type_1 = "Wooden Bow"
        weapon_name_2_type_1 = "Ebony Longbow"
        weapon_name_3_type_1 = "Elven Longbow"
        weapon_name_4_type_1 = "Dryad's Bow"
        weapon_name_5_type_1 = "Ice Typhoon"
        
        weapon_desc_1_type_1 = "A curved stick with a\ntwine string tied to it."
        weapon_desc_2_type_1 = "A longbow carved from\na piece of old ebony wood."
        weapon_desc_3_type_1 = "A carved ash wood longbow\ncommonly used by elves."
        weapon_desc_4_type_1 = "A bow made from cherry wood\nwith painted feathers."
        weapon_desc_5_type_1 = "A bow carved from ice\nwith an imbedded frost core.\nThis rare weapon belonged\nto the frost emperor\nKheirad Nezan."
        
        
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

    starter_weapon = item("Stick", "Nothing but a very\ngeneric stick.", pg.image.load(DATA_ROOT + "/data/textures/weapons/stick.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board", True, [1,1,1,1,None],"weapon_0")
    starter_weapon.shown = True
    starter_weapon.bought = True
    player.weapon = starter_weapon
    weapon_1_type_1 = item(weapon_name_1_type_1, weapon_desc_1_type_1, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_1/1.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board", False, [1,1,1,1,None],"weapon_1_1")
    weapon_2_type_1 = item(weapon_name_2_type_1, weapon_desc_2_type_1, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_1/2.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board", False, [1,1,1,1,None],"weapon_2_1")
    weapon_3_type_1 = item(weapon_name_3_type_1, weapon_desc_3_type_1, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_1/3.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board", False, [1,1,1,1,None],"weapon_3_1")
    weapon_4_type_1 = item(weapon_name_4_type_1, weapon_desc_4_type_1, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_1/4.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board", False, [1,1,1,1,None],"weapon_4_1")
    weapon_5_type_1 = item(weapon_name_5_type_1, weapon_desc_5_type_1, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_1/5.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board", False, [1,1,1,1,None],"weapon_5_1")

    weapon_1_type_2 = item(weapon_name_1_type_2, weapon_desc_1_type_2, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_2/1.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board", False, [1,1,1,1,None],"weapon_1_2")
    weapon_2_type_2 = item(weapon_name_2_type_2, weapon_desc_2_type_2, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_2/2.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board", False, [1,1,1,1,None],"weapon_2_2")
    weapon_3_type_2 = item(weapon_name_3_type_2, weapon_desc_3_type_2, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_2/3.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board", False, [1,1,1,1,None],"weapon_3_2")
    weapon_4_type_2 = item(weapon_name_4_type_2, weapon_desc_4_type_2, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_2/4.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board", False, [1,1,1,1,None],"weapon_4_2")
    weapon_5_type_2 = item(weapon_name_5_type_2, weapon_desc_5_type_2, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_2/5.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board", False, [1,1,1,1,None],"weapon_5_2")
        
    weapon_1_type_3 = item(weapon_name_1_type_3, weapon_desc_1_type_3, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_3/1.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board", False, [1,1,1,1,None],"weapon_1_3")
    weapon_2_type_3 = item(weapon_name_2_type_3, weapon_desc_2_type_3, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_3/2.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board", False, [1,1,1,1,None],"weapon_2_3")
    weapon_3_type_3 = item(weapon_name_3_type_3, weapon_desc_3_type_3, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_3/3.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board", False, [1,1,1,1,None],"weapon_3_3")
    weapon_4_type_3 = item(weapon_name_4_type_3, weapon_desc_4_type_3, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_3/4.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board", False, [1,1,1,1,None],"weapon_4_3")
    weapon_5_type_3 = item(weapon_name_5_type_3, weapon_desc_5_type_3, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_3/5.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board", False, [1,1,1,1,None],"weapon_5_3")
    
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
    
    ### BRNĚNÍ ###
    armor_name_1 = "ARMOR 1"
    armor_name_2 = "ARMOR 2"
    armor_name_3 = "ARMOR 3"
    armor_name_4 = "ARMOR 4"
    armor_name_5 = "ARMOR 5"
    
    armor_desc_1 = "armor desc 1"
    armor_desc_2 = "armor desc 2"
    armor_desc_3 = "armor desc 3"
    armor_desc_4 = "armor desc 4"
    armor_desc_5 = "armor desc 5"
    
    starter_armor = item("Plain Clothes", "Just slightly torn\nwoolen clothes.", pg.image.load(DATA_ROOT + "/data/textures/weapons/stick.png"),((resolution[0]/4) - 96, (resolution[1]/2) - 225),"Armor board", False, [1,1,1,1,None],"armor_0")
    starter_armor.shown = True
    starter_armor.bought = True
    armor_1 = item(armor_name_1, armor_desc_1, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_1/1.png"),((resolution[0]/4) - 96, (resolution[1]/2) - 225),"Armor board", False, [1,1,1,1,None],"armor_1")
    armor_2 = item(armor_name_2, armor_desc_2, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_1/2.png"),((resolution[0]/4) - 96, (resolution[1]/2) - 225),"Armor board", False, [1,1,1,1,None],"armor_2")
    armor_3 = item(armor_name_3, armor_desc_3, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_1/3.png"),((resolution[0]/4) - 96, (resolution[1]/2) - 225),"Armor board", False, [1,1,1,1,None],"armor_3")
    armor_4 = item(armor_name_4, armor_desc_4, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_1/4.png"),((resolution[0]/4) - 96, (resolution[1]/2) - 225),"Armor board", False, [1,1,1,1,None],"armor_4")
    armor_5 = item(armor_name_5, armor_desc_5, pg.image.load(DATA_ROOT + "/data/textures/weapons/"+ player.role +"/type_1/5.png"),((resolution[0]/4) - 96, (resolution[1]/2) - 225),"Armor board", False, [1,1,1,1,None],"armor_5")
    
    armors = [
        starter_armor,
        armor_1,
        armor_2,
        armor_3,
        armor_4,
        armor_5
        ]
    
    armor_class.armors = armors
    
class item():
    def __init__(self, name, description, texture, position, belonging, bought, stats, identificator):
        self.id = identificator
        self.name = name
        self.description = description
        self.texture = texture
        self.position = position
        self.name_size = 75
        self.desc_size = 35
        self.belonging = belonging
        self.shown = False
        self.bought = bought
        self.price = stats[0]
        self.damage = stats[1]
        self.armor = stats[2]
        self.misc_stat = stats[3]
        self.special_effect = stats[4]
        self.item_type = None
        
    def item_type_check(self):
        if self.misc_stat == None and armor == None:
            self.item_type = weapon
            return self.item_type
        if self.damage == None and self.misc_stat == None:
            self.item_type = armor
            return self.item_type
        else:
            self.item_type = misc
            return self.item_type
        
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
        
class armor_cl():
    def __init__(self, armors):
        self.armors = armors
        
weapon_class = weapon_cl(weapons)
armor_class = armor_cl(armors)