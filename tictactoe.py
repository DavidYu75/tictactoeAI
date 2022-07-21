"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy
import random

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
    x_turns = 0
    o_turns = 0
    empty_spaces = 0

    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == EMPTY:
                empty_spaces += 1
            elif board[r][c] == X:
                x_turns += 1
            else:
                o_turns += 1
    if x_turns > o_turns:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == EMPTY:
                possible_actions.add((r, c))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]

    if i not in [0, 1, 2] or j not in [0, 1, 2]:
        raise Exception("That was not a valid input")
    if board[i][j] != EMPTY:
        raise Exception("That was not a valid input")

    copy_of_board = deepcopy(board)
    copy_of_board[i][j] = player(board)

    return copy_of_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        x_count = 0
        o_count = 0
        for c in row:
            if c == X:
                x_count += 1
            elif c == O:
                o_count += 1
            else:
                pass
        if x_count == 3:
            return X
        elif o_count == 3:
            return O
        else:
            pass

    # Check columns
    for column in range(3):
        x_count = 0
        o_count = 0
        for row in range(3):
            if board[row][column] == X:
                x_count += 1
            elif board[row][column] == O:
                o_count += 1
            else:
                pass
        if x_count == 3:
            return X
        elif o_count == 3:
            return O
        else:
            pass

    # Check Diagonals
    for diagonal in range(2):
        col = 0
        if diagonal == 1:
            col = 2
        x_count = 0
        o_count = 0
        for row in range(3):
            if board[row][col] == X:
                x_count += 1
            elif board[row][col] == O:
                o_count += 1
            else:
                pass
            if diagonal == 0:
                col += 1
            else:
                col -= 1
        if x_count == 3:
            return X
        elif o_count == 3:
            return O
        else:
            pass

    # If no winner, return None
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    game_over = True
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == EMPTY:
                game_over = False
    return game_over


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

    
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            best_move = max_action(board)[1]
            return best_move
        else:
            best_move = min_action(board)[1]
            return best_move


def max_action(board):
    """
    Helper method for finding the action that would give the max value in a given board
    """
    if terminal(board):
        return utility(board), None

    value = - math.inf
    best_action = None
    action_set = actions(board)

    for action in action_set:
        # Picks a random action if AI starts the game, more optimal
        if len(action_set) >= 9:
            best_action = random.choice(tuple(action_set))
            break
        min_result = min_action(result(board, action))
        if min_result[0] > value:
            best_action = action
            value = min_result[0]
    return value, best_action


def min_action(board):
    """
    Helper method for finding the action that would give the min value in a given board
    """
    if terminal(board):
        return utility(board), None

    value = + math.inf
    best_action = None
    action_set = actions(board)

    for action in action_set:
        max_result = max_action(result(board, action))
        if max_result[0] < value:
            best_action = action
            value = max_result[0]
    return value, best_action
