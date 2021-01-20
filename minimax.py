import random
import math
import copy

# function to pass random playing of moves
def random_choice(position):
    moves = position.legal_moves()
    return random.choice(moves)

# randomly play moves
def random_strategy():
    def fxn(pos):
        move = random_choice(pos)
        return move
    return fxn

# function to allow player to pass arguments personally
def player_strategy():
    def fxn2(pos):
        pos.print_board()
        while True:
            move = int(input("Player 1 make your selection (0-6):"))
            if pos.is_valid_location(move):
                break
            else:
                print("Invalid move, please go again!")
        return move
    return fxn2

# used to calculate scores for certain positions
def score_board(subset, piece):
    h = 0
    opp_piece = 1
    if piece == 1:
        opp_piece = 2

    # Add good positions
    if subset.count(piece) == 4:
        h += 10000000000
    elif subset[0] == piece and subset[1] == piece and subset[2] == piece:
        h += 6
    elif subset[1] == piece and subset[2] == piece and subset[3] == piece:
        h += 6
    elif subset.count(piece) == 3 and subset.count(0) == 1:
        h += 4
    elif subset.count(piece) == 2 and subset.count(0) == 2:
        h += 1

    # Subtract Opponent good positions
    if subset.count(opp_piece) == 4 and subset.count(0) == 1:
        h -= 100000000
    elif subset[0] == opp_piece and subset[1] == opp_piece and subset[2] == opp_piece:
        h -= 5
    elif subset[1] == opp_piece and subset[2] == opp_piece and subset[3] == opp_piece:
        h -= 5
    elif subset.count(opp_piece) == 3 and subset.count(0) == 1:
        h -= 3
    
    # Incentivize Blocking an opponent 3 in a row
    if  subset.count(opp_piece) == 3 and subset.count(piece) == 1:
        h += 20

    return h

# used to calculate heuristic for minimax
def heuristic(board, piece):
    h = 0
    board = board.board

    # Score center positions
    center_array = [int(i) for i in list(board[:, 7//2])]
    center_count = center_array.count(piece)
    h += center_count * 3

    # Score horizontal positions
    for r in range(6):
        row = [i for i in list(board[r,:])]
        for c in range(7-3):
            row_subset = row[c:c+4]
            h += score_board(row_subset, piece)

    ## Score vertical positions
    for c in range(7):
        column = [i for i in list(board[:,c])]
        for r in range(3):
            col_subset = column[r:r+4]
            h += score_board(col_subset, piece)

    ## Score upward sloped diagonal positions
    for r in range(3):
        for c in range(4):
            diag = [board[r+i][c+i] for i in range(4)]
            h += score_board(diag, piece)

    ## Score downward sloped diagonal positions
    for r in range(3):
        for c in range(4):
            diag = [board[r+3-i][c+i] for i in range(4)]
            h += score_board(diag, piece)

    return h


# function to pass minimax algorithm
def minimax_strategy(depth, maximizer):
    def fxn3(pos, alpha, beta):
        value, move = minimax(pos, depth, alpha, beta, maximizer)
        return move
    return fxn3

# minimax algorithm
def minimax(pos, depth, alpha, beta, maximizer):
    
    piece = pos.next_player()
    if piece == 0:
        piece = 2

    if pos.game_over() or depth == 0:
        return (heuristic(pos, piece), None)
    else:
        if maximizer == 1:
            best_val = -math.inf
            move_to_make = None
            moves = pos.legal_moves()
            for move in moves:
                pos2 = copy.deepcopy(pos)
                child = pos2.result(move)
                mmax, _ = minimax(child, depth - 1, alpha, beta, 0)
                if mmax > best_val:
                    best_val = mmax
                    move_to_make = move
                alpha = max(alpha, mmax)
                if alpha >= beta:
                    break
            return (best_val, move_to_make)
            
        else:
            best_val = math.inf
            move_to_make = None
            moves = pos.legal_moves()
            for move in moves:
                pos2 = copy.deepcopy(pos)
                child = pos2.result(move)
                mmax, _ = minimax(child, depth - 1, alpha, beta, 1)
                if mmax < best_val:
                    best_val = mmax
                    move_to_make = move
                beta = min(beta, mmax)
                if alpha >= beta:
                    break
            return (best_val, move_to_make)