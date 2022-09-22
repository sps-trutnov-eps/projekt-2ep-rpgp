import pygame as pg

# LMB = určení prvního rohu
# RMB = určení druhého rohu
# SPACE = výpis hodnot

class button_tool():
    def __init__(self):
        self.corner1 = []
        self.corner2 = []
        
    def find_l(self):
        self.corner1 = [round(pg.mouse.get_pos()[0]), round(pg.mouse.get_pos()[1])]
    def find_r(self):
        self.corner2 = [round(pg.mouse.get_pos()[0]), round(pg.mouse.get_pos()[1])]
            
    def calculate(self):
        if not self.corner1 == [] and not self.corner2 == []:
            width = (abs(self.corner1[0] - self.corner2[0]))
            height = (abs(self.corner1[1] - self.corner2[1]))
            return self.corner1, self.corner2, width, height
        elif not self.corner1 == [] or not self.corner2 == []:
            if self.corner1 == []:
                return [0,0], self.corner2,0,0
            elif self.corner2 == []:
                return self.corner1, [0,0],0,0
        else:
            return [0,0],[0,0],0,0

bt = button_tool()
