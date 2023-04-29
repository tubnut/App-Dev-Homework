import pygame as pg
from pygame.locals import *
from Player import *
from Levels import *
from Key import *
from Enemy import *
from Teleporter import *



#Basic PyGame setup code
pg.init()
pg.key.set_repeat(1)
screen = pg.display.set_mode((800, 800))
clock = pg.time.Clock()
run = True

def collideWall(maze):
    walls = []
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if type(maze[r][c]) == Wall:
                walls.append(maze[r][c])

    if any([wall.collision(player) for wall in walls]):
        return True
    

#Objects
level1 =  [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1],
           [1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1],
           [1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1],
           [1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1],
           [1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1],
           [1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

level2 =  [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
           [1,1,1,0,1,1,1,0,1,0,0,1,0,1,0,1],
           [1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1],
           [1,0,1,0,1,0,1,0,1,1,1,1,0,1,0,1],
           [1,0,1,0,1,0,1,0,0,0,0,1,0,1,0,1],
           [1,0,1,0,1,0,1,0,1,1,1,1,1,1,0,1],
           [1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1],
           [1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,1],
           [1,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1],
           [1,0,0,0,1,1,1,0,0,0,1,0,0,0,0,1],
           [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
           [1,0,0,0,0,0,1,0,1,1,1,1,1,1,1,1],
           [1,0,0,0,0,1,1,0,1,0,0,0,0,0,0,1],
           [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

level3 =  [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
           [1,1,1,0,1,1,1,0,1,0,0,0,0,0,0,1],
           [1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1],
           [1,0,0,0,1,0,0,0,1,1,1,1,0,0,0,1],
           [1,0,1,0,1,1,1,0,0,0,0,0,0,0,0,1],
           [1,0,1,0,1,0,1,0,1,1,1,1,1,1,0,1],
           [1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1],
           [1,1,0,1,1,0,1,0,0,0,0,1,0,0,0,1],
           [1,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1],
           [1,0,0,0,1,1,1,0,0,1,1,0,0,0,0,1],
           [1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,1],
           [1,0,1,0,1,0,1,0,0,0,1,1,1,1,1,1],
           [1,0,0,0,1,0,1,0,1,1,0,0,0,0,0,1],
           [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

font = pg.font.Font('freesansbold.ttf', 32)

Maze1 = Level(level1, 16, 16)
Maze2 = Level(level2, 16, 16)
Maze3 = Level(level3, 16, 16)
player = Player(300,420, 50, 50, "Green")
teleporter1 = Teleporter(400,300,50,50, "Red")
teleporter2 = Teleporter(700,50,50,50, "Red")
teleporter3 = Teleporter(250,600,50,50, "Red")
teleporter4 = Teleporter(300,700,50,50, "Red")
finalTeleporter = Teleporter(700,700,50,50, "Red")
key = Key(700,100)
enemy = Enemy(60, 358, 40, 40)

hasKey = False
lives = 3

firstLevel = True 
secondLevel = False
thirdLevel = False

enemySpeed = 10

youWin = False

youLose = pg.image.load("Resources/Ninya Sadge.jpg")
winnerScreen = pg.image.load("Resources/MR BEASTT.jpg")
loserText = font.render(f'YOU LOSE!!!!', True, (255,0,0))
loserRect = loserText.get_rect()
loserRect.center = (400,400)

winnerText = font.render(f'YOU WIN!!!!', True, (255,0,0))
winnerRect = loserText.get_rect()
winnerRect.center = (400,400)

#Game Loop
while run:
    screen.fill((192,192,192))
    clock.tick(60) 
    #Objects

    livesText = font.render(f'Lives = {lives}', True, (255,255,255))
    livesRect = livesText.get_rect()
    livesRect.center = (100, 780)

    if firstLevel:
        Maze1.draw(screen)
        teleporter1.draw(screen)
        if player.collision(teleporter1):
            firstLevel = False
            secondLevel = True
            player.setPos(55, 55)
    elif secondLevel:
        Maze2.draw(screen)
        teleporter2.draw(screen)
        teleporter3.draw(screen)
        teleporter4.draw(screen)
        if player.collision(teleporter2):
            player.setPos(246, 609)
        if player.collision(teleporter4):
            secondLevel = False
            thirdLevel = True
    elif thirdLevel:
        Maze3.draw(screen)
        enemy.draw(screen)
        finalTeleporter.draw(screen)
        if hasKey == False:
            key.draw(screen)
        enemy.x_pos += enemySpeed
        if enemy.x_pos > 750:
            enemy.x_pos *= -1
        if player.collision(enemy):
            player.setPos(246, 609)
            lives -= 1
        if player.collision(key):
            hasKey = True
        if player.collision(finalTeleporter) and hasKey:
            youWin = True


    player.draw(screen)
    print(player)

    #Event Loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            pg.quit()
        if event.type == pg.KEYDOWN:
            if event.key == K_UP:
                player.move_up()
                
                if firstLevel:
                    if collideWall(level1):
                        player.setPos(300,420)
                        lives -= 1
                        #player.move_down()
                elif secondLevel:
                    if collideWall(level2):
                        #player.move_down()
                        player.setPos(55, 55)
                        lives -= 1
                elif thirdLevel:
                    if collideWall(level3):
                        #player.move_down()
                        player.setPos(246, 609)
                        lives -= 1
            if event.key == K_DOWN:
                player.move_down()
                if firstLevel:
                    if collideWall(level1):
                        #player.move_up()
                        player.setPos(300,420)
                        lives -= 1
                elif secondLevel:
                    if collideWall(level2):
                        #player.move_up()
                        player.setPos(55, 55)
                        lives -= 1
                elif thirdLevel:
                    if collideWall(level3):
                        #player.move_up()
                        player.setPos(246, 609)
                        lives -= 1
            if event.key == K_LEFT:
                player.move_left()
                if firstLevel:
                    if collideWall(level1):
                        #player.move_right()
                        player.setPos(300,420)
                        lives -= 1
                elif secondLevel:
                    if collideWall(level2):
                        #player.move_right()
                        player.setPos(55, 55)
                        lives -= 1
                elif thirdLevel:
                    if collideWall(level3):
                        #player.move_right()
                        player.setPos(246, 609)
                        lives -= 1
            if event.key == K_RIGHT:
                player.move_right()
                if firstLevel:
                    if collideWall(level1):
                        #player.move_left()
                        player.setPos(300,420)
                        lives -= 1
                elif secondLevel:
                    if collideWall(level2):
                        player.setPos(55, 55)
                        lives -= 1
                        #player.move_left()
                elif thirdLevel:
                    if collideWall(level3):
                        #player.move_left()
                        player.setPos(246, 609)
                        lives -= 1
                
    screen.blit(livesText, livesRect)

    if youWin:
        firstLevel = False
        secondLevel = False
        thirdLevel = False
        screen.blit(winnerScreen, (0,0))
        screen.blit(winnerText, winnerRect)

    if lives == 0:
        firstLevel = False
        secondLevel = False
        thirdLevel = False
        screen.blit(youLose, (0,0))
        screen.blit(loserText, loserRect)


    pg.display.update()
