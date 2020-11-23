from app.models.player import *
import random

# Establish Game Class
class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.choice = ["rock", "paper", "scissors"]
        
    
    
# Determin winner of RPS, if player 2 name is set to computer and move is set to an empty string it then uses random.choice to pick a move, simulating and AI game.
    def winner(self, player1, player2):
        if self.player2.name == "Computer" and self.player2.move == "com":
            self.player2.move = random.choice(list(self.choice)) 
        
        winner = self.player2.name

        if self.player1.move == self.player2.move:
            winner = "tie"
        elif self.player1.move == "rock" and self.player2.move == "scissors":
            winner = self.player1.name
        elif self.player1.move == "paper" and self.player2.move == "rock":
            winner = self.player1.name
        elif self.player1.move == "scissors" and self.player2.move == "paper":
            winner = self.player1.name

        return winner
        

    