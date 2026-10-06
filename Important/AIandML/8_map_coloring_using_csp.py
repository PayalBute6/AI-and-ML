"""
Question: Write a program to solve the Map Coloring Problem using the Constraint Satisfaction Problem (CSP) approach.
"""

# The graph: which nodes are connected to each other
graph = {
    1: [2, 5],
    2: [1, 3],
    3: [2, 4],
    4: [3, 5],
    5: [4, 1]
}

colors = ["Pink", "Brown", "Orange"]

color = {}


def is_safe(node, c):

    for neighbour in graph[node]:
        if neighbour in color and color[neighbour] == c:
            return False

    return True


def solve(node):

    if node > 5:
        return True

    for c in colors:

        if is_safe(node, c):

            color[node] = c

            if solve(node + 1):
                return True

            del color[node]

    return False


if solve(1):

    print("Map Coloring Solution:")

    for node in color:
        print("Node", node, "=", color[node])

else:
    print("No solution")
