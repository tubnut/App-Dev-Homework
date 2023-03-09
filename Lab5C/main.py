import pygame, sys
from pygame.locals import *
from Card import *

pygame.init()
my_display = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

card1 = Card("ace", "spades", 1)
card2 = Card("two", "hearts", 2)
card3 = Card("five", "clubs", 5)

cards = [card1, card2, card3]
i = 0

end = True
while end:
    pygame.display.update()
    clock.tick(30)

    card1.display(my_display, 100, 100)
    card2.display(my_display, 300,100)
    card3.display(my_display, 500,100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
            end = False
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                cards[i].flip()
                i += 1
        
        print(event)
