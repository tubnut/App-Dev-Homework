from Card import *
from Deck import *

ace = Card("Ace", "Spades", 1)
ace2 = Card("Ace", "Spades", 1)
king = Card("KING", "Clubs", 10)
ten = Card("Ten", "Hearts", 10)
five = Card("Five", "Spades", 5)
five2 = Card("Five", "Hearts", 1)
deck = BlackJackDeck()

print(deck)
print(len(deck))

deck.discardCard()
deck.discardCard()
deck.discardCard()
deck.discardCard()

print(deck)
print(len(deck))
print('\n')
print(deck.showDiscardPile())






