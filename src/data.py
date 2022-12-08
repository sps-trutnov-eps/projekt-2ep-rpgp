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
        self.hp = 100
        self.mana = 100
        self.equipped_skills = [None, None, None]
        self.id = "player"

class settings():
    def __init__(self):
        self.volume = 100
        
player = player()
settings = settings()
