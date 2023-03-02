##Imports
import pygame, sys
from pygame.locals import *
from Person import *
from Wall import *


pygame.init()
my_display = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
pygame.key.set_repeat(100,100)

player = Person(100,100)
obstacle = Wall(400,300)
dimensions = player.get_rect()

down = True
end = True
while end:
    
    pygame.display.update()
    clock.tick(1000)
    my_display.fill((255,255,255))

    player.draw(my_display)
    obstacle.draw(my_display)

    print(player.collision(obstacle))
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type==KEYDOWN and event.key==K_ESCAPE):
            end = False
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                player.move_up()
                if player.y_pos <= 0:
                    player.move_down()
                elif player.collision(obstacle) == True:
                    player.move_down()
            
            if event.key == K_RIGHT:
                player.move_right()
                if player.x_pos >= (800-50):
                    player.move_left()
                elif player.collision(obstacle) == True:
                    player.move_left()

            if event.key == K_LEFT:
                player.move_left()
                if player.x_pos <= 0:
                    player.move_right()
                elif player.collision(obstacle) == True:
                    player.move_right()

            if event.key == K_SPACE:
                
