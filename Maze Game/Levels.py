import pygame as pg
from pygame.locals import *
from Wall import *

class Level():
    def __init__(self):
        self.mat = mat
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 1:
                    self.mat[r][c] = Wall(r*50, c*50, 50, 50)

    def draw(self, window):
        for r in range(len(self.mat)):
            for c in range(len(self.mat[0])):
                if type(self.mat[r][c]) == Wall:
                    self.mat[r][c].draw(window)
