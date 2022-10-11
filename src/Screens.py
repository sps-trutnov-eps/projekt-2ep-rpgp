import sys
import pygame as pg
from text import *

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'

#obrazovky
class screen():
    def __init__(self, name, background, l_buttons, t_buttons, texts, objects):
        self.name = name
        self.background = pg.transform.scale(background, (1200,900))
        self.l_buttons = l_buttons
        self.t_buttons = t_buttons
        if not text == []:
            self.texts = texts
        self.objects = objects

class table():
    def __init__(self, name, l_buttons, t_buttons, texts):
        self.name = name
        self.position = [100,100]
        self.size = [1000,700]
        self.colour = (30,30,30)
        self.alpha = 220
        self.l_buttons = l_buttons
        self.t_buttons = t_buttons
        if not text == []:
            self.texts = texts

class link_button():
    def __init__(self, position, colour, width, height, link, draw, text, texture, scale):
        self.position = position
        self.width = width
        self.height = height
        self.link = link
        self.draw = draw
        self.colour = colour
        self.alpha = 180
        if not text == []:
            self.text = text
        else:
            self.text = True
        if not texture == None:
            if scale:
                self.texture = pg.transform.scale(texture, (width, height))
            else:
                self.texture = texture
        else:
            self.texture = None
        
    def check(self, m_pressed):
        if self.position[0] < pg.mouse.get_pos()[0] < (self.position[0] + self.width) and self.position[1] < pg.mouse.get_pos()[1] < (self.position[1] + self.height) and m_pressed[0]:
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
    def __init__(self, position, colour, width, height, link, draw, text, texture, scale):
        self.position = position
        self.width = width
        self.height = height
        self.link = link
        self.colour = colour
        self.alpha = 180
        self.draw = draw
        if not text == []:
            self.text = text
        else:
            self.text = True
        if not texture == None:
            if scale:
                self.texture = pg.transform.scale(texture, (width, height))
            else:
                self.texture = texture
        else:
            self.texture = None
        
        
    def check(self, m_pressed):
        if self.position[0] < pg.mouse.get_pos()[0] < (self.position[0] + self.width) and self.position[1] < pg.mouse.get_pos()[1] < (self.position[1] + self.height) and m_pressed[0]:
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
exit_lb = link_button((490,760), None, 215, 85, "Exit", False, [], None, False)
new_game_lb = link_button((150,675), (200,200,200), 900, 75, "Game menu", True, [], None, False)
main_menu_lb = link_button((30,30), (30,30,30), 64, 64, "Main menu", True, [], pg.image.load(DATA_ROOT + "/data/textures/icons/back_icon.png"), False)
shop_lb = link_button((940, 550), None, 100, 100, "Shop", False, [], pg.image.load(DATA_ROOT + "/data/textures/icons/shop_icon.png"), True)
profile_lb = link_button((95,550), None, 100, 100, "Profile", False, [], pg.image.load(DATA_ROOT + "/data/textures/icons/profile_icon.png"),True)
game_menu_lb = link_button((30,30), (30,30,30), 64, 64, "Game menu", True, [], pg.image.load(DATA_ROOT + "/data/textures/icons/back_icon.png"), False)

shop_back_lb = link_button((30,30), (30,30,30), 64, 64, "Shop", True, [], pg.image.load(DATA_ROOT + "/data/textures/icons/back_icon.png"), False)
weapon_board_lb = link_button((731,245), (255,0,0), 221, 267, "Weapon_Board", False, [], None, False)
armor_board_lb = link_button((239,240), (255,0,0), 232, 126, "Armor_Board", False, [], None, False)
item_board_lb = link_button((248,395), (255,0,0), 224, 105, "Item_Board", False, [], None, False)

link_buttons = [

                ]

# Tlačítka tabulek
new_game_tb = table_button((75,485), None, 445, 85, "New game table", False, [], None, False)
settings_tb = table_button((75,625), None, 445,85,"Settings table", False, [], None, False)
credits_tb = table_button((680,625), None, 445,85,"Credits table", False, [], None, False)

t_close = table_button((1000,125), None, 64, 64, "Close", False, [], pg.image.load(DATA_ROOT + "/data/textures/icons/close_icon.png"), False)

table_buttons = [
            new_game_tb,
            settings_tb,
            credits_tb,
            t_close
                ]

# Obrazovky
main_menu = screen("Main menu", pg.image.load(DATA_ROOT + "/data/textures/screens/main_menu.png"), [exit_lb], [new_game_tb, settings_tb, credits_tb], [], None)
game_menu = screen("Game menu", pg.image.load(DATA_ROOT + "/data/textures/screens/game_menu.png"), [main_menu_lb, shop_lb, profile_lb], [], [], None)
shop = screen("Shop", pg.image.load(DATA_ROOT + "/data/textures/screens/shop.png"), [game_menu_lb, weapon_board_lb, armor_board_lb, item_board_lb], [], [], None)
profile = screen("Profile", pg.image.load(DATA_ROOT + "/data/textures/screens/profile.png"), [game_menu_lb], [], [], None)

# Podobrazovky obchodu
weapon_board = screen("Weapon_Board",pg.image.load(DATA_ROOT + "/data/textures/screens/shop/shop_board.png"), [shop_back_lb], [], [], [weapon_tree])
armor_board = screen("Armor_Board",pg.image.load(DATA_ROOT + "/data/textures/screens/shop/shop_board.png"), [shop_back_lb], [], [], [armour_tree])
item_board = screen("Item_Board",pg.image.load(DATA_ROOT + "/data/textures/screens/shop/shop_board.png"), [shop_back_lb], [], [], [item_tree])

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
new_game_table = table("New game table", [new_game_lb], [t_close], [])
settings_table = table("Settings table", [], [t_close], texts_settings)
credits_table = table("Credits table", [], [t_close], texts_credits)

tables = [
            new_game_table,
            settings_table,
            credits_table
            ]