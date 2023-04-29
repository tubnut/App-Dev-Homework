import pygame
from pygame.locals import *

#Inherits Sprite class from pygame to allow
class Player(pygame.sprite.Sprite):
    
    def __init__(self, xPos, yPos, width, height) -> None:
        self.xPos = xPos
        self.yPos = yPos
        self.width = width
        self.height = height
        self.img = pygame.image.load('Resources/goofyAhhCat.png')
    
    def moveUp(self):
        self.yPos -= 1
    
    def moveDown(self):
        self.yPos += 1
    
    def moveLeft(self):
        self.xPos -= 1
    
    def moveRight(self):
        self.xPos += 1
    
    def draw(self, window):
        window.blit(self.img,(self.xPos,self.yPos))    
    
    def collision(self, other):
        pass