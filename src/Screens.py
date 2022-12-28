import sys
import pygame as pg
from text import *
from data import *
from items import *
from campaign import *
from skills import *

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'

class on_screen():
    def __init__(self):
        self.screens = []
        self.tables = []
        self.blit_objects = []
        self.bought_icons = []
        self.active_screen = None
        self.active_table = "Close"
        self.button_activity = True
        self.battle = False
        self.active_level = None
        
on__screen = on_screen()

class button_cl():
    def __init__(self):
        self.buttons = []
        self.skill_buttons = []
        
button_class = button_cl()

class screen():
    def __init__(self, name, background, backbackground = None):
        on__screen.screens.append(self)
        self.name = name
        self.background = pg.transform.scale(background, (1200,900))
        if not backbackground == None:
            self.backbackground = pg.transform.scale(backbackground, (1200,900))
        else:
            self.backbackground = None
        buttons = button_class.buttons
        self.buttons = []
        for button in buttons:
            for place in button.belonging:
                if place == self.name:
                    self.buttons.append(button)
    
class tooltip_cl():
    def __init__(self):
        self.tooltips = []
        
tooltip_class = tooltip_cl()

class tooltip():
    def __init__(self, area, table_name, table_description, belonging, draw_pos, conditional, condition):
        tooltip_class.tooltips.append(self)
        self.belonging = belonging
        self.area = area
        self.table_name = table_name
        self.table_desc = table_description
        self.border = 20
        self.draw_pos = draw_pos
        self.show = True
        self.conditional = conditional
        self.condition = condition
        self.condition_met = False
        if "Item" in self.table_name:
            self.show = False
        if self.conditional == True and self.condition == True:
            self.condition_met = True
        if self.conditional == False and self.condition == None:
            self.condition_met = True
            
    def update_tooltip(self, updated_condition):
        self.condition = updated_condition
        if self.conditional == True and self.condition == True:
            self.condition_met = True
        if self.condition == False:
            self.condition_met = False
        
    def draw_tooltip(self, mouse_pos, screen, on__screen):
        if self.condition_met == True:
            if not on__screen.active_screen == "Exit":
                if on__screen.active_screen.name in self.belonging and self.show:
                    pg.font.init()
                    
                    name_size = 40
                    desc_size = 25
                    
                    table_width = 0
                    table_height = 0
                    
                    name_font = pg.font.Font(DATA_ROOT + "/data/fonts/VeniceClassic.ttf", name_size)
                    desc_font = pg.font.Font(DATA_ROOT + "/data/fonts/VeniceClassic.ttf", desc_size)
                    name = name_font.render(self.table_name, False, (255,255,255))
                    name_rect = name.get_rect()
                    
                    # Dělení řádků popisu
                    desc_text_list = []
                    desc_pos_list = []
                    desc_i = 0
                    desc_widths = []
                    
                    for desc_line in self.table_desc.split('\n'):
                        desc_text_line = desc_font.render(desc_line, True, (200,200,200))
                        desc_text_list.append(desc_text_line)
                        desc_widths.append(desc_text_line.get_rect().width)
                        desc_pos = desc_text_line.get_rect(topleft=(mouse_pos[0] + self.border, mouse_pos[1] + (name_size / 1.2) + (desc_size * desc_i) + self.border))
                        desc_pos_list.append(desc_pos)
                        desc_i = desc_i + 1
                     
                    if name_rect.width > max(desc_widths):
                        table_width = name_rect.width + (self.border * 2)
                        
                    elif name_rect.width < max(desc_widths):
                        table_width = max(desc_widths) + (self.border * 2)
                     
                    table_height = name_rect[1] + (int(len(desc_pos_list)) * desc_size) + (self.border * 2) + desc_size
                    
                    table = pg.surface.Surface((table_width,table_height), pg.SRCALPHA)
                    table.fill((30,30,30,180))
                    
                    if mouse_pos[0] >= self.area[0] and mouse_pos[0] <= (self.area[0] + self.area[2]):
                        if mouse_pos[1] >= self.area[1] and mouse_pos[1] <= (self.area[1] + self.area[3]):
                            if self.draw_pos == "bottom_right":
                                screen.blit(table, mouse_pos)
                                screen.blit(name, (mouse_pos[0] + self.border, mouse_pos[1] + (self.border/2)))
                                for desc_j in range(desc_i):
                                    screen.blit(desc_text_list[desc_j], desc_pos_list[desc_j])
                            
                            if self.draw_pos == "bottom_left":
                                screen.blit(table, (mouse_pos[0] - table_width, mouse_pos[1]))
                                screen.blit(name, (mouse_pos[0] + self.border - table_width, mouse_pos[1] + (self.border/2)))
                                for desc_j in range(desc_i):
                                    screen.blit(desc_text_list[desc_j], (desc_pos_list[desc_j][0] - table_width, desc_pos_list[desc_j][1]))
                                    
                            if self.draw_pos == "top_right":
                                screen.blit(table, (mouse_pos[0], mouse_pos[1] - table_height))
                                screen.blit(name, (mouse_pos[0] + self.border, mouse_pos[1] + (self.border/2) - table_height))
                                for desc_j in range(desc_i):
                                    screen.blit(desc_text_list[desc_j], (desc_pos_list[desc_j][0], desc_pos_list[desc_j][1] - table_height))
                                    
                            if self.draw_pos == "top_left":
                                screen.blit(table, (mouse_pos[0] - table_width, mouse_pos[1] - table_height))
                                screen.blit(name, (mouse_pos[0] + self.border - table_width, mouse_pos[1] + (self.border/2) - table_height))
                                for desc_j in range(desc_i):
                                    screen.blit(desc_text_list[desc_j], (desc_pos_list[desc_j][0] - table_width, desc_pos_list[desc_j][1] - table_height))
                    
health_stat_tooltip = tooltip((700,170,64,64), "Maximum health", "Each point of this stat increases\nmaximum health by 20.", ["Profile"],"bottom_left",False, None)
mana_stat_tooltip = tooltip((700,254,64,64), "Maximum mana", "Each point of this stat increases\nmaximum mana by 20.", ["Profile"],"bottom_left",False, None)
int_stat_tooltip = tooltip((700,338,64,64), "Intelligence", "Each point of this stat increases\nthe experience reward for each campaign level.", ["Profile"],"top_left",False, None)
luck_stat_tooltip = tooltip((700,422,64,64), "Luck", "Each point of this stat increases\nthe gold reward for each campaign level.", ["Profile"],"top_left",False, None)
stat_point_tooltip = tooltip((800,506,64,64),"Stat Point", "With every level up you gain\na stat point which you can\nuse to upgrade your stats.", ["Profile"], "top_left", False, None)
cost_tooltip = tooltip((60,640,54,54), "Item cost", "Cost of the item", ["Weapon board", "Armor board", "Item board"],"top_right",False, None)
level_tooltip = tooltip((60,700,54,54), "Item level", "Level needed to buy item", ["Weapon board", "Armor board", "Item board"],"top_right",False, None)
damage_tooltip = tooltip((330,670,54,54), "Item damage", "Damage this weapon deals", ["Weapon board"],"top_left",False, None)
armour_tooltip = tooltip((330,670,54,54), "Item armor", "Armor provided", ["Armor board"],"top_left",False, None)
effect_tooltip = tooltip((330,640,54,54), "Item effect", "What the item does", ["Item board"],"top_left",False, None)
quantity_tooltip = tooltip((330,700,54,54), "Item quantity", "How much of this\nitem you own", ["Item board"],"top_left",False, None)

