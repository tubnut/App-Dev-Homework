import pygame
from pygame.locals import *
from Board import Board

pygame.init()

FPS = 60

screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()

board = Board()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill("black")

    board.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

