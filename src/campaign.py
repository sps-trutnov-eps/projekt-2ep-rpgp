import sys
import pygame as pg

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'
    
t_size = (135,378)
    
class Level():
    def __init__(self, number):
        self.number = number
        self.completed = False
        self.unlocked = False
        
    def get_enemies(self, enemies):
        self.enemies = enemies
        
class Counter():
    def __init__(self):
        self.number = 1
        self.font = pg.font.Font(DATA_ROOT + "/data/fonts/VeniceClassic.ttf", 100)
        texture = pg.image.load(DATA_ROOT + "/data/textures/icons/lock.png")
        self.lock = pg.transform.scale(texture, (80,80))
        
    def blit_self(self, screen, on_screen):
        if on_screen.active_screen.name == "Campaign":
            for l in levels:
                if l.unlocked == False:
                    end_index = l.number
                    break
            if self.number < end_index:
                text = str(self.number)
                surf = self.font.render(text, True, (30,30,30))
                width = self.font.size(text)[0]
                screen.blit(surf, ((600 - (width / 2)+2),754))
            elif self.number == end_index:
                screen.blit(self.lock, (562, 760))
        
    def up(self):
        for l in levels:
            if l.unlocked == False:
                end_index = l.number
                break
        if not self.number == 20 and self.number < end_index:
            self.number += 1
        
    def down(self):
        if not self.number == 1:
            self.number -= 1
            
class Enemy():
    def __init__(self, name, texture, hp, damage, armor):
        self.name = name
        self.position = (800,450)
        self.texture = texture
        self.hp = hp
        self.damage = damage
        self.armor = armor
        
    def blit_self(self, screen):
        screen.blit(self.texture, (885, 285))
        
class Battle_info():
    def get_info(self, level):
        self.level = level
        self.active_enemy = level.enemies[0]
    
    def make_player(self, player):
        self.player_texture = pg.transform.scale(pg.image.load(DATA_ROOT + "/data/textures/characters/player/player_template.png"), t_size)
        
    def blit_player(self, screen):
        screen.blit(self.player_texture, (180, 285))
        
battle_info = Battle_info()
        
counter = Counter()
levels = []

for i in range(1,20):
    levels.append(Level(i))

levels[0].unlocked = True

zombie = Enemy("Zombie", pg.transform.scale(pg.image.load(DATA_ROOT + "/data/textures/enemy/zombie.png"), t_size), 50, 4, 0)
slime = Enemy("Slime", pg.transform.scale(pg.image.load(DATA_ROOT + "/data/textures/enemy/slime.png"), t_size), 20, 2, 2)

levels[0].get_enemies([zombie,slime])
