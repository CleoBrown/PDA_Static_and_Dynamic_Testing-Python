import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("spades", 1)    
        self.card2 = Card("hearts", 3)
        self.card3 = Card("diamonds", 4)
        self.cardgame = CardGame()

    def test_check_for_ace_true(self):
        result = self.cardgame.check_for_ace(self.card1)
        self.assertEqual(result, True)

    def test_check_for_ace_false(self):
        result = self.cardgame.check_for_ace(self.card2)
        self.assertEqual(result, False)

    def test_highest_card(self):
        result = self.cardgame.highest_card(self.card2, self.card3) 
        self.assertEqual(result, self.card3)  

    def test_cards_total(self):
        result = self.cardgame.cards_total([self.card1, self.card2, self.card3])
        self.assertEqual(result, "You have a total of 8")