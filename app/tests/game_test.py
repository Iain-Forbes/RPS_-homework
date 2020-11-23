import unittest

from app.models.game import *
from app.models.player import * 

class GameTest(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Player 1", "rock")
        self.player2 = Player("Player 2", "paper")
        self.player3 = Player("Player 3", "scissors")
        self.game = Game(self.player1, self.player2)
        self.game2 = Game(self.player1, self.player3)
        self.game3 = Game(self.player2, self.player3)

    def test_game_winner_paper_win(self):
        self.game.winner(self.player1, self.player2)
        self.assertEqual('Player 2', self.player2.name)
    

    def test_game2_winner_rock_win(self):
        self.game2.winner(self.player1, self.player3)
        self.assertEqual('Player 1', self.player1.name)

    def test_game2_winner_scissors_win(self):
        self.game2.winner(self.player2, self.player3)
        self.assertEqual('Player 3', self.player3.name)
        
        