import pygame as pg
from pygame.locals import *
from Player import *
from Levels import *
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

    # if any([Wall.collision(player) for wall in walls]):
    #     pass
    print(walls)

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
           [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
           [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
           [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
           [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
           [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
           [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
           [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
           [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
           [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
           [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
           [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
           [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
           [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
           [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

Maze1 = Level(level1, 16, 16)
Maze2 = Level(level2, 16, 16)
Maze3 = Level(level3, 16, 16)
player = Player(300,420, 50, 50, "Green")
teleporter1 = Teleporter(400,300,50,50, "Red")
teleporter2 = Teleporter(700,50,50,50, "Red")
teleporter3 = Teleporter(250,600,50,50, "Red")

firstLevel = True
secondLevel = False
thirdLevel = False

collideWall(Maze1)

#Game Loop
while run:
    screen.fill((192,192,192))
    clock.tick(60)
    #Objects
    
    if firstLevel:
        Maze1.draw(screen)
        teleporter1.draw(screen)
        if player.collision(teleporter1):
            firstLevel = False
            secondLevel = True
            player.setPos(55, 50)
    elif secondLevel:
        Maze2.draw(screen)
        teleporter2.draw(screen)
        teleporter3.draw(screen)
        if player.collision(teleporter2):
            player.setPos(246, 609)

    player.draw(screen)
    

    #Logic


    

    #Event Loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            pg.quit()
        if event.type == pg.KEYDOWN:
            if event.key == K_UP:
                player.move_up()
            if event.key == K_DOWN:
                player.move_down()
            if event.key == K_LEFT:
                player.move_left()
            if event.key == K_RIGHT:
                player.move_right()

    pg.display.update()
