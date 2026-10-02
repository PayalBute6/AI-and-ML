# Q 3. Write a program toiImplement BFS traversal for a graph.
        #       A
        #     /   \
        #    B     C
        #   / \   / \
        #  D   E F   G
        #           ↑
        #         Goal

from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

queue = deque(['A'])
visited = []

while queue:
    node = queue.popleft()

    if node not in visited:
        visited.append(node)
        print(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)