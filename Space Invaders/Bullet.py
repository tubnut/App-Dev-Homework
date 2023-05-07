import pygame
from pygame.locals import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load('Resources/hot.png')
        self.rect = self.image.get_rect()
        self.rect.move_ip((x,y))

    def draw(self, window):
        window.blit(self.img, self.rect) 

    def update(self):
        self.rect.x += 3
