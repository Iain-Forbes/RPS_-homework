from app.models.player import *
import random

Player


# Picks a random computer move from a list of three, using randint
def computer_move():
    choice = ["rock", "paper", "scissors"]
    return choice[random.randint(0,2)]

 
#PVP function
def pvp_winner(player1_move, player2_move):
    if player1_move == player2_move:
        pvp_winner = "tie"
    elif player1_move == "rock" and player2_move == "sissors":
        pvp_winner = "player1"
    elif player1_move == "paper" and player2_move == "rock":
        pvp_winner = "player1"
    elif player1_move == "scissors" and player2_move == "paper":
    

    return winner

# Function to return winner, computer set to default, if statement then compares play move to computer move, and either set plaeyer or computer to winner depending on choice
def return_winner(player_move, computer_choice):
    ai_winner = "computer"

    if player_move == computer_choice:
        ai_winner = "tie"
    elif player_move == "rock" and computer_choice == "sissors":
        ai_winner = "player"
    elif player_move == "paper" and computer_choice == "rock":
        ai_winner = "player"
    elif player_move == "scissors" and computer_choice == "paper":
        ai_winner = "player"

    return winner