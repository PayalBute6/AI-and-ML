"""
Assignment 2 (Set A - Q1)
Title: Best First Search (Greedy Heuristic Search)
Description: Implements the Best First Search algorithm using heuristic values 
             to find a path from a start node to a goal node.
"""

from queue import PriorityQueue

# Graph representation using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Heuristic values h(n) estimating distance to goal 'G'
heuristic = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 6,
    'F': 2,
    'G': 0
}

def best_first_search(start, goal):
    print("=" * 50)
    print("BEST FIRST SEARCH ALGORITHM")
    print("=" * 50)
    print(f"Start Node : {start}")
    print(f"Goal Node  : {goal}")
    print("Heuristics :", heuristic)
    print("-" * 50)

    visited = set()
    # Priority Queue stores tuples of (heuristic_value, node, path)
    pq = PriorityQueue()
    pq.put((heuristic[start], start, [start]))

    traversal_order = []

    while not pq.empty():
        h, current, path = pq.get()

        if current in visited:
            continue

        visited.add(current)
        traversal_order.append(current)
        print(f"Selected Node: '{current}' with Heuristic h={h}")

        if current == goal:
            print("-" * 50)
            print("Goal Found!")
            print(f"Traversal Order: {' -> '.join(traversal_order)}")
            print(f"Solution Path  : {' -> '.join(path)}")
            return path

        for neighbor in graph[current]:
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor, path + [neighbor]))

    print("\nGoal Not Found!")
    return None

if __name__ == "__main__":
    start_node = 'A'
    goal_node = 'G'
    best_first_search(start_node, goal_node)