#Skill Debuff Tooltips
on_fire_tooltip = tooltip((345,575,135,35), "On Fire!", "Deals X damage per second\nfor the duration of the debuff.", ["Skill board"],"top_right",True, fireball.shown)
wet_tooltip = tooltip((860,535,75,35), "Wet!", "Lowers defense by X % for\nthe duration of the debuff.", ["Skill board"],"top_left",True, water_blast.shown)
frozen_tooltip = tooltip((340,570,130,40), "Frozen!", "For the duration of the debuff\nthere is an X % chance to\nfreeze completely every round.", ["Skill board"],"top_right",True, ice_storm.shown)
poisoned_tooltip = tooltip((530,480,160,40), "Poisoned!", "Deals X damage per second and\nlowers attack damage and defense by X %\nfor the duration of the debuff.", ["Skill board"],"top_right",True, poison_dart.shown)
shocked_tooltip = tooltip((345,525,150,35), "Shocked!", "Lowers attack damage by X % for\nthe duration of the debuff.", ["Skill board"],"top_right",True, lightning_bolt.shown)

class table():
    def __init__(self, name):
        on__screen.tables.append(self)
        self.name = name
        self.position = [100,100]
        self.size = [1000,700]
        self.colour = (30,30,30)
        self.alpha = 220
        buttons = button_class.buttons
        self.buttons = []
        for button in buttons:
            for place in button.belonging:
                if place == self.name:
                    self.buttons.append(button)
                    
    def change_format(self, new_position, new_size):
        self.position = new_position
        self.size = new_size

