from colorama import Fore
from Card import *
from Deck import *

def dealCards():
    for x in range(2):
        dealerHand.append(deck.draw())
    for c in range(2):
        playerHand.append(deck.draw())

def countPoints(hand):
    output = []
    for card in hand:
        output.append(card.value)
    return sum(output)

def startsWithTen():
    pass

def displayHand(player):
    for card in playerHand:
        print(card)

deck = BlackJackDeck()

dealerHand = []
dealerPoints = 0
playerHand = []
playerPoints = 0

startLoop = input(Fore.WHITE + "Would you like to play a game?(y/n) ")
while startLoop == 'y':
    if startLoop == "n":
        quit()

    dealCards()

    print('\n' + Fore.RED + f"Dealer shows: {dealerHand[0]} \n")

    print(Fore.GREEN + "Player has:")
    displayHand(playerHand)

    print("Player points: " + str(countPoints(playerHand)))

    ask = input(Fore.WHITE + "Would you like to draw a card(y/n) ")
    if ask == 'n':
        startLoop = 'n'