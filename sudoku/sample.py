import numpy as np
from sudoku_solver import sudoku_puzzle

def main():
    sample = sudoku_puzzle()
    sample.puzzle[3, 0] = 2
    sample.puzzle[5, 0] = 4
    sample.puzzle[6, 0] = 5
    sample.puzzle[8, 0] = 3
    sample.puzzle[5, 1] = 6
    sample.puzzle[6, 1] = 9
    sample.puzzle[7, 1] = 7
    sample.puzzle[1, 2] = 5
    sample.puzzle[3, 2] = 1
    sample.puzzle[4, 2] = 7
    sample.puzzle[8, 2] = 6
    sample.puzzle[0, 3] = 5
    sample.puzzle[4, 3] = 3
    sample.puzzle[6, 3] = 6
    sample.puzzle[0, 4] = 2
    sample.puzzle[3, 4] = 8
    sample.puzzle[4, 4] = 6
    sample.puzzle[5, 4] = 7
    sample.puzzle[8, 4] = 5
    sample.puzzle[2, 5] = 6
    sample.puzzle[4, 5] = 9
    sample.puzzle[8, 5] = 7
    sample.puzzle[0, 6] = 6
    sample.puzzle[4, 6] = 1
    sample.puzzle[5, 6] = 3
    sample.puzzle[7, 6] = 2
    sample.puzzle[1, 7] = 4
    sample.puzzle[2, 7] = 9
    sample.puzzle[3, 7] = 7
    sample.puzzle[0, 8] = 7
    sample.puzzle[2, 8] = 3
    sample.puzzle[3, 8] = 6
    sample.puzzle[5, 8] = 8
    return sample

