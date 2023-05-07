import pygame
from pygame.locals import *

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.img = pygame.image.load('Resources/hot.png')
        self.rect = self.img.get_rect()

    def draw(self, window):
        window.blit(self.img, self.rect)  