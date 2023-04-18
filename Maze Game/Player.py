import pygame as pg
from pygame.locals import *

class Player():
    def __init__(self, x_pos=10, y_pos=10, length = 50, height = 50, color = "Black"):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.length = length
        self.height = height
        self.color = color
        self.img = pg.image.load('Resources/goofyAhhCat.png')
        self.rect = self.img.get_rect()

    def draw(self, window):
        window.blit(self.img,(self.x_pos,self.y_pos))    

    def move_up(self):
        self.y_pos -= 10

    def move_down(self):
        self.y_pos += 10
    
    def move_left(self):
        self.x_pos -= 10
    
    def move_right(self):
        self.x_pos += 10

    def collision(self, other):
        if (self.y_pos + 50 >= other.y_pos and self.y_pos <= other.y_pos + 50) and (self.x_pos + 50 >= other.x_pos and self.x_pos <= other.x_pos + 50):
            return True

    
    