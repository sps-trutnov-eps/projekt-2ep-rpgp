import sys
import pygame as pg
from data import *

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'
    
pg.font.init()
    
def gold_level_position(x, y,text):
    return (x - (coin_level_font.size(text)[0] / 2),y + (coin_level_font.size(text)[1] / 2))
    
class text_cl():
    def __init__(self):
        self.texts = []
        self.messages = []
        
    def texts_bundling(self):
        self.all = []
        self.all = self.texts + self.messages
        
    def hide_messages(self):
        for m in self.messages:
            m.shown = False
            
    def show_message(self, wanted_name):
        for m in self.messages:
            if m.name == wanted_name:
                m.shown = True
                
    def check(self):
        got_it = False
        for m in self.messages:
            if m.shown == True:
                got_it = True
        return got_it
        
text_class = text_cl()
    
class text():
    def __init__(self, belonging, text, position, font, colour, id_ ="basic"):
        text_class.texts.append(self)
        self.belonging = belonging
        self.text = text
        self.position = position
        self.font = font
        self.colour = colour
        self.size = self.font.size(self.text)
        self.id = id_
        self.show = True
        
    def blit_self(self, screen, on__screen):
        if not on__screen.active_screen == "Exit" and self.show:
            if not on__screen.active_table == "Close":
                if on__screen.active_table.name in self.belonging:
                    surf = self.font.render(self.text, True, self.colour)
                    width, height = self.font.size(self.text)[0], self.font.size(self.text)[1]
                    if self.id == "f":
                        screen.blit(surf, (self.position[0], self.position[1]))
                    elif self.id == "b":
                        screen.blit(surf, ((self.position[0] - width), (self.position[1] - height)))
                    else:
                        screen.blit(surf, ((self.position[0] - (width / 2)), (self.position[1] - (height / 2))))
            elif on__screen.active_screen.name in self.belonging:
                surf = self.font.render(self.text, True, self.colour)
                width, height = self.font.size(self.text)[0], self.font.size(self.text)[1]
                if self.id == "f":
                    screen.blit(surf, (self.position[0], self.position[1]))
                elif self.id == "b":
                    screen.blit(surf, ((self.position[0] - width), (self.position[1])))
                else:
                    screen.blit(surf, ((self.position[0] - (width / 2)), (self.position[1] - (height / 2))))
            
        
    def update(self, new_text, new_pos):
        self.text = new_text
        if not new_pos == None:
            self.position = new_pos
            
class message():
    def __init__(self, name, belonging, text, pos, font, colour):
        text_class.messages.append(self)
        self.name = name
        self.belonging = belonging
        self.text = text
        self.position = pos
        self.font = font
        self.colour = colour
        self.size = self.font.size(self.text)
        self.shown = False
        
    def blit_self(self, screen, on__screen):
        if self.shown == True:
            if not on__screen.active_screen == "Exit":
                if not on__screen.active_table == "Close":
                    if on__screen.active_table.name in self.belonging:
                        surf = self.font.render(self.text, True, self.colour)
                        width, height = self.font.size(self.text)[0], self.font.size(self.text)[1]
                        screen.blit(surf, ((self.position[0] - (width / 2)), (self.position[1] - (height / 2))))
                elif on__screen.active_screen.name in self.belonging:
                    surf = self.font.render(self.text, True, self.colour)
                    width, height = self.font.size(self.text)[0], self.font.size(self.text)[1]
                    screen.blit(surf, ((self.position[0] - (width / 2)), (self.position[1] - (height / 2))))
        
heading0_size  = 80
heading1_size = 66
message_size = 50
settings_size = 45
regular_size = 30

def_link = DATA_ROOT + "/data/fonts/VeniceClassic.ttf"
def_colour = (200,200,200)
dark_colour = (30,30,30)
dark_red = (190,20,20)
black = (0,0,0)
white = (255,255,255)
cooldown_color = (220,100,220)
golden = (240,200,60)
skill_colour = (60,200,240)

coin_level_font = pg.font.Font(def_link, 54)

# Texty v tabulce nové hry
tn1 = text(["New game table"], "Choose your role:", (600,200), pg.font.Font(def_link, heading0_size), def_colour) 

# Texty v tabulce nastavení
ts1 = text(["Settings table"], "Settings", (600,200), pg.font.Font(def_link, heading1_size), def_colour)

# Texty v tabulce credits
tc1 = text(["Credits table"], "Credits", (600, 200), pg.font.Font(def_link, heading1_size), def_colour)

# Texty v obchodě
tsh_buy = text(["Weapon board", "Armor board", "Item board"], "Buy", (162, 810), pg.font.Font(def_link, heading1_size), def_colour)
tsh_equip = text(["Weapon board", "Armor board", "Item board"], "Equip", (437, 810), pg.font.Font(def_link, heading1_size), def_colour)

