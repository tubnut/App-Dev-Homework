import pygame
from pygame.locals import *

class Checkers():

    def __init__(self, x, y, color) -> None:
        self.x = x
        self.y = y
        self.color = color
        self.image = pygame.image.load("Resources/blackPiece") if color == "black" else pygame.image.load("Resources/redPiece")
    
    def draw(self, window):
        pass