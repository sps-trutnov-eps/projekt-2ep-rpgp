import sys
import pygame as pg

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'

class screen():
    def __init__(self, name, background, buttons):
        self.name = name
        self.background = background
        self.buttons = buttons

class table():
    def __init__(self, name, size, buttons):
        self.name = name
        self.size = size
        self.buttons = buttons

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
        self.position = postition
        self.width = width
        self.height = height
        self.link = link
        
# Tlačítka pro změnu obrazovky
new_game_b = link_button((75,485), 445, 85, "Game menu")

link_buttons = [
            new_game_b
                ]
# Obrazovky
main_menu = screen("Main menu", pg.image.load(DATA_ROOT + "/data/textures/screens/main_menu.png"), [])
game_menu = screen("Game menu", pg.image.load(DATA_ROOT + "/data/textures/screens/game_menu.png"), [])

screens = [
            main_menu,
            game_menu
            ]