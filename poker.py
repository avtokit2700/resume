"""

A poker hand has a constructor that accepts a string containing 5 cards:

    PokerHand(hand)

The characteristics of the string of cards are:

   - A space is used as card seperator
   - Each card consists of two characters
   - The first character is the value of the card, valid characters are:
    2, 3, 4, 5, 6, 7, 8, 9, T(en), J(ack), Q(ueen), K(ing), A(ce)
   - The second character represents the suit, valid characters are:
    S(pades), H(earts), D(iamonds), C(lubs)

"""


class PokerHand:
    RESULT = ["Loss", "Tie", "Win"]

    def __init__(self, hand):
        self.hand = hand
        self.maximum = 0
        self.ordered = 'AKSQJST98765432A'

    @staticmethod
    def make_str(hand, switcher):
        """This function make string of card value or suit"""
        if switcher == 0:
            # Get a value of card (Ace, King, Queen, ..., 2)
            return ''.join([h[0] for h in hand.split()])
        elif switcher == 1:
            # Get a suit( Heart, Diamonds, etc.)
            return ''.join([h[1] for h in hand.split()])

    @staticmethod
    def sorted_funct(hand_str):
        card_value = {'A': 15, 'K': 14, 'Q': 13, 'J': 12, 'T': 10}
        reverse_card_value = {15: 'A', 14: 'K', 13: 'Q', 12: 'J', 10: 'T'}
        hand_int = []
        ordered = ''
        for h in hand_str:
            if h in card_value:
                hand_int.append(card_value.get(h))
            else:
                hand_int.append(int(h))
        for h_int in sorted(hand_int, reverse=True):
            if h_int > 9:
                ordered += reverse_card_value.get(h_int)
            else:
                ordered += str(h_int)
        return ordered

    def check_order(self, hand_card):
        """This method checking order of value card (98765 or AKQJT)"""
        # call 2 function for creating string and sorting it
        my_hand = self.sorted_funct(self.make_str(hand_card, 0))
        # start point to slice ordered string
        start = self.ordered.find(my_hand[0])
        if my_hand == self.ordered[start: start + 5]:
            return True
        else:
            return False

    def check_suit(self):
        """This method check, if suit is the same (all hearts or all diamonds)"""
        my_hand_suite = self.make_str(self.hand, 1)
        if (my_hand_suite == 'SSSSS' or my_hand_suite == 'DDDDD' or
            my_hand_suite == 'HHHHH' or my_hand_suite == 'CCCCC'):
            return True
        return False

    def count_value(self, number, my_hand_value, times):
        """Method count number of occurrences value"""
        if times == 1:
            for order in self.ordered:
                if my_hand_value.count(order) == number:
                    return True
        elif times == 2:
            counter = 0
            for order in self.ordered:
                if my_hand_value.count(order) == number:
                    counter += 1
            if counter == 2:
                return True
        return False

    def check_combination(self, hand_card):
        """Main logic of finding combination exept older card"""
        my_hand_value = self.sorted_funct(self.make_str(hand_card, 0))
        my_hand_suit = self.make_str(hand_card, 1)
        # Royal-flash
        if my_hand_value == 'AKQJT' and self.check_suit():
            return 1000
        # Steet-flash
        elif self.check_order(hand_card) and self.check_suit():
            return 800
        # Care
        elif self.count_value(4, my_hand_value, 1):
            return 600
        # Full-house
        elif (self.count_value(3, my_hand_value, 1) and
              self.count_value(2, my_hand_value, 1)):
            return 500
        # flash
        elif (my_hand_suit.count('S') == 5 or
              my_hand_suit.count('H') == 5 or
              my_hand_suit.count('D') == 5 or
              my_hand_suit.count('C') == 5):
            return 400
        # Street
        elif self.check_order(hand_card):
            return 300
        # Triple
        elif self.count_value(3, my_hand_value, 1):
            return 200
        # Two pairs
        elif self.count_value(2, my_hand_value, 2):
            return 150
        # One pair
        elif self.count_value(2, my_hand_value, 1):
            return 100
        return False

    @staticmethod
    def older_card(hand):
        # Check older card if no combination
        card_value = {'A': 15, 'K': 14, 'Q': 13, 'J': 12, 'T': 10}
        maximum = []
        for card in hand.split():
            if card[0] in card_value:
                maximum.append(card_value.get(card[0]))
            else:
                maximum.append(int(card[0]))
        return sum(maximum)

    def compare_with(self, other):
        if self.check_combination(self.hand):
            my_hand = self.check_combination(self.hand)
        else:
            my_hand = self.older_card(self.hand)
        if self.check_combination(other):
            other_hand = self.check_combination(other)
        else:
            other_hand = self.older_card(other)
        if my_hand > other_hand:
            return 'Win'
        elif my_hand < other_hand:
            return "Loss"
        else:
            my_hand = self.older_card(self.hand)
            other_hand = self.older_card(other)
            if my_hand > other_hand:
                return 'Win'
            elif my_hand < other_hand:
                return "Loss"
            else:
                return 'Tie'

first_hand = "2S AH 4H 5S 6C"
second_hand = "AD 4C 5H 6H 2C"


if __name__ == '__main__':
    P = PokerHand(first_hand)
    print(P.compare_with(second_hand))
