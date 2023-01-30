from colorama import Fore
from Card import *
from Deck import *

def dealCards():
    for x in range(2):
        dealerHand.append(deck.draw())
    for c in range(2):
        playerHand.append(deck.draw())

def countPoints():
    pass

def startsWithTen():
    pass

deck = BlackJackDeck()

dealerHand = []
dealerPoints = 0
playerHand = []
playerPoints = 0



startLoop = input("Would you like to play a game?(y/n) ")
while startLoop == 'y':
    if startLoop == "n":
        quit()

    dealCards()

    print('\n' + Fore.RED + f"Dealer shows: {dealerHand[0]} \n")

    print(Fore.GREEN + "Player has:")
    print(Fore.GREEN + '\n'.join(playerHand))
    print(Fore.GREEN + f"\nCurrent player points: {}")


    ask = input("Would you like to draw a card(y/n)")
    if ask == 'n':
        startLoop = 'n'
    

