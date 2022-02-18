from consts import SUITS, RANKS
from itertools import product
from random import shuffle


class Card:
    def __init__(self, suit, rank, name, points):
        self.suit = suit
        self.rank = rank
        self.name = name
        self.points = points

    def __str__(self):
        message = self.name + " points: " + str(self.points)
        return message


class Deck:
    def __init__(self):
        self.cards = self.create_deck()
        shuffle(self.cards)

    def create_deck(self):
        cards = []
        for suit, rank in product(SUITS, RANKS):
            if rank == 'ace':
                points = 11
            elif rank.isdigit():
                points = int(rank)
            else:
                points = 10
            name = f'suit: {suit} rank: {rank}'
            c = Card(suit, rank, name, points)
            cards.append(c)
        return cards

    def get_card(self):
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)
