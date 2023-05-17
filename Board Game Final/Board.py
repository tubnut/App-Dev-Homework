import pygame
from pygame.locals import *

class Board(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.board = [[0,1,0,1,0,1,0,1],
                      [1,0,1,0,1,0,1,0],
                      [0,1,0,1,0,1,0,1],
                      [1,0,1,0,1,0,1,0],
                      [0,1,0,1,0,1,0,1],
                      [1,0,1,0,1,0,1,0],
                      [0,1,0,1,0,1,0,1],
                      [1,0,1,0,1,0,1,0]]
        
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                if self.board[r][c] == 1:
                    self.board[r][c] = Rect(r*75, c*75, 75, 75)

    def draw(self, window):
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                if type(self.board[r][c]) == Rect:
                    pygame.draw.rect(window, (200,0,0) ,self.board[r][c])
