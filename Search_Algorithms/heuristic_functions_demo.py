"""
Assignment 2 (Set B - Q4)
Title: Demonstration of Heuristic Functions in Search Problems
Description: Compares and demonstrates different heuristic functions (Manhattan, 
             Euclidean, Chebyshev, and Zero/Dijkstra) in 2D grid pathfinding.
"""

import math
import heapq

# 0 = Free cell, 1 = Obstacle
GRID = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

ROWS, COLS = len(GRID), len(GRID[0])
START = (0, 0)
GOAL = (4, 4)

# 1. Manhattan Distance (L1 norm: 4-directional moves)
def manhattan_h(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# 2. Euclidean Distance (L2 norm: straight-line distance)
def euclidean_h(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# 3. Chebyshev Distance (L-infinity norm: 8-directional moves)
def chebyshev_h(p1, p2):
    return max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))

# 4. Zero Heuristic (Uninformed / Dijkstra / Uniform Cost Search)
def zero_h(p1, p2):
    return 0

def run_astar(h_func, name):
    frontier = [(h_func(START, GOAL), 0, START, [START])]
    visited = set()
    nodes_expanded = 0

    while frontier:
        f, g, current, path = heapq.heappop(frontier)

        if current in visited:
            continue
        visited.add(current)
        nodes_expanded += 1

        if current == GOAL:
            return path, g, nodes_expanded

        r, c = current
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS and GRID[nr][nc] == 0:
                if (nr, nc) not in visited:
                    new_g = g + 1
                    new_f = new_g + h_func((nr, nc), GOAL)
                    heapq.heappush(frontier, (new_f, new_g, (nr, nc), path + [(nr, nc)]))

    return None, float('inf'), nodes_expanded

def display_grid():
    print("Grid Map (S = Start, G = Goal, # = Wall, . = Open):")
    for r in range(ROWS):
        row_str = []
        for c in range(COLS):
            if (r, c) == START:
                row_str.append('S')
            elif (r, c) == GOAL:
                row_str.append('G')
            elif GRID[r][c] == 1:
                row_str.append('#')
            else:
                row_str.append('.')
        print("  " + " ".join(row_str))
    print()

def main():
    print("=" * 70)
    print("DEMONSTRATION OF HEURISTIC FUNCTIONS IN SEARCH PROBLEMS")
    print("=" * 70)
    display_grid()

    heuristics = [
        ("Zero Heuristic (Dijkstra / Blind Search)", zero_h),
        ("Chebyshev Distance: max(|dx|, |dy|)", chebyshev_h),
        ("Euclidean Distance: sqrt(dx^2 + dy^2)", euclidean_h),
        ("Manhattan Distance: |dx| + |dy|", manhattan_h)
    ]

    print(f"{'Heuristic Function':<40} | {'Nodes Expanded':<15} | {'Path Cost':<10}")
    print("-" * 72)

    for name, func in heuristics:
        path, cost, expanded = run_astar(func, name)
        print(f"{name:<40} | {expanded:<15} | {cost:<10}")

    print("=" * 70)
    print("CONCLUSION:")
    print(" - Admissible heuristics guide search towards the goal.")
    print(" - Manhattan Distance expands fewer nodes because it closely matches 4-way grid motion.")
    print(" - Zero Heuristic explores uniformly in all directions, expanding maximum nodes.")
    print("=" * 70)

if __name__ == "__main__":
    main()
