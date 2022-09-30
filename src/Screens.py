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
        self.colour = (30,30,30)
        self.alpha = 220
        self.l_buttons = l_buttons
        self.t_buttons = t_buttons

class link_button():
    def __init__(self, position, width, height, link, draw):
        self.position = position
        self.width = width
        self.height = height
        self.link = link
        self.draw = draw
        self.colour = (150,150,150)
        
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
            
class table_button():
    def __init__(self, position, width, height, link, draw):
        self.position = position
        self.width = width
        self.height = height
        self.link = link
        self.colour = (200,200,200)
        self.draw = draw
        
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
        
# Tlačítka pro změnu obrazovky
exit_lb = link_button((490,760), 215, 85, "Exit", False)
new_game_lb = link_button((150,675), 900, 75, "Game menu", True)
main_menu_lb = link_button((30,30), 75, 75, "Main menu", True)

link_buttons = [

                ]

# Tlačítka tabulek
new_game_tb = table_button((75,485), 445, 85, "New game table", False)
settings_tb = table_button((75,625),445,85,"Settings table", False)
credits_tb = table_button((680,625),445,85,"Credits table", False)

t_close = table_button((1000,125), 75, 75, "Close", True)

table_buttons = [
            new_game_tb,
            settings_tb,
            credits_tb,
            t_close
                ]

# Obrazovky
main_menu = screen("Main menu", pg.image.load(DATA_ROOT + "/data/textures/screens/main_menu.png"), [exit_lb], [new_game_tb, settings_tb, credits_tb])
game_menu = screen("Game menu", pg.image.load(DATA_ROOT + "/data/textures/screens/game_menu.png"), [main_menu_lb], [])

screens = [
            main_menu,
            game_menu
            ]

# Tabulky
new_game_table = table("New game table", [new_game_lb], [t_close])
settings_table = table("Settings table", [], [t_close])
credits_table = table("Credits table", [], [t_close])

tables = [
            new_game_table,
            settings_table,
            credits_table
            ]