class Button():
    def __init__(self, belonging, position, colour, width, height, tasks, draw, texture, scale, condition):
        button_class.buttons.append(self)
        if belonging[0] == "Skill board" and tasks[0][0] == "change_item":
            button_class.skill_buttons.append(self)
        self.belonging = belonging
        self.position = position
        self.width = width
        self.height = height
        self.tasks = tasks
        self.colour = colour
        self.alpha = 180
        self.draw = draw
        self.active_skill_slot = None
        self.offset = width/3
        self.draw_texture = True
        if not texture == None:
            if scale:
                self.texture = pg.transform.scale(texture, (width, height))
            else:
                self.texture = texture
        else:
            self.texture = None
        if not condition == None:
            self.condition = condition
        else:
            self.condition = True
        
    def get_texture(self, texture):
        if texture == None:
            self.texture = None
        else:
            self.texture = pg.transform.scale(texture, (self.width, self.height))
            
    def change(self, m_pressed):
        if self.tasks[0][0] == "equip_item":
            for it in item_class.all_items:
                for i in it:
                    if i.shown and (player.weapon == i or player.armor == i):
                        for t in text_class.texts:
                            if t.text == "Equip":
                                t.text = "Unequip"
                                t.font = pg.font.Font(def_link, 55)
        if self.position[0] < pg.mouse.get_pos()[0] < (self.position[0] + self.width) and self.position[1] < pg.mouse.get_pos()[1] < (self.position[1] + self.height) and m_pressed[0] and self.condition:
            if self.tasks[0][0] == "change_item" or self.tasks[0][0] == "change_screen":
                for button in button_class.buttons:
                    if button.tasks[0][0] == "buy_item":
                        button.colour = (30,30,30,100)
                    elif button.tasks[0][0] == "equip_item":
                        for t in text_class.texts:
                            if t.text == "Unequip":
                                t.text = "Equip"
                                t.font = pg.font.Font(def_link, 66)
            elif self.tasks[0][0] == "equip_item" or self.tasks[0][0] == "change_screen":
                for t in text_class.texts:
                    if t.text == "Unequip":
                        t.text = "Equip"
                        t.font = pg.font.Font(def_link, 66)
        if self.tasks[0][0] == "buy_item":
            for it in item_class.all_items:
                for i in it:
                    if i.shown and i.bought:
                        self.colour = (80,30,30,180)
            
    def check(self, m_pressed, on__screen):
        if not on__screen.active_screen == "Exit":
            if not on__screen.active_table == "Close":
                if on__screen.active_table.name in self.belonging:
                    self.change(m_pressed)
                    if self.position[0] < pg.mouse.get_pos()[0] < (self.position[0] + self.width) and self.position[1] < pg.mouse.get_pos()[1] < (self.position[1] + self.height) and m_pressed[0] and self.condition:
                        on__screen.button_activity = False
                        self.work()
            elif on__screen.active_screen.name in self.belonging:
                self.change(m_pressed)
                if self.position[0] < pg.mouse.get_pos()[0] < (self.position[0] + self.width) and self.position[1] < pg.mouse.get_pos()[1] < (self.position[1] + self.height) and m_pressed[0] and self.condition:
                   on__screen.button_activity = False
                   self.work()
            
    def blit_self(self, screen, on__screen):
        if not on__screen.active_screen == "Exit":
            if not on__screen.active_table == "Close":
                if on__screen.active_table.name in self.belonging:
                    if not self.draw == False:
                        if self.draw == "c":
                            backgr_size = self.width + self.offset
                            button_sf = pg.Surface((backgr_size, backgr_size), pg.SRCALPHA)
                            pg.draw.circle(button_sf, self.colour, ((backgr_size/2),(backgr_size/2)), backgr_size/2)
                            screen.blit(button_sf, ((self.position[0] - self.offset/2),(self.position[1] - self.offset/2)))
                        elif self.draw == "r":
                            button_sf = pg.Surface((self.width, self.height), pg.SRCALPHA)
                            button_sf.fill(self.colour)
                            screen.blit(button_sf, (self.position[0], self.position[1]))
                    if self.texture == None:
                        pass
                    else:
                        if self.draw_texture:
                            screen.blit(self.texture, (self.position))
            elif on__screen.active_screen.name in self.belonging:
                if not self.draw == False:
                    if self.draw == "c":
                        backgr_size = self.width + self.offset
                        button_sf = pg.Surface((backgr_size, backgr_size), pg.SRCALPHA)
                        pg.draw.circle(button_sf, self.colour, ((backgr_size/2),(backgr_size/2)), backgr_size/2)
                        screen.blit(button_sf, ((self.position[0] - self.offset/2),(self.position[1] - self.offset/2)))
                    elif self.draw == "r":
                        button_sf = pg.Surface((self.width, self.height), pg.SRCALPHA)
                        button_sf.fill(self.colour)
                        screen.blit(button_sf, (self.position[0], self.position[1]))
                if self.texture == None:
                    pass
                else:
                    if self.draw_texture:
                        screen.blit(self.texture, (self.position))
        
    def work(self):
        for task in self.tasks:
            if task[0] == "change_role":
                self.change_role(task[1])
            if task[0] == "change_screen":
                self.change_screen(task[1], on__screen)
                text_class.hide_messages()
            if task[0] == "change_table":
                self.change_table(task[1], on__screen)
                text_class.hide_messages()
            if task[0] == "change_item":
                self.change_item(task[1], task[2])
                text_class.hide_messages()
            if task[0] == "create_items":
                init_items(player.role)
                shop_b_init()
            if task[0] == "change_level":
                self.change_level(task[1])
            if task[0] == "start_battle":
                self.start_battle(on__screen)
            if task[0] == "restart_battle":
                self.restart_battle(on__screen)
            if task[0] == "end_battle":
                self.end_battle()
            if task[0] == "pause_battle":
                battle_info.pause_battle()
            if task[0] == "unpause_battle":
                battle_info.unpause_battle()
            if task[0] == "save":
                self.save()
            if task[0] == "load":
                self.load()
            if task[0] == "delete_save":
                self.delete_save()
            if task[0] == "buy_item":
                text_class.hide_messages()
                self.buy_item()
                index = text_class.texts.index(golds)
                text_class.texts[index].update(str(player.gold), gold_level_position(1110,30,str(player.gold)))
            if task[0] == "equip_item":
                text_class.hide_messages()
                self.equip_item(True)
            if task[0] == "reset_item_show":
                self.reset_item_show()
            if task[0] == "win_battle":
                self.win_battle()
            if task[0] == "continue_battle":
                self.continue_battle()
            if task[0] == "select_skill_slot":
                self.select_skill_slot(task[1])
            if task[0] == "equip_skill":
                self.equip_skill()
            if task[0] == "change_stat":
                self.change_stat(task[1])
            if task[0] == "activate_skill":
                self.activate_skill(task[1])
            if task[0] == "drink_potion":
                self.drink_potion(task[1])
        
    def change_screen(self, new_screen, on_screen):
        if new_screen == "Exit":
            on_screen.active_screen = "Exit"
        else:
            for screen in on__screen.screens:
                if screen.name == new_screen:
                    on_screen.active_screen = screen
                    on_screen.active_table = "Close"
                
    def change_table(self, new_table, on_screen):
        if new_table == "Close":
            on_screen.active_table = "Close"
        else:
            for table in on__screen.tables:
                if table.name == new_table:
                    on_screen.active_table = table
                    
    def change_item(self, new_item_number, items):
        for item in items:
            item.shown = False
        if len(items) - 1 >= new_item_number:
            items[new_item_number].shown = True
        
    def change_role(self, role):
        player.role = role
        
    def change_level(self, direction):
        if direction == "up":
            counter.up()
        elif direction == "down":
            counter.down()
    
    def start_battle(self, on__screen):
        if levels[counter.number - 1].unlocked == True:
            on__screen.battle = True
            for screen in on__screen.screens:
                if screen.name == "Battle":
                    on__screen.active_screen = screen
            for l in levels:
                if counter.number == l.number:
                    level_text = text(["Battle"], "Level " + str(l.number), (600,180), pg.font.Font(def_link, heading0_size), dark_colour)
                    text_class.texts_bundling()
                    
                    battle_info.get_info(l)
                    battle_info.make_player(player)
                    battle_info.start()
                                    
    def restart_battle(self, on__screen):
        text_class.texts.pop()
        if levels[counter.number - 1].unlocked == True:
            on__screen.battle = True
            for screen in on__screen.screens:
                if screen.name == "Battle":
                    on__screen.active_screen = screen
            for l in levels:
                if counter.number == l.number:
                    level_text = text(["Battle"], "Level " + str(l.number), (600,180), pg.font.Font(def_link, heading0_size), dark_colour)
                    text_class.texts_bundling()
                    
                    battle_info.get_info(l)
                    battle_info.make_player(player)
                    battle_info.start()
                    on__screen.active_table = "Close"
                
    def end_battle(self):
        on__screen.battle = False
        self.change_screen("Campaign", on__screen)
        text_class.texts.pop()
        
    def win_battle(self):
        # Update textů
        index_stat = text_class.texts.index(stat_point_value)
        text_class.texts[index_stat],update(str(player.stat_point))
        index_golds = text_class.texts.index(golds)
        text_class.texts[index_golds].update(str(player.gold), gold_level_position(1110,30,str(player.gold)))
        index_level = text_class.texts.index(p_level)
        text_class.texts[index_level].update(str(player.level), None)
        index_xp_name = text_class.texts.index(xp_name)
        text_class.texts[index_xp_name].update("LEVEL: " + str(player.level), None)
        index_xp_value = text_class.texts.index(xp_value)
        text_class.texts[index_xp_value].update("XP: " + str(player.xp) + " / " + str(player.xp_req), None)
        index_hp_p = text_class.texts.index(hp_p)
        text_class.texts[index_hp_p].update(": " + str(player.inventory["healing_potion"]), None)
        index_mana_p = text_class.texts.index(mana_p)
        text_class.texts[index_mana_p].update(": " + str(player.inventory["mana_potion"]), None)
        
        # Odemknutí dalšího levelu
        levels[counter.number].unlocked = True
        levels[counter.number - 1].completed = True
        counter.number += 1
        self.end_battle()
    
    def continue_battle(self):
        levels[counter.number].unlocked = True
        counter.number += 1
        self.restart_battle(on__screen)
                
    def save(self):
        file = open("saved_data.csv", "w", encoding = "UTF-8")
        file.write(player.role + ",")
        if not player.weapon == None:
            file.write(str(player.weapon.id) + ",")
        else:
            file.write("None,") 
        if not player.armor == None:
            file.write(str(player.armor.id) + ",")
        else:
            file.write("None,")
        file.write(str(player.gold) + ",")
        file.write(str(player.level) + ",")
        file.write(str(player.xp) + ",")
        file.write(str(player.xp_req) + ",")
        file.write(str(player.inventory["healing_potion"]) + "," + str(player.inventory["mana_potion"]) + ",")
        for l in list(reversed(levels)):
            if l.unlocked == False:
                pass
            elif l.unlocked == True:
                file.write(str(l.number) + ",")
                break
        file.write(str(player.hp_stat) + ",")
        file.write(str(player.mana_stat) + ",")
        file.write(str(player.int_stat) + ",")
        file.write(str(player.luck_stat) + ",")
        file.write(str(player.stat_point) + ",")
        # Vybrané skilly
        for s in player.equipped_skills:
            if s == None:
                file.write("None,")
            elif s == "None":
                file.write("None,")
            else:
                file.write(s.name + ",")
        # Odemčené skilly
        for skill in player.skills:
            file.write(skill.name + ",")
            
        if len(player.skills) < 7:
            missing = 7 - len(player.skills)
            for x in range(missing):
                file.write("None,")
        # Itemy
        for i_l in item_class.all_items:
            for i in i_l:
                if i.bought == True:
                    file.write("True,")
                elif i.bought == False:
                    file.write("False,")
        file.close()
        text_class.show_message("save")
        
    def load(self):
        
        file = open("saved_data.csv", "r", encoding = "UTF-8")
        data = file.readline()
        if data == "":
            pass
        else:
            d_l = data.split(",")
            player.role = d_l[0]
            init_items(player.role)
            item_class.item_bundling()
            shop_b_init()
            for w in item_class.weapons:
                if w.id == d_l[1]:
                    player.weapon = w
            for a in item_class.armors:
                if a.id == d_l[2]:
                    player.weapon = a
            player.gold = int(d_l[3])
            player.level = int(d_l[4])
            player.xp = int(d_l[5])
            player.xp_req = int(d_l[6])
            player.inventory = {"healing_potion":int(d_l[7]), "mana_potion":int(d_l[8])}
            for l in levels:
                if l.number <= int(d_l[9]):
                    l.unlocked = True
                    levels[l.number - 1].completed = True
            player.hp_stat = int(d_l[10])
            player.mana_stat = int(d_l[11])
            player.int_stat = int(d_l[12])
            player.luck_stat = int(d_l[13])
            player.stat_point = int(d_l[14])
            # Načtení vybavených skillů 15-17
            s = 15
            i = 0
            while s < 18:
                if d_l[s] == "None":
                    player.equipped_skills[i] = None
                    i += 1
                else:
                    for sk in skill_class.skills:
                        if d_l[s] == sk.name:
                            player.equipped_skills[i] = sk
                            i += 1
                s += 1
            # Načtení odemčených skillů 18-24
            player.skills = []
            sk = 18
            while sk < 25:
                if d_l[sk] == "None":
                    pass
                else:
                    for skl in skill_class.skills:
                        if d_l[sk] == skl.name:
                            player.skills.append(skl)
                sk += 1
            # Načtení itemů v obchodě
            x = 25
            for il in item_class.all_items:
                for i in il:
                    if d_l[x] == "False":
                        i.bought = False
                    elif d_l[x] == "True":
                        i.bought = True
                    x += 1
                
            # Update textů
            index_golds = text_class.texts.index(golds)
            text_class.texts[index_golds].update(str(player.gold), gold_level_position(1110,30,str(player.gold)))
            index_level = text_class.texts.index(p_level)
            text_class.texts[index_level].update(str(player.level), None)
            index_hp_p = text_class.texts.index(hp_p)
            text_class.texts[index_hp_p].update(str(player.inventory["healing_potion"]), None)
            index_mana_p = text_class.texts.index(mana_p)
            text_class.texts[index_mana_p].update(str(player.inventory["mana_potion"]), None)
            index_hp = text_class.texts.index(hp_stat_value)
            text_class.texts[index_hp].update(str(player.hp_stat + "/10"), None)
            index_mana = text_class.texts.index(mana_stat_value)
            text_class.texts[index_mana].update(str(player.mana_stat + "/10"), None)
            index_int = text_class.texts.index(int_stat_value)
            text_class.texts[index_int].update(str(player.int_stat + "/10"), None)
            index_luck = text_class.texts.index(luck_stat_value)
            text_class.texts[index_luck].update(str(player.luck_stat + "/10"), None)
            index_xp_name = text_class.texts.index(xp_name)
            text_class.texts[index_xp_name].update("LEVEL: " + str(player.level), None)
            index_xp_value = text_class.texts.index(xp_value)
            text_class.texts[index_xp_value].update("XP: " + str(player.xp) + " / " + str(player.xp_req), None)
            index_stat_point = text_class.texts.index(stat_point_value)
            text_class.texts[index_stat_point].update(str(player.stat_point),None)
               
            # Update seznamů čudlíků
            skill_1_b.tasks[0][2] = player.skills
            skill_2_b.tasks[0][2] = player.skills
            skill_3_b.tasks[0][2] = player.skills
            skill_4_b.tasks[0][2] = player.skills
            skill_5_b.tasks[0][2] = player.skills
            skill_6_b.tasks[0][2] = player.skills
            skill_7_b.tasks[0][2] = player.skills
                
            # Update textur čudlíků
            for b in button_class.buttons:
                if b.tasks[0][0] == "select_skill_slot":
                    if not player.equipped_skills[b.tasks[0][1] - 1] == None or not not player.equipped_skills[b.tasks[0][1] - 1] == "None":
                        b.get_texture(player.equipped_skills[b.tasks[0][1] - 1].icon)
                    else:
                        b.get_texture(None)
                if b.tasks[0][0] == "change_item" and b.tasks[0][2] == player.skills:
                    if len(player.skills) > b.tasks[0][1]:
                        b.get_texture(player.skills[b.tasks[0][1]].icon)
            
            self.change_screen("Game menu", on__screen)
        
    def delete_save(self):
        file = open("saved_data.csv", "w", encoding = "UTF-8")
        file.truncate()
        file.close()
        
    def item_test(self):
        if item.bought == False:
            pass
        elif item.bought == True:
            pass
           
    def reset_item_show(self):
        for item_type in item_class.all_items:
            for item in item_type:
                if item.shown == True:
                    item.shown = False
                    
    def buy_item(self):
        active_item = None
        multi_click_prevention = False
        for item_type in item_class.all_items:
            for item in item_type:
                if item.shown == True:
                    active_item = item
                    active_item_type = Button.item_type_check(active_item)
        if not active_item == None:
            if active_item.price <= player.gold and active_item.bought == False and active_item.level <= player.level and multi_click_prevention == False:
                active_item.bought = True
                player.gold = player.gold - active_item.price
                multi_click_prevention = True        
                if not active_item.id == "healing_potion" or active_item.id == "mana_potion" and player.inventory[active_item.id] < 99:
                    text_class.show_message("buy")
                
                ### MISC. ITEMY ####
                # Potiony #
                if active_item.id == "healing_potion" or active_item.id == "mana_potion":
                    if player.inventory[active_item.id] < 99:
                        player.inventory[active_item.id] += 1
                        active_item.bought = False
                        text_class.show_message("buy")
                        
                        index_hp_p = text_class.texts.index(hp_p)
                        text_class.texts[index_hp_p].update(": " + str(player.inventory["healing_potion"]), None)
                        index_mana_p = text_class.texts.index(mana_p)
                        text_class.texts[index_mana_p].update(": " + str(player.inventory["mana_potion"]), None)
        
                    if active_item_type == "misc_item" and player.inventory[active_item.id] >= 99:
                        text_class.show_message("no more")
                        player.gold += active_item.price
                        active_item.bought = False
                            
                # Skill scrolly #
                if active_item.id == "skill_1":
                    for i in skill_class.skills:
                        if i.name == "Poison Dart":
                            if not i in player.skills:
                                player.skills.append(i)
                                index = len(player.skills) - 1
                                button_class.skill_buttons[index].get_texture(i.icon)
                                text_class.show_message("buy")
                                multi_click_prevention = True
                                
                if active_item.id == "skill_2":
                    for i in skill_class.skills:
                        if i.name == "Lightning Bolt":
                            if not i in player.skills:
                                player.skills.append(i)
                                index = len(player.skills) - 1
                                button_class.skill_buttons[index].get_texture(i.icon)
                                text_class.show_message("buy")
                                multi_click_prevention = True
                                        
                if active_item.id == "skill_3":
                    for i in skill_class.skills:
                        if i.name == "Life Steal":
                            if not i in player.skills:
                                player.skills.append(i)
                                index = len(player.skills) - 1
                                button_class.skill_buttons[index].get_texture(i.icon)
                                text_class.show_message("buy")
                                multi_click_prevention = True
                    
                self.equip_item(False)
                
            if active_item.bought == True and multi_click_prevention == False:
                text_class.show_message("bought")
                multi_click_prevention = True
                
            if active_item.price > player.gold and multi_click_prevention == False:
                text_class.show_message("no golds")
                multi_click_prevention = True
            elif active_item.level > player.level and multi_click_prevention == False:
                text_class.show_message("no level")
                multi_click_prevention = True
                
            multi_click_prevention = False
        
        
    def item_type_check(active_item):
        if not active_item == None:
            if active_item.damage == None and active_item.armor == None:
                active_item_type = "misc_item"
                return active_item_type
                
            if active_item.armor == None and active_item.misc_stat == None:
                active_item_type = "weapon"
                return active_item_type
                
            if active_item.damage == None and active_item.misc_stat == None:
                active_item_type = "armor"
                return active_item_type
            
            else:
                return None
        else:
            return None
        
    def equip_item(self, show_message):
        multi_click_prevention = False
        active_item = None
        for item_type in item_class.all_items:
            for item in item_type:
                if item.shown == True:
                    active_item = item
                
        active_item_type = Button.item_type_check(active_item)
        
        if active_item_type == "weapon":
            if player.weapon is not active_item and active_item.bought and multi_click_prevention == False:
                player.weapon = active_item
                if show_message:
                    text_class.show_message("equip")
                multi_click_prevention = True
                    
            if player.weapon == active_item and active_item.bought and multi_click_prevention == False:
                player.weapon = None
                if show_message:
                    text_class.show_message("unequip")
                multi_click_prevention = True
                
            if active_item.bought == False and multi_click_prevention == False:
                if show_message:
                    text_class.show_message("no owner")
                multi_click_prevention = True
            
            multi_click_prevention = False
            
        if active_item_type == "armor":
            if player.armor is not active_item and active_item.bought and multi_click_prevention == False:
                player.armor = active_item
                if show_message:
                    text_class.show_message("equip")
                multi_click_prevention = True
                    
            if player.armor == active_item and active_item.bought and multi_click_prevention == False:
                player.armor = None
                if show_message:
                    text_class.show_message("unequip")
                multi_click_prevention = True
                
            if active_item.bought == False and multi_click_prevention == False:
                if show_message:
                    text_class.show_message("no owner")
                multi_click_prevention = True
            
            multi_click_prevention = False
            
        if active_item_type == "misc_item":
            if show_message:
                text_class.show_message("no equip")

    def select_skill_slot(self, slot_index):
        for button in button_class.buttons:
            if button.tasks[0][0] == "select_skill_slot":
                button.colour = (30,30,30,180)
        self.colour = (40,140,40,180)
        active_skill_slot = slot_index
        for button in button_class.buttons:
            if button.tasks[0][0] == "equip_skill":
                button.active_skill_slot = active_skill_slot

    def equip_skill(self):
        if not self.active_skill_slot == None:
            multi_click_prevention = False
            active_skill = None
            for skill in skill_class.skills:
                if skill.shown == True:
                    active_skill = skill
                
            if multi_click_prevention == False:
                for x, p_skill in enumerate(player.equipped_skills):
                    if p_skill == active_skill:
                        player.equipped_skills[x] = player.equipped_skills[self.active_skill_slot - 1]
                        
                player.equipped_skills[self.active_skill_slot - 1] = active_skill
                        
                for x, p_skill in enumerate(player.equipped_skills):
                    if p_skill == None:
                        for button in button_class.buttons:
                            if button.tasks[0][0] == "select_skill_slot" and button.tasks[0][1] == x + 1:
                                button.get_texture(None)
                            if button.tasks[0][0] == "activate_skill" and button.tasks[0][1] == x:
                                button.get_texture(None)
                    else:
                        for button in button_class.buttons:
                            if button.tasks[0][0] == "select_skill_slot" and button.tasks[0][1] == x + 1:
                                button.get_texture(p_skill.icon)
                            if button.tasks[0][0] == "activate_skill" and button.tasks[0][1] == x:
                                button.get_texture(p_skill.icon)
                        
                multi_click_prevention = True
            
            multi_click_prevention = False
            
    def change_stat(self, stat):
        multi_click_prevention = False
        if stat == "hp" and multi_click_prevention == False and player.stat_point > 0 and player.hp_stat < 10:
            player.max_hp += 40
            player.stat_point = player.stat_point - 1
            player.hp_stat += 1
            hp_stat_value.update(str(player.hp_stat) + "/10",None)
            stat_point_value.update(str(player.stat_point), None)
            multi_click_prevention = True
            
        if stat == "mana" and multi_click_prevention == False and player.stat_point > 0 and player.mana_stat < 10:
            player.max_mana += 20
            player.stat_point = player.stat_point - 1
            player.mana_stat += 1
            mana_stat_value.update(str(player.mana_stat) + "/10",None)
            stat_point_value.update(str(player.stat_point), None)
            multi_click_prevention = True
            
        if stat == "int" and multi_click_prevention == False and player.stat_point > 0 and player.int_stat < 10:
            player.stat_point = player.stat_point - 1
            player.int_stat += 1
            int_stat_value.update(str(player.int_stat) + "/10",None)
            stat_point_value.update(str(player.stat_point), None)
            multi_click_prevention = True
            
        if stat == "luck" and multi_click_prevention == False and player.stat_point > 0 and player.luck_stat < 10:
            player.stat_point = player.stat_point - 1
            player.luck_stat += 1
            luck_stat_value.update(str(player.luck_stat) + "/10",None)
            stat_point_value.update(str(player.stat_point), None)
            multi_click_prevention = True
            
        multi_click_prevention = False
            
    def activate_skill(self, index):
        if battle_info.awaiting_skill == None and not player.equipped_skills[index] == None:
            if player.equipped_skills[index].momental_cooldown == 0 and player.equipped_skills[index].mana_cost <= battle_info.player_mana_copy:
                battle_info.awaiting_skill = player.equipped_skills[index]
                self.draw = "c"
                self.offset = 5
            elif player.equipped_skills[index].momental_cooldown == 0 and not player.equipped_skills[index].mana_cost <= battle_info.player_mana_copy:
                text_class.show_message("no mana")
                
    def drink_potion(self, potion_type):
        if battle_info.awaiting_skill == None:
            if potion_type == "health" and player.inventory["healing_potion"] > 0:
                battle_info.awaiting_skill = drink_health_potion
                self.draw = "r"
            elif potion_type == "mana" and player.inventory["mana_potion"] > 0:
                battle_info.awaiting_skill = drink_mana_potion
                self.draw = "r"
        
