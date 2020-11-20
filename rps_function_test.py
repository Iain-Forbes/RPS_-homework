import random

def computer_move():
    move = ["rock", "paper", "scissors"]
    return move[random.randint(0,2)]

print (computer_move())

