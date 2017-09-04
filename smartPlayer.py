from autoPlayer import AutoPlayer
import itertools
import copy

class SmartPlayer(AutoPlayer):

    def get_cards_to_drop(self):
        cards_to_drop = copy.deepcopy(self.hand)

        for card_outer_loop, card_inner_loop in itertools.combinations(self.hand, 2):
            if card_outer_loop[0] == card_inner_loop[0]:
                if card_outer_loop in cards_to_drop:
                    del cards_to_drop[cards_to_drop.index(card_outer_loop)]
                if card_inner_loop in cards_to_drop:
                    del cards_to_drop[cards_to_drop.index(card_inner_loop)]

        return cards_to_drop