from flask import render_template, request, redirect
from app import app
from app.models.rps import *
from app.models.player import Player 
import random

# Setting up the routes for the webapp 
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")


@app.route('/ai/<move>')
def rps(move):
    computer_choice = computer_move()
    player_move = move.lower()
    result = return_winner(player_move, computer_choice)

    return render_template("ai.html", winner = result, player_move = player_move, computer_choice = computer_choice)

