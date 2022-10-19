from const import PRINTED, SUITS, RANKS
from itertools import product
from random import shuffle

class Card:
    def __init__(self,suit,rank,points,picture):
        self.suit = suit
        self.rank = rank
        self.points = points
        self.picture = picture

    def __str__(self):
        mess = self.picture + '\nPoints' + str(self.points)
        return mess

class Deck:
    def __init__(self):
        self.cards = self.generate_deck()
        shuffle(self.cards)

    def generate_deck(self):
        cards = []
        for suit,rank in product(SUITS,RANKS):
            if rank == 'ace':
                points = 11   ### ЦИКЛ ДЛЯ ВИБОРУ 1\11
            elif rank.isdigit():
                points = int(rank)
            else:
                points = 10
            picture = PRINTED.get(rank)
            c = Card(suit,rank,points,picture)
            cards.append(c)
        return cards

    def get_card(self):
        self.cards.pop()

    def __len__(self):
        return len(self.cards)