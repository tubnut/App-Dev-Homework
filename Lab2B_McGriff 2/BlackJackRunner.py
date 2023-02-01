from colorama import Fore
from Card import *
from Deck import *

deck = BlackJackDeck()

def dealCards():
    for _ in range(2):
        dealerHand.append(deck.draw())
    for _ in range(2):
        playerHand.append(deck.draw())

def countPoints(hand):
    return sum([card.value for card in hand])

def startsWithTen(hand):
    for c in hand:
        if c.value == 10 and c.rank == "Ace"  :
            return True
        else:
            return False

def displayHand(player):
    for card in player:
        print(card)

def board():
    print('\n' + Fore.RED + f"Dealer shows: {dealerHand[0]} \n")
    print(Fore.GREEN + "Player has:")
    displayHand(playerHand)
    print("Player points: " + str(countPoints(playerHand)))

def aceMoment():
    for c in playerHand:
        if c.rank == "Ace"  :
            c.aceChange()
    for i in dealerHand:
        if i.rank == "Ace"  :
            i.aceChange()

playerHand = []
dealerHand = []

while True:
    startLoop = input(Fore.WHITE + "Would you like to play BlackJack?(y/n) ")

    deck.discard += playerHand + dealerHand

    playerHand = []
    dealerHand = []
    dealerPoints = 0
    playerPoints = 0

    if startLoop == "n":    
        quit()

    dealCards()
    aceMoment()
    board()

    if startsWithTen(playerHand) == True:  
        print("You have 21 you win!")
        continue 
    if startsWithTen(dealerHand) == True:
        print("Dealer has 21 and you lose.")
        continue

    if countPoints(playerHand) == 21:
            print("You Win")
            break
    if countPoints(dealerHand) == 21:
            print("Dealer wins")
            break
    
    while countPoints(dealerHand) < 17:
        dealerHand.append(deck.draw())
    
    ask = input(Fore.WHITE + "Would you like to hit?(y/n) ")
    while ask == 'y':   
        playerHand.append(deck.draw())
        board()
        dealerHand.append(deck.draw())
        if countPoints(playerHand) > 21:
            print("You busted and the Dealer wins")
            break
        if countPoints(playerHand) == 21:
            print("You Win")
            break
        ask = input(Fore.WHITE + "Would you like to hit again?(y/n) ")
        if ask == 'n':
            break
        
    if ask == 'n':
        if countPoints(dealerHand) == countPoints(playerHand):
            print("Draw")
            continue
        
        elif countPoints(playerHand) > countPoints(dealerHand):
            print("You win")
            continue
        
        else:
            print("Dealer wins")
            continue