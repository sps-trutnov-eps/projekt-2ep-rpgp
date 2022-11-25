import sys
import pygame as pg

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'
    
tp_size = (135,378)
te_size = (352,374)
    
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
        
class Battle_info():
    def start(self):
        self.player_turn = True
        self.pause = False
        
    def get_info(self, level):
        self.level = level
        self.stages = (len(level.enemies) - 1)
        self.stage = 0
        self.active_enemy = level.enemies[self.stage]
        self.enemy_hp_copy = level.enemies[self.stage].hp
    
    def make_player(self, player):
        self.player_copy = player
        self.player_hp_copy = player.hp
        self.player_texture_copy = pg.transform.scale(pg.image.load(DATA_ROOT + "/data/textures/characters/player/player_template.png"), tp_size)
        
    def blit_player(self, screen):
        screen.blit(self.player_texture_copy, (180, 285))
        
    def blit_enemy(self, screen):
        if not self.active_enemy == None:
            screen.blit(self.active_enemy.texture, (790, 285))
        
    def fight(self):
        if self.player_turn:
            damage = self.player_copy.weapon.damage - self.active_enemy.armor
            if damage >= 0:
                self.enemy_hp_copy -= damage
            else:
                pass
            self.player_turn = False
        else:
            if self.player_copy.armor == None:
                self.player_hp_copy -= self.active_enemy.damage
            else:
                damage = self.active_enemy.damage - self.player_copy.armor.armor
                if damage >= 0:
                    self.player_hp_copy -= damage
                else:
                    pass
            self.player_turn = True
        print("Player HP: " + str(self.player_hp_copy) + " Enemy HP: " + str(self.enemy_hp_copy))
            
    def pause_battle(self):
        self.pause = True
        
    def unpause_battle(self):
        self.pause = False
            
    def check_fight(self, on__screen):
        if not self.active_enemy == None:
            self.fight()
        if self.enemy_hp_copy <= 0 and not self.active_enemy == None:
            self.active_enemy = None
            self.player_turn = True
        elif self.player_hp_copy <= 0:
            self.pause_battle()
            for table in on__screen.tables:
                if table.name == "Death table":
                    on__screen.active_table = table
        elif self.active_enemy == None:
            self.stage += 1
            if self.stage <= self.stages:
                self.active_enemy = self.level.enemies[self.stage]
                self.enemy_hp_copy = self.level.enemies[self.stage].hp
            else:
                self.pause_battle()
                for table in on__screen.tables:
                    if table.name == "Win table":
                        on__screen.active_table = table
    
    def activate_skill(self):
        pass
        
battle_info = Battle_info()
        
counter = Counter()
levels = []

for i in range(1,20):
    levels.append(Level(i))

levels[0].unlocked = True

zombie = Enemy("Zombie", pg.transform.scale(pg.image.load(DATA_ROOT + "/data/textures/enemy/zombie.png"), te_size), 2, 2, 0)
slime = Enemy("Slime", pg.transform.scale(pg.image.load(DATA_ROOT + "/data/textures/enemy/slime.png"), te_size), 20, 2, 0)

levels[0].get_enemies([zombie, slime])
