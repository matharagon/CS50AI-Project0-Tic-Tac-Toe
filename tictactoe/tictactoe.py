"""
Tic Tac Toe Player
"""

import math
import random
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    n = 0 
    for i in range(3):
        for j in range(3):
            if board[i][j] is not None:
                n+=1  
    if n % 2 == 1: 
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = {(i,j) for i in range(3) for j in range(3) if board[i][j] is None}

    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError("This is not a valid move!")

    board_copy = copy.deepcopy(board)

    board_copy[action[0]][action[1]] = player(board_copy)

    return board_copy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    X = "X"
    O = "O"
    EMPTY = None
    ## determine who's turn it is
    turn = player(board)

    if turn == X:
        possible_winner = O
    else:
        possible_winner = X

    ## checks for columns

    for j in range(3):
        if all(val == possible_winner for val in [board[0][j], board[1][j], board[2][j]]) and None not in [board[0][j], board[1][j], board[2][j]]:
            return possible_winner
    
    ## checks for rows

    for i in range(3):
        if all(val == possible_winner for val in board[i]) and None not in board[i]:
            return possible_winner

    ## checks for diagonals 

    if all(val == possible_winner for val in [board[0][0], board[1][1], board[2][2]]) and None not in [board[0][0], board[1][1], board[2][2]]:
        return possible_winner
    elif all(val == possible_winner for val in [board[0][2], board[1][1], board[2][0]]) and None not in [board[0][2], board[1][1], board[2][0]]:
        return possible_winner
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == 'X' or winner(board) == 'O':
        return True
    elif winner(board) is None and not any([None in board[i] for i in range(3)]):
        return True
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board): 
        if winner(board) == 'X':
            return 1
        elif winner(board) == 'O':
            return -1
        else:
            return 0

def minimax_value(board):
    if terminal(board):
        return utility(board)
    
    if player(board)=='X':
        v = -math.inf
        for action in actions(board):
            new_board = result(board, action)
            v = max(v, minimax_value(new_board))
        return v
    else:
        v = math.inf
        for action in actions(board):
            new_board = result(board, action)
            v = min(v, minimax_value(new_board))
        return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board): 
        return None

    if player(board) == 'X':
        if board == initial_state():
            return random.choice(list(actions(board)))
        else: 
            best_value = -math.inf
            best_action = None
            for action in actions(board):
                new_board = result(board, action)
                value = minimax_value(new_board)
                if value > best_value:
                    best_value = value
                    best_action = action
            return best_action    
                
    else:
        best_value = math.inf
        best_action = None
        for action in actions(board):
            new_board = result(board, action)
            value = minimax_value(new_board)
            if value < best_value:
                best_value = value
                best_action = action
        return best_action

          
