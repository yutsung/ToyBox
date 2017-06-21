""" solve sudoku puzzle"""
import itertools
import numpy as np


class sudoku_puzzle:
    """sudoku puzzle and solve method"""

    def __init__(self, init_puzzle="none"):
        self.olist = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.ilist = list(itertools.chain.from_iterable(itertools.repeat(x, 9) for x in self.olist))
        self.jlist = self.olist[:] * 9

        self.puzzle = np.empty((9, 9), dtype=object)
        self.puzzle.fill([1, 2, 3, 4, 5, 6, 7, 8, 9])
        if not init_puzzle == "none":
            self.merge(init_puzzle.puzzle)

    def __str__(self):
        puzzle_str = ""
        for i in range(9):
            for j in range(9):
                puzzle_str += str("%i" %self.puzzle[i, j])+","
            puzzle_str += "\n"
        puzzle_str
        return puzzle_str

    def merge(self, puzzle2):
        """merge two sudoku puzzle"""
        for i, j in zip(self.ilist, self.jlist):
            if isinstance(self.puzzle[i, j], int):
                continue
            else:
                if isinstance(puzzle2[i, j], int):
                    self.puzzle[i, j] = puzzle2[i, j]
                    continue
            self.puzzle[i, j] = [x for x in self.puzzle[i, j] if x in puzzle2[i, j]]

    def solve_elim(self):
        """solve the puzzle by elimination"""

        for i, j in zip(self.ilist, self.jlist):
            if isinstance(self.puzzle[i, j], int):
                continue
            if isinstance(self.puzzle[i, j], list):
                if len(self.puzzle[i, j]) == 1:
                    self.puzzle[i, j] = self.puzzle[i, j][0]
                    continue
            if isinstance(self.puzzle[i, j], list):
                i2list = [x for x in range(9)]
                i2list.remove(i)
                j2list = [x for x in range(9)]
                j2list.remove(j)
                # ----------------
                for i2 in i2list:
                    if isinstance(self.puzzle[i2, j], int):
                        try:
                            self.puzzle[i, j].remove(self.puzzle[i2, j])
                        except:
                            pass
                for j2 in j2list:
                    if isinstance(self.puzzle[i, j2], int):
                        try:
                            self.puzzle[i, j].remove(self.puzzle[i, j2])
                        except:
                            pass
                for i3 in range(int(i/3)*3, int(i/3)*3+3):
                    for j3 in range(int(j/3)*3, int(j/3)*3+3):
                        if isinstance(self.puzzle[i3, j3], int):
                            try:
                                self.puzzle[i, j].remove(self.puzzle[i3, j3])
                            except:
                                pass




def main():
    """main precess of the solver"""
    pass

if __name__=="__main__":
    import sample2
    init_puzzle = sample2.main()
    puz = sudoku_puzzle(init_puzzle)
    for i in range(100):
        puz.solve_elim()

    print(puz)