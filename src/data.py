import pygame as pg
from Screens import *

contin = False

class player():
    def __init__(self):
        self.role = "warrior"
        self.weapon = None
        self.armor = None
        self.inventory = {"healing_potion":0, "mana_potion":0}
        self.skills = {"skill_1":False, "skill_2":False, "skill_3":False, "":False, "":False}
        self.gold = 1000
        self.level = 1
        self.hp = 100
        self.mana = 100
        self.equipped_skills = [None, None, None]
        self.max_hp = self.hp
        self.max_mana = self.mana
        self.hp_stat = 1
        self.mana_stat = 1
        self.int_stat = 1
        self.luck_stat = 1
        
class settings():
    def __init__(self):
        self.volume = 100
        
player = player()
settings = settings()
