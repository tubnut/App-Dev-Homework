from typing import Any
import pygame
from pygame.locals import *

class Checkers(pygame.sprite.Sprite):

    def __init__(self, x, y, color: str):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.image = pygame.image.load("Resources/blackPiece.png") if color == "BLACK" else pygame.image.load("Resources/redPiece.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pos = (self.rect.x, self.rect.y)
        self.king = False
    
    def __str__(self) -> str:
        return f"({self.rect.x}, {self.rect.y})"

    def becomeKing(self):
        self.king = True

    def draw(self, window):
        window.blit(self.image, self.rect)