# Texty v nastavení ve hře
caption = text(["Game table"], "Settings", (600,200), pg.font.Font(def_link, heading1_size), def_colour)
save = text(["Game table"], "Save", (600,400), pg.font.Font(def_link, settings_size), def_colour)
exit_t = text(["Game table"], "Exit", (600,500), pg.font.Font(def_link, settings_size), def_colour)
save_and_exit = text(["Game table"], "Save and Exit", (600,600), pg.font.Font(def_link, settings_size), def_colour)

# Peníze a level
golds = text(["Game menu", "Shop", "Campaign", "Profile", "Weapon board", "Armor board", "Item board"], str(player.gold), gold_level_position(1110,30,str(player.gold)), coin_level_font, dark_colour)
p_level = text(["Game menu", "Shop", "Campaign", "Profile", "Weapon board", "Armor board", "Item board"], str(player.level), gold_level_position(1110,85,str(player.level)), coin_level_font, dark_colour)

# Texty před bitvou
fight = text(["Campaign"], "Fight", (1000, 810), pg.font.Font(def_link, heading1_size), def_colour)
hp_p = text(["Campaign"], ": " + str(player.inventory["healing_potion"]), (125, 760), pg.font.Font(def_link, settings_size), dark_colour, "f")
mana_p = text(["Campaign"], ": " + str(player.inventory["mana_potion"]), (125, 810), pg.font.Font(def_link, settings_size), dark_colour, "f")

# Texty v bitvě
player_hp = text(["Battle"], "/", (290,795), pg.font.Font(def_link, regular_size), def_colour, "p_hp")
player_mana = text(["Battle"], "/", (290,845), pg.font.Font(def_link, regular_size), def_colour, "p_mana")
enemy_hp = text(["Battle"], "/", (915,56), pg.font.Font(def_link, regular_size), def_colour, "e_hp")
pause_question = text(["Pause table"], "Do you wish to leave the battle?", (600,330), pg.font.Font(def_link, settings_size), def_colour)
pause_yes = text(["Pause table"], "Yes", (450,542), pg.font.Font(def_link, 38), def_colour)
pause_no = text(["Pause table"], "No", (750,542), pg.font.Font(def_link, 38), def_colour)
health_p_counter = text(["Battle"], str(player.inventory["healing_potion"]), (1100,845), pg.font.Font(def_link, regular_size), def_colour)
mana_p_counter = text(["Battle"], str(player.inventory["mana_potion"]), (1020,845), pg.font.Font(def_link, regular_size), def_colour)
text_class.counter_texts = [
                    health_p_counter,
                    mana_p_counter
                            ]
cooldown_text1 = text(["Battle"], "0", (749,825), pg.font.Font(def_link, heading1_size), cooldown_color)
cooldown_text2 = text(["Battle"], "0", (837,825), pg.font.Font(def_link, heading1_size), cooldown_color)
cooldown_text3 = text(["Battle"], "0", (925,825), pg.font.Font(def_link, heading1_size), cooldown_color)
text_class.cooldown_texts = [
                    cooldown_text1,
                    cooldown_text2,
                    cooldown_text3
                            ]
for t in text_class.cooldown_texts:
    t.show = False
    
# Texty po bitvě
death_statement = text(["Death table"], "You have lost the battle", (600,330), pg.font.Font(def_link, heading0_size), def_colour)
death_leave = text(["Death table"], "Leave", (450,542), pg.font.Font(def_link, 38), def_colour)
death_retry = text(["Death table"], "Retry", (750,542), pg.font.Font(def_link, 38), def_colour)
win_statement = text(["Win table"], "You have won this battle!", (600, 200), pg.font.Font(def_link, heading0_size), def_colour)
win_leave = text(["Win table"], "Back", (450,722), pg.font.Font(def_link, 38), def_colour)
win_continue = text(["Win table"], "Next level", (750, 722), pg.font.Font(def_link, 38), def_colour)
gold_gained = text(["Win table"], "", (600, 300), pg.font.Font(def_link, regular_size), def_colour)
xp_gained = text(["Win table"], "", (600, 350), pg.font.Font(def_link, regular_size), def_colour)
new_level = text(["Win table"], "NEXT LEVEL", (600, 470), pg.font.Font(def_link, message_size), golden)
new_point = text(["Win table"], "you gained a stat point", (600, 500), pg.font.Font(def_link, regular_size), golden)
new_skill_1 = text(["Win table"], "NEW SKILL", (600, 580), pg.font.Font(def_link, message_size), skill_colour)
new_skill_2 = text(["Win table"], "you unlocked a new skill", (600, 610), pg.font.Font(def_link, regular_size), skill_colour)