class blit_object():
    def __init__(self, belonging, position, texture, scale, width, height, id_ = "basic"):
        on__screen.blit_objects.append(self)
        self.belonging = belonging
        self.texture = texture
        self.position = position
        if scale:
            self.texture = pg.transform.scale(texture, (width, height))
        self.show = True
        self.id = id_
        
    def blit_self(self, screen, on__screen):
        if self.show:
            if not on__screen.active_screen == "Exit":
                if not on__screen.active_table == "Close":
                    if on__screen.active_table.name in self.belonging:
                        screen.blit(self.texture, self.position)
                elif on__screen.active_screen.name in self.belonging:
                    screen.blit(self.texture, self.position)
        else:
            if on__screen.active_screen.name in self.belonging:
                self.check_active_item(screen)
            
    def check_active_item(self, screen):
        for it in item_class.all_items:
            for i in it:
                if (i.shown and not self.position == (330,700)) or (i.shown and not i.name in ["Vitriolic scroll", "Tempestous scroll", "Rancid scroll"] and not (i.name == "Healing potion" and self.id == "mq") and not (i.name == "Mana potion" and self.id == "hq")):
                    screen.blit(self.texture, self.position)
    
    def get_condition(self, condition):
        self.condition = condition
                
class bought_icon():
        def __init__(self, item, button):
            on__screen.bought_icons.append(self)
            self.item = item
            self.button = button
            self.scale = 18
            self.offset = 90
            self.texture = pg.transform.scale(pg.image.load(DATA_ROOT + "/data/textures/icons/completed_icon.png"), (self.scale,self.scale))
            self.texture_e = pg.transform.scale(pg.image.load(DATA_ROOT + "/data/textures/icons/euqipped_icon.png"), (self.scale,self.scale))
            
        def blit_self(self, screen, on_screen):
            if not on_screen.active_screen == "Exit":
                if self.item == None:
                    self.find_equiped(screen)
                elif self.item.belonging == on_screen.active_screen.name and self.item.bought:
                    screen.blit(self.texture, (self.button.position[0] + self.offset, self.button.position[1] + self.offset))
                    if self.item == player.weapon or self.item == player.armor:
                        screen.blit(self.texture_e, (self.button.position[0] + self.offset, self.button.position[1]))
                    elif self.item.id == player.weapon or self.item.id == player.armor:
                        screen.blit(self.texture_e, (self.button.position[0] + self.offset, self.button.position[1] - 10))
                 
