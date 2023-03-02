##Imports
import pygame, sys
from pygame.locals import *
from Smiley import *
from Block import *


pygame.init()
my_display = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
pygame.key.set_repeat(100,100)


blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)

b2 = Smiley(100,100)
obstacle = Block(400,300,50,50)
dimensions = b2.get_rect()

down = True
end = True
while end:
    
    pygame.display.update()
    clock.tick(1000)
    my_display.fill((255,255,255))

    b2.draw(my_display)
    obstacle.draw(my_display)

    print(b2.collision(obstacle))
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type==KEYDOWN and event.key==K_ESCAPE):
            end = False
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                b2.move_down()
                if b2.y_pos >= (600-50):
                    b2.move_up()
                elif b2.collision(obstacle) == True:
                    b2.move_up()

            if event.key == K_UP:
                b2.move_up()
                if b2.y_pos <= 0:
                    b2.move_down()
                elif b2.collision(obstacle) == True:
                    b2.move_down()
            
            if event.key == K_RIGHT:
                b2.move_right()
                if b2.x_pos >= (800-50):
                    b2.move_left()
                elif b2.collision(obstacle) == True:
                    b2.move_left()

            if event.key == K_LEFT:
                b2.move_left()
                if b2.x_pos <= 0:
                    b2.move_right()
                elif b2.collision(obstacle) == True:
                    b2.move_right()

            if event.key == K_SPACE:
                print(b2.get_rect())