# Zprávy v ochodě
buy = message("buy", ["Weapon board", "Armor board", "Item board"], "Item has been purchased", (300,150), pg.font.Font(def_link, message_size), dark_colour)
bought = message("bought", ["Weapon board", "Armor board", "Item board"], "Item already purchased", (300,150), pg.font.Font(def_link, message_size), dark_red)
equip = message("equip", ["Weapon board", "Armor board", "Item board"], "Item has been equiped", (300,150), pg.font.Font(def_link, message_size), dark_colour)
unequip = message("unequip", ["Weapon board", "Armor board", "Item board"], "Item has been unequiped", (300,150), pg.font.Font(def_link, message_size), dark_colour)
equiped = message("equiped", ["Weapon board", "Armor board", "Item board"], "Item already equiped", (300,150), pg.font.Font(def_link, message_size), dark_red)
no_golds = message("no golds", ["Weapon board", "Armor board", "Item board"], "Insufficient funds", (300,150), pg.font.Font(def_link, message_size), dark_red)
no_level = message("no level", ["Weapon board", "Armor board", "Item board"], "Insufficient level", (300,150), pg.font.Font(def_link, message_size), dark_red)
no_more = message("no more", ["Weapon board", "Armor board", "Item board"], "Can't buy more of this", (300,150), pg.font.Font(def_link, message_size), dark_red)
no_equip = message("no equip", ["Weapon board", "Armor board", "Item board"], "Can't equip this item", (300,150), pg.font.Font(def_link, message_size), dark_red)
no_owner = message("no owner", ["Weapon board", "Armor board", "Item board"], "You don't own this yet", (300,150), pg.font.Font(def_link, message_size), dark_red)
no_mana = message("no mana", ["Battle"], "You don't have enough mana", (600, 700), pg.font.Font(def_link, message_size), dark_red)
save = message("save", ["Game table"], "Game saved", (600, 700), pg.font.Font(def_link, message_size), def_colour)

# Texty v profilu
skill_title = text(["Skill board"], "Skills", (600,75), pg.font.Font(def_link,heading1_size),dark_colour)
debuff_title = text(["Debuff board"], "Debuffs", (600,75), pg.font.Font(def_link,heading1_size),dark_colour)
slot_1 = text(["Skill board"], "1", (500,710), pg.font.Font(def_link,heading1_size),dark_colour)
slot_2 = text(["Skill board"], "2", (600,710), pg.font.Font(def_link,heading1_size),dark_colour)
slot_3 = text(["Skill board"], "3", (700,710), pg.font.Font(def_link,heading1_size),dark_colour)
to_debuffs = text(["Skill board"], "Debuffs", (1007.5, 775), pg.font.Font(def_link,heading1_size),def_colour)
to_skills = text(["Debuff board"], "Skills", (1007.5, 775), pg.font.Font(def_link,heading1_size),def_colour)
equip_skill = text(["Skill board"], "Equip", (192.5, 775), pg.font.Font(def_link,heading1_size),def_colour)
hp_stat_value = text(["Profile"], str(player.hp_stat) + "/10", (900,202), pg.font.Font(def_link,settings_size),def_colour)
mana_stat_value = text(["Profile"], str(player.mana_stat) + "/10", (900,286), pg.font.Font(def_link,settings_size),def_colour)
int_stat_value = text(["Profile"], str(player.int_stat) + "/10", (900,370), pg.font.Font(def_link,settings_size),def_colour)
luck_stat_value = text(["Profile"], str(player.luck_stat) + "/10", (900,454), pg.font.Font(def_link,settings_size),def_colour)
stat_point_value = text(["Profile"], str(player.stat_point), (900,538), pg.font.Font(def_link,heading1_size),def_colour)
stat_table_name = text(["Profile"], "Stats", (900,120), pg.font.Font(def_link,heading1_size),def_colour)
skill_icon_name = text(["Profile"], "Skills", (900, 625), pg.font.Font(def_link,heading1_size),def_colour)
xp_name = text(["Profile"], "LEVEL: " + str(player.level), (165, 210), pg.font.Font(def_link,regular_size),def_colour,"f")
xp_value = text(["Profile"], "XP: " + str(player.xp) + " / " + str(player.xp_req), (555, 210), pg.font.Font(def_link,regular_size),def_colour,"b")

# Texty v game menu
profile = text(["Game menu"], "PROFILE", (145,520), pg.font.Font(def_link, settings_size),def_colour)
campaign = text(["Game menu"], "CAMPAIGN", (600,530), pg.font.Font(def_link, settings_size),def_colour)
shop = text(["Game menu"], "SHOP", (990, 520), pg.font.Font(def_link, settings_size),def_colour)

text_class.texts_bundling()