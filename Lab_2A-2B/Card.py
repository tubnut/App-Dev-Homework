global order 
global sorder 

order = ["Two", "Three", "Four", "Five", "Six", "Seven","Eight", "Nine", "Ten", "JACK", "QUEEN", "KING", "Ace"]
sorder = ["Hearts", "Diamonds", "Clubs", "Spades" ]

class Card():
    def __init__(self, rank,suit,value):
        self.rank = rank
        self.suit = suit
        self.value = value
    
    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return f"{self.rank} of {self.suit} (Value = {self.value})"
    
    def aceChange(self):
        if self.rank == "Ace":
            self.value = 11
        return self.value


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