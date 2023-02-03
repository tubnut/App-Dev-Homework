from ModifiedWarHand import *
from Card import *

WarDeck = ModifiedWarHand()

winner = 0

while winner == 0:
    playerHand = []
    opponentHand = []
    field = []

    playerHand.append(WarDeck.play())
    opponentHand.append(WarDeck.play())

    field += playerHand + opponentHand

    if field[0].value > field[1].value:
        print("Player wins")
        winner = 1
    elif field[0].value < field[1].value:
        print("Dealer wins")
        winner = 1
    elif field[0].value == field[1].value:
        pass

    winner = 1
