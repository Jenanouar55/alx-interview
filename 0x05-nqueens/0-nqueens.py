#!/usr/bin/python3
""" N queens """
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])


def queens(n, i=0, a=[], b=[], c=[]):
    """Find all possible solutions for N-Queens problem."""
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def solve(n):
    """Print each solution as a list of positions."""
    for solution in queens(n):
        # Create a list of queen positions for each solution
        k = [[i, solution[i]] for i in range(n)]
        print(k)


solve(n)
