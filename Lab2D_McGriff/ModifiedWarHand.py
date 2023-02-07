from Card import *
import random

class ModifiedWarHand():

    def __init__(self):
        self.deck = [Card(r,s, cardOrderofGreatness[r]) for r in cardOrderofGreatness.keys() for s in sorder]
        self.handList = []
        self.discardPile = []
        
    def __str__(self):
        output = []
        for c in self.deck:
            output.append(str(c))
        return '\n'.join(output)

    def __len__(self):
        return len(self.deck)
    
    def discardCard(self):
        self.discard.append(self.deck[0])
        self.deck.remove(self.deck[0])
    
    def add_to_discard_pile(self, listy):
        self.discard += listy
        listy = []

    def play(self):
        return self.deck.pop(0)

    def showDiscardPile(self):
        discard = []
        for c in self.discard:
            discard.append(str(c))
        return '\n'.join(discard)

    def shuffleMoment(self):
        #credit to ShadowRunner on StackOverflow
        for i, card in enumerate(self.deck):
            cringeSwap = random.randrange(i, len(self.deck)) 
            self.deck[i], self.deck[cringeSwap] = self.deck[cringeSwap], card
    
    def endit(self, hand, hand2):
        if len(hand) or len(hand2) > 0:
            return True
        return False
