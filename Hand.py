# Hand class
# makes a hand of five cards
# has the ability to check what type of hand the current hand is
# it also can compare with another hand and determine who wins

from Card import Card




class Hand:
    all_cards = []

    def __init__(self):
        self.cards = []
        self.values = []

    def add_card(self, card: Card):
        if len(self.cards) < 5:
            self.cards.append(card)
            self.cards.sort(reverse=True, key=Hand.by_value)
            self.values.append(card.value)
            self.values.sort(reverse=True)
            self.all_cards.append(card)
        else:
            print('Hand already has 5 cards')
        return self.cards

    def print_hand(self):
        print(x for x in self.cards)

    @classmethod
    def by_value(cls, card):
        return card.value

    def is_royal_flush(self):
        suit = self.cards[1].suit
        if sum(x.value for x in self.cards) == 60 and not any(x.suit != suit for x in self.cards):
            return True
        else:
            return False

    def is_straight_flush(self):
        suit = self.cards[0].suit
        return self.is_straight() and not any(x.suit != suit for x in self.cards)

    def is_four_of_a_kind(self):
        return [self.values[0] == self.values[3] or self.values[1] == self.values[4], self.values[2]]

    def is_full_house(self):
        if self.values[0] == self.values[1] and self.values[1] != self.values[2]:
            if all(x == self.values[2] for x in self.values[2:5]):
                return [True, self.values[3], self.values[0]]
        if self.values[3] == self.values[4] and self.values[3] != self.values[2]:
            if all(x == self.values[0] for x in self.values[0:3]):
                return [True, self.values[0], self.values[3]]
        return [False, 0, 0]

    def is_flush(self):
        return not any(x.suit != self.cards[0].suit for x in self.cards)

    def is_straight(self):
        hand = self.values[::-1]
        straight = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        return hand == straight[hand[0]:hand[0]+5]

    def is_three_of_a_kind(self):
        return [self.values[0] == self.values[2] or self.values[2] == self.values[4] or self.values[1] == \
                self.values[4], self.values[2]]

    def is_pair(self):
        buffer_set = self.values
        pair_list = []
        for i in range(4):
            if any(buffer_set[i] == x for x in buffer_set[i+1:len(buffer_set)+1]):
                pair_list.append(i)
        try:
            if pair_list[1] == pair_list[0] + 1:
                pair_list.remove(pair_list[1])
        finally:
            try:
                return [len(pair_list), buffer_set[pair_list[0]], buffer_set[pair_list[1]]]
            except IndexError:
                if len(pair_list) == 1:
                    return [len(pair_list), buffer_set[pair_list[0]]]
                else:
                    return [len(pair_list), 0]

    def is_high_card(self):
        return self.values[1]

    def rank(self):
        high_card = [self.values[0]]
        rank = 0
        rank += self.is_pair()[0]
        if rank != 0:
            try:
                high_card = [self.is_pair()[1], self.is_pair()[2]]
            except IndexError:
                high_card = [self.is_pair()[1]]
        if self.is_three_of_a_kind()[0]:
            rank = 3
            high_card = [self.is_three_of_a_kind()[1], self.values[0]]
        if self.is_straight():
            rank = 4
            high_card = [self.values[0]]
        if self.is_flush():
            rank = 5
            high_card = [self.values[0]]
        if self.is_full_house()[0]:
            rank = 6
            high_card = [self.is_full_house()[1], self.is_full_house()[2]]
        if self.is_four_of_a_kind()[0]:
            rank = 7
            high_card = [self.is_four_of_a_kind()[1]]
        if self.is_straight_flush():
            rank = 8
            high_card = [self.values[0]]
        if self.is_royal_flush():
            rank = 9
        return [rank, high_card]

    def get_hand_type(self):
        names = ['High Card', 'One Pair', 'Two Pair', 'Three-of-a-kind', 'Straight', 'Flush', 'Full House',
                 'Four-of-a-kind', 'Straight Flush', 'Royal Flush']
        return names[self.rank()[0]]

    def compare(self, hand):
        my_rank = self.rank()[0]
        my_high_card = self.rank()[1]
        opponent_rank = hand.rank()[0]
        opponent_high_card = hand.rank()[1]
        if my_rank > opponent_rank:
            return 1
        if my_rank < opponent_rank:
            return -1
        if my_rank == opponent_rank:
            if my_rank == 1:
                for i in range(5):
                    if self.values[i] > hand.values[i]:
                        return 1
                    elif self.values[i] < hand.values[i]:
                        return -1
                    else:
                        continue
                return 0
            if my_high_card > opponent_high_card:
                return 1
            if my_high_card < opponent_high_card:
                return -1
            if my_high_card < opponent_high_card:
                return 0

    def clean_hand(self):
        self.cards = []



















