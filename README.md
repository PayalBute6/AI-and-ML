# Artificial Intelligence & Machine Learning (AI & ML) Repository

This repository contains implementations of fundamental AI algorithms, constraint satisfaction techniques, search strategies, and classic AI problem-solving puzzles.

---

## 📁 Repository Structure

```
AI and ML/
├── Search_Algorithms/       # Uninformed & Informed Search Algorithms
├── Constraint_Satisfaction/ # Constraint Satisfaction Problem (CSP) Solvers
├── Puzzles_and_Games/       # Classic Problem-Solving Games & Puzzles
├── Notes/                   # HTML Guides and Syllabus Explanations
└── Important/               # Additional reference implementations & practical slips
```

---

## 🔍 1. Search Algorithms (`Search_Algorithms/`)

Contains both blind (uninformed) and heuristic (informed) graph and tree search algorithms:

| File | Algorithm / Description |
| :--- | :--- |
| `bfs_graph.py` | Breadth-First Search (BFS) graph traversal |
| `dfs_graph.py` | Depth-First Search (DFS) graph traversal |
| `dls_graph.py` | Depth-Limited Search (DLS) |
| `ids_graph.py` | Iterative Deepening Search (IDS) |
| `bfs_complexity.py` | Time & Space complexity benchmark for BFS |
| `state_space_bfs.py` | State-space formulation with BFS traversal |
| `best_first_search.py` | Best-First Search using heuristic evaluation |
| `greedy_best_first_search.py` | Greedy Best-First Search algorithm |
| `astar_search.py` | $A^*$ Search Algorithm with path reconstruction |
| `ao_star_search.py` | $AO^*$ Algorithm for AND-OR graphs |
| `hill_climbing.py` | Simple & Steepest-Ascent Hill Climbing |
| `means_end_analysis.py` | Means-End Analysis (MEA) goal reduction |
| `route_finding_heuristic.py` | Route-Finding problem using $A^*$ search |
| `heuristic_functions_demo.py` | Euclidean, Manhattan, and Chebyshev heuristics |
| `astar_vs_greedy_bfs.py` | Direct performance comparison: $A^*$ vs. Greedy BFS |

---

## 🧩 2. Constraint Satisfaction Problems (`Constraint_Satisfaction/`)

Solvers and optimization techniques for CSPs:

| File | Topic / Description |
| :--- | :--- |
| `backtracking_csp.py` | General backtracking CSP solver framework |
| `backtracking_performance_analysis.py` | Performance and branching metrics analysis |
| `constraint_propagation_csp.py` | Constraint propagation (AC-3 arc consistency) |
| `forward_checking_csp.py` | Forward Checking (FC) pruning during search |
| `domain_reduction_csp.py` | Domain reduction & consistency filtering |
| `graph_coloring_csp.py` | Graph Coloring formulated as a CSP |
| `map_coloring_csp.py` | Map Coloring problem with adjacency constraints |
| `csp_vs_traditional_search.py` | Comparative study: CSP vs. Standard BFS/DFS |

---

## 🎮 3. Classic Puzzles & Problem-Solving Games (`Puzzles_and_Games/`)

Classic benchmark AI problems and game spaces:

| File | Problem Description |
| :--- | :--- |
| `water_jug_bfs.py` | Water Jug Problem (4L & 3L jugs to get 2L) |
| `monkey_banana_bfs.py` | Monkey and Banana planning problem |
| `missionaries_and_cannibals.py` | Missionaries and Cannibals river crossing |
| `tower_of_hanoi.py` | Tower of Hanoi state transition puzzle |
| `puzzle_8_astar.py` | 8-Puzzle sliding tile solver using $A^*$ heuristic |
| `cryptarithmetic_csp.py` | Cryptarithmetic puzzle (`SEND + MORE = MONEY`) |
| `eight_queens_backtracking.py` | 8-Queens placement puzzle via backtracking |
| `n_queens_backtracking.py` | Generalized $N$-Queens solver |
| `sudoku_backtracking.py` | 9×9 Sudoku grid solver using backtracking |

---

## 📑 4. Notes & Explanations (`Notes/`)

Interactive HTML guides and study material:

- **`python_programs_explained.html`**: Comprehensive breakdown of blind search algorithms, state formulations, and assignment questions.
- **`assignment_2_and_3_explained.html`**: Detailed guide for Assignment 2 (Informed Search) and Assignment 3 (Constraint Satisfaction Problems).
- **`ai_search_problem.html`**: Visual and theoretical foundations of search problems.

---

## 🚀 How to Run Any Program

All Python programs are self-contained using Python's standard library. Run any script directly:

```bash
# Example 1: Run A* search
python Search_Algorithms/astar_search.py

# Example 2: Solve 8-Puzzle
python Puzzles_and_Games/puzzle_8_astar.py

# Example 3: Solve Map Coloring CSP
python Constraint_Satisfaction/map_coloring_csp.py
```
