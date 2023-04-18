import pygame as pg
from pygame.locals import *

class Wall():
    def __init__(self, x_pos=10, y_pos=10, length = 50, height = 50, color = "Black"):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.length = length
        self.height = height
        self.color = color
        self.img = pg.image.load('Resources/wall.png')
        self.rect = self.img.get_rect()


    def draw(self, window):
        window.blit(self.img,(self.x_pos,self.y_pos))

    
    