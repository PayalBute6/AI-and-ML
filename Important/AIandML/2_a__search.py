"""
Question: Write a program to implement the A* Search Algorithm to find the shortest path between a source node and a destination node.
"""

import heapq

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'F': 3},
    'D': {'G': 3},
    'E': {'G': 1},
    'F': {'G': 2},
    'G': {}
}

# Heuristic values
h = {
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 2,
    'G': 0
}


def a_star(start, goal):

    # f, g, node, path
    queue = [(h[start], 0, start, [start])]

    visited = set()

    while queue:

        f, g, node, path = heapq.heappop(queue)

        if node in visited:
            continue

        visited.add(node)

        print("Visiting:", node)

        if node == goal:
            print("\nShortest Path:", " -> ".join(path))
            print("Total Cost:", g)
            return

        for neighbour, cost in graph[node].items():

            new_g = g + cost
            new_f = new_g + h[neighbour]

            heapq.heappush(
                queue,
                (new_f, new_g, neighbour, path + [neighbour])
            )


a_star('A', 'G')
