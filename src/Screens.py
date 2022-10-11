import sys
import pygame as pg
from text import *
from data import *

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'

#obrazovky
class screen():
    def __init__(self, name, background, l_buttons, t_buttons, f_buttons, texts, objects):
        self.name = name
        self.background = pg.transform.scale(background, (1200,900))
        self.l_buttons = l_buttons
        self.t_buttons = t_buttons
        self.f_buttons = f_buttons
        if not text == []:
            self.texts = texts
        self.objects = objects

class table():
    def __init__(self, name, l_buttons, t_buttons, f_buttons, texts):
        self.name = name
        self.position = [100,100]
        self.size = [1000,700]
        self.colour = (30,30,30)
        self.alpha = 220
        self.l_buttons = l_buttons
        self.t_buttons = t_buttons
        self.f_buttons = f_buttons
        if not text == []:
            self.texts = texts

class link_button():
    def __init__(self, position, colour, width, height, link, draw, texture, scale, condition):
        self.position = position
        self.width = width
        self.height = height
        self.link = link
        self.draw = draw
        self.colour = colour
        self.alpha = 180
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
        
    def check(self, m_pressed):
        if self.position[0] < pg.mouse.get_pos()[0] < (self.position[0] + self.width) and self.position[1] < pg.mouse.get_pos()[1] < (self.position[1] + self.height) and m_pressed[0] and self.condition:
            if self.link == "Exit":
                return "Exit"
            else:
                return self.change_screen(screens)
        else:
            pass
        
    def change_screen(self, screens):
        for screen in screens:
            if self.link == screen.name:
                return screen
            else:
                pass
    
    def blit_self(self, screen):
        if self.draw:
            button_sf = pg.Surface((self.width, self.height))
            button_sf.set_alpha(self.alpha)
            button_sf.fill(self.colour)
            screen.blit(button_sf, (self.position))
        if self.texture == None:
            pass
        else:
            screen.blit(self.texture, (self.position))
            
class table_button():
    def __init__(self, position, colour, width, height, link, draw, texture, scale, condition):
        self.position = position
        self.width = width
        self.height = height
        self.link = link
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
        
        
    def check(self, m_pressed):
        if self.position[0] < pg.mouse.get_pos()[0] < (self.position[0] + self.width) and self.position[1] < pg.mouse.get_pos()[1] < (self.position[1] + self.height) and m_pressed[0] and self.condition:
            if self.link == "Close":
                return "Close"
            else:
                return self.open_table(tables)
        else:
            pass
        
    def open_table(self, tabls):
        for table in tables:
            if self.link == table.name:
                return table
            else:
                pass
            
    def blit_self(self, screen):
        if self.draw:
            button_sf = pg.Surface((self.width, self.height))
            button_sf.set_alpha(self.alpha)
            button_sf.fill(self.colour)
            screen.blit(button_sf, (self.position))
        if self.texture == None:
            pass
        else:
            screen.blit(self.texture, (self.position))
            
class function_button():
    def __init__(self, position, colour, width, height, tasks, draw, texture, scale, condition):
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
            
    def check(self, m_pressed):
        if self.position[0] < pg.mouse.get_pos()[0] < (self.position[0] + self.width) and self.position[1] < pg.mouse.get_pos()[1] < (self.position[1] + self.height) and m_pressed[0] and self.condition:
            self.work()
        else:
            pass
            
    def blit_self(self, screen):
        if self.draw:
            button_sf = pg.Surface((self.width, self.height))
            button_sf.set_alpha(self.alpha)
            button_sf.fill(self.colour)
            screen.blit(button_sf, (self.position))
        if self.texture == None:
            pass
        else:
            screen.blit(self.texture, (self.position))
        
    def work(self):
        for task in self.tasks:
            if task[0] == "change_role":
                self.change_role(task[1], task[2])
        
    def change_role(self, player, role):
        player.role = role
        
class blit_object():
    def __init__(self, position, texture, scale, width, height):
        self.texture = texture
        self.position = position
        if scale:
            self.texture = pg.transform.scale(texture, (width, height))
        
    def blit_self(self, screen):
        screen.blit(self.texture, self.position)
    
# Objekty na vykreslení
weapon_tree = blit_object((0,0), pg.image.load(DATA_ROOT + "/data/textures/screens/shop/weapon_tree.png"), True, 1200, 900)
armour_tree = blit_object((0,0), pg.image.load(DATA_ROOT + "/data/textures/screens/shop/general_item_tree.png"), True, 1200, 900)
item_tree = blit_object((0,0), pg.image.load(DATA_ROOT + "/data/textures/screens/shop/general_item_tree.png"), True, 1200, 900)