class Xp_bar():
    def __init__(self, size_m, position):
        self.size_m = size_m
        self.size = (400 * size_m,25 * size_m)
        self.inner_size = 17 * size_m
        self.position = position
        self.inner_position = (position[0] + ((self.size[1] - self.inner_size) / 2), position[1] + ((self.size[1] - self.inner_size) / 2))
        self.difference = None
        
    def draw_bar(self, screen, xp, level, xp_req):
        xp_1_percent = xp_req / 100
        xp_percent = xp / xp_1_percent
        rect_width = (3.92 * self.size_m) * xp_percent
        pg.draw.rect(screen,(30,30,30),(self.position,self.size))
        pg.draw.rect(screen,(200,200,200),(self.inner_position, (rect_width, self.inner_size)))
        if not self.difference == None:
            pg.draw.rect(screen,(40,200,20),(self.inner_position, (rect_width, self.inner_size)))
            xp_percent = (xp - self.difference) / xp_1_percent
            rect2_width = (3.92 * self.size_m) * xp_percent
            pg.draw.rect(screen,(200,200,200),(self.inner_position, (rect2_width, self.inner_size)))
        
    def get_xp_difference(self, xp_difference):
        self.difference = xp_difference
        
xp_bar = Xp_bar(1, (160,250))
small_xp_bar = Xp_bar(3/4, (450, 400))

