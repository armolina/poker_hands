from utils.card_dealer import CardDealer
from vo.player_hand import PlayerHand
from utils.poker_hands import PokerHands

class Game():
    def __init__(self, game_hands) -> None:
        self.game_hands = game_hands;
        self.players = []

    def resolve_game(self):
        card_dealer = CardDealer(5)
        hands = card_dealer.deal_hands(self.game_hands)

        for player, hand in hands.items():
            player_hand = PlayerHand()
            poker_hands = PokerHands(hand)
            player_hand.player_name = player

            player_hand.higest_card = poker_hands.get_high_card()
            player_hand.pair = poker_hands.get_pair_in_hand()
            player_hand.pairs = poker_hands.get_pairs_in_hand()
            player_hand.tree = poker_hands.get_three_in_hand()

            self.players.append(player_hand)

        poker_hands.check_hands(self.players)
        return self.players
