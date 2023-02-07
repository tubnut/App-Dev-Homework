from ModifiedWarHand import *
from Card import *
from time import sleep

WarDeck = ModifiedWarHand()

winner = 0

WarDeck.shuffleMoment()

def war():
    warPlayerHand = []
    warOpponentHand = []
    for _ in range(3):
        warPlayerHand.append(WarDeck.play())
    for _ in range(3):
        warOpponentHand.append(WarDeck.play())
    
    if warPlayerHand[0].value + warPlayerHand[1].value + warPlayerHand[2].value > warOpponentHand[0].value + warOpponentHand[1].value + warOpponentHand[2].value:
        winner = 1
    else:
        war()

count = 0
playerHand = []
opponentHand = []

while winner == 0:
    WarDeck.discardPile += playerHand + opponentHand
    playerHand = []
    opponentHand = []
    field = []

    playerHand.append(WarDeck.play())
    opponentHand.append(WarDeck.play())

    field += playerHand + opponentHand

    if field[0].value > field[1].value:
        winner = 1
    elif field[0].value < field[1].value:
        pass
    elif field[0].value == field[1].value:
        war()
    count += 1

winner = 1

print(f"It took {count} round to win")
    
    