from game import Game
from randomPlayer import RandomPlayer
from smartPlayer import SmartPlayer

NUMBER_OF_PLAYERS = 2
NUMBER_OF_CARDS = 5
NUMBER_OF_ROUNDS = 3
NUMBER_OF_GAMES = 10000

game_engine = Game()

number_of_games_played = 0
winners = [0, 0]

while number_of_games_played < NUMBER_OF_GAMES:
    number_of_games_played += 1
    players = []

    # Create a number of players
    for i in range(NUMBER_OF_PLAYERS - 1):
        players.append(RandomPlayer(i))

    players.append(SmartPlayer(NUMBER_OF_PLAYERS - 1))

    game_engine.deal_cards(NUMBER_OF_PLAYERS, NUMBER_OF_CARDS, NUMBER_OF_ROUNDS)

    for player in players:
        player.set_hand(game_engine.get_player_hand(player.get_player_id()))

    game_active = True

    round_num = 0

    while game_engine.is_game_active():
        round_num += 1
        for player in players:
            dropped_cards = player.get_cards_to_drop()
            new_cards = game_engine.get_new_cards(dropped_cards, player.get_player_id())

            player.set_hand(game_engine.get_player_hand(player.get_player_id()))

    # print("{}".format(game_engine.get_all_hands()))
    winner, winning_hand = game_engine.get_winning_hand()
    # print("\n\nGAME OVER\n\nPlayer {} won with: {}".format(winner, winning_hand))
    winners[winner] += 1

print("Player 0 won {} times and Player 1 won {} times (out of {})".format(winners[0], winners[1], NUMBER_OF_GAMES))
print(winners[1] / NUMBER_OF_GAMES)