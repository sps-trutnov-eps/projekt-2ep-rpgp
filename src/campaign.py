import sys
import pygame as pg

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'
    
class Level():
    def __init__(self, number):
        self.number = number
        self.completed = False
        
    def get_enemies(enemies):
        self.enemies = enemies
        
class Counter():
    def __init__(self):
        self.number = 1
        self.font = pg.font.Font(DATA_ROOT + "/data/fonts/VeniceClassic.ttf", 100)
        
    def blit_self(self, screen, on_screen):
        if on_screen.active_screen.name == "Campaign":
            text = str(self.number)
            surf = self.font.render(text, True, (30,30,30))
            width = self.font.size(text)[0]
            screen.blit(surf, ((600 - (width / 2)+2),754))
        
    def up(self):
        if not self.number == 20:
            self.number += 1
        
    def down(self):
        if not self.number == 1:
            self.number -= 1
            
class Enemy():
    def __init__(self, name, hp):
        self.name = name
        self.position = (800,450)
        self.hp = hp
        #self.texture = texture
        
counter = Counter()
levels = []

for i in range(1,20):
    levels.append(Level(i))

