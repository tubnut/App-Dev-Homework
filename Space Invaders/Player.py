import pygame
from pygame.locals import *

#Inherits Sprite class from pygame to allow
class Player(pygame.sprite.Sprite):
    
    def __init__(self, xPos, yPos, width, height) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.xPos = xPos
        self.yPos = yPos
        self.width = width
        self.height = height
        self.img = pygame.image.load('Resources/goofyAhhCat.png')
        self.rect = self.img.get_rect()
    
    def moveUp(self):
        self.rect.y -= 1
    
    def moveDown(self):
        self.rect.y += 1
    
    def moveLeft(self):
        self.rect.x -= 1
    
    def moveRight(self):
        self.rect.x += 1
    
    def draw(self, window):
        window.blit(self.img, self.rect)    
    
    def collision(self, other):
        pass