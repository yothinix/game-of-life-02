import os
import time

from utils import (
    constrain,
    print_board,
)


INITIAL_BOARD = {
    (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9),
    (10, 11), (10, 12), (10, 13), (10, 14), (10, 15),
    (10, 19),
}


def get_neighbors_of(cell):
    """
    Return the neighbors of cell.
    """
    result = [
        (cell[0], cell[1]-1),
        (cell[0], cell[1]+1),
        (cell[0]+1, cell[1]-1),
        (cell[0]+1, cell[1]),
        (cell[0]+1, cell[1]+1),
        (cell[0]-1, cell[1]-1),
        (cell[0]-1, cell[1]),
        (cell[0]-1, cell[1]+1)
    ]

    return set(result)


def count_neighbors(board, possible_neighbors):
    neighbors = board & possible_neighbors
    return len(neighbors)


def rule_1(board, center, possible_neighbors):
    if count_neighbors(board, possible_neighbors) < 2:
        return board - {center}
    else:
        return board


def rule_2(board, center, possible_neighbors):
    if count_neighbors(board, possible_neighbors) == 2:
        return board
    else:
        return board - {center}


def advance(board):
    """
    Advance the board one step and return it.
    """
    new_board = set()
    for cell in board:
        # your code below
        pass

    return new_board


def start(board, steps=100, size=20):
    for i in range(1, steps + 1):
        os.system('clear')
        print('step:', i, '/', steps)
        print_board(board, size)
        time.sleep(0.1)
        board = constrain(advance(board), size)


if __name__ == '__main__':
    start(INITIAL_BOARD)
