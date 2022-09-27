import sys
import pygame as pg

#obrazovky
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'

class screen():
    def __init__(self, name, background, l_buttons, t_buttons):
        self.name = name
        self.background = background
        self.l_buttons = l_buttons
        self.t_buttons = t_buttons

class table():
    def __init__(self, name, l_buttons, t_buttons):
        self.name = name
        self.position = [100,100]
        self.size = [1000,700]
        self.l_buttons = l_buttons
        self.t_buttons = t_buttons

class link_button():
    def __init__(self, position, width, height, link):
        self.position = position
        self.width = width
        self.height = height
        self.link = link
        
    def check(self, m_pressed):
        if self.position[0] < pg.mouse.get_pos()[0] < (self.position[0] + self.width) and self.position[1] < pg.mouse.get_pos()[1] < (self.position[1] + self.height) and m_pressed[0]:
            return self.change_screen(screens)
        else:
            pass
        
    def change_screen(self, screens):
        for screen in screens:
            if self.link == screen.name:
                return screen
            else:
                pass
            
class table_button():
    def __init__(self, position, width, height, link):
        self.position = position
        self.width = width
        self.height = height
        self.link = link
        
    def check(self, m_pressed):
        if self.position[0] < pg.mouse.get_pos()[0] < (self.position[0] + self.width) and self.position[1] < pg.mouse.get_pos()[1] < (self.position[1] + self.height) and m_pressed[0]:
            return self.open_table(tables)
        else:
            pass
        
    def open_table(self, tabls):
        for table in tables:
            if self.link == table.name:
                return table
            else:
                pass
        
# Tlačítka pro změnu obrazovky

link_buttons = [

                ]

# Tlačítka pro vytvoření tabulek
new_game_tb = table_button((75,485), 445, 85, "New game table")

table_buttons = [
            new_game_tb
                ]

# Obrazovky
main_menu = screen("Main menu", pg.image.load(DATA_ROOT + "/data/textures/screens/main_menu.png"), [], [new_game_tb])
game_menu = screen("Game menu", pg.image.load(DATA_ROOT + "/data/textures/screens/game_menu.png"), [], [])

screens = [
            main_menu,
            game_menu
            ]

# Tabulky
new_game_table = table("New game table", [], [])

tables = [
            new_game_table
            ]