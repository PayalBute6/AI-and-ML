"""
Assignment 3 (Set A - Q3)
Title: 9x9 Sudoku Puzzle Solver using Backtracking Algorithm
Description: Solves a standard 9x9 Sudoku puzzle using recursive backtracking, 
             enforcing row, column, and 3x3 subgrid constraints.
"""

def print_board(board):
    """Displays the 9x9 Sudoku board with clear grid box borders."""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("  ------+-------+------")
        row_str = []
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row_str.append("|")
            val = board[i][j]
            row_str.append(str(val) if val != 0 else ".")
        print("  " + " ".join(row_str))

def find_empty(board):
    """Finds the next empty cell (denoted by 0). Returns (row, col) or None."""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board, row, col, num):
    """Checks whether placing 'num' at (row, col) violates any Sudoku constraints."""
    # 1. Check Row Constraint
    for j in range(9):
        if board[row][j] == num:
            return False

    # 2. Check Column Constraint
    for i in range(9):
        if board[i][col] == num:
            return False

    # 3. Check 3x3 Subgrid Constraint
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def solve_sudoku(board):
    """Solves the Sudoku board using recursive backtracking."""
    empty_cell = find_empty(board)
    if empty_cell is None:
        return True  # Puzzle completely solved!

    row, col = empty_cell

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            # Backtrack
            board[row][col] = 0

    return False

if __name__ == "__main__":
    print("=" * 45)
    print("9x9 SUDOKU SOLVER (BACKTRACKING CSP)")
    print("=" * 45)

    # Initial 9x9 Sudoku puzzle (0 represents empty cells)
    sample_board = [
        [5, 3, 0,  0, 7, 0,  0, 0, 0],
        [6, 0, 0,  1, 9, 5,  0, 0, 0],
        [0, 9, 8,  0, 0, 0,  0, 6, 0],

        [8, 0, 0,  0, 6, 0,  0, 0, 3],
        [4, 0, 0,  8, 0, 3,  0, 0, 1],
        [7, 0, 0,  0, 2, 0,  0, 0, 6],

        [0, 6, 0,  0, 0, 0,  2, 8, 0],
        [0, 0, 0,  4, 1, 9,  0, 0, 5],
        [0, 0, 0,  0, 8, 0,  0, 7, 9]
    ]

    print("Initial Sudoku Board:")
    print_board(sample_board)
    print("-" * 45)

    if solve_sudoku(sample_board):
        print("Solved Sudoku Board:")
        print_board(sample_board)
    else:
        print("No solution exists for this Sudoku puzzle.")
    print("=" * 45)
