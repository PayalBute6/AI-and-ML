"""
Assignment 3 (Set B - Q6)
Title: Performance Analysis of Backtracking Algorithm on CSP (N-Queens)
Description: Analyzes the computational complexity and empirical performance of 
             CSP Backtracking across varying problem sizes (N = 4 to 9). Measures execution 
             time, recursive calls, and backtracks.
"""

import time

class NQueensAnalyzer:
    def __init__(self, n):
        self.n = n
        self.recursive_calls = 0
        self.backtracks = 0
        self.solutions_count = 0
        self.execution_time = 0.0

    def is_safe(self, queens, row, col):
        """Checks if placing a queen at (row, col) is safe."""
        for r in range(row):
            c = queens[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def backtrack(self, queens, row):
        """Standard recursive backtracking function."""
        self.recursive_calls += 1

        if row == self.n:
            self.solutions_count += 1
            return

        for col in range(self.n):
            if self.is_safe(queens, row, col):
                queens[row] = col
                self.backtrack(queens, row + 1)
                queens[row] = -1
                self.backtracks += 1

    def run(self):
        queens = [-1] * self.n
        start = time.perf_counter()
        self.backtrack(queens, 0)
        end = time.perf_counter()
        self.execution_time = end - start
        return {
            'N': self.n,
            'solutions': self.solutions_count,
            'recursive_calls': self.recursive_calls,
            'backtracks': self.backtracks,
            'time_sec': self.execution_time
        }

def main():
    print("=" * 80)
    print("EMPIRICAL PERFORMANCE ANALYSIS OF CSP BACKTRACKING (N-QUEENS)")
    print("=" * 80)
    print("Analyzing scaling behavior for N = 4 through N = 9...")
    print("-" * 80)

    results = []
    for n in range(4, 10):
        analyzer = NQueensAnalyzer(n)
        stats = analyzer.run()
        results.append(stats)

    # Print Formatted Table
    print(f"{'N (Size)':<10} | {'Solutions':<12} | {'Recursive Calls':<18} | {'Backtracks':<15} | {'Time (sec)':<12}")
    print("-" * 80)
    for r in results:
        print(f"{r['N']:<10} | {r['solutions']:<12} | {r['recursive_calls']:<18} | {r['backtracks']:<15} | {r['time_sec']:<12.6f}")
    print("=" * 80)

    print("\nPERFORMANCE OBSERVATIONS & COMPLEXITY ANALYSIS:")
    print("1. TIME COMPLEXITY:")
    print("   - Worst-case time complexity is O(N!), as branching factor decreases per row.")
    print("   - Notice how recursive calls and runtime grow rapidly as N increases from 4 to 9.")
    print("2. SPACE COMPLEXITY:")
    print("   - Space complexity remains strictly O(N) because the recursion stack depth is capped at N.")
    print("3. BACKTRACKING PRUNING EFFICIENCY:")
    print("   - For N=8, brute-force search space is 8^8 = 16,777,216 states.")
    print(f"   - CSP Backtracking evaluates only {results[4]['recursive_calls']} states to find all 92 solutions!")
    print("   - This represents an astronomical search-space pruning efficiency of >98.8%.")
    print("=" * 80)

if __name__ == "__main__":
    main()
