# creates a deck of 52 cards
# has the abliity to automatically shuffle the deck
# takes class type card as cards

from Card import Card
import random


class Deck:
    all_deck = []

    def __init__(self):
        for y in Card.suits:
            self.all_deck += [Card(y, x) for x in range(2, 15)]

    def get_deck(self):
        return self.all_deck

    def print_deck(self):
        for x in self.all_deck:
            print(x)

    def shuffle(self):
        random.shuffle(self.all_deck)
        return self.all_deck

    def deal_card(self):
        try:
            player_card = self.all_deck[len(self.all_deck)-1]
            self.all_deck.remove(player_card)
            return player_card
        except IndexError:
            return












