"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
NTRIALS = 10        # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player


def mc_trial(board, player):
    """
    This function takes a current board and the next player to move.
    It then plays a game starting with the given player by making
    random moves, alternating between players. The function returns when
    the game is over. The modified board contains the state of the game,
    so the function does not return anything.
    """
    while board.check_win() == None:
        empty_squares = board.get_empty_squares()
        random_square = random.choice(empty_squares)
        board.move(random_square[0], random_square[1], player)
        player = provided.switch_player(player)


def mc_update_scores(scores, board, player):
    """
    This function takes a grid of scores (a list of lists) with the same
    dimensions as the Tic-Tac-Toe board, a board from a completed game,
    and which player the machine player is. It then scores the completed
    board and updates the scores grid. As the function updates the scores
    grid directly, it does not return anything.
    """
    dim = board.get_dim()
    winner = board.check_win()

    # set scorring values depending on winner
    if player == winner:
        score_current = SCORE_CURRENT
        score_other = -SCORE_OTHER
    else:
        score_current = -SCORE_CURRENT
        score_other = SCORE_OTHER

    # score the board and update scores list
    if winner != provided.DRAW:
        for row in range(dim):
            for col in range(dim):
                square = board.square(row, col)
                if square == player:
                    scores[row][col] += score_current
                elif square == provided.switch_player(player):
                    scores[row][col] += score_other


def get_best_move(board, scores):
    """
    This function takes a current board and a grid of scores. It then
    finds all of the empty squares with the maximum score and randomly
    return one of them as a (row, column) tuple. It is an error to call this
    function with a board that has no empty squares (there is no possible next
    move).
    """
    # get top score for empty squares in scores grid
    empty_squares = board.get_empty_squares()
    score_list = []
    for square in empty_squares:
        score_list.append(scores[square[0]][square[1]])

    top_score = max(score_list)

    # get all possible moves with top score
    possible_moves = []
    for square in empty_squares:
        if scores[square[0]][square[1]] == top_score:
            possible_moves.append(square)

    # return random choice from possible best moves
    best_move = []
    if len(possible_moves) > 1:
        best_move = random.choice(possible_moves)
    elif len(possible_moves) == 0:
        pass
    else:
        best_move = possible_moves[0]

    return best_move

def mc_move(board, player, trials):
    """
    This function takes a current board, which player the machine player is,
    and the number of trials to run. It then use the mc_trial() Monte Carlo
    simulation above to return a move for the machine player in the form of
    a (row, column) tuple.
    """
    # initial empty scores list
    dim = board.get_dim()
    scores = [[0 for dummycol in range(dim)]
              for dummyrow in range(dim)]

    # simulate n number of trials
    for _ in range(trials):
        trial = board.clone()
        mc_trial(trial, player)
        #update the scores list after every trial
        mc_update_scores(scores, trial, player)

    return get_best_move(board, scores)
