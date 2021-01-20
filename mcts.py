import random
import copy
import math

#is move to capture or move again a better move

def mcts_strategy(iterations):
    def function(b):
        move_results = {}
        move_results[str(b.board)] = [0,0]

        for i in range(iterations):
            board = copy.deepcopy(b)
            moved = []
            move_results[str(b.board)][1] += 1
            moved.append(b)

            while not board.game_over():
                moves = board.legal_moves()
                not_moved_yet = []

                # get not yet made moves
                for move in moves:
                    board2 = copy.deepcopy(board)
                    next_board = board2.result(move)

                    if str(next_board.board) not in move_results:
                        not_moved_yet.append(move)

                # if there are moves that haven't been played
                if len(not_moved_yet) != 0:
                    move_to_make = random.choice(not_moved_yet)
                    board = board.result(move_to_make)
                    moved.append(copy.deepcopy(board))
                    move_results[str(board.board)] = [0,1] #wins/visits

                    # play the rest randomly
                    while not board.game_over():
                        moves = board.legal_moves()
                        move_to_make = random.choice(moves)
                        for move in moves:
                            board2 = copy.deepcopy(board)
                            next_board = board2.result(move)
                            if next_board.win_move():
                                move_to_make = move
                        board = board.result(move_to_make)    
                
                # else play move with highest UCB
                else:
                    # calculate ucb
                    curr = move_results[str(board.board)]
                    t = curr[1]
                    best_move = 0
                    ucb1 = float("-inf")
                    ucb2 = float("inf")

                    for move in moves:
                        board2 = copy.deepcopy(board)
                        next_board = board2.result(move)
                        data = move_results[str(next_board.board)]
                        r_j = data[0]/data[1]
                        n_j = data[1]
                        multiple = 1

                        #encourage exploring moves with a winner - with priority to winning moves
                        if next_board.winner() == 1 and next_board.next_player() == 0:
                            multiple = multiple*3
                        
                        elif next_board.winner() == 2 and next_board.next_player() == 1:
                            multiple = multiple*3
                        
                        elif next_board.win_move() == 1:
                            multiple = multiple*2
                        
                        # encourage exploring moves in the middle of the board
                        if move == 3:
                            multiple = multiple * 1.05
                        if move == 2 or move == 4:
                            multiple = multiple * 1.03
                        
                        # find best UCB depending on player
                        if board.next_player() == 0:
                            val = float(r_j +  math.sqrt((2 * math.log(t) * multiple) / n_j))
                            if (val > ucb1):
                                ucb1 = val
                                best_move = move

                        else:
                            val = float(r_j -  math.sqrt((2 * math.log(t) * multiple) / n_j))
                            if (val < ucb2):
                                ucb2 = val
                                best_move = move
                    
                    # make best move
                    board = board.result(best_move)
                    moved.append(copy.deepcopy(board))
                    move_results[str(board.board)][1] += 1
            
            value_of_game = board.winner()
            if value_of_game == 2:
                value_of_game = 0

            for move in moved:
                move_results[str(move.board)][0] += value_of_game

        b2 = copy.deepcopy(b)
        moves = b2.legal_moves()
        next_board = b2.result(moves[0])
        stats = move_results[str(next_board.board)]
        best_move = moves[0]
        best_move_stats = stats[0]/stats[1]
        for move in moves:
            b2 = copy.deepcopy(b)
            next_board = b2.result(move)
            stats = move_results[str(next_board.board)]

            # if move results in end_game, always make it
            if next_board.win_move() == 1:
                best_move = move
                break

            if b2.next_player() != 0:
                if (stats[0]/stats[1]) > best_move_stats:
                    best_move_stats = stats[0]/stats[1]
                    best_move = move
            else:
                if (stats[0]/stats[1]) < best_move_stats:
                    best_move_stats = stats[0]/stats[1]
                    best_move = move
        
        return best_move

    return function