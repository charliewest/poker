from autoPlayer import AutoPlayer
import random


class RandomPlayer(AutoPlayer):

    def get_cards_to_drop(self):
        dropped_cards = random.sample(self.hand, random.randint(0, len(self.hand)))
        print("Dropping {} cards, {}".format(len(dropped_cards), dropped_cards))
        return dropped_cards
