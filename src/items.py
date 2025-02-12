import pygame as pg
import sys
from text import *
from data import *
from Screens import *

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'

pg.init()
pg.font.init()
resolution = 1200, 900


class item_cl():
    def __init__(self):
        self.weapons = []
        self.armors = []
        self.misc_items = []
        
    def item_bundling(self):
        self.all_items = self.weapons,self.armors,self.misc_items

item_class = item_cl()


def init_items(role):
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
        
        weapon_desc_1_type_3 = "A simple wooden\nmallet made from a stick\nand a piece of wood."
        weapon_desc_2_type_3 = "A solid hammer made\nof cast steel."
        weapon_desc_3_type_3 = "A spiked mace on a stick."
        weapon_desc_4_type_3 = "A spiky metal ball\non a chain."
        weapon_desc_5_type_3 = "The mythical hammer\nof the norse god\nof thunder, Thor."
        
    if role == "mage":
        weapon_name_1_type_1 = "Magic Stick"
        weapon_name_2_type_1 = "Shadewood Wand"
        weapon_name_3_type_1 = "Wallnut Staff"
        weapon_name_4_type_1 = "Elf Druid's Staff"
        weapon_name_5_type_1 = "Luxury Fire Staff"
        
        weapon_desc_1_type_1 = "You discovered that your\nstick seems to contain a\nlittle bit of magic."
        weapon_desc_2_type_1 = "A Small wand carved from\nshadewood with a dragon scale core."
        weapon_desc_3_type_1 = "A large, wallnut staff,\npossibly made by a forest dryad."
        weapon_desc_4_type_1 = "A thin, carved, wooden staff\nwith an encrested green emerald,\nit is fairly powerful."
        weapon_desc_5_type_1 = "A luxury staff with an\nembedded fire gem,\nthis staff was used by Gnem Swól,\nthe advisor of king Craidz."
        
        
        weapon_name_1_type_2 = "Wizards Notes"
        weapon_name_2_type_2 = "Magic Manual"
        weapon_name_3_type_2 = "Ancient Scroll"
        weapon_name_4_type_2 = "Advanced Magic"
        weapon_name_5_type_2 = "Necrobombicon"
        
        weapon_desc_1_type_2 = "These are the notes of\na beginner wizard."
        weapon_desc_2_type_2 = "An edition of Magic for Dummies,\ncontaining basic magic."
        weapon_desc_3_type_2 = "An ancient scroll that was\npart of a powerful spell book."
        weapon_desc_4_type_2 = "A brand new hardcover\nmanual for advanced magic."
        weapon_desc_5_type_2 = "An ancient and infamous\nspell book of the dead,\ncursed with raw power and hate."
        
        
        weapon_name_1_type_3 = "Wooden Necklace"
        weapon_name_2_type_3 = "Jeweled Amulet"
        weapon_name_3_type_3 = "Rune Stones"
        weapon_name_4_type_3 = "Crystal Runes"
        weapon_name_5_type_3 = "Smarlin's Crown"
        
        weapon_desc_1_type_3 = "A magical rune carved\ninto a piece of wood."
        weapon_desc_2_type_3 = "A powerful gemstone amulet."
        weapon_desc_3_type_3 = "Ancient runes carved into stones."
        weapon_desc_4_type_3 = "Large quartz crystals\nimbued with magical runes."
        weapon_desc_5_type_3 = "The mysthical crown of\nSmarlin the Great.\nIt posseses extreme amounts of power."
        
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
        
        
        weapon_name_1_type_3 = "Boomerang"
        weapon_name_2_type_3 = "Steel Shuriken"
        weapon_name_3_type_3 = "Kunai"
        weapon_name_4_type_3 = "Metal Flail"
        weapon_name_5_type_3 = "Thor's Mjölnir"
        
        weapon_desc_1_type_3 = "Surprisingly, it doesn't return."
        weapon_desc_2_type_3 = "Be a proper ninja with\nthis iconic throwing weapon!"
        weapon_desc_3_type_3 = "Now this is next-level ninja gear."
        weapon_desc_4_type_3 = "A spiky metal ball\non a chain."
        weapon_desc_5_type_3 = "The mythical hammer\nof the norse god\nof thunder, Thor."

    starter_weapon = item("Stick", "Nothing but a very\ngeneric stick.", pg.image.load(DATA_ROOT + "/data/textures/items/weapons/stick.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board", True, [1,1,None,None,None,1],"weapon_0")
    starter_weapon.shown = False
    player.weapon = starter_weapon
    weapon_1_type_1 = item(weapon_name_1_type_1, weapon_desc_1_type_1, pg.image.load(DATA_ROOT + "/data/textures/items/weapons/"+ player.role +"/type_1/1.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board", False, [40,5,None,None,None,1],"weapon_1_1")
    weapon_2_type_1 = item(weapon_name_2_type_1, weapon_desc_2_type_1, pg.image.load(DATA_ROOT + "/data/textures/items/weapons/"+ player.role +"/type_1/2.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board", False, [100,15,None,None,None,2],"weapon_2_1")
    weapon_3_type_1 = item(weapon_name_3_type_1, weapon_desc_3_type_1, pg.image.load(DATA_ROOT + "/data/textures/items/weapons/"+ player.role +"/type_1/3.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board", False, [350,35,None,None,None,6],"weapon_3_1")
    weapon_4_type_1 = item(weapon_name_4_type_1, weapon_desc_4_type_1, pg.image.load(DATA_ROOT + "/data/textures/items/weapons/"+ player.role +"/type_1/4.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board", False, [650,50,None,None,None,10],"weapon_4_1")
    weapon_5_type_1 = item(weapon_name_5_type_1, weapon_desc_5_type_1, pg.image.load(DATA_ROOT + "/data/textures/items/weapons/"+ player.role +"/type_1/5.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board", False, [925,100,None,None,None,15],"weapon_5_1")

    weapon_1_type_2 = item(weapon_name_1_type_2, weapon_desc_1_type_2, pg.image.load(DATA_ROOT + "/data/textures/items/weapons/"+ player.role +"/type_2/1.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board", False, [50,10,None,None,None,2],"weapon_1_2")
    weapon_2_type_2 = item(weapon_name_2_type_2, weapon_desc_2_type_2, pg.image.load(DATA_ROOT + "/data/textures/items/weapons/"+ player.role +"/type_2/2.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board", False, [150,25,None,None,None,4],"weapon_2_2")
    weapon_3_type_2 = item(weapon_name_3_type_2, weapon_desc_3_type_2, pg.image.load(DATA_ROOT + "/data/textures/items/weapons/"+ player.role +"/type_2/3.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board", False, [400,40,None,None,None,8],"weapon_3_2")
    weapon_4_type_2 = item(weapon_name_4_type_2, weapon_desc_4_type_2, pg.image.load(DATA_ROOT + "/data/textures/items/weapons/"+ player.role +"/type_2/4.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board", False, [700,55,None,None,None,12],"weapon_4_2")
    weapon_5_type_2 = item(weapon_name_5_type_2, weapon_desc_5_type_2, pg.image.load(DATA_ROOT + "/data/textures/items/weapons/"+ player.role +"/type_2/5.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board", False, [1000,115,None,None,None,20],"weapon_5_2")
        
    weapon_1_type_3 = item(weapon_name_1_type_3, weapon_desc_1_type_3, pg.image.load(DATA_ROOT + "/data/textures/items/weapons/"+ player.role +"/type_3/1.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board", False, [40,5,None,None,None,1],"weapon_1_3")
    weapon_2_type_3 = item(weapon_name_2_type_3, weapon_desc_2_type_3, pg.image.load(DATA_ROOT + "/data/textures/items/weapons/"+ player.role +"/type_3/2.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board", False, [120,20,None,None,None,3],"weapon_2_3")
    weapon_3_type_3 = item(weapon_name_3_type_3, weapon_desc_3_type_3, pg.image.load(DATA_ROOT + "/data/textures/items/weapons/"+ player.role +"/type_3/3.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board", False, [300,30,None,None,None,5],"weapon_3_3")
    weapon_4_type_3 = item(weapon_name_4_type_3, weapon_desc_4_type_3, pg.image.load(DATA_ROOT + "/data/textures/items/weapons/"+ player.role +"/type_3/4.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board", False, [550,55,None,None,None,9],"weapon_4_3")
    weapon_5_type_3 = item(weapon_name_5_type_3, weapon_desc_5_type_3, pg.image.load(DATA_ROOT + "/data/textures/items/weapons/"+ player.role +"/type_3/5.png"), ((resolution[0]/4) - 96, (resolution[1]/2) - 225), "Weapon board", False, [850,90,None,None,None,12],"weapon_5_3")
    
    item_class.weapons = [
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
    
    ### BRNĚNÍ ###
    armor_1 = item("Leather Padding", "Tough leather padding and hat.", pg.image.load(DATA_ROOT + "/data/textures/items/armors/1.png"),((resolution[0]/4) - 96, (resolution[1]/2) - 225),"Armor board", False, [40,None,5,None,None,2],"armor_1")
    armor_2 = item("Sturdy Shield", "A fairly big shield\nthat can block some blows.", pg.image.load(DATA_ROOT + "/data/textures/items/armors/2.png"),((resolution[0]/4) - 96, (resolution[1]/2) - 225),"Armor board", False, [120,None,10,None,None,5],"armor_2")
    armor_3 = item("Iron Armor", "Thonny Stank built\nthis in a cave.", pg.image.load(DATA_ROOT + "/data/textures/items/armors/3.png"),((resolution[0]/4) - 96, (resolution[1]/2) - 225),"Armor board", False, [350,None,15,None,None,8],"armor_3")
    armor_4 = item("Golden Armor", "This is one very glorious,\nvery shiny set of armor.", pg.image.load(DATA_ROOT + "/data/textures/items/armors/4.png"),((resolution[0]/4) - 96, (resolution[1]/2) - 225),"Armor board", False, [600,None,25,None,None,15],"armor_4")
    armor_5 = item("ARMOR 5", "armor desc 5", pg.image.load(DATA_ROOT + "/data/textures/items/armors/5.png"),((resolution[0]/4) - 96, (resolution[1]/2) - 225),"Armor board", False, [850,None,50,None,None,20],"armor_5")
    
    item_class.armors = [
        armor_1,
        armor_2,
        armor_3,
        armor_4,
        armor_5
        ]
    
    ### MISC ITEMY ###
    potion_healing = item("Healing potion", "A round bottle filled\nwith a strange red liquid.", pg.image.load(DATA_ROOT + "/data/textures/items/healing_potion.png"),((resolution[0]/4) - 96, (resolution[1]/2) - 225),"Item board", False, [50,None,None,1,None,2],"healing_potion")
    potion_mana = item("Mana potion", "A small bottle full of\nblue shimmering liquid.", pg.image.load(DATA_ROOT + "/data/textures/items/mana_potion.png"),((resolution[0]/4) - 96, (resolution[1]/2) - 225),"Item board", False, [50,None,None,1,None,8],"mana_potion")
    skill_scroll_1 = item("The scroll of tears", "It is suspiciously wet and\nseems to be dripping water.", pg.image.load(DATA_ROOT + "/data/textures/items/scrolls/scroll_water.png"),((resolution[0]/4) - 96, (resolution[1]/2) - 225),"Item board", False, [600,None,None,1,None,8],"skill_1")
    skill_scroll_2 = item("Vitriolic scroll", "Your eyes begin to water\njust in the presence of it.", pg.image.load(DATA_ROOT + "/data/textures/items/scrolls/scroll_poison.png"),((resolution[0]/4) - 96, (resolution[1]/2) - 225),"Item board", False, [1000,None,None,1,None,12],"skill_2")
    skill_scroll_3 = item("Tempestous scroll", "Sometimes it flashes and makes your\nmuscles twitch when touched.", pg.image.load(DATA_ROOT + "/data/textures/items/scrolls/scroll_lightning.png"),((resolution[0]/4) - 96, (resolution[1]/2) - 225),"Item board", False, [1200,None,None,1,None,15],"skill_3")
    
    item_class.misc_items = [
        potion_healing,
        potion_mana,
        skill_scroll_1,
        skill_scroll_2,
        skill_scroll_3
        ]
    
    item_class.item_bundling()
    
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
        self.level = stats[5]
        self.item_type = None
        
    def draw(self, font, screen, on_screen, tooltip_class):
        if on_screen.active_screen.name in self.belonging and self.shown:
            
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
            
            # Cena a potřebný level
            price_surf = self.desc_font.render(str(self.price), True, (0,0,0))
            screen.blit(price_surf, (125,645))
            level_surf = self.desc_font.render(str(self.level), True, (0,0,0))
            screen.blit(level_surf, (125, 710))
            
            weapon = False
            armor = False
            potion = False
            scroll = False
            
            if not self.damage == None:
                damage_surf = self.desc_font.render(str(self.damage), True, (0,0,0))
                screen.blit(damage_surf, (395,675))
                weapon = True
            
            if not self.armor == None:
                armor_surf = self.desc_font.render(str(self.armor) + "%", True, (0,0,0))
                screen.blit(armor_surf, (395,675))
                armor = True
            
            if self.armor == None and self.damage == None:
                if "potion" in self.name:
                    if self.name == "Healing potion":
                        effect_surf = self.desc_font.render("+50 HP", True, (0,0,0))
                        quantity_surf = self.desc_font.render(str(player.inventory["healing_potion"]), True, (0,0,0))
                        potion = True
                    elif self.name == "Mana potion":
                        effect_surf = self.desc_font.render("+50 Mana", True, (0,0,0))
                        quantity_surf = self.desc_font.render(str(player.inventory["mana_potion"]), True, (0,0,0))
                        potion = True
                    screen.blit(effect_surf, (395, 645))
                    screen.blit(quantity_surf, (395, 710))
                    
                elif "scroll" in self.name:
                    effect_surf = self.desc_font.render("New skill", True, (0,0,0))
                    screen.blit(effect_surf, (395, 645))
                    scroll = True
                
            for t in tooltip_class.tooltips:
                if t.table_name == "Item cost":
                    t.show = True
                elif t.table_name == "Item level":
                    t.show = True
                elif t.table_name == "Item damage" and weapon:
                    t.show = True
                elif t.table_name == "Item armor" and armor:
                    t.show = True
                elif (t.table_name == "Item effect" or t.table_name == "Item quantity") and potion:
                    t.show = True
                elif t.table_name == "Item effect" and scroll:
                    t.show = True
                    
        return tooltip_class.tooltips
                    