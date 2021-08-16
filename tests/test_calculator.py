from utils.poker_hands import PokerHands
from utils.card_dealer import CardDealer
from game import Game

def test_given_split_in_hands():
    input = "Black: 2H 3D 5S 9C KD White: 2C 3H 4S 8C AH Yellow: 4H 2D 6S 9C 3D"
    
    card_dealer = CardDealer(5)
    result = card_dealer.deal_hands(input)
    
    assert(result['Black:']==['2H', '3D', '5S', '9C', 'KD'])
    assert(result['White:']==['2C', '3H', '4S', '8C', 'AH'])
    assert(result['Yellow:']==['4H', '2D', '6S', '9C', '3D'])

def test_get_higer_value_in_hand():
    input1 = ["2C", "3H", "4S", "8C", "AH"]
    input2 = ["4H", "2D", "6S", "9C", "3D"]
    input3 = ["JH", "2D", "6S", "9C" "3D"]

    poker_hand1 = PokerHands(input1)
    poker_hand2 = PokerHands(input2)
    poker_hand3 = PokerHands(input3)

    result1 = poker_hand1.get_higher_card()
    result2 = poker_hand2.get_higher_card()
    result3 = poker_hand3.get_higher_card()
    
    assert(result1 == 'AH')
    assert(result2 == '9C')
    assert(result3 == 'JH')

def test_get_highest_card_between_two():
    card1 = "AH"
    card2 = "KH"

    poker_hands = PokerHands()
    result = poker_hands.compare_two_cards(card1, card2)
    assert(result==1)

def test_get_a_pair_in_hand():
    input = ["2H", "3D", "KS", "9C", "KD"]
    poker_hands = PokerHands(input)
    result = poker_hands.get_pair_in_hand()
    assert(result==["KS", "KD"])

def test_get_two_pairs_in_hand():
    input = ["2H", "2D", "KS", "9C", "KD"]
    poker_hands = PokerHands(input)
    result = poker_hands.get_pairs_in_hand()
    assert(result==[["2H", "2D"],['KS', 'KD']])

# High Card: Hands which do not fit any higher category are ranked by the value of their highest card. If the highest cards have the same value, the hands are ranked by the next highest, and so on.
# Pair: 2 of the 5 cards in the hand have the same value. Hands which both contain a pair are ranked by the value of the cards forming the pair. If these values are the same, the hands are ranked by the values of the cards not forming the pair, in decreasing order.
# Two Pairs: The hand contains 2 different pairs. Hands which both contain 2 pairs are ranked by the value of their highest pair. Hands with the same highest pair are ranked by the value of their other pair. If these values are the same the hands are ranked by the value of the remaining card.
# Three of a Kind: Three of the cards in the hand have the same value. Hands which both contain three of a kind are ranked by the value of the 3 cards.
# Straight: Hand contains 5 cards with consecutive values. Hands which both contain a straight are ranked by their highest card.
# Flush: Hand contains 5 cards of the same suit. Hands which are both flushes are ranked using the rules for High Card.
# Full House: 3 cards of the same value, with the remaining 2 cards forming a pair. Ranked by the value of the 3 cards.
# Four of a kind: 4 cards with the same value. Ranked by the value of the 4 cards.
# Straight flush: 5 cards of the same suit with consecutive values. Ranked by the highest card in the hand.