class Stat_bar():
    def __init__(self, bar_color):
        self.color = bar_color
        
    def draw_stat_bar(self, screen, stat, index):
        one_percent = 0.1
        percent = stat / one_percent
        pg.draw.rect(screen, (30,30,30), (780,(175 + (84 * index)),250,55))
        pg.draw.rect(screen, self.color, (784,(179 + (84 * index)),2.42*percent,47))
        
health_stat_bar = Stat_bar((240,17,17))
mana_stat_bar = Stat_bar((0,30,255))
int_stat_bar = Stat_bar((98,61,99))
luck_stat_bar = Stat_bar((90,156,81))
                 
def shop_b_init():
    weapon_textures = []
    armor_textures = []
    misc_item_textures = []
    for weapon in item_class.weapons:
        weapon_textures.append(weapon.texture)
    for armor in item_class.armors:
        armor_textures.append(armor.texture)
    for misc_item in item_class.misc_items:
        misc_item_textures.append(misc_item.texture)
       
    ### Tlačítka zbraní ###
    sw = Button(["Weapon board"], (840,70), None, 105,105, [["change_item", 0, item_class.weapons]], False, weapon_textures[0], True, None)
    bwsw = bought_icon(item_class.weapons[0], sw)
    w1t1 = Button(["Weapon board"], (685,200), None, 105,105, [["change_item", 1, item_class.weapons]], False, weapon_textures[1], True, None)
    bw11 = bought_icon(item_class.weapons[1], w1t1)
    w2t1 = Button(["Weapon board"], (685,330), None, 105,105, [["change_item", 2, item_class.weapons]], False, weapon_textures[2], True, None)
    bw21 = bought_icon(item_class.weapons[2], w2t1)
    w3t1 = Button(["Weapon board"], (685,460), None, 105,105, [["change_item", 3, item_class.weapons]], False, weapon_textures[3], True, None)
    bw31 = bought_icon(item_class.weapons[3], w3t1)
    w4t1 = Button(["Weapon board"], (685,590), None, 105,105, [["change_item", 4, item_class.weapons]], False, weapon_textures[4], True, None)
    bw41 = bought_icon(item_class.weapons[4], w4t1)
    w5t1 = Button(["Weapon board"], (685,720), None, 105,105, [["change_item", 5, item_class.weapons]], False, weapon_textures[5], True, None)
    bw51 = bought_icon(item_class.weapons[5], w5t1)

    w1t2 = Button(["Weapon board"], (840,200), None, 105,105, [["change_item", 6, item_class.weapons]], False, weapon_textures[6], True, None)
    bw12 = bought_icon(item_class.weapons[6], w1t2)
    w2t2 = Button(["Weapon board"], (840,330), None, 105,105, [["change_item", 7, item_class.weapons]], False, weapon_textures[7], True, None)
    bw22 = bought_icon(item_class.weapons[7], w2t2)
    w3t2 = Button(["Weapon board"], (840,460), None, 105,105, [["change_item", 8, item_class.weapons]], False, weapon_textures[8], True, None)
    bw32 = bought_icon(item_class.weapons[8], w3t2)
    w4t2 = Button(["Weapon board"], (840,590), None, 105,105, [["change_item", 9, item_class.weapons]], False, weapon_textures[9], True, None)
    bw42 = bought_icon(item_class.weapons[9], w4t2)
    w5t2 = Button(["Weapon board"], (840,720), None, 105,105, [["change_item", 10, item_class.weapons]], False, weapon_textures[10], True, None)
    bw52 = bought_icon(item_class.weapons[10], w5t2)
    
    w1t3 = Button(["Weapon board"], (995,200), None, 105,105, [["change_item", 11, item_class.weapons]], False, weapon_textures[11], True, None)
    bw13 = bought_icon(item_class.weapons[11], w1t3)
    w2t3 = Button(["Weapon board"], (995,330), None, 105,105, [["change_item", 12, item_class.weapons]], False, weapon_textures[12], True, None)
    bw23 = bought_icon(item_class.weapons[12], w2t3)
    w3t3 = Button(["Weapon board"], (995,460), None, 105,105, [["change_item", 13, item_class.weapons]], False, weapon_textures[13], True, None)
    bw33 = bought_icon(item_class.weapons[13], w3t3)
    w4t3 = Button(["Weapon board"], (995,590), None, 105,105, [["change_item", 14, item_class.weapons]], False, weapon_textures[14], True, None)
    bw43 = bought_icon(item_class.weapons[14], w4t3)
    w5t3 = Button(["Weapon board"], (995,720), None, 105,105, [["change_item", 15, item_class.weapons]], False, weapon_textures[15], True, None)
    bw53 = bought_icon(item_class.weapons[15], w5t3)
    
    
    ### Tlačítka brnění ###
    a1 = Button(["Armor board"], (840, 135), None, 105,105, [["change_item", 0, item_class.armors]], False, armor_textures[0], True, None)
    ba1 = bought_icon(item_class.armors[0], a1)
    a2 = Button(["Armor board"], (840, 265), None, 105,105, [["change_item", 1, item_class.armors]], False, armor_textures[1], True, None)
    ba2 = bought_icon(item_class.armors[1], a2)
    a3 = Button(["Armor board"], (840, 395), None, 105,105, [["change_item", 2, item_class.armors]], False, armor_textures[2], True, None)
    ba3 = bought_icon(item_class.armors[2], a3)
    a4 = Button(["Armor board"], (840, 525), None, 105,105, [["change_item", 3, item_class.armors]], False, armor_textures[3], True, None)
    ba4 = bought_icon(item_class.armors[3], a4)
    a5 = Button(["Armor board"], (840, 655), None, 105,105, [["change_item", 4, item_class.armors]], False, armor_textures[4], True, None)
    ba5 = bought_icon(item_class.armors[4], a5)
    
    #### Tlačítka misc itemů ###
    m1 = Button(["Item board"], (840, 135), None, 105,105, [["change_item", 0, item_class.misc_items]], False, misc_item_textures[0], True, None)
    m2 = Button(["Item board"], (840, 265), None, 105,105, [["change_item", 1, item_class.misc_items]], False, misc_item_textures[1], True, None)
    m3 = Button(["Item board"], (840, 395), None, 105,105, [["change_item", 2, item_class.misc_items]], False, misc_item_textures[2], True, None)
    m4 = Button(["Item board"], (840, 525), None, 105,105, [["change_item", 3, item_class.misc_items]], False, misc_item_textures[3], True, None)
    m5 = Button(["Item board"], (840, 655), None, 105,105, [["change_item", 4, item_class.misc_items]], False, misc_item_textures[4], True, None)
    
