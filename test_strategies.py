import random
import sys
import copy
import minimax
import mcts
import math

from Connect4 import Connect4

def random_choice(position):
    moves = position.legal_moves()
    return random.choice(moves)


def compare_strategies(board, p1, p2, games, prob, p1_name, p2_name):
    p1_wins = 0
    p2_wins = 0

    for i in range(games):
        p1_strat = p1()
        p2_strat = p2()
        position = board.initial_position()
        
        while not position.game_over():
            if random.random() < prob:
                if position.next_player() == 0:
                    if p1_name == "Minimax":
                        move = p1_strat(position, -math.inf, math.inf)
                    else:
                        move = p1_strat(position)
                else:
                    if p2_name == "Minimax":
                        move = p2_strat(position, -math.inf, math.inf)
                    else:
                        move = p2_strat(position)
            else:
                move = random_choice(position)
            position = position.result(move)
            
        if position.winner() == 0:
            p1_wins += 0.5
            p2_wins += 0.5
        
        elif (position.winner() == 1):
            print(p1_name + " win as 1st move!")
            p1_wins += 1
        else:
            print(p2_name + " win as 2nd move!")
            p2_wins += 1
    
    return p1_wins / games

def test_game(count, depth, p_random, strat_1, strat_2, iterations):
    
    # create board
    board = Connect4()
    i = (depth) % 2

    # load strategies
    if (strat_1 == 1):
        p1_strategy_fxn = mcts.mcts_strategy(iterations)
        p1 = "MCTS"
    elif (strat_1 == 2):
        p1_strategy_fxn = minimax.minimax_strategy(depth, i)
        p1 = "Minimax"
    elif (strat_1 == 3):
        p1_strategy_fxn = minimax.random_strategy()
        p1 = "Random"
    else:
        p1_strategy_fxn = minimax.player_strategy()
        p1 = "Player2"
    
    if (strat_2 == 1):
        p2_strategy_fxn = mcts.mcts_strategy(iterations)
        p2 = "MCTS"
    elif (strat_2 == 2):
        p2_strategy_fxn = minimax.minimax_strategy(depth, i)
        p2 = "Minimax"
    elif (strat_2 == 3):
        p2_strategy_fxn = minimax.random_strategy()
        p2 = "Random"
    else:
        p2_strategy_fxn = minimax.player_strategy()
        p2 = "Player2"
    
    # run test
    win_pct = compare_strategies(board, lambda: p1_strategy_fxn, lambda: p2_strategy_fxn, count, 1.0 - p_random,p1,p2)

    # output results
    print("Player 1: " + p1 + " win rate " + str(win_pct))
    print("Player 2: " + p2 + " win rate " + str(1.0-win_pct))



if __name__ == '__main__':
# Main function - drive testing
    if len(sys.argv) == 7:
        count = int(sys.argv[1])  # number of times running the test
        p_random = float(sys.argv[2]) # percent of moves random
        strat_1 = int(sys.argv[3]) # strategy for player 1 - 1 = MCTS, 2 = Minimax, 3 = Random, 4 = Player input
        strat_2 = int(sys.argv[4]) # strategy for player 2 - 1 = MCTS, 2 = Minimax, 3 = Random, 4 = Player input
        depth = int(sys.argv[5]) # depth of minimax
        iterations = int(sys.argv[6])  # iterations for MCTS 
        test_game(count, depth, p_random, strat_1, strat_2, iterations)
        sys.exit(0)