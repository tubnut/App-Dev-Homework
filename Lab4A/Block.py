import pygame as pg
from pygame.locals import *

class Block():
    def __init__(self, x_pos=10, y_pos=10, height = 10, width = 20, color = 'Black'):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.height = height
        self.width = width
        self.color = color
    
    def __str__(self):
        return f"Position = ({self.x_pos}, {self.y_pos}), Height = {self.height}, Weight = {self.weight}, Color = {self.color}"

    def change_x(self, value):
        self.x_pos += value
    
    def change_y(self, value):
        self.y_pos += value
    
    def change_color(self, value):
        self.color = value

    def draw(self, window):
        pg.draw.rect(window, self.color, (self.x_pos, self.y_pos, self.width, self.height))