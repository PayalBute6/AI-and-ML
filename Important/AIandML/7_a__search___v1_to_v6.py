"""
Question: Write a program to implement the A* Search Algorithm to find the shortest path between a source node (V1) and a destination node (V6).
"""

import heapq

graph = {
    'V1': {'V2': 2, 'V3': 4},
    'V2': {'V1': 2, 'V4': 3},
    'V3': {'V1': 4, 'V4': 1, 'V5': 5},
    'V4': {'V2': 3, 'V3': 1, 'V6': 2},
    'V5': {'V3': 5, 'V6': 1},
    'V6': {'V4': 2, 'V5': 1}
}

heuristic = {
    'V1': 7, 'V2': 5, 'V3': 3, 'V4': 2, 'V5': 1, 'V6': 0
}

def astar(start, goal):
    queue = [(heuristic[start], 0, start, [start])]
    visited = set()

    while queue:
        f, g, node, path = heapq.heappop(queue)

        if node in visited:
            continue
        visited.add(node)

        print(f"Visiting {node} (Cost so far: {g})")

        if node == goal:
            print("-" * 20)
            print("Path:", " -> ".join(path))
            print("Total Cost:", g)
            return

        for neighbour, cost in graph[node].items():
            if neighbour not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbour]
                heapq.heappush(queue, (new_f, new_g, neighbour, path + [neighbour]))

print("Starting A* Search...")
astar('V1', 'V6')
