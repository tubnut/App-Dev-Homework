import pygame, sys
from pygame.locals import *
from Card import *
from Deck import *

#checks if player starts with 10 and an Ace
def startsWithTen(hand):
    for c in hand:
        if c.value == 10 and c.rank == "Ace"  :
            return True
        else:
            return False
        
#Changes ace value to 11 by default
def aceMoment():
    for c in playerCards:
        if c.rank == "Ace"  :
            c.aceChange()
    for i in dealerCards:
        if i.rank == "Ace"  :
            i.aceChange()

#Deals cards to both players
def dealCards():
    for _ in range(2):
        dealerCards.append(deck.draw())
    for _ in range(2):
        playerCards.append(deck.draw())

#Counts points 
def countPoints(hand):
    return sum([card.value for card in hand])

#Prints cards to the screen and offsets them evenly by 200
def displayCards():
    x = 100
    x2 = 100
    for card in dealerCards:
        card.display(my_display, x, 50)
        x += 200
    for card in playerCards:
        card.display(my_display, x2, 350)
        x2 += 200
    dealerCards[1].flipDown()

#Declaring hands and deck
playerCards = []
dealerCards = []

deck = Deck()

score = 0

pygame.init()
my_display = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
pygame.display.set_caption('Please help me')

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render(f'Score: {score}', True, (255,255,255))
textRect = text.get_rect()

dealCards()

playerTurn = True

#Game Loop
end = True
while end:
    pygame.display.update()
    clock.tick(30)

    my_display.blit(text, textRect)


    displayCards()
    if startsWithTen(playerCards):
        pass
    
    if startsWithTen(dealerCards):
        pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
            end = False
            pygame.quit()
        #Checks if space is pressed and if it is it draws a card
        if event.type == KEYDOWN:
            if event.key == K_SPACE and playerTurn == True:
                #Draws a card until player is done.
                deck.draw()
                if sum([card.value for card in playerCards]) > 21:
                    print("Working")
            if event.key == K_SPACE and playerTurn != True:
                pass      
