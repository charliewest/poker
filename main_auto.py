from game import Game
from randomPlayer import RandomPlayer

NUMBER_OF_PLAYERS = 2
NUMBER_OF_CARDS = 5
NUMBER_OF_ROUNDS = 3

game_engine = Game()
players = []

# Create a number of players
for i in range(NUMBER_OF_PLAYERS):
    players.append(RandomPlayer(i))

hands = game_engine.deal_cards(NUMBER_OF_PLAYERS, NUMBER_OF_CARDS, NUMBER_OF_ROUNDS)

for hand, player in zip(hands, players):
    player.set_hand(game_engine.get_player_hand(player.get_player_id()))

game_active = True

round_num = 0
while game_engine.is_game_active():
    round_num += 1
    for player, hand in zip(players, hands):
        print("PLAYER {}, ROUND {} - {}.".format(player.get_player_id(),
                                                 round_num,
                                                 game_engine.get_player_hand(player.get_player_id())))
        dropped_cards = player.get_cards_to_drop()
        new_cards = game_engine.get_new_cards(dropped_cards, player.get_player_id())

        player.set_hand(game_engine.get_player_hand(player.get_player_id()))

print("\n\nGAME OVER\n\nWinning Hand: {}".format(game_engine.get_winning_hand()))

for player in players:
    print(player.get_hand_history())