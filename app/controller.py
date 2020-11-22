from flask import render_template, request, redirect
from app import app
from app.models.player import Player 
from app.models.game import *
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
    player1 = Player("player1", move)
    player2 = Player("Computer", "com")
    game = Game(player1, player2)
    result = game.play_computer(player1, player2)
    
    return render_template("ai.html", ai_winner = result, move1=player1.move, move2=player2.move)

@app.route('/player/<move1>/<move2>')
def game(move1, move2):
    player1 =  Player("player1", move1)
    player2 =  Player("player2", move2)
    game = Game(player1, player2)
    result = game.pvp_result(player1, player2)
    return render_template("result.html", pvp_winner = result, move1 = move1, move2 = move2)
