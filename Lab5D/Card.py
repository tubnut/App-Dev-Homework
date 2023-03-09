import pygame
from pygame.locals import *

global cardOrderofGreatness
global sorder
global order

cardOrderofGreatness = {"two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,"jack": 10, "queen": 10, "king": 10, "ace": 1}
sorder = ["hearts", "diamonds", "clubs", "spades" ]
order = list(cardOrderofGreatness.keys())

class Card():
    def __init__(self, rank,suit,value, facing = True):
        self.rank = rank
        self.suit = suit
        self.value = value
        self.up = facing
        self.frontImage = pygame.image.load(f'Resources/Cards/{self.rank.lower()}Of{self.suit.title()}.png')
        self.backImage = pygame.image.load('Resources/cardBack.png')

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return f"{self.rank} of {self.suit} (Value = {self.value})"
    
    def aceChange(self):
        if self.rank == "Ace":
            self.value = 11
        return self.value
    
    def display(self, win, x, y):
        if self.up:
            win.blit(self.frontImage, (x,y))
        else:
            win.blit(self.backImage, (x,y))

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
    
    def flipUp(self):
        self.up = True

    def flipDown(self):
        self.up = False