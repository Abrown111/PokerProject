# card has several types and suits with values
# each card has a suit and value
# numerical value and name value
# each card also as the ability to return the name of the image in the computers memory associated with that card

class Card:
    suits = ['spades', 'hearts', 'clubs', 'diamonds']

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.name = f"{value}"

    def get_suit(self):
        return self.suit

    def __repr__(self):
        names = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
        self.name = names[self.value - 2]
        return f"{self.name} of {self.suit}"

    def image_file_name(self):
        names = ['jack', 'queen', 'king', 'ace']
        name = self.value
        if 10 < self.value < 15:
            name = names[self.value-11]
        return f"{name}_of_{self.suit}.png"


