import pygame
from pygame.locals import *

class Checkers(pygame.sprite.Sprite):

    def __init__(self, x, y, color) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.color = color
        self.image = pygame.image.load("Resources/blackPiece.png") if color == "black" else pygame.image.load("Resources/redPiece.png")
        self.rect = self.image.get_rect()
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def draw(self, window):
        window.blit(self.image, self.rect)