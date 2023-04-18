import pygame as pg
from pygame.locals import *

class Rectangle():
    def __init__(self, x_pos=10, y_pos=10, length = 50, height = 50, color = "Black"):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.length = length
        self.height = height
        self.color = color
        self.img = pg.image.load('Resources/wall.png')

    def draw(self, window):
        pg.draw.rect(window, self.color, (self.x_pos, self.y_pos, self.length, self.height))
    
    def move_up(self):
        self.y_pos -= 10
    def move_down(self):
        self.y_pos += 10
    def move_left(self):
        self.x_pos -= 10
    def move_right(self):
        self.x_pos += 10

    
    