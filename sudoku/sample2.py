import numpy as np
from sudoku_solver import sudoku_puzzle

def main():
    sample = sudoku_puzzle()
    sample.puzzle[2, 0] = 7
    sample.puzzle[3, 0] = 5
    sample.puzzle[4, 0] = 4
    sample.puzzle[5, 0] = 6
    sample.puzzle[6, 0] = 8
    sample.puzzle[7, 0] = 2
    #-----------------------
    sample.puzzle[2, 1] = 3
    sample.puzzle[4, 1] = 1
    sample.puzzle[8, 1] = 7
    # -----------------------
    sample.puzzle[1, 2] = 8
    sample.puzzle[2, 2] = 4
    sample.puzzle[4, 2] = 2
    sample.puzzle[6, 2] = 1
    sample.puzzle[7, 2] = 9
    # -----------------------
    sample.puzzle[5, 3] = 4
    # -----------------------
    sample.puzzle[2, 4] = 9
    sample.puzzle[3, 4] = 8
    sample.puzzle[4, 4] = 3
    sample.puzzle[5, 4] = 7
    sample.puzzle[6, 4] = 5
    # -----------------------
    sample.puzzle[3, 5] = 1
    # -----------------------
    sample.puzzle[1, 6] = 9
    sample.puzzle[2, 6] = 2
    sample.puzzle[4, 6] = 7
    sample.puzzle[6, 6] = 6
    sample.puzzle[7, 6] = 8
    # -----------------------
    sample.puzzle[0, 7] = 7
    sample.puzzle[4, 7] = 6
    sample.puzzle[6, 7] = 3
    # -----------------------
    sample.puzzle[1, 8] = 6
    sample.puzzle[2, 8] = 1
    sample.puzzle[3, 8] = 3
    sample.puzzle[4, 8] = 8
    sample.puzzle[5, 8] = 5
    sample.puzzle[6, 8] = 2

    return sample

