"""
"""
import numpy as np


def solve_sudoku(puzzle):
    while puzzle[puzzle == 0].size > 0:
        for n in range(81):
            i = n % 9
            j = n//9
            k = ((n % 9) // 3) * 3
            m = n//27 * 3
            if not puzzle[i, j]:
                elem = (
                    set(range(1, 10)) -
                    set(puzzle[i, :]) -
                    set(puzzle[:, j]) -
                    set(puzzle[k:k+3, m:m+3].reshape(9))
                    )
                puzzle[i, j] = elem.pop() if len(elem) == 1 else 0
    return puzzle


if __name__ == "__main__":

    question = np.array(
                   [[0, 2, 5, 0, 0, 6, 3, 0, 0],
                    [0, 1, 0, 0, 0, 8, 0, 4, 0],
                    [9, 0, 8, 0, 3, 7, 0, 0, 0],
                    [1, 0, 2, 0, 0, 0, 5, 6, 0],
                    [5, 8, 0, 0, 0, 0, 0, 3, 4],
                    [0, 3, 6, 0, 0, 0, 1, 0, 2],
                    [0, 0, 0, 1, 8, 0, 7, 0, 6],
                    [0, 6, 0, 9, 0, 0, 0, 2, 0],
                    [0, 0, 9, 3, 0, 0, 8, 5, 0]]
                   )

    answer = solve_sudoku(question)
    print(answer)

