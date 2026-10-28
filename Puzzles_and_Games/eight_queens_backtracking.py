"""
Assignment 3 (Set B - Q3)
Title: Eight Queens Problem using Backtracking Algorithm
Description: Solves the classic 8-Queens problem on an 8x8 chessboard using recursive 
             backtracking, displaying the board visualization and finding all 92 valid configurations.
"""

BOARD_SIZE = 8

def print_8x8_board(queen_positions):
    """Visualizes the 8x8 chessboard with Queen placements."""
    print("     a   b   c   d   e   f   g   h")
    print("   +---+---+---+---+---+---+---+---+")
    for row in range(BOARD_SIZE):
        row_str = []
        for col in range(BOARD_SIZE):
            if queen_positions[row] == col:
                row_str.append(" Q ")
            else:
                row_str.append(" . ")
        print(f" {8 - row} |" + "|".join(row_str) + f"| {8 - row}")
        print("   +---+---+---+---+---+---+---+---+")
    print("     a   b   c   d   e   f   g   h\n")

def is_safe(queen_positions, row, col):
    """Checks whether placing a queen at (row, col) is safe against existing placed queens."""
    for prev_row in range(row):
        prev_col = queen_positions[prev_row]
        # Column collision or diagonal collision
        if prev_col == col or abs(prev_col - col) == abs(prev_row - row):
            return False
    return True

def solve_8_queens(queen_positions, current_row, all_solutions):
    """Recursive backtracking function."""
    if current_row == BOARD_SIZE:
        all_solutions.append(list(queen_positions))
        return

    for col in range(BOARD_SIZE):
        if is_safe(queen_positions, current_row, col):
            queen_positions[current_row] = col
            solve_8_queens(queen_positions, current_row + 1, all_solutions)
            queen_positions[current_row] = -1  # Backtrack

def main():
    print("=" * 65)
    print("8-QUEENS PUZZLE SOLVER (BACKTRACKING CSP)")
    print("=" * 65)

    queen_positions = [-1] * BOARD_SIZE
    all_solutions = []

    solve_8_queens(queen_positions, 0, all_solutions)

    total_solutions = len(all_solutions)
    print(f"Search Completed! Total Valid Solutions Found: {total_solutions}")
    print("-" * 65)

    # Display First Solution in detail
    first_sol = all_solutions[0]
    print("FIRST VALID 8-QUEENS SOLUTION:")
    print_8x8_board(first_sol)

    print("Queen Coordinates (Row, Column):")
    chess_coords = []
    cols_letters = "abcdefgh"
    for r, c in enumerate(first_sol):
        chess_coords.append(f"{cols_letters[c]}{8 - r}")
    print("  Chess Notation : " + ", ".join(chess_coords))
    print(f"  Matrix Indices : {[(r, c) for r, c in enumerate(first_sol)]}")
    print("=" * 65)

if __name__ == "__main__":
    main()
