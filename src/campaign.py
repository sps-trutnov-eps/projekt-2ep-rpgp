import sys
import pygame as pg

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DATA_ROOT = '.'
else:
    DATA_ROOT = '..'
    
class Level():
    def __init__(self, number):
        self.number = number
        
levels = []

for i in range(1,20):
    levels.append(Level(i))

