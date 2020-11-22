from app.models.player import *
import random

# Establish Game Class
class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.choice = ["rock", "paper", "scissors"]
        
    
    
# Determin winner of Player vs Player Battle
    def pvp_result(self, player1, player2):
        
        pvp_winner = self.player2.name

        if self.player1.move == self.player2.move:
            pvp_winner = "tie"
        elif self.player1.move == "rock" and self.player2.move == "scissors":
            pvp_winner = self.player1.name
        elif self.player1.move == "paper" and self.player2.move == "rock":
            pvp_winner = self.player1.name
        elif self.player1.move == "scissors" and self.player2.move == "paper":
            pvp_winner = self.player1.name

        return pvp_winner
        

 # Function to return winner of an AI game, sets second player as the computer and uses random choice to return a move, off the moves list setup the game class, then uses same set of IF statments from PVP to set winner. 
  
    def play_computer(self, player, computer):   
        if self.player2.name == "Computer" and self.player2.move == "com":
            self.player2.move = random.choice(list(self.choice)) 
        
        ai_winner = self.player2.name
        
        if self.player1.move == self.player2.move:
            ai_winner = "a tie"
        elif self.player1.move == "rock" and self.player2.move == "sissors":
            ai_winner = self.player1.name
        elif self.player1.move == "paper" and self.player2.move == "rock":
            ai_winner = self.player1.name
        elif self.player1.move == "scissors" and self.player2.move == "paper":
            ai_winner = self.player1.name

        return ai_winner

    