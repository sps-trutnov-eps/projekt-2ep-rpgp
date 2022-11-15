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
        self.hp = 10
        
class settings():
    def __init__(self):
        self.volume = 100
        
player = player()
settings = settings()
