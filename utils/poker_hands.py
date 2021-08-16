from typing import List
from vo.player_hand import PlayerHand


class PokerHands():
    hand_hierarchy = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, player_hand) -> None:
        self.player_hand = player_hand

    def get_high_card(self):
        higher_value = 0
        highest_card = ""

        for card in self.player_hand:
            number=card[0]
            suit=card[1]

            if(self.hand_hierarchy.index(number)>=higher_value):
                higher_value = self.hand_hierarchy.index(number)
                highest_card = card

        return highest_card

    def compare_two_cards(self, card1, card2):
        value_card1 = self.hand_hierarchy.index(card1[0])
        value_card2 = self.hand_hierarchy.index(card2[0])

        if(value_card1>value_card2):
            return 1
        elif(value_card2>value_card1):
            return 2
        else:
            return 0

    def get_pair_in_hand(self):
        value_hash_map = {}

        for card in self.player_hand:

            if(str(card[0]) in value_hash_map):
                existent_cards = value_hash_map[str(card[0])]
                existent_cards.append(card)
                value_hash_map[str(card[0])] = existent_cards
  
            else:
                existent_cards = []
                existent_cards.append(card)

                value_hash_map[str(card[0])] = {}
                value_hash_map[str(card[0])] = existent_cards

    
        for value, cards in value_hash_map.items():
            if len(cards)==2:
                return cards
        
        return None

    def get_pairs_in_hand(self):
        value_hash_map = {}

        for card in self.player_hand:

            if(str(card[0]) in value_hash_map):
                existent_cards = value_hash_map[str(card[0])]
                existent_cards.append(card)
                value_hash_map[str(card[0])] = existent_cards
  
            else:
                existent_cards = []
                existent_cards.append(card)

                value_hash_map[str(card[0])] = {}
                value_hash_map[str(card[0])] = existent_cards

        pairs = []
        num_pairs = 0

        for value, cards in value_hash_map.items():
            if len(cards)==2:
                pairs.append(cards)
                num_pairs +=1
        
        if(num_pairs == 2):
            return pairs
        else:
            return None

    def get_three_in_hand(self):
        value_hash_map = {}

        for card in self.player_hand:

            if(str(card[0]) in value_hash_map):
                existent_cards = value_hash_map[str(card[0])]
                existent_cards.append(card)
                value_hash_map[str(card[0])] = existent_cards
  
            else:
                existent_cards = []
                existent_cards.append(card)

                value_hash_map[str(card[0])] = {}
                value_hash_map[str(card[0])] = existent_cards

    
        for value, cards in value_hash_map.items():
            if len(cards)==3:
                return cards
        
        return None

    def check_hands(self, players_hands: List[PlayerHand]):
        for player_hand in players_hands:
            if player_hand.tr
            pass
