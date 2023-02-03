global cardOrderofGreatness
global sorder
global order

cardOrderofGreatness = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,"JACK": 10, "QUEEN": 10, "KING": 10, "Ace": 1}
sorder = ["Hearts", "Diamonds", "Clubs", "Spades" ]
order = list(cardOrderofGreatness.keys())

class Card():
    def __init__(self, rank,suit,value):
        self.rank = rank
        self.suit = suit
        self.value = value
    
    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return f"{self.rank} of {self.suit} (Value = {self.value})"

    def compareValues(self, other):
        if order.index(self.rank) > order.index(other.rank):
            return 1
        elif order.index(self.rank) == order.index(other.rank):
            if sorder.index(self.suit) == sorder.index(other.suit):
                return 0
            elif sorder.index(self.suit) > sorder.index(other.suit):
                return 1
            return -1
        return -1