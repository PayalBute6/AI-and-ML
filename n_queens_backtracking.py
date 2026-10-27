"""
Assignment 3 (Set A - Q5)
Title: N-Queens Problem using Backtracking Algorithm
Description: Solves the classic N-Queens puzzle by placing N chess queens on an N x N 
             chessboard such that no two queens attack each other.
"""

def print_board(board, n):
    """Prints the chessboard visually."""
    print("  +" + "---+" * n)
    for r in range(n):
        row_str = " | ".join("Q" if board[r][c] == 1 else "." for c in range(n))
        print(f"  | {row_str} |")
        print("  +" + "---+" * n)

def is_safe(board, row, col, n):
    """Checks whether placing a queen at (row, col) is safe from existing queens."""
    # Check vertical column upwards
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens(board, row, n, solutions):
    """Recursive backtracking function to place queens row by row."""
    # Base case: All N queens are placed successfully
    if row == n:
        # Save a copy of the valid board configuration
        solution = [row[:] for row in board]
        solutions.append(solution)
        return

    # Try placing a queen in each column of the current row
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            solve_n_queens(board, row + 1, n, solutions)

            # Backtrack
            board[row][col] = 0

def run_n_queens(n=4):
    print("=" * 55)
    print(f"{n}-QUEENS PROBLEM SOLVER (CSP BACKTRACKING)")
    print("=" * 55)
    print(f"Board Dimensions : {n} x {n}")
    print(f"Number of Queens : {n}")
    print("-" * 55)

    board = [[0] * n for _ in range(n)]
    solutions = []

    solve_n_queens(board, 0, n, solutions)

    print(f"Total Unique Valid Solutions Found: {len(solutions)}\n")

    for idx, sol in enumerate(solutions, 1):
        print(f"Solution #{idx}:")
        print_board(sol, n)
        
        # Display coordinates (Row, Column)
        coords = []
        for r in range(n):
            for c in range(n):
                if sol[r][c] == 1:
                    coords.append((r + 1, c + 1))
        print(f"  Queen Positions (Row, Col): {coords}\n")

    print("=" * 55)

if __name__ == "__main__":
    # Standard 4-Queens demonstration
    run_n_queens(4)
