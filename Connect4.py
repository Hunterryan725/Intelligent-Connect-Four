import numpy as np
import random
import time
import copy
import math

ROW_COUNT = 6
COLUMN_COUNT = 7

class Connect4:
    def __init__(self):
        self.board = np.zeros((ROW_COUNT,COLUMN_COUNT))
        self.w = 0
        self.turn = 1
        self.most_recent = [0,0]

    def initial_position(self):
        self.board = np.zeros((ROW_COUNT,COLUMN_COUNT))
        self.w = 0
        self.turn = 1
        self.most_recent = [0,0]

        return self
    
    # return the board
    def boardi(self):
        return self.board

    # get row to put next piece for a certain column
    def get_next_open_row(self, col):
        for r in range(ROW_COUNT):
            if self.board[r][col] == 0:
                return r

    # return next player
    def next_player(self):
        return ((self.turn + 1) % 2)
    
    # drop piece
    def result(self, col):
        row = self.get_next_open_row(col)
        piece = self.turn
        if piece == 0:
            piece = 2
        self.board[row][col] = piece
        self.most_recent = [row,col]
        self.turn +=1
        self.turn = (self.turn % 2)
        return self
    
    # check if there is room to drop a piece
    def is_valid_location(self, col):
        if col <0 or col >= COLUMN_COUNT:
            return 0
        return self.board[ROW_COUNT-1][col] == 0

    def legal_moves(self):
        valid_locations = []
        for col in range (COLUMN_COUNT):
            if self.is_valid_location(col):
                valid_locations.append(col)
        return valid_locations

    # print board
    def print_board(self):
        print(np.flip(self.board, 0))

    #return the winner
    def winner(self):
        return self.w
    
    # return if the move resulted in a win
    def winning_move(self, piece):
        r = self.most_recent[0]
        c = self.most_recent[1]

        left = max(c - 4, 0)
        right = min(c + 4, COLUMN_COUNT)
        top = max(r - 4, 0)
        bottom = min(r + 4, ROW_COUNT)

        #check left to right
        consecutive = 0
        for i in range(left,right):
            if self.board[r][i] == piece:
                consecutive +=1
            else: 
                consecutive = 0
            if consecutive == 4:
                self.w = piece
                return True
        
        consecutive = 0
        #check top to bottom
        for i in range(top,bottom):
            if self.board[i][c] == piece:
                consecutive +=1
            else: 
                consecutive = 0
            if consecutive == 4:
                self.w = piece
                return True
        
        #check positive-slope diagnonal
        consecutive = 0
        for i in range(-4,5):
            if (c+i >= 0) and (r-i < ROW_COUNT):
                if (c+i < COLUMN_COUNT) and (r-i >= 0):
                    if self.board[r-i][c+i] == piece:
                        consecutive +=1
                    else:
                        consecutive = 0
                    if consecutive == 4:
                        self.w = piece
                        return True

        #check negative-slope diagnonal
        consecutive = 0
        for i in range(-4,5):
            if (c+i >= 0) and (r+i < ROW_COUNT):
                if (c+i < COLUMN_COUNT) and (r+i >= 0):
                    if self.board[r+i][c+i] == piece:
                        consecutive +=1
                    else:
                        consecutive = 0
                    if consecutive == 4:
                        self.w = piece
                        return True

    # return a random move choice
    def random_choice(self):
        return random.choice(board.legal_moves())
    
    # return if game over
    def game_over(self):
        if len(self.legal_moves()) == 0:
            return True
        if self.winning_move(1):
            return True
        if self.winning_move(2):
            return True
    
    # return if it is a winning move
    def win_move(self):
        if self.winning_move(1) == 1 or self.winning_move(2) == 1:
            return 1
        return 0