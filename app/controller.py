from flask import render_template, request, redirect
from app import app
from app.models.ai import *
from app.models.player import Player 
import random

# Setting up the routes for the webapp 
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/computer')
def welcome():
    return render_template("computer.html")

@app.route('/player')
def player():
    return render_template("player.html")

@app.route('/ai/<move>')
def ai(move):
    computer_choice = computer_move()
    player_move = move.lower()
    result = return_winner(player_move, computer_choice)

    return render_template("ai.html", ai_winner = result, player_move = player_move, computer_choice = computer_choice)

