import random
import copy

SUITS = ["C", "D", "H", "S"]
RANKS = [2, 3, 4, 5, 6, 7, 8, 9, "T", "J", "Q", "K", "A"]

class Game:
    def poker(self, hands):
        scores = [(i, self.score(hand)) for i, hand in enumerate(hands)]
        winner = sorted(scores, key=lambda x: x[1])[-1][0]
        self.winner = winner
        return hands[winner]

    def score(self, hand):
        ranks = '23456789TJQKA'
        #   index (value)  "<rank><suite><rank><suite>..."  r=<rank> _=<suite>  hand=["<rank><suite>", ...]
        rcounts = {ranks.find(r): ''.join(hand).count(r) for r, _ in hand}.items()
        score, ranks = zip(*sorted((cnt, rank) for rank, cnt in rcounts)[::-1])
        if len(score) == 5: # All cards are different
            if ranks[0:2] == (12, 3):  # adjust if 5 high straight
                ranks = (3, 2, 1, 0, -1)
            straight = ranks[0] - ranks[4] == 4
            flush = len({suit for _, suit in hand}) == 1
            '''no pair, straight, flush, or straight flush'''
            score = ([(1,), (3, 1, 1, 1)], [(3, 1, 1, 2), (5,)])[flush][straight]
        return score, ranks

    def __init__(self):
        hands = None
        self.number_of_changes = 0
        self.number_of_players = 0
        self.winning_hand = []
        self.winner = -1
        self.more_rounds = False

    def deal_cards(self, number_of_players, number_of_cards, number_of_rounds):
        """Takes a number of players and a number of cards and returns a list of list of player hands."""

        self.deck = ["{}{}".format(r, s) for s in SUITS for r in RANKS]
        self.number_of_players = number_of_players
        self.number_of_changes = 0
        self.number_of_rounds = number_of_rounds
        self.more_rounds = True

        if len(self.deck) < number_of_players * number_of_cards:
            print("Not enough cards")
            return None

        self.hands = [[] for i in range(number_of_players)]
        random.shuffle(self.deck)
        for i in range(number_of_cards):
            for j in range(number_of_players):
                self.hands[j].append(self.deck[0])
                del self.deck[0]
        return copy.deepcopy(self.hands)

    def get_new_cards(self, dropped_cards, player_index=1): # TODO This index shouldn't be hard coded.
        # handle the player
        if player_index == self.number_of_players - 1:
            self.number_of_changes += 1
        new_cards = []
        for dropped_card in dropped_cards:
            dropped_card_index = self.hands[player_index].index(dropped_card)
            del self.hands[player_index][dropped_card_index]
            self.hands[player_index].append(self.deck[0])
            new_cards.append(self.deck[0])
            del self.deck[0]
        self.more_rounds = self.number_of_changes < self.number_of_rounds
        if not self.more_rounds:
            self.winning_hand = self.poker(self.hands)
        return new_cards

    def get_player_hand(self, player_id):
        return copy.deepcopy(self.hands[player_id])

    def get_winning_hand(self):
        return self.winner, self.winning_hand

    def is_game_active(self):
        return self.more_rounds

    def get_all_hands(self):
        return self.hands
