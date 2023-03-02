import pygame as pg
from pygame.locals import *

class Wall():
    def __init__(self, x_pos=10, y_pos=10):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.img = pg.image.load('wall.png')
    
    def __str__(self):
        return f"Position = ({self.x_pos}, {self.y_pos}), Height = {self.height}, Weight = {self.weight}, Color = {self.color}"

    def change_x(self, value):
        self.x_pos += value
    
    def change_y(self, value):
        self.y_pos += value
    
    def change_color(self, value):
        self.color = value

    def draw(self, window):
        window.blit(self.img,(self.x_pos,self.y_pos))