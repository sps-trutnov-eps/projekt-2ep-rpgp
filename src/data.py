import pygame as pg
from Screens import *

contin = False

class player():
    def __init__(self):
        self.role = "warrior"
        self.weapon = None
        self.gold = 1000
        self.level = 1
        
class settings():
    def __init__(self):
        self.volume = 100
        
player = player()
settings = settings()
        