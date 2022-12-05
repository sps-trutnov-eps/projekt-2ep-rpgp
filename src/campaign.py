import sys
import pygame as pg
from skills import *

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
        self.id = "enemy"
        
class Battle_info():
    def start(self):
        self.player_turn = True
        self.pause = False
        self.hp_color = (190,50,50)
        self.mana_color = (80,110,200)
        self.bar_width = 300
        
    def get_info(self, level):
        self.level = level
        self.stages = (len(level.enemies) - 1)
        self.stage = 0
        self.active_enemy = level.enemies[self.stage]
        self.enemy_hp_copy = level.enemies[self.stage].hp
        self.enemy_max_hp = self.enemy_hp_copy = level.enemies[self.stage].hp
        self.enemy_effects = {"damage_ef" : 0, "defense_ef" : 0}
        debuff_class.enemy_debuffs = []
    
    def make_player(self, player):
        self.player_copy = player
        self.player_max_hp = player.hp
        self.player_hp_copy = player.hp
        self.player_max_mana = player.mana
        self.player_mana_copy = player.mana
        self.player_texture_copy = pg.transform.scale(pg.image.load(DATA_ROOT + "/data/textures/characters/player/player_template.png"), tp_size)
        self.awaiting_skill = None
        self.player_effects = {"damage_ef" : 0, "defense_ef" : 0}
        debuff_class.player_debuffs = []
        
    def blit_player(self, screen):
        screen.blit(self.player_texture_copy, (180, 285))
        
    def blit_enemy(self, screen):
        if not self.active_enemy == None:
            screen.blit(self.active_enemy.texture, (790, 285))
        
    def fight(self):
        if self.player_turn and self.awaiting_skill == None:
            damage = (self.player_copy.weapon.damage * ((100 - self.player_effects["damage_ef"]) / 100)) * ((100 - self.active_enemy.armor + self.enemy_effects["defense_ef"]) / 100)
            damage = round(damage)
            if damage >= 0:
                self.enemy_hp_copy -= damage
            else:
                pass
            self.player_turn = False
        elif self.player_turn and not self.awaiting_skill == None:
            self.awaiting_skill.skill_used("player", battle_info)
            self.awaiting_skill = None
        else:
            if self.player_copy.armor == None:
                self.player_hp_copy -= self.active_enemy.damage
            else:
                damage = (self.active_enemy.damage * ((100 - self.enemy_effects["damage_ef"]) / 100)) * ((100 - self.player_copy.armor.armor + self.player_effects["defense_ef"]) / 100)
                damage = round(damage)
                if damage >= 0:
                    self.player_hp_copy -= damage
                else:
                    pass
            self.player_turn = True
            
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
        
        for s in player.equipped_skills:
            if not s == None:
                if s.momental_cooldown > 0:
                    s.momental_cooldown -= 1
    
    def show_bars(self, screen):
        if not self.active_enemy == None:
            max_enemy_hp = self.active_enemy.hp
        # HP bar nepřítele
        pg.draw.rect(screen, self.hp_color, (765,35,(self.bar_width * (self.enemy_hp_copy / self.enemy_max_hp)),44))
        # HP a mana bar hráče
        pg.draw.rect(screen, self.hp_color, (135,775,(self.bar_width * (self.player_hp_copy / self.player_max_hp)),44))
        pg.draw.rect(screen, self.mana_color, (135, 820,(self.bar_width * (self.player_mana_copy / self.player_max_mana)),44))
        
    def check_debuffs(self):
        for d in debuff_class.debuffs:
            d.debuff_tick(self.player_copy, self.player_hp_copy)
            d.debuff_tick(self.active_enemy, self.enemy_hp_copy)
        print(debuff_class.debuffs[0].duration_e)
        
battle_info = Battle_info()
        
counter = Counter()
levels = []

for i in range(1,21):
    levels.append(Level(i))

levels[0].unlocked = True

# Nepřátelé
zombie = Enemy("Zombie", pg.transform.scale(pg.image.load(DATA_ROOT + "/data/textures/enemy/zombie.png"), te_size), 50, 5, 30)
slime = Enemy("Slime", pg.transform.scale(pg.image.load(DATA_ROOT + "/data/textures/enemy/slime.png"), te_size), 20, 2, 0)
# Zařazení nepřátel do levelu
levels[0].get_enemies([zombie, slime])
levels[1].get_enemies([zombie])
levels[2].get_enemies([zombie])
levels[3].get_enemies([zombie])
levels[4].get_enemies([zombie])
levels[5].get_enemies([zombie])
levels[6].get_enemies([zombie])
levels[7].get_enemies([zombie])
levels[8].get_enemies([zombie])
levels[9].get_enemies([zombie])
levels[10].get_enemies([zombie])
levels[11].get_enemies([zombie])
levels[12].get_enemies([zombie])
levels[13].get_enemies([zombie])
levels[14].get_enemies([zombie])
levels[15].get_enemies([zombie])
levels[16].get_enemies([zombie])
levels[17].get_enemies([zombie])
levels[18].get_enemies([zombie])
levels[19].get_enemies([zombie])
