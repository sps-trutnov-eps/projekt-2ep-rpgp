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
        
button_class = button_cl()

class screen():
    def __init__(self, name, background):
        on__screen.screens.append(self)
        self.name = name
        self.background = pg.transform.scale(background, (1200,900))
        buttons = button_class.buttons
        self.buttons = []
        for button in buttons:
            for place in button.belonging:
                if place == self.name:
                    self.buttons.append(button)
                    
### ZAHOZENO ###
class tooltip():
    def __init_(self, area, mouse_pos, table_name, table_description, table_width, table_height, screen):
        # area = (x,y,width,height)
        
        pg.font.init()
        
        name_size = 20
        desc_size = 10
        t_width = 0
        t_height = 0
                
        for char in table_name:
            t_width += name_size
            
        for char in table_description:
            pass
            
        name_font = pg.font.Font(DATA_ROOT + "/data/fonts/VeniceClassic.ttf", name_size)
        desc_font = pg.font.Font(DATA_ROOT + "/data/fonts/VeniceClassic.ttf", desc_size)
        name = name_font.render(table_name, False, (255,255,255))
        desc = desc_font.render(table_description, False, (200,200,200))
        name_rect = name.get_rect()
        desc_rect = desc.get_rect()
        
        screen.blit(name,(0,0))
        screen.blit(desc,(0,30))
        
        print(name_rect.get_height())
        print(desc_rect.get_height())
        
        tooltip_table = pg.Surface()
        if mouse_pos[0] >= area[0] and mouse_pos[0] <= (area[0] + area[2]):
            if mouse_pos[1] >= area[1] and mouse_pos[1] <= (area[1] + area[3]):
                pass

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
        self.belonging = belonging
        self.position = position
        self.width = width
        self.height = height
        self.tasks = tasks
        self.colour = colour
        self.alpha = 180
        self.draw = draw
        self.active_skill_slot = None
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
                            offset = self.width/3
                            backgr_size = self.width + offset
                            button_sf = pg.Surface((backgr_size, backgr_size), pg.SRCALPHA)
                            pg.draw.circle(button_sf, self.colour, ((backgr_size/2),(backgr_size/2)), backgr_size/2)
                            screen.blit(button_sf, ((self.position[0] - offset/2),(self.position[1] - offset/2)))
                        elif self.draw == "r":
                            button_sf = pg.Surface((self.width, self.height), pg.SRCALPHA)
                            button_sf.fill(self.colour)
                            screen.blit(button_sf, (self.position[0], self.position[1]))
                    if self.texture == None:
                        pass
                    else:
                        screen.blit(self.texture, (self.position))
            elif on__screen.active_screen.name in self.belonging:
                if not self.draw == False:
                    if self.draw == "c":
                        offset = self.width/3
                        backgr_size = self.width + offset
                        button_sf = pg.Surface((backgr_size, backgr_size), pg.SRCALPHA)
                        pg.draw.circle(button_sf, self.colour, ((backgr_size/2),(backgr_size/2)), backgr_size/2)
                        screen.blit(button_sf, ((self.position[0] - offset/2),(self.position[1] - offset/2)))
                    elif self.draw == "r":
                        button_sf = pg.Surface((self.width, self.height), pg.SRCALPHA)
                        button_sf.fill(self.colour)
                        screen.blit(button_sf, (self.position[0], self.position[1]))
                if self.texture == None:
                    pass
                else:
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
                    level_text = text(["Battle"], "Level " + str(l.number), (600,180), pg.font.Font(def_link, heading0_size), def_colour)
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
                    level_text = text(["Battle"], "Level " + str(l.number), (600,180), pg.font.Font(def_link, heading0_size), def_colour)
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
        levels[counter.number].unlocked = True
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
        file.write(str(player.inventory["healing_potion"]) + "," + str(player.inventory["mana_potion"]) + ",")
        for l in list(reversed(levels)):
            if l.unlocked == False:
                pass
            elif l.unlocked == True:
                file.write(str(l.number) + ",")
                break
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
            player.inventory = {"healing_potion":int(d_l[5]), "mana_potion":int(d_l[6])}
            for l in levels:
                if l.number <= int(d_l[7]):
                    l.unlocked = True
                    levels[l.number - 1].completed = True
                    
            x = 8
            for il in item_class.all_items:
                for i in il:
                    if d_l[x] == "False":
                        i.bought = False
                    elif d_l[x] == "True":
                        i.bought = True
                    x += 1
                
            index_golds = text_class.texts.index(golds)
            text_class.texts[index_golds].update(str(player.gold), gold_level_position(1110,30,str(player.gold)))
            index_level = text_class.texts.index(p_level)
            text_class.texts[index_level].update(str(player.level), None)
            
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
            if active_item.price <= player.gold and active_item.bought == False and multi_click_prevention == False:
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
                        print(player.inventory[active_item.id])
                    if active_item_type == "misc_item" and player.inventory[active_item.id] >= 99:
                        text_class.show_message("no more")
                        player.gold += active_item.price
                        active_item.bought = False
                            
                # Skill scrolly #
                if active_item.id == "skill_scroll_1" or active_item.id == "skill_scroll_2" or active_item.id == "skill_scroll_3":
                    player.skills[active_item.id] = True
                    
                self.equip_item(False)
                
            if active_item.bought == True and multi_click_prevention == False:
                text_class.show_message("bought")
                multi_click_prevention = True
                
            if active_item.price > player.gold and multi_click_prevention == False:
                text_class.show_message("no golds")
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
                    else:
                        for button in button_class.buttons:
                            if button.tasks[0][0] == "select_skill_slot" and button.tasks[0][1] == x + 1:
                                button.get_texture(p_skill.icon)
                        
                multi_click_prevention = True
            
            multi_click_prevention = False
            print_list = []
            for p_skill in player.equipped_skills:
                if p_skill == None:
                    print_list.append("None")
                else:
                    print_list.append(p_skill.name)
            print(print_list)
        
