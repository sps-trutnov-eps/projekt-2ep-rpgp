import sys
import pygame as pg
from text import *
from data import *
from items import *

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'

class on_screen():
    def __init__(self):
        self.active_screen = None
        self.active_table = "Close"


on__screen = on_screen()


class screen():
    def __init__(self, name, background, buttons, texts, objects):
        self.name = name
        self.background = pg.transform.scale(background, (1200,900))
        self.buttons = []
        for button in buttons:
            for place in button.belonging:
                if place == self.name:
                    self.buttons.append(button)
        if not text == []:
            self.texts = texts
        self.objects = objects

class table():
    def __init__(self, name, buttons, texts):
        self.name = name
        self.position = [100,100]
        self.size = [1000,700]
        self.colour = (30,30,30)
        self.alpha = 220
        self.buttons = []
        for button in buttons:
            for place in button.belonging:
                if place == self.name:
                    self.buttons.append(button)
        if not text == []:
            self.texts = texts
            
class button():
    def __init__(self, belonging, position, colour, width, height, tasks, draw, texture, scale, condition):
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
                self.change_role(task[1], player)
            if task[0] == "change_screen":
                self.change_screen(task[1], task[2], on__screen)
            if task[0] == "change_table":
                self.change_table(task[1], task[2], on__screen)
            if task[0] == "change_item":
                self.change_item(task[1], task[2])
        
    def change_screen(self, screens, new_screen, on_screen):
        if new_screen == "Exit":
            on_screen.active_screen = "Exit"
        else:
            for screen in screens:
                if screen.name == new_screen:
                    on_screen.active_screen = screen
                    on_screen.active_table = "Close"
                
    def change_table(self, tables, new_table, on_screen):
        if new_table == "Close":
            on_screen.active_table = "Close"
        else:
            for table in tables:
                if table.name == new_table:
                    on_screen.active_table = table
                    
    def change_item(self, new_item, items):
        for item in items:
            item.shown = False
        new_item.shown = True
        
    def change_role(self, role, player):
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
exit_b = button(["Main menu"], (490,760), None, 215, 85, [["change_screen", [], "Exit"]], False, None, False, None)

warrior_class_b = button(["New game table"], (230, 400), None, 180, 220, [["change_role", "warrior"], ["change_screen", [], "Game menu"]], False, pg.image.load(DATA_ROOT + "/data/textures/icons/warrior_class_icon.png"), True, None)
ranger_class_b = button(["New game table"], (510, 400), None, 180, 220, [["change_role", "ranger"], ["change_screen", [], "Game menu"]], False, pg.image.load(DATA_ROOT + "/data/textures/icons/ranger_class_icon.png"), True, None)
mage_class_b = button(["New game table"], (790, 400), None, 180, 220, [["change_role", "mage"], ["change_screen", [], "Game menu"]], False, pg.image.load(DATA_ROOT + "/data/textures/icons/mage_class_icon.png"), True, None)

main_menu_b = button(["Game menu"], (30,30), (30,30,30), 64, 64, [["change_screen", [], "Main menu"]], True, pg.image.load(DATA_ROOT + "/data/textures/icons/back_icon.png"), False, None)
shop_b = button(["Game menu"], (940, 550), None, 100, 100, [["change_screen", [], "Shop"]], False, pg.image.load(DATA_ROOT + "/data/textures/icons/shop_icon.png"), True, None)
profile_b = button(["Game menu"], (95,550), None, 100, 100, [["change_screen", [], "Profile"]], False, pg.image.load(DATA_ROOT + "/data/textures/icons/profile_icon.png"),True, None)
game_menu_b = button(["Shop", "Profile"], (30,30), (30,30,30), 64, 64, [["change_screen", [], "Game menu"]], True, pg.image.load(DATA_ROOT + "/data/textures/icons/back_icon.png"), False, None)

