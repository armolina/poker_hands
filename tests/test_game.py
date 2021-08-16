from game import Game

def test_given_white_winner_for_highest_card_A2():
    game_hands = "Black: 2H 3D 5S 9C KD White: 2C 3H 4S 8C AH Yellow: 4H 2D 6S 9C 3D"
    game = Game(game_hands)
    result = game.resolve_game()

    assert(result == 'White wins. - with high card: Ace ')

def test_given_white_winner_for_pairs_yellow():
    game_hands = "Black: 2H 3D 5S 9C KD White: 2C 3H 4S 8C AH Yellow: 4H 4D 6S 9C 3D"
    game = Game(game_hands)
    result = game.resolve_game()

    assert(result == 'White wins. - with high card: Ace ')

def test_given_white_winner_for_double_pairs_yelow():
    game_hands = "Black: 3H 3D 4S 9C KD White: 2C 2H 4S 8C AH Yellow: 4H 4D 6S 6C 3D"
    game = Game(game_hands)
    result = game.resolve_game()

    assert(result == 'White wins. - with high card: Ace ')


def test_given_white_winner_for_double_pairs_yelow():
    game_hands = "Black: 3H 3D 3S 9C KD White: 2C 2H 4S 8C AH Yellow: 4H 4D 6S 6C 3D"
    game = Game(game_hands)
    result = game.resolve_game()

    assert(result == 'White wins. - with high card: Ace ')