class blit_object():
    def __init__(self, belonging, position, texture, scale, width, height):
        on__screen.blit_objects.append(self)
        self.belonging = belonging
        self.texture = texture
        self.position = position
        if scale:
            self.texture = pg.transform.scale(texture, (width, height))
        self.show = True
        
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
                if i.shown:
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
            if self.item == None:
                self.find_equiped(screen)
            elif self.item.belonging == on_screen.active_screen.name and self.item.bought:
                screen.blit(self.texture, (self.button.position[0] + self.offset, self.button.position[1] + self.offset))
                if self.item == player.weapon or self.item == player.armor:
                    screen.blit(self.texture_e, (self.button.position[0] + self.offset, self.button.position[1]))
                elif self.item.id == player.weapon or self.item.id == player.armor:
                    screen.blit(self.texture_e, (self.button.position[0] + self.offset, self.button.position[1] - 10))
                    
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
player_profile = blit_object(["Profile"], (270,320), pg.image.load(DATA_ROOT + "/data/textures/characters/player/player_template.png"), True, 180, 504)
shop_price = blit_object(["Weapon board", "Armor board", "Item board"], (60, 640), pg.image.load(DATA_ROOT + "/data/textures/icons/money_icon.png"), True, 54, 54)
shop_level = blit_object(["Weapon board", "Armor board", "Item board"], (60, 700), pg.image.load(DATA_ROOT + "/data/textures/icons/player_level_icon.png"), True, 54, 54)
shop_damage = blit_object(["Weapon board"], (330,670), pg.image.load(DATA_ROOT + "/data/textures/icons/damage_icon_2.png"), True, 54, 54)
shop_armor = blit_object(["Armor board"], (330,670), pg.image.load(DATA_ROOT + "/data/textures/icons/defense_icon.png"), True, 54, 54)
shop_potion = blit_object(["Item board"], (330,670), pg.image.load(DATA_ROOT + "/data/textures/icons/potion_effect_icon.png"), True, 54, 54)
shop_price.show = False
shop_level.show = False
shop_damage.show = False
shop_armor.show = False
shop_potion.show = False

