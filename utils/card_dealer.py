from vo.player_hand import PlayerHand


class CardDealer():
    __hand_player_size: int
    number_players: int

    def __init__(self, hand_player_size: int):
        self.__hand_player_size=hand_player_size
        self.number_players = 0

    def deal_hands(self, hand: str):
        hand_split = hand.split()
        hand_cards_counter = 0
        hands_reparted = {}
        cards = []
        player_name = ''

        for value in hand_split:

            if(hand_cards_counter==0):
                player_name = value
                hands_reparted[player_name]={}
                hand_cards_counter += 1
            
            elif(hand_cards_counter > 0 and hand_cards_counter <=self.__hand_player_size+1):
                cards.append(str(value))
                hand_cards_counter += 1

                if hand_cards_counter == self.__hand_player_size+1:
                    hands_reparted[player_name]=cards
                    self.number_players += 1
                    hand_cards_counter=0
                    cards=[]
            
        return hands_reparted
        