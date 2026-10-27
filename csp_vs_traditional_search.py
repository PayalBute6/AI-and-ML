"""
Assignment 3 (Set A - Q6)
Title: Comparative Analysis: CSP Backtracking vs. Traditional Blind Search (BFS/DFS)
Description: Benchmarks and compares CSP Backtracking against Traditional Blind Search 
             (DFS) on the 4-Queens problem to illustrate the power of early constraint pruning.
"""

import time

# -------------------------------------------------------------
# 1. Traditional Blind Search (DFS without early pruning)
# Generates candidate states blindly and only tests constraints at the end
# -------------------------------------------------------------
def solve_traditional_dfs(n=4):
    nodes_explored = 0
    solutions = []

    def dfs(current_placement):
        nonlocal nodes_explored
        nodes_explored += 1

        if len(current_placement) == n:
            # Check if this complete configuration is valid
            if is_valid_complete(current_placement):
                solutions.append(list(current_placement))
            return

        for col in range(n):
            dfs(current_placement + [col])

    def is_valid_complete(queens):
        for i in range(len(queens)):
            for j in range(i + 1, len(queens)):
                if queens[i] == queens[j] or abs(queens[i] - queens[j]) == abs(i - j):
                    return False
        return True

    start_time = time.perf_counter()
    dfs([])
    end_time = time.perf_counter()

    return len(solutions), nodes_explored, (end_time - start_time)

# -------------------------------------------------------------
# 2. CSP Approach (Backtracking with Early Constraint Pruning)
# Prunes immediately when a partial assignment violates constraints
# -------------------------------------------------------------
def solve_csp_backtracking(n=4):
    nodes_explored = 0
    solutions = []

    def is_safe(queens, row, col):
        for r in range(row):
            c = queens[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def backtrack(queens, row):
        nonlocal nodes_explored
        nodes_explored += 1

        if row == n:
            solutions.append(list(queens))
            return

        for col in range(n):
            if is_safe(queens, row, col):
                queens[row] = col
                backtrack(queens, row + 1)
                queens[row] = -1  # Backtrack

    start_time = time.perf_counter()
    initial_queens = [-1] * n
    backtrack(initial_queens, 0)
    end_time = time.perf_counter()

    return len(solutions), nodes_explored, (end_time - start_time)

def main():
    n = 4
    print("=" * 75)
    print("COMPARATIVE STUDY: TRADITIONAL BLIND SEARCH VS. CSP APPROACH")
    print(f"Problem: {n}-Queens Placement ({n}x{n} Chessboard)")
    print("=" * 75)

    trad_sol, trad_nodes, trad_time = solve_traditional_dfs(n)
    csp_sol, csp_nodes, csp_time = solve_csp_backtracking(n)

    print(f"\n{'Performance Metric':<30} | {'Traditional Blind Search (DFS)':<30} | {'CSP with Backtracking':<25}")
    print("-" * 88)
    print(f"{'Valid Solutions Found':<30} | {trad_sol:<30} | {csp_sol:<25}")
    print(f"{'Total Nodes Explored':<30} | {trad_nodes:<30} | {csp_nodes:<25}")
    print(f"{'Search Space Reduction':<30} | {'0% (Exhaustive brute-force)':<30} | {f'{((trad_nodes - csp_nodes)/trad_nodes)*100:.1f}% Pruned':<25}")
    print(f"{'Execution Time (sec)':<30} | {trad_time:<30.6f} | {csp_time:<25.6f}")
    print("=" * 88)

    print("\n" + "=" * 75)
    print("THEORETICAL COMPARISON REPORT:")
    print("=" * 75)
    print("""
1. STATE REPRESENTATION:
   - Traditional Search (BFS/DFS): Treats states as 'black-box' atomic entities. 
     Goal test is applied without understanding internal variable constraints.
   - CSP: Represents states in factored form using (Variables, Domains, Constraints).
     The problem structure is transparent to the solver.

2. PRUNING POWER & COMBINATORICS:
   - Traditional Search: Expands states blindly (n^n = 4^4 = 256 leaves + tree nodes = 341).
   - CSP Backtracking: Fails early upon encountering any constraint violation, 
     pruning entire branches of invalid subtrees (only 17 nodes explored!).

3. HEURISTICS & PROPAGATION:
   - Traditional Search: Requires domain-specific heuristics (like A* with h(n)).
   - CSP: Uses general-purpose domain-independent heuristics (MRV, Degree Heuristic,
     Least Constraining Value) and constraint propagation (AC-3, Forward Checking).
""")
    print("=" * 75)

if __name__ == "__main__":
    main()
