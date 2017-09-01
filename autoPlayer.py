import copy


class AutoPlayer:

    def __init__(self, player_id):
        self.player_id = player_id
        self.hand = []
        self.hand_history = []

    def set_hand(self, hand):
        if len(self.hand) > 0:
            self.hand_history.append(copy.deepcopy(self.hand))
        self.hand = hand

    def get_player_id(self):
        return self.player_id

    def get_hand_history(self):
        return self.hand_history