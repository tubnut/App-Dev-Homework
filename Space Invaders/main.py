import pygame
from pygame.locals import *
from Obstacles import *
from Player import *
from Bullet import *

pygame.init()
pygame.key.set_repeat(1)

screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

player = Player(50,50,50,50)
fireball = Obstacle(770, 50)
background = pygame.image.load("Resources/background.png")

playerGroup = pygame.sprite.Group()
playerGroup.add(player)
enemyGroup = pygame.sprite.Group()
bulletGroup = pygame.sprite.Group()

addBullets = False
while True:
    screen.blit(background, (0,0))
    clock.tick(60)

    player.draw(screen)
    fireball.draw(screen)

    print(player.xPos, player.yPos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
            end = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                player.moveUp()
                if player.yPos < 0:
                    player.moveDown()
            if event.key == K_DOWN:
                player.moveDown()
                if player.yPos > 570:
                    player.moveUp()
            if event.key == K_SPACE:
                addBullets = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                addBullets = False

    if addBullets: 
        b = Bullet(player.rect.x, player.rect.y)
        bulletGroup.add(b)

    bulletGroup.draw(screen)

    bulletGroup.update() 

    pygame.display.update()