# Objekty na vykreslení
weapon_tree = blit_object(["Weapon board"], (0,0), pg.image.load(DATA_ROOT + "/data/textures/screens/shop/weapon_tree.png"), True, 1200, 900)
armour_tree = blit_object(["Armor board"], (0,0), pg.image.load(DATA_ROOT + "/data/textures/screens/shop/general_item_tree.png"), True, 1200, 900)
item_tree = blit_object(["Item board"], (0,0), pg.image.load(DATA_ROOT + "/data/textures/screens/shop/general_item_tree.png"), True, 1200, 900)
shopkeeper = blit_object(["Shop"], (505, 300), pg.image.load(DATA_ROOT + "/data/textures/characters/shopkeep.png"), True, 180, 504)
shop_foreground = blit_object(["Shop"], (0,0), pg.image.load(DATA_ROOT + "/data/textures/screens/shop/shop_foreground.png"), True, 1200, 900)
coin = blit_object(["Game menu", "Shop", "Profile", "Campaign", "Weapon board", "Armor board", "Item board"], (1125,30), pg.image.load(DATA_ROOT + "/data/textures/icons/money_icon.png"), True, 54, 54)
level = blit_object(["Game menu", "Shop", "Profile", "Campaign", "Weapon board", "Armor board", "Item board"], (1125,85), pg.image.load(DATA_ROOT + "/data/textures/icons/player_level_icon.png"), True, 54, 54)
player_profile = blit_object(["Profile"], (270,320), pg.image.load(DATA_ROOT + "/data/textures/characters/player/player.png"), True, 180, 504)
shop_price = blit_object(["Weapon board", "Armor board", "Item board"], (60, 640), pg.image.load(DATA_ROOT + "/data/textures/icons/money_icon.png"), True, 54, 54)
shop_level = blit_object(["Weapon board", "Armor board", "Item board"], (60, 700), pg.image.load(DATA_ROOT + "/data/textures/icons/player_level_icon.png"), True, 54, 54)
shop_damage = blit_object(["Weapon board"], (330,670), pg.image.load(DATA_ROOT + "/data/textures/icons/damage_icon_2.png"), True, 54, 54)
shop_armor = blit_object(["Armor board"], (330,670), pg.image.load(DATA_ROOT + "/data/textures/icons/defense_icon.png"), True, 54, 54)
shop_potion_effect = blit_object(["Item board"], (330,640), pg.image.load(DATA_ROOT + "/data/textures/icons/item_effect_icon.png"), True, 54, 54)
shop_potion_quantity_hp = blit_object(["Item board"], (330,700), pg.image.load(DATA_ROOT + "/data/textures/items/healing_potion.png"), True, 54, 54, "hq")
shop_potion_quantity_mana = blit_object(["Item board"], (330,700), pg.image.load(DATA_ROOT + "/data/textures/items/mana_potion.png"), True, 54, 54, "mq")
campaign_potions_hp = blit_object(["Campaign"], (75, 760), pg.image.load(DATA_ROOT + "/data/textures/items/healing_potion.png"), True, 48, 48)
campaign_potions_mana = blit_object(["Campaign"], (75, 810), pg.image.load(DATA_ROOT + "/data/textures/items/mana_potion.png"), True, 48, 48)
health_stat = blit_object(["Profile"], (700,170), pg.image.load(DATA_ROOT + "/data/textures/icons/stats/health_icon.png"), True, 64,64)
mana_stat = blit_object(["Profile"], (700,254), pg.image.load(DATA_ROOT + "/data/textures/icons/stats/mana_icon.png"), True, 64,64)
intelligence_stat = blit_object(["Profile"], (700,338), pg.image.load(DATA_ROOT + "/data/textures/icons/stats/intelligence_icon.png"), True, 64,64)
luck_stat = blit_object(["Profile"], (700,422), pg.image.load(DATA_ROOT + "/data/textures/icons/stats/luck_icon.png"), True, 64,64)
stat_point_icon = blit_object(["Profile"], (800,506), pg.image.load(DATA_ROOT + "/data/textures/icons/stats/stat_point_icon.png"), True, 64,64)
shop_price.show = False
shop_level.show = False
shop_damage.show = False
shop_armor.show = False
shop_potion_effect.show = False
shop_potion_quantity_hp.show = False
shop_potion_quantity_mana.show = False

# Tlačítka pro změnu obrazovky
exit_b = Button(["Main menu"], (806,726), None, 187, 92, [["change_screen", "Exit"]], False, None, False, None)
continue_b = Button(["Main menu"], (733, 431), None, 334, 88, [["load"]], False, None, False, None)
warrior_class_b = Button(["New game table"], (230, 400), None, 180, 220, [["change_role", "warrior"], ["change_screen", "Game menu"], ["create_items"], ["delete_save"]], False, pg.image.load(DATA_ROOT + "/data/textures/icons/warrior_class_icon.png"), True, None)
ranger_class_b = Button(["New game table"], (510, 400), None, 180, 220, [["change_role", "ranger"], ["change_screen", "Game menu"], ["create_items"], ["delete_save"]], False, pg.image.load(DATA_ROOT + "/data/textures/icons/ranger_class_icon.png"), True, None)
mage_class_b = Button(["New game table"], (790, 400), None, 180, 220, [["change_role", "mage"], ["change_screen", "Game menu"], ["create_items"], ["delete_save"]], False, pg.image.load(DATA_ROOT + "/data/textures/icons/mage_class_icon.png"), True, None)

shop_b = Button(["Game menu"], (940, 550), (30,30,30,180), 100, 100, [["change_screen", "Shop"]], "c", pg.image.load(DATA_ROOT + "/data/textures/icons/shop_icon.png"), True, None)
profile_b = Button(["Game menu"], (95,550), (30,30,30,180), 100, 100, [["change_screen", "Profile"]], "c", pg.image.load(DATA_ROOT + "/data/textures/icons/profile_icon.png"), True, None)
campaign_b = Button(["Game menu"], (550,400), (30,30,30,180), 100, 100, [["change_screen", "Campaign"]], "c", pg.image.load(DATA_ROOT + "/data/textures/icons/campaign_icon.png"), True, None)
game_menu_b = Button(["Shop", "Profile", "Campaign"], (30,30), (30,30,30,180), 64, 64, [["change_screen", "Game menu"]], "c", pg.image.load(DATA_ROOT + "/data/textures/icons/back_icon.png"), False, None)

battle_pause_b = Button(["Battle"], (100,30), (30,30,30,180), 64, 64, [["change_table", "Pause table"],["pause_battle"]], "c", pg.image.load(DATA_ROOT + "/data/textures/icons/back_icon.png"), False, None)
leave_battle_b = Button(["Pause table", "Death table"], (320,500), (30,30,30,180), 260, 85, [["end_battle"]], "r", None, False, None)
stay_battle_b = Button(["Pause table"], (620, 500), (30,30,30,180), 260, 85, [["change_table", "Close"],["unpause_battle"]], "r", None, False, None)
retry_battle_b = Button(["Death table"], (620, 500), (30,30,30,180), 260, 85, [["restart_battle"]], "r", None, False, None)
completed_battle_b = Button(["Win table"], (320,680), (30,30,30,180), 260, 85, [["win_battle"]], "r", None, False, None)
continue_battle_b = Button(["Win table"], (620,680), (30,30,30,180), 260, 85, [["continue_battle"]], "r", None, False, None)

shop_back_b = Button(["Weapon board", "Armor board", "Item board"], (30,30), (30,30,30,180), 64, 64, [["change_screen", "Shop"]], "c", pg.image.load(DATA_ROOT + "/data/textures/icons/back_icon.png"), False, None)
weapon_board_b = Button(["Shop"], (731,245), (255,0,0), 221, 267, [["change_screen", "Weapon board"],["reset_item_show"]], False, None, False, None)
armor_board_b = Button(["Shop"], (239,240), (255,0,0), 232, 126, [["change_screen", "Armor board"],["reset_item_show"]], False, None, False, None)
item_board_b = Button(["Shop"], (248,395), (255,0,0), 224, 105, [["change_screen", "Item board"],["reset_item_show"]], False, None, False, None)
buy_b = Button(["Weapon board", "Armor board", "Item board"], (50,760), (30,30,30,100), 225, 100, [["buy_item"]], "r", None, False, None)
equip_b = Button(["Weapon board", "Armor board", "Item board"], (325,760), (30,30,30,100), 225, 100, [["equip_item"]], "r", None, False, None)

save_b = Button(["Game table"], (450, 360), (30,30,30,180), 300, 80, [["save"]], "r", None, False, None)
exit_b2 = Button(["Game table"], (450, 460), (30,30,30,180), 300, 80, [["change_screen", "Exit"]], "r", None, False, None)
save_and_exit = Button(["Game table"], (450, 560), (30,30,30,180), 300, 80, [["save"], ["change_screen", "Exit"]], "r", None, False, None)

