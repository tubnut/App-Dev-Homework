import pygame as pg
from pygame.locals import *
from Rectangle import *

class Level():
    def __init__(self, mat, length=10, height=10):
        self.mat = mat
        self.length = length
        self.height = height

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 1:
                    self.mat[r][c] = Rectangle(r*50, c*50, 50, 50)

    def draw(self, window):
        for r in range(len(self.mat)):
            for c in range(len(self.mat[0])):
                if type(self.mat[r][c]) == Rectangle:
                    self.mat[r][c].draw(window)
