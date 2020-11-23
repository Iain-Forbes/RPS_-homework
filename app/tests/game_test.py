import unittest

from app.models.game import *
from app.models.player import * 

class GameTest(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Player 1", "rock")
        self.player2 = Player("Player 2", "paper")
        self.player3 = Player("Player 3", "scissors")
        self.game = Game(self.player1, self.player2)

    # def test_player_1_win(self):
    #     self.game.pvp_result(self.player1.move, self.player2.move)
    #     self.assertEqual(self.player1.name, self.player1.name)
        