# Tlačítka pro změnu obrazovky
exit_b = Button(["Main menu"], (490,760), None, 215, 85, [["change_screen", "Exit"]], False, None, False, None)
continue_b = Button(["Main menu"], (680, 485), None, 445, 85, [["load"]], False, None, False, None)
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
completed_battle_b = Button(["Win table"], (320,500), (30,30,30,180), 260, 85, [["win_battle"]], "r", None, False, None)
continue_battle_b = Button(["Win table"], (620,500), (30,30,30,180), 260, 85, [["continue_battle"]], "r", None, False, None)

shop_back_b = Button(["Weapon board", "Armor board", "Item board"], (30,30), (30,30,30,180), 64, 64, [["change_screen", "Shop"]], "c", pg.image.load(DATA_ROOT + "/data/textures/icons/back_icon.png"), False, None)
weapon_board_b = Button(["Shop"], (731,245), (255,0,0), 221, 267, [["change_screen", "Weapon board"],["reset_item_show"]], False, None, False, None)
armor_board_b = Button(["Shop"], (239,240), (255,0,0), 232, 126, [["change_screen", "Armor board"],["reset_item_show"]], False, None, False, None)
item_board_b = Button(["Shop"], (248,395), (255,0,0), 224, 105, [["change_screen", "Item board"],["reset_item_show"]], False, None, False, None)
buy_b = Button(["Weapon board", "Armor board", "Item board"], (50,760), (30,30,30,100), 225, 100, [["buy_item"]], "r", None, False, None)
equip_b = Button(["Weapon board", "Armor board", "Item board"], (325,760), (30,30,30,100), 225, 100, [["equip_item"]], "r", None, False, None)

save_b = Button(["Game table"], (520, 460), (30,30,30,180), 165, 80, [["save"]], "r", None, False, None)

higher_level_b = Button(["Campaign"], (670,775), (30,30,30,180), 72, 72, [["change_level", "up"]], False, None, False, None)
lower_level_b = Button(["Campaign"], (460,775), (30,30,30,180), 72, 72, [["change_level", "down"]], False, None, False, None)
fight_b = Button(["Campaign"], (1000, 760), (30,30,30,180), 100, 100, [["start_battle"]], "r", None, False, None)

skill_board_b = Button(["Profile"], (760, 345), (30,30,30,180), 160,160, [["change_screen", "Skill board"]], "c", pg.image.load(DATA_ROOT + "/data/textures/screens/profile/skill_board_icon.png"), True, None)
skill_debuff_board_back = Button(["Skill board","Debuff board"], (30,30), (30,30,30,180), 64, 64, [["change_screen", "Profile"]], "c", pg.image.load(DATA_ROOT + "/data/textures/icons/back_icon.png"), True, None)
skill_to_debuff = Button(["Skill board"], (895, 725), (30,30,30,180), 225,100, [["change_screen", "Debuff board"]], "r", None, True, None) #Button(["Skill board"], (1050,750),(30,30,30,180),64,64, [["change_screen", "Debuff board"]], "c", None, True, None)
debuff_to_skill = Button(["Debuff board"], (895, 725), (30,30,30,180), 225,100, [["change_screen", "Skill board"]], "r", None, True, None) #Button(["Debuff board"], (1050, 750), (30,30,30,180), 64,64, [["change_screen", "Skill board"]], "c", None, True, None)

