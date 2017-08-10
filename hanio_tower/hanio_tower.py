#!/usr/local/bin/python3
"""
"""


def hanio(n, A="left", B="middle", C="right"):
    if n:
        hanio(n - 1, A, C, B)
        print(A, "==>", C)
        hanio(n - 1, B, A, C)


if __name__ == "__main__":
    hanio(3)
