"""
Assignment 2 (Set B - Q2)
Title: Greedy Best First Search Algorithm
Description: Implements the Greedy Best First Search algorithm where f(n) = h(n).
             At each step, it chooses the node that appears closest to the goal.
"""

from queue import PriorityQueue

# Graph with edge costs
graph = {
    'S': {'A': 3, 'B': 2},
    'A': {'C': 4, 'D': 1},
    'B': {'E': 3, 'F': 1},
    'C': {},
    'D': {'G': 3},
    'E': {'G': 2},
    'F': {'G': 4},
    'G': {}
}

# Heuristic values h(n): Straight-line distance estimate to Goal 'G'
heuristics = {
    'S': 7,
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 1,
    'G': 0
}

def greedy_best_first_search(start, goal):
    print("=" * 60)
    print("GREEDY BEST FIRST SEARCH ALGORITHM (f(n) = h(n))")
    print("=" * 60)
    print(f"Start Node: '{start}' | Goal Node: '{goal}'")
    print("Heuristic Table:", heuristics)
    print("-" * 60)

    # Priority queue stores tuples: (heuristic_cost, current_node, path, accumulated_cost)
    pq = PriorityQueue()
    pq.put((heuristics[start], start, [start], 0))

    visited = set()
    step = 1

    while not pq.empty():
        h_val, current, path, actual_cost = pq.get()

        if current in visited:
            continue
        visited.add(current)

        print(f"Step {step}: Exploring Node '{current}' with Heuristic h={h_val}")
        step += 1

        if current == goal:
            print("-" * 60)
            print("Target Goal Found!")
            print(f"Solution Path : {' -> '.join(path)}")
            print(f"Total Path Cost: {actual_cost}")
            print(f"Nodes Visited : {list(visited)}")
            print("=" * 60)
            return path, actual_cost

        for neighbor, edge_cost in graph[current].items():
            if neighbor not in visited:
                pq.put((heuristics[neighbor], neighbor, path + [neighbor], actual_cost + edge_cost))

    print("Goal not found!")
    return None, float('inf')

if __name__ == "__main__":
    greedy_best_first_search('S', 'G')
