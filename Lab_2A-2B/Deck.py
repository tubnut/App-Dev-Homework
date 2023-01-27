from Card import *
class BlackJackDeck():

    def __init__(self):
        values = [2,3,4,5,6,7,8,9,10,10,10,1] * 4
        self.deck = [Card(r,s, 0) for r in order for s in sorder]
        self.discard = []
        for i, card in enumerate(self.deck):
           card.value = values[i]

    
    def __str__(self):
        output = []
        for c in self.deck:
            output.append(str(c))
        return '\n'.join(output)

    def __len__(self):
        return len(self.deck)
    
    def shuffleMoment(self):
        pass