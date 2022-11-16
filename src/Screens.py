import sys
import pygame as pg
from text import *
from data import *
from items import *
from campaign import *

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'

class on_screen():
    def __init__(self):
        self.screens = []
        self.tables = []
        self.blit_objects = []
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
            
    def check(self, m_pressed, on__screen):
        if not on__screen.active_screen == "Exit":
            if not on__screen.active_table == "Close":
                if on__screen.active_table.name in self.belonging:
                    if self.position[0] < pg.mouse.get_pos()[0] < (self.position[0] + self.width) and self.position[1] < pg.mouse.get_pos()[1] < (self.position[1] + self.height) and m_pressed[0] and self.condition:
                        on__screen.button_activity = False
                        self.work()
            elif on__screen.active_screen.name in self.belonging:
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
            if task[0] == "save":
                self.save()
            if task[0] == "buy_item":
                text_class.hide_messages()
                self.buy_item()
                index = text_class.texts.index(golds)
                text_class.texts[index].update(str(player.gold), gold_level_position(1110,30,str(player.gold)))
            if task[0] == "equip_item":
                text_class.hide_messages()
                self.equip_item()
                
            if task [0] == "reset_item_show":
                self.reset_item_show()
        
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
    
    def start_battle(self, on_screen):
        on_screen.battle = True
        index = on_screen.screens.index(battle)
        on_screen.active_screen = on_screen.screens[index]
        for l in levels:
            if counter.number == l.number:
                level_text = text(["Battle"], "Level " + str(l.number), (600,180), pg.font.Font(def_link, heading0_size), def_colour)
                text_class.texts.append(level_text)
                text_class.texts_bundling()
                
    def save(self):
        file = open("saved_data.csv", "w", encoding = "UTF-8")
        file.write(player.role + ",")
        if not player.weapon == None:
            file.write(str(player.weapon.id) + ",")
        else:
            file.write("None,")
        file.write(str(player.gold) + ",")
        file.write(str(player.level))
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
        
        if active_item.price <= player.gold and active_item.bought == False and multi_click_prevention == False:
            active_item.bought = True
            player.gold = player.gold - active_item.price
            multi_click_prevention = True        
            if not active_item.id == "healing_potion" or active_item.id == "mana_potion" and player.inventory[active_item.id] < 99:
                text_class.show_message("buy") ### TOTO VYPSAT ###
            
            ### MISC. ITEMY ####
            # Potiony #
            if active_item.id == "healing_potion" or active_item.id == "mana_potion":
                if player.inventory[active_item.id] < 99:
                    player.inventory[active_item.id] += 1
                    active_item.bought = False
                    text_class.show_message("buy")
                    print(player.inventory[active_item.id])
                if active_item_type == "misc_item" and player.inventory[active_item.id] >= 99:
                    text_class.show_message("no more") ### TOTO VYPSAT ###
                    player.gold += active_item.price
                    active_item.bought = False
                        
            # Skill scrolly #
            if active_item.id == "skill_scroll_1" or active_item.id == "skill_scroll_2" or active_item.id == "skill_scroll_3":
                player.skills[active_item.id] = True
            
        if active_item.bought == True and multi_click_prevention == False:
            text_class.show_message("bought") ### TOTO VYPSAT ###
            multi_click_prevention = True
            
        if active_item.price > player.gold and multi_click_prevention == False:
            text_class.show_message("no golds") ### TOTO VYPSAT ###
            multi_click_prevention = True
            
        multi_click_prevention = False
        
    def item_type_check(active_item):
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
        
    def equip_item(self):
        multi_click_prevention = False
        for item_type in item_class.all_items:
            for item in item_type:
                if item.shown == True:
                    active_item = item
                
        active_item_type = Button.item_type_check(active_item)
                
        if active_item_type == "weapon":
            if player.weapon is not active_item.id and active_item.bought and multi_click_prevention == False:
                player.weapon = active_item.id
                text_class.show_message("equip") ### TOTO VYPSAT ###
                multi_click_prevention = True
                    
            if player.weapon == active_item.id and active_item.bought and multi_click_prevention == False:
                player.weapon = None
                text_class.show_message("unequip") ### TOTO VYPSAT ###
                multi_click_prevention = True
                
            if active_item.bought == False and multi_click_prevention == False:
                text_class.show_message("no owner") ### TOTO VYPSAT ###
                multi_click_prevention = True
            
            multi_click_prevention = False
            
        if active_item_type == "armor":
            if player.armor is not active_item.id and active_item.bought and multi_click_prevention == False:
                player.armor = active_item.id
                text_class.show_message("equip") ### TOTO VYPSAT ###
                multi_click_prevention = True
                    
            if player.armor == active_item.id and active_item.bought and multi_click_prevention == False:
                player.armor = None
                text_class.show_message("unequip") ### TOTO VYPSAT ###
                multi_click_prevention = True
                
            if active_item.bought == False and multi_click_prevention == False:
                text_class.show_message("no owner") ### TOTO VYPSAT ###
                multi_click_prevention = True
            
            multi_click_prevention = False
            
        if active_item_type == "misc_item":
            text_class.show_message("no equip") ### TOTO VYPSAT ###

        
class blit_object():
    def __init__(self, belonging, position, texture, scale, width, height):
        on__screen.blit_objects.append(self)
        self.belonging = belonging
        self.texture = texture
        self.position = position
        if scale:
            self.texture = pg.transform.scale(texture, (width, height))
        
    def blit_self(self, screen, on__screen):
        if not on__screen.active_screen == "Exit":
            if not on__screen.active_table == "Close":
                if on__screen.active_table.name in self.belonging:
                    screen.blit(self.texture, self.position)
            elif on__screen.active_screen.name in self.belonging:
                screen.blit(self.texture, self.position)
                