shop_back_b = button(["Weapon board", "Armor board", "Item board"], (30,30), (30,30,30), 64, 64, [["change_screen", [], "Shop"]], True, pg.image.load(DATA_ROOT + "/data/textures/icons/back_icon.png"), False, None)
weapon_board_b = button(["Shop"], (731,245), (255,0,0), 221, 267, [["change_screen", [], "Weapon board"]], False, None, False, None)
armor_board_b = button(["Shop"], (239,240), (255,0,0), 232, 126, [["change_screen", [], "Armor board"]], False, None, False, None)
item_board_b = button(["Shop"], (248,395), (255,0,0), 224, 105, [["change_screen", [], "Item board"]], False, None, False, None)

# Tlačítka tabulek
new_game_b = button(["Main menu"], (75,485), None, 445, 85, [["change_table", [], "New game table"]], False, None, False, None)
settings_b = button(["Main menu"], (75,625), None, 445,85, [["change_table", [], "Settings table"]], False, None, False, None)
credits_b = button(["Main menu"], (680,625), None, 445,85, [["change_table", [], "Credits table"]], False, None, False, None)

close_b = button(["New game table", "Settings table", "Credits table"], (1000,125), None, 64, 64, [["change_table", [], "Close"]], False, pg.image.load(DATA_ROOT + "/data/textures/icons/close_icon.png"), False, None)

# Tlačítka v obchodu
sw = button(["Weapon board"], (840,70), None, 105,105, [["change_item", starter_weapon, weapons]], False, starter_weapon.texture, True, None)
w1t1 = button(["Weapon board"], (685,200), None, 105,105, [["change_item", weapon_1_type_1, weapons]], False, weapon_1_type_1.texture, True, None)
w2t1 = button(["Weapon board"], (685,330), None, 105,105, [["change_item", weapon_2_type_1, weapons]], False, weapon_2_type_1.texture, True, None)
w3t1 = button(["Weapon board"], (685,460), None, 105,105, [["change_item", weapon_3_type_1, weapons]], False, weapon_3_type_1.texture, True, None)
w4t1 = button(["Weapon board"], (685,590), None, 105,105, [["change_item", weapon_4_type_1, weapons]], False, weapon_4_type_1.texture, True, None)
w5t1 = button(["Weapon board"], (685,720), None, 105,105, [["change_item", weapon_5_type_1, weapons]], False, weapon_5_type_1.texture, True, None)


buttons = [
            exit_b,
            main_menu_b,
            shop_b,
            profile_b,
            game_menu_b,
            shop_back_b,
            weapon_board_b,
            armor_board_b,
            item_board_b,
            new_game_b,
            settings_b,
            credits_b,
            close_b,
            warrior_class_b,
            ranger_class_b,
            mage_class_b,
            sw,
            w1t1,
            w2t1,
            w3t1,
            w4t1,
            w5t1
            ]

# Obrazovky
main_menu = screen("Main menu", pg.image.load(DATA_ROOT + "/data/textures/screens/main_menu.png"), buttons, [], None)
game_menu = screen("Game menu", pg.image.load(DATA_ROOT + "/data/textures/screens/game_menu.png"), buttons, [], None)
shop = screen("Shop", pg.image.load(DATA_ROOT + "/data/textures/screens/shop.png"), buttons, [], None)
profile = screen("Profile", pg.image.load(DATA_ROOT + "/data/textures/screens/profile.png"), buttons, [], None)

# Podobrazovky obchodu
weapon_board = screen("Weapon board",pg.image.load(DATA_ROOT + "/data/textures/screens/shop/shop_board.png"), buttons, [], [weapon_tree])
armor_board = screen("Armor board",pg.image.load(DATA_ROOT + "/data/textures/screens/shop/shop_board.png"), buttons, [], [armour_tree])
item_board = screen("Item board",pg.image.load(DATA_ROOT + "/data/textures/screens/shop/shop_board.png"), buttons, [], [item_tree])

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
new_game_table = table("New game table", buttons, texts_new_game)
settings_table = table("Settings table", buttons, texts_settings)
credits_table = table("Credits table", buttons, texts_credits)

tables = [
            new_game_table,
            settings_table,
            credits_table
            ]

# Speciální vyjímky pro přepínací čudlíky
for button in buttons:
    for task in button.tasks:
        if task[0] == "change_screen":
            task[1] = screens
        if task[0] == "change_table":
            task[1] = tables
        