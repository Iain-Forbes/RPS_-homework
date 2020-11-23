import unittest

from app.models.game import *
from app.models.player import * 

class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Player 1", "rock")
        self.player2 = Player("Player 2", "paper")

    def test_player1_has_name(self):
        self.assertEqual("Player 1", self.player1.name)

    def test_player2_has_move(self):
        self.assertEqual("paper", self.player2.move)