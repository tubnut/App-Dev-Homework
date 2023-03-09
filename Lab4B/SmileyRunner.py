##Imports
import pygame, sys
from pygame.locals import *
from Person import *
from Wall import *


pygame.init()
my_display = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
pygame.key.set_repeat(100,100)

player = Person(100,550)
obstacle = Wall(750,550)
dimensions = player.get_rect()

down = True
end = True
while end:
    
    pygame.display.update()
    clock.tick(60)
    my_display.fill((255,255,255))

    player.draw(my_display)
    obstacle.draw(my_display)

    print(player.collision(obstacle))

    obstacle.change_x(-3)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type==KEYDOWN and event.key==K_ESCAPE):
            end = False
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                player.jump()
    
    if player.collision(obstacle):
        while down:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                    down = False
                    pygame.quit()
        end = False

    if obstacle.x_pos == 0:
        obstacle.x_pos = 750

    if player.y_pos + 50 < 600:
        player.change_y(1)