higher_level_b = Button(["Campaign"], (670,775), (30,30,30,180), 72, 72, [["change_level", "up"]], False, None, False, None)
lower_level_b = Button(["Campaign"], (460,775), (30,30,30,180), 72, 72, [["change_level", "down"]], False, None, False, None)
fight_b = Button(["Campaign"], (900, 760), (30,30,30,180), 200, 100, [["start_battle"]], "r", None, False, None)

battle_skill_1_b = Button(["Battle"], (708, 788), (30,30,30,180), 82, 82, [["activate_skill", 0]], False, player.equipped_skills[0].icon, True, None)
battle_skill_2_b = Button(["Battle"], (796, 788), (30,30,30,180), 82, 82, [["activate_skill", 1]], False, None, True, None)
battle_skill_3_b = Button(["Battle"], (884, 788), (30,30,30,180), 82, 82, [["activate_skill", 2]], False, None, True, None)
battle_health_potion = Button(["Battle"], (984, 752), (30,30,30,180), 68, 112, [["drink_potion", "mana"]], False, None, True, None)
battle_health_potion = Button(["Battle"], (1064, 752), (30,30,30,180), 68, 112, [["drink_potion", "health"]], False, None, True, None)
skill_board_b = Button(["Profile"], (820, 680), (30,30,30,180), 160,160, [["change_screen", "Skill board"]], "c", pg.image.load(DATA_ROOT + "/data/textures/screens/profile/skill_board_icon.png"), True, None)
to_profile = Button(["Skill board","Debuff board","Stat board"], (30,30), (30,30,30,180), 64, 64, [["change_screen", "Profile"]], "c", pg.image.load(DATA_ROOT + "/data/textures/icons/back_icon.png"), True, None)
skill_to_debuff = Button(["Skill board"], (895, 725), (30,30,30,180), 225,100, [["change_screen", "Debuff board"]], "r", None, True, None)
debuff_to_skill = Button(["Debuff board"], (895, 725), (30,30,30,180), 225,100, [["change_screen", "Skill board"]], "r", None, True, None)

skill_slot_1 = Button(["Skill board"], (468, 750), (30,30,30,180), 64,64, [["select_skill_slot", 1]], "c", pg.image.load(DATA_ROOT + "/data/textures/icons/skills/fireball.png"), True, None)
skill_slot_2 = Button(["Skill board"], (568, 750), (30,30,30,180), 64,64, [["select_skill_slot", 2]], "c", None, True, None)
skill_slot_3 = Button(["Skill board"], (668, 750), (30,30,30,180), 64,64, [["select_skill_slot", 3]], "c", None, True, None)

equip_skill = Button(["Skill board"], (80, 725), (30,30,30,180), 225,100, [["equip_skill"]], "r", None, True, None)

skill_1_b = Button(["Skill board"], (130,120), (30,30,30,180), 100, 100, [["change_item", 0, player.skills]], "c", pg.image.load(DATA_ROOT + "/data/textures/icons/skills/fireball.png"), True, None)
skill_2_b = Button(["Skill board"], (270,120), (30,30,30,180), 100, 100, [["change_item", 1, player.skills]], "c", pg.image.load(DATA_ROOT + "/data/textures/icons/lock.png"), True, None)
skill_3_b = Button(["Skill board"], (410,120), (30,30,30,180), 100, 100, [["change_item", 2, player.skills]], "c", pg.image.load(DATA_ROOT + "/data/textures/icons/lock.png"), True, None)
skill_4_b = Button(["Skill board"], (550,120), (30,30,30,180), 100, 100, [["change_item", 3, player.skills]], "c", pg.image.load(DATA_ROOT + "/data/textures/icons/lock.png"), True, None)
skill_5_b = Button(["Skill board"], (690,120), (30,30,30,180), 100, 100, [["change_item", 4, player.skills]], "c", pg.image.load(DATA_ROOT + "/data/textures/icons/lock.png"), True, None)
skill_6_b = Button(["Skill board"], (830,120), (30,30,30,180), 100, 100, [["change_item", 5, player.skills]], "c", pg.image.load(DATA_ROOT + "/data/textures/icons/lock.png"), True, None)
skill_7_b = Button(["Skill board"], (970,120), (30,30,30,180), 100, 100, [["change_item", 6, player.skills]], "c", pg.image.load(DATA_ROOT + "/data/textures/icons/lock.png"), True, None)

hp_stat_b = Button(["Profile"], (1036,170), (30,30,30,180), 64, 64, [["change_stat", "hp"]], False, pg.image.load(DATA_ROOT + "/data/textures/icons/stats/plus_icon.png"), True, None)
mana_stat_b = Button(["Profile"], (1036,254), (30,30,30,180), 64, 64, [["change_stat", "mana"]], False, pg.image.load(DATA_ROOT + "/data/textures/icons/stats/plus_icon.png"), True, None)
int_stat_b = Button(["Profile"], (1036,338), (30,30,30,180), 64, 64, [["change_stat", "int"]], False, pg.image.load(DATA_ROOT + "/data/textures/icons/stats/plus_icon.png"), True, None)
luck_stat_b = Button(["Profile"], (1036,422), (30,30,30,180), 64, 64, [["change_stat", "luck"]], False, pg.image.load(DATA_ROOT + "/data/textures/icons/stats/plus_icon.png"), True, None)

# Tlačítka tabulek
new_game_b = Button(["Main menu"], (707,283), None, 388, 88, [["change_table", "New game table"]], False, None, False, None)
credits_b = Button(["Main menu"], (765,573), None, 270,94, [["change_table", "Credits table"]], False, None, False, None)
game_b = Button(["Game menu"], (30,30), (30,30,30,180), 64, 64, [["change_table", "Game table"]], "c", pg.image.load(DATA_ROOT+ "/data/textures/icons/menu_icon.png"), True, None)

close_b = Button(["New game table", "Settings table", "Credits table", "Game table"], (1000,125), None, 64, 64, [["change_table", "Close"]], False, pg.image.load(DATA_ROOT + "/data/textures/icons/close_icon.png"), False, None)

# Obrazovky
main_menu = screen("Main menu", pg.image.load(DATA_ROOT + "/data/textures/screens/main_menu_2.png"))
game_menu = screen("Game menu", pg.image.load(DATA_ROOT + "/data/textures/screens/game_menu.png"))
shop = screen("Shop", pg.image.load(DATA_ROOT + "/data/textures/screens/shop/shop.png"))
profile = screen("Profile", pg.image.load(DATA_ROOT + "/data/textures/screens/profile/profile.png"))
campaign = screen("Campaign", pg.image.load(DATA_ROOT + "/data/textures/screens/campaign/campaign.png"))
battle = screen("Battle", pg.image.load(DATA_ROOT + "/data/textures/screens/campaign/campaign_battle.png"), pg.image.load(DATA_ROOT + "/data/textures/screens/campaign/campaign_battle_bg.png"))

# Podobrazovky profilu
skill_board = screen("Skill board",pg.image.load(DATA_ROOT + "/data/textures/screens/profile/skill_board.png"))
debuff_board = screen("Debuff board",pg.image.load(DATA_ROOT + "/data/textures/screens/profile/skill_board.png"))

# Podobrazovky obchodu
weapon_board = screen("Weapon board",pg.image.load(DATA_ROOT + "/data/textures/screens/shop/shop_board.png"))
armor_board = screen("Armor board",pg.image.load(DATA_ROOT + "/data/textures/screens/shop/shop_board.png"))
item_board = screen("Item board",pg.image.load(DATA_ROOT + "/data/textures/screens/shop/shop_board.png"))

# Tabulky
new_game_table = table("New game table")
settings_table = table("Settings table")
credits_table = table("Credits table")
game_table = table("Game table")
pause_table = table("Pause table")
death_table = table("Death table")
win_table = table("Win table")
pause_table.change_format([275,275],[650,350])        