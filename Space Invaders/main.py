import pygame
from pygame.locals import *
from Obstacles import *
from Player import *

pygame.init()
pygame.key.set_repeat(1)

screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

player = Player(50,50,50,50)

while True:
    screen.fill((255,255,255))
    clock.tick(60)



    player.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
            end = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                player.moveUp()
            if event.key == K_DOWN:
                player.moveDown()
            if event.key == K_LEFT:
                player.moveLeft()
            if event.key == K_RIGHT:
                player.moveRight()
    


    pygame.display.update()

