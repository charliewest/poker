import random
SUITS = ["C", "D", "H", "S"]
RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

class Game:

    def __init__(self):
        hands = None
        self.number_of_changes = 0

    def deal_cards(self, number_of_players, number_of_cards):
        self.deck = ["{} of {}".format(r, s) for s in SUITS for r in RANKS]

        if len(self.deck) < number_of_players * number_of_cards:
            print("Not enough cards")
            return None

        self.hands = [[] for i in range(number_of_players)]
        random.shuffle(self.deck)
        for i in range(number_of_cards):
            for j in range(number_of_players):
                self.hands[j].append(self.deck[0])
                del self.deck[0]
        return self.hands

    def get_new_cards(self, dropped_cards):
        # handle the player
        print(self.hands[1])
        self.number_of_changes += 1
        new_cards = []
        for dropped_card in dropped_cards:
            dropped_card_index = self.hands[1].index(dropped_card)
            del self.hands[1][dropped_card_index]
            self.hands[1].append(self.deck[0])
            new_cards.append(self.deck[0])
            del self.deck[0]
        print(self.hands[1])
        return self.number_of_changes != 3, new_cards
