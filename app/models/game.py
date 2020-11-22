from app.models.player import *
import random


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.choice = ["rock", "paper", "scissors"]
        
        #PVP function
    
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
        
    # def computer_move(self):
    #     return random.choice(list(self.choice))

 # Function to return winner,if statement compares play move to computer move, and either set plaeyer or computer to winner depending on choice
  
    def play_computer(self, player, computer):   
        if self.player2.name == "Computer" and self.player2.move == "com":
            self.player2.move = random.choice(list(self.choice)) 
        
        ai_winner = self.player2.name
        
        if self.player1.move == self.player2.move:
            ai_winner = "tie"
        elif self.player1.move == "rock" and self.player2.move == "sissors":
            ai_winner = self.player1.name
        elif self.player1.move == "paper" and self.player2.move == "rock":
            ai_winner = self.player1.name
        elif self.player1.move == "scissors" and self.player2.move == "paper":
            ai_winner = self.player1.name

        return ai_winner

    