"""
Assignment 2 (Set A - Q3)
Title: 8-Puzzle Problem using A* Search Algorithm
Description: Solves the classic 8-Puzzle sliding tile problem using A* search 
             with the Manhattan Distance heuristic.
"""

import heapq

# Target goal state (0 denotes the blank tile)
GOAL_STATE = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)

def manhattan_distance(state):
    """Calculates the sum of Manhattan distances of tiles from their goal positions."""
    distance = 0
    for i in range(9):
        val = state[i]
        if val != 0:
            target_index = GOAL_STATE.index(val)
            current_r, current_c = divmod(i, 3)
            target_r, target_c = divmod(target_index, 3)
            distance += abs(current_r - target_r) + abs(current_c - target_c)
    return distance

def get_neighbors(state):
    """Generates valid states reachable by sliding the blank tile Up, Down, Left, or Right."""
    neighbors = []
    blank = state.index(0)
    row, col = divmod(blank, 3)

    moves = [(-1, 0, "UP"), (1, 0, "DOWN"), (0, -1, "LEFT"), (0, 1, "RIGHT")]

    for dr, dc, move_name in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_blank = new_row * 3 + new_col
            state_list = list(state)
            # Swap blank with adjacent tile
            state_list[blank], state_list[new_blank] = state_list[new_blank], state_list[blank]
            neighbors.append((tuple(state_list), move_name))

    return neighbors

def print_board(state):
    """Prints 3x3 grid cleanly."""
    for i in range(0, 9, 3):
        row_str = " ".join(str(x) if x != 0 else "_" for x in state[i:i+3])
        print(f"  [ {row_str} ]")

def solve_8_puzzle(start_state):
    print("=" * 50)
    print("8-PUZZLE SOLVER USING A* SEARCH")
    print("=" * 50)
    print("Initial State:")
    print_board(start_state)
    print("\nGoal State:")
    print_board(GOAL_STATE)
    print("-" * 50)

    # Priority queue item: (f_score, g_cost, state, path)
    h_start = manhattan_distance(start_state)
    frontier = [(h_start, 0, start_state, [(start_state, "INITIAL")])]
    visited = set()

    nodes_expanded = 0

    while frontier:
        f, g, current_state, path = heapq.heappop(frontier)

        if current_state in visited:
            continue
        visited.add(current_state)
        nodes_expanded += 1

        if current_state == GOAL_STATE:
            print(f"SUCCESS! Goal State Reached in {g} moves!")
            print(f"Total Nodes Expanded: {nodes_expanded}")
            print("=" * 50)
            print("STEP-BY-STEP SOLUTION PATH:")
            print("=" * 50)
            for step_num, (st, move) in enumerate(path):
                print(f"Step {step_num}: Action = {move}")
                print_board(st)
                print()
            return path

        for next_state, move_name in get_neighbors(current_state):
            if next_state not in visited:
                new_g = g + 1
                new_h = manhattan_distance(next_state)
                new_f = new_g + new_h
                heapq.heappush(frontier, (new_f, new_g, next_state, path + [(next_state, move_name)]))

    print("No solution found!")
    return None

if __name__ == "__main__":
    # Solvable 8-puzzle starting configuration (6 moves to goal)
    start = (1, 2, 3,
             4, 0, 6,
             7, 5, 8)

    solve_8_puzzle(start)
