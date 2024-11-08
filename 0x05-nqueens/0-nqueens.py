#!/usr/bin/python3
"""N Queens Puzzle Solver"""
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Check if N is a valid integer
try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

# Check if N is at least 4
if n < 4:
    print("N must be at least 4")
    sys.exit(1)


def solve_nqueens(n):
    """Solve the N queens puzzle and print all solutions"""
    def backtrack(row, diagonals, anti_diagonals, cols, state):
        # If all queens are placed
        if row == n:
            solution = [[r, c] for r, c in enumerate(state)]
            solutions.append(solution)
            return
        
        for col in range(n):
            curr_diag = row - col
            curr_anti_diag = row + col

            # Check if the queen is under attack in the column or diagonals
            if (col in cols or
                curr_diag in diagonals or
                curr_anti_diag in anti_diagonals):
                continue

            # Place the queen
            cols.add(col)
            diagonals.add(curr_diag)
            anti_diagonals.add(curr_anti_diag)
            state.append(col)

            # Move to the next row
            backtrack(row + 1, diagonals, anti_diagonals, cols, state)

            # Remove the queen
            cols.remove(col)
            diagonals.remove(curr_diag)
            anti_diagonals.remove(curr_anti_diag)
            state.pop()

    solutions = []
    backtrack(0, set(), set(), set(), [])
    return solutions


# Print each solution
for solution in solve_nqueens(n):
    print(solution)
