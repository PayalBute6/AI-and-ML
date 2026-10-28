"""
Assignment 2 (Set A - Q2)
Title: A* Search Algorithm
Description: Implements the A* Search Algorithm to find the shortest path 
             between a source node and a destination node using f(n) = g(n) + h(n).
"""

import heapq

# Weighted graph with actual step costs g(n)
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'F': 3},
    'D': {'G': 3},
    'E': {'G': 1},
    'F': {'G': 2},
    'G': {}
}

# Heuristic values h(n) estimating distance to goal 'G'
heuristics = {
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 2,
    'G': 0
}

def a_star_search(start, goal):
    print("=" * 60)
    print("A* SEARCH ALGORITHM (f(n) = g(n) + h(n))")
    print("=" * 60)
    print(f"Start Node: {start} | Goal Node: {goal}")
    print("-" * 60)

    # Priority queue stores tuples: (f_score, g_score, current_node, path)
    # Start node: g = 0, f = g + h = 0 + h(start)
    start_f = 0 + heuristics[start]
    open_queue = [(start_f, 0, start, [start])]
    
    # Track the best g-score recorded for each node
    best_g = {start: 0}
    visited = set()

    step = 1
    while open_queue:
        f, g, current, path = heapq.heappop(open_queue)

        if current in visited:
            continue
        visited.add(current)

        print(f"Step {step}: Expanding Node '{current}' | g={g}, h={heuristics[current]}, f={f}")
        step += 1

        if current == goal:
            print("=" * 60)
            print("Target Goal Reached!")
            print(f"Optimal Shortest Path: {' -> '.join(path)}")
            print(f"Total Optimal Cost (g): {g}")
            print("=" * 60)
            return path, g

        for neighbor, edge_cost in graph[current].items():
            new_g = g + edge_cost
            new_h = heuristics[neighbor]
            new_f = new_g + new_h

            # If neighbor not visited or found a cheaper path to neighbor
            if neighbor not in best_g or new_g < best_g[neighbor]:
                best_g[neighbor] = new_g
                heapq.heappush(open_queue, (new_f, new_g, neighbor, path + [neighbor]))

    print("Goal not reachable!")
    return None, float('inf')

if __name__ == "__main__":
    start_node = 'A'
    goal_node = 'G'
    a_star_search(start_node, goal_node)
