import pygame
from pygame.locals import *
from Board import Board
from Checkers import Checkers

pygame.init()

FPS = 60

screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()

board = Board()
redPieces = pygame.sprite.Group()
blackPieces = pygame.sprite.Group()

for _ in range(1,12):
    r = Checkers(0,0, "red")
    redPieces.add(r)

for _ in range(1,12):
    b = Checkers(0,0, "black")
    blackPieces.add(r)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill("black")

    board.draw(screen)
    redPieces.draw(screen)



    pygame.display.flip()
    clock.tick(FPS)