class bought_icon():
        def __init__(self, item, button):
            on__screen.blit_objects.append(self)
            self.item = item
            self.button = button
            self.texture = pg.image.load(DATA_ROOT + "/data/textures/icons/completed_v2.png")
            
        def blit_self(self, screen, on_screen):
            if self.item.belonging == on_screen.active_screen.name and self.item.bought:
                screen.blit(self.texture, (self.button.position[0] + 90, self.button.position[1] + 90))
        
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
coin = blit_object(["Game menu", "Shop", "Profile", "Campaign", "Weapon board", "Armor board", "Item board"], (1125,30), pg.image.load(DATA_ROOT + "/data/textures/icons/money_icon.png"), True, 54, 54)
level = blit_object(["Game menu", "Shop", "Profile", "Campaign", "Weapon board", "Armor board", "Item board"], (1125,85), pg.image.load(DATA_ROOT + "/data/textures/icons/player_level_icon.png"), True, 54, 54)

# Tlačítka pro změnu obrazovky
exit_b = Button(["Main menu"], (490,760), None, 215, 85, [["change_screen", "Exit"]], False, None, False, None)

warrior_class_b = Button(["New game table"], (230, 400), None, 180, 220, [["change_role", "warrior"], ["change_screen", "Game menu"], ["create_items"]], False, pg.image.load(DATA_ROOT + "/data/textures/icons/warrior_class_icon.png"), True, None)
ranger_class_b = Button(["New game table"], (510, 400), None, 180, 220, [["change_role", "ranger"], ["change_screen", "Game menu"], ["create_items"]], False, pg.image.load(DATA_ROOT + "/data/textures/icons/ranger_class_icon.png"), True, None)
mage_class_b = Button(["New game table"], (790, 400), None, 180, 220, [["change_role", "mage"], ["change_screen", "Game menu"], ["create_items"]], False, pg.image.load(DATA_ROOT + "/data/textures/icons/mage_class_icon.png"), True, None)

#main_menu_b = Button(["Game menu"], (30,30), (30,30,30,180), 64, 64, [["change_screen", "Main menu"]], True, pg.image.load(DATA_ROOT + "/data/textures/icons/back_icon.png"), False, None)
shop_b = Button(["Game menu"], (940, 550), (30,30,30,180), 100, 100, [["change_screen", "Shop"]], "c", pg.image.load(DATA_ROOT + "/data/textures/icons/shop_icon.png"), True, None)
profile_b = Button(["Game menu"], (95,550), (30,30,30,180), 100, 100, [["change_screen", "Profile"]], "c", pg.image.load(DATA_ROOT + "/data/textures/icons/profile_icon.png"), True, None)
campaign_b = Button(["Game menu"], (550,400), (30,30,30,180), 100, 100, [["change_screen", "Campaign"]], "c", pg.image.load(DATA_ROOT + "/data/textures/icons/campaign_icon.png"), True, None)
game_menu_b = Button(["Shop", "Profile", "Campaign"], (30,30), (30,30,30,180), 64, 64, [["change_screen", "Game menu"]], "c", pg.image.load(DATA_ROOT + "/data/textures/icons/back_icon.png"), False, None)

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

# Tlačítka tabulek
new_game_b = Button(["Main menu"], (75,485), None, 445, 85, [["change_table", "New game table"]], False, None, False, None)
settings_b = Button(["Main menu"], (75,625), None, 445,85, [["change_table", "Settings table"]], False, None, False, None)
credits_b = Button(["Main menu"], (680,625), None, 445,85, [["change_table", "Credits table"]], False, None, False, None)
game_b = Button(["Game menu"], (30,30), (30,30,30,180), 64, 64, [["change_table", "Game table"]], "c", None, False, None)

close_b = Button(["New game table", "Settings table", "Credits table", "Game table"], (1000,125), None, 64, 64, [["change_table", "Close"]], False, pg.image.load(DATA_ROOT + "/data/textures/icons/close_icon.png"), False, None)

# Obrazovky
main_menu = screen("Main menu", pg.image.load(DATA_ROOT + "/data/textures/screens/main_menu.png"))
game_menu = screen("Game menu", pg.image.load(DATA_ROOT + "/data/textures/screens/game_menu.png"))
shop = screen("Shop", pg.image.load(DATA_ROOT + "/data/textures/screens/shop.png"))
profile = screen("Profile", pg.image.load(DATA_ROOT + "/data/textures/screens/profile.png"))
campaign = screen("Campaign", pg.image.load(DATA_ROOT + "/data/textures/screens/campaign.png"))
battle = screen("Battle", pg.image.load(DATA_ROOT + "/data/textures/screens/campaign_battle.png"))

# Podobrazovky obchodu
weapon_board = screen("Weapon board",pg.image.load(DATA_ROOT + "/data/textures/screens/shop/shop_board.png"))
armor_board = screen("Armor board",pg.image.load(DATA_ROOT + "/data/textures/screens/shop/shop_board.png"))
item_board = screen("Item board",pg.image.load(DATA_ROOT + "/data/textures/screens/shop/shop_board.png"))

# Tabulky
new_game_table = table("New game table")
settings_table = table("Settings table")
credits_table = table("Credits table")
game_table = table("Game table")
        