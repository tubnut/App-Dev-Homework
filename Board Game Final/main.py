import pygame
from pygame.locals import *
from Board import *
from Checkers import Checkers

def placeCheckers():
    for y in range(3):
        for x in range(0,8):
            if y == 1:
                if x % 2 == 1:
                    r = Checkers(x * 75,y * 75, "RED")
                    redPieces.add(r)
                    allPieces.add(r)
            else:
                if x % 2 == 0:
                    r = Checkers(x * 75,y * 75, "RED")
                    redPieces.add(r)
                    allPieces.add(r)

    for y in range(3):
        for x in range(0,8):
            if y == 1:
                if x % 2 == 0:
                    b = Checkers(x * 75, 525 - (75 * y), "BLACK",)
                    blackPieces.add(b)
                    allPieces.add(b)
            else:
                if x % 2 == 1:
                    b = Checkers(x * 75, 525 - (75 * y), "BLACK")
                    blackPieces.add(b)
                    allPieces.add(b)

def followMouse(sprite, bool):
    if bool:
        sprite.pos = pos

def drawMovements(sprite):
    if sprite in redPieces:
        pygame.draw.rect(screen, (255,255,255), Rect(sprite.rect.x - 75, sprite.rect.y + 75, 75, 75))
        pygame.draw.rect(screen, (255,255,255), Rect(sprite.rect.x + 75, sprite.rect.y + 75, 75, 75))
    else:
        pygame.draw.rect(screen, (255,255,255), Rect(sprite.rect.x - 75, sprite.rect.y - 75, 75, 75))
        pygame.draw.rect(screen, (255,255,255), Rect(sprite.rect.x + 75, sprite.rect.y - 75, 75, 75))

pygame.init()

FPS = 60

screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()

board = Board()
redPieces = pygame.sprite.Group()
blackPieces = pygame.sprite.Group()
allPieces = pygame.sprite.Group()
redSquares = pygame.sprite.Group()

placeCheckers()

running = True
showMovements = False
clickCount = 0
while running:

    pos = pygame.mouse.get_pos()

    screen.fill("black")
    board.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for sprite in allPieces:
                if sprite.rect.collidepoint(event.pos):
                    showMovements = True
                    clickedSprite = sprite

    if showMovements:
        drawMovements(clickedSprite)

    allPieces.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