# Tlačítka pro změnu obrazovky
exit_lb = link_button((490,760), None, 215, 85, "Exit", False, None, False, None)

warrior_class_lb = link_button((200, 500), None, 200, 200,"Game menu", False, None, False, None)
ranger_class_lb = link_button((500,500), None, 200, 200,"Game menu", False, None, False, None)
mage_class_lb = link_button((800, 500), None, 200, 200,"Game menu", False, None, False, None)

main_menu_lb = link_button((30,30), (30,30,30), 64, 64, "Main menu", True, pg.image.load(DATA_ROOT + "/data/textures/icons/back_icon.png"), False, None)
shop_lb = link_button((940, 550), None, 100, 100, "Shop", False, pg.image.load(DATA_ROOT + "/data/textures/icons/shop_icon.png"), True, None)
profile_lb = link_button((95,550), None, 100, 100, "Profile", False, pg.image.load(DATA_ROOT + "/data/textures/icons/profile_icon.png"),True, None)
game_menu_lb = link_button((30,30), (30,30,30), 64, 64, "Game menu", True, pg.image.load(DATA_ROOT + "/data/textures/icons/back_icon.png"), False, None)

shop_back_lb = link_button((30,30), (30,30,30), 64, 64, "Shop", True, pg.image.load(DATA_ROOT + "/data/textures/icons/back_icon.png"), False, None)
weapon_board_lb = link_button((731,245), (255,0,0), 221, 267, "Weapon_Board", False, None, False, None)
armor_board_lb = link_button((239,240), (255,0,0), 232, 126, "Armor_Board", False, None, False, None)
item_board_lb = link_button((248,395), (255,0,0), 224, 105, "Item_Board", False, None, False, None)

# Tlačítka tabulek
new_game_tb = table_button((75,485), None, 445, 85, "New game table", False, None, False, None)
settings_tb = table_button((75,625), None, 445,85,"Settings table", False, None, False, None)
credits_tb = table_button((680,625), None, 445,85,"Credits table", False, None, False, None)

t_close = table_button((1000,125), None, 64, 64, "Close", False, pg.image.load(DATA_ROOT + "/data/textures/icons/close_icon.png"), False, None)

# Funkcionální tlačítka
warrior_class_fb = function_button((230, 400), None, 180, 220, [("change_role", player, "warrior")], False, pg.image.load(DATA_ROOT + "/data/textures/icons/warrior_class_icon.png"), True, None)
ranger_class_fb = function_button((510, 400), None, 180, 220, [("change_role", player, "ranger")], False, pg.image.load(DATA_ROOT + "/data/textures/icons/ranger_class_icon.png"), True, None)
mage_class_fb = function_button((790, 400), None, 180, 220, [("change_role", player, "mage")], False, pg.image.load(DATA_ROOT + "/data/textures/icons/mage_class_icon.png"), True, None)

# Obrazovky
main_menu = screen("Main menu", pg.image.load(DATA_ROOT + "/data/textures/screens/main_menu.png"), [exit_lb], [new_game_tb, settings_tb, credits_tb], [], [], None)
game_menu = screen("Game menu", pg.image.load(DATA_ROOT + "/data/textures/screens/game_menu.png"), [main_menu_lb, shop_lb, profile_lb], [], [], [], None)
shop = screen("Shop", pg.image.load(DATA_ROOT + "/data/textures/screens/shop.png"), [game_menu_lb, weapon_board_lb, armor_board_lb, item_board_lb], [], [], [], None)
profile = screen("Profile", pg.image.load(DATA_ROOT + "/data/textures/screens/profile.png"), [game_menu_lb], [], [], [], None)

# Podobrazovky obchodu
weapon_board = screen("Weapon_Board",pg.image.load(DATA_ROOT + "/data/textures/screens/shop/shop_board.png"), [shop_back_lb], [], [], [], [weapon_tree])
armor_board = screen("Armor_Board",pg.image.load(DATA_ROOT + "/data/textures/screens/shop/shop_board.png"), [shop_back_lb], [], [], [], [armour_tree])
item_board = screen("Item_Board",pg.image.load(DATA_ROOT + "/data/textures/screens/shop/shop_board.png"), [shop_back_lb], [], [], [], [item_tree])

screens = [
            main_menu,
            game_menu,
            shop,
            weapon_board,
            armor_board,
            item_board,
            profile
            ]

# Tabulky
new_game_table = table("New game table", [warrior_class_lb, ranger_class_lb, mage_class_lb], [t_close], [warrior_class_fb, ranger_class_fb, mage_class_fb], texts_new_game)
settings_table = table("Settings table", [], [t_close], [], texts_settings)
credits_table = table("Credits table", [], [t_close], [], texts_credits)

tables = [
            new_game_table,
            settings_table,
            credits_table
            ]