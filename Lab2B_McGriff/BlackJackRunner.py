from colorama import Fore
from Card import *
from Deck import *

def dealCards():
    for _ in range(2):
        dealerHand.append(deck.draw())
    for _ in range(2):
        playerHand.append(deck.draw())

def countPoints(hand):
    output = []
    for card in hand:
        output.append(card.value)
    return sum(output)

def startsWithTen(hand):
    for c in hand:
        if c.value == 10  c.rank == "Ace"  :
            return True
        else:
            return False

def displayHand(player):
    for card in playerHand:
        print(card)

def winCondition(winner):
    print(f"{winner} wins!")
    dealerHand = []
    playerHand = []

deck = BlackJackDeck()

while True:
    dealerHand = []
    dealerPoints = 0
    playerHand = []
    playerPoints = 0

    startLoop = input(Fore.WHITE + "Would you like to play a game?(y/n) ")
    if startLoop == "n":    
        quit()

    dealCards()

    print('\n' + Fore.RED + f"Dealer shows: {dealerHand[0]} \n")

    print(Fore.GREEN + "Player has:")
    displayHand(playerHand)

    print("Player points: " + str(countPoints(playerHand)))
    if startsWithTen(playerHand) == True:  
        winCondition("Player")
        continue 
    if startsWithTen(dealerHand) == True:
        winCondition("Dealer")
        continue

    ask = input(Fore.WHITE + "Would you like to draw a card(y/n) ")
    if ask == 'y':
        playerHand.append(deck.draw)
    else:
        continue