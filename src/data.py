import pygame as pg
from Screens import *

contin = False

class player():
    def __init__(self):
        self.role = "warrior"
        self.weapon = None
        self.armor = None
        self.inventory = {"healing_potion":0, "mana_potion":0}
        self.skills = []
        self.gold = 1000
        self.level = 1
        self.xp = 0
        self.xp_req = 100
        self.max_hp = 100
        self.max_mana = 100
        self.hp = self.max_hp
        self.mana = self.max_mana
        self.equipped_skills = [None, None, None]
        self.int = 0
        self.luck = 0
        self.hp_stat = 0
        self.mana_stat = 0
        self.int_stat = 0
        self.luck_stat = 0
        self.stat_point = 20
        self.id = "player"
        
    def calculate_level(self):
        if self.xp >= self.xp_req:
            self.xp -= self.xp_req
            self.lvl += 1
            self.xp_req += self.xp_req / 8
        
player = player()