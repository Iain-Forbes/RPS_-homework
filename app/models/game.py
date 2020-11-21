class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        #PVP function
    
def pvp_result(player1_move, player2_move):
    pvp_winner = "player2"

    if player1_move == player2_move:
        pvp_winner = "tie"
    elif player1_move == "rock" and player2_move == "scissors":
        pvp_winner = "player1"
    elif player1_move == "paper" and player2_move == "rock":
        pvp_winner = "player1"
    elif player1_move == "scissors" and player2_move == "paper":
        pvp_winner = "player1"

    return pvp_winner