skill_slot_1 = Button(["Skill board"], (468, 750), (30,30,30,180), 64,64, [["select_skill_slot", 1]], "c", pg.image.load(DATA_ROOT + "/data/textures/icons/skills/fireball.png"), True, None)
skill_slot_2 = Button(["Skill board"], (568, 750), (30,30,30,180), 64,64, [["select_skill_slot", 2]], "c", None, True, None)
skill_slot_3 = Button(["Skill board"], (668, 750), (30,30,30,180), 64,64, [["select_skill_slot", 3]], "c", None, True, None)

equip_skill = Button(["Skill board"], (80, 725), (30,30,30,180), 225,100, [["equip_skill"]], "r", None, True, None)

skill_1_b = Button(["Skill board"], (130,120), (30,30,30,180), 100, 100, [["change_item", 0, skill_class.skills]], "c", pg.image.load(DATA_ROOT + "/data/textures/icons/skills/fireball.png"), True, None)
skill_2_b = Button(["Skill board"], (270,120), (30,30,30,180), 100, 100, [["change_item", 1, skill_class.skills]], "c", pg.image.load(DATA_ROOT + "/data/textures/icons/skills/water_blast.png"), True, None)
skill_3_b = Button(["Skill board"], (410,120), (30,30,30,180), 100, 100, [["change_item", 2, skill_class.skills]], "c", pg.image.load(DATA_ROOT + "/data/textures/icons/skills/rock_throw.png"), True, None)
skill_4_b = Button(["Skill board"], (550,120), (30,30,30,180), 100, 100, [["change_item", 3, skill_class.skills]], "c", pg.image.load(DATA_ROOT + "/data/textures/icons/skills/ice_storm.png"), True, None)
skill_5_b = Button(["Skill board"], (690,120), (30,30,30,180), 100, 100, [["change_item", 4, skill_class.skills]], "c", pg.image.load(DATA_ROOT + "/data/textures/icons/skills/poison_dart.png"), True, None)
skill_6_b = Button(["Skill board"], (830,120), (30,30,30,180), 100, 100, [["change_item", 5, skill_class.skills]], "c", pg.image.load(DATA_ROOT + "/data/textures/icons/skills/lightning_bolt.png"), True, None)
skill_7_b = Button(["Skill board"], (970,120), (30,30,30,180), 100, 100, [["change_item", 6, skill_class.skills]], "c", pg.image.load(DATA_ROOT + "/data/textures/icons/skills/life_steal.png"), True, None)

# Tlačítka tabulek
new_game_b = Button(["Main menu"], (75,485), None, 445, 85, [["change_table", "New game table"]], False, None, False, None)
settings_b = Button(["Main menu"], (75,625), None, 445,85, [["change_table", "Settings table"]], False, None, False, None)
credits_b = Button(["Main menu"], (680,625), None, 445,85, [["change_table", "Credits table"]], False, None, False, None)
game_b = Button(["Game menu"], (30,30), (30,30,30,180), 64, 64, [["change_table", "Game table"]], False, pg.image.load(DATA_ROOT+ "/data/textures/icons/menu_icon.png"), True, None)

close_b = Button(["New game table", "Settings table", "Credits table", "Game table"], (1000,125), None, 64, 64, [["change_table", "Close"]], False, pg.image.load(DATA_ROOT + "/data/textures/icons/close_icon.png"), False, None)

# Obrazovky
main_menu = screen("Main menu", pg.image.load(DATA_ROOT + "/data/textures/screens/main_menu.png"))
game_menu = screen("Game menu", pg.image.load(DATA_ROOT + "/data/textures/screens/game_menu.png"))
shop = screen("Shop", pg.image.load(DATA_ROOT + "/data/textures/screens/shop.png"))
profile = screen("Profile", pg.image.load(DATA_ROOT + "/data/textures/screens/profile.png"))
campaign = screen("Campaign", pg.image.load(DATA_ROOT + "/data/textures/screens/campaign.png"))
battle = screen("Battle", pg.image.load(DATA_ROOT + "/data/textures/screens/campaign/campaign_battle.png"))

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
