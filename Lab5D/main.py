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
def countPoints():
    playerScoreText = font.render(f'Score: {sum([card.value for card in playerCards])}', True, (255,255,255))
    playerRect = playerScoreText.get_rect()
    playerRect.center = (75,575)
    my_display.blit(playerScoreText, playerRect)

    #dealerScoreText = font.render(f'Score: {sum([card.value for card in dealerCards if card.up] )}', True, (255,255,255))
    #dealerRect = dealerScoreText.get_rect()
    #my_display.blit(dealerScoreText, dealerRect)


#Prints cards to the screen and offsets their x value by 50
def displayCards():
    x = 100
    x2 = 100
    for card in dealerCards:
        card.display(my_display, x, 50)
        x += 50
    for card in playerCards:
        card.display(my_display, x2, 350)
        x2 += 50
    dealerCards[1].flipDown()

def declareWinner(winner):
    winnerText = font.render(f'{winner} Wins!', True, (255,255,255))
    winnerRect = winnerText.get_rect()
    winnerRect.center = (400,300)
    my_display.blit(winnerText, winnerRect)

def buttonMakerBecauseImTooLazyToMakeAClass(button, x, y):
    pygame.draw.rect(my_display, (255,255,255), pygame.Rect((x,y),(70,30)), 15, 3)
    my_display.blit(button, (x,y))


#Declaring hands and deck
playerCards = []
dealerCards = []

deck = Deck()

pygame.init()
my_display = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
pygame.display.set_caption('BlackJack Time')


font = pygame.font.Font('freesansbold.ttf', 32)

dealCards()

button1 = font.render('Hit!' , True , (0,0,0))
button2 = font.render('Stay' , True , (0,0,0))
button3 = font.render('Play again?', True, (0,0,0))


playerTurn = True
winner = "None"
displayWinner = False

title = font.render('Blackjack Game', True, (255,255,255))

#Game Loop
end = True
while end:

    pygame.display.update()
    clock.tick(30)
    my_display.fill((40,125,60))
    my_display.blit(title, (263,2))

    if startsWithTen(playerCards):
        declareWinner("Player")
    
    if startsWithTen(dealerCards):
        declareWinner("Dealer")

    displayCards()
    countPoints()

    buttonMakerBecauseImTooLazyToMakeAClass(button1, 25, 200)
    buttonMakerBecauseImTooLazyToMakeAClass(button2, 25, 300)

    mouse = pygame.mouse.get_pos()
    print(mouse)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
            end = False
            pygame.quit()
        #Checks if button is pressed and if it is it draws a card
        if event.type == MOUSEBUTTONDOWN:
            if (25 <= mouse[0] <= 95 and 200 <= mouse[1] <= 230) and playerTurn == True:
                #Draws a card until player is done
                playerCards.append(deck.draw())
                #Checks if you would go over 21 with next draw
                if sum([card.value for card in playerCards]) > 21:
                    winner = "Dealer"
                    displayWinner = True
            if (25 <= mouse[0] <= 95 and 300 <= mouse[1] <= 330) and playerTurn == True:
                while sum([card.value for card in dealerCards]) < 17:
                    dealerCards.append(deck.draw())
                if sum([card.value for card in dealerCards]) > 21:
                    winner = "Player"
                    displayWinner = True
    if displayWinner == True:
        declareWinner(winner)

        dealerCards[1].flipUp()
        dealerScoreText = font.render(f'Score: {sum([card.value for card in dealerCards])}', True, (255,255,255))
        dealerRect = dealerScoreText.get_rect()
        my_display.blit(dealerScoreText, dealerRect)

        buttonMakerBecauseImTooLazyToMakeAClass(button3, 600, 300)
