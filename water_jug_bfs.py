# Q 2. Write a program to solve the Water Jug Problem using BFS.  

from collections import deque

def water_jug():
    visited = set()
    queue = deque([((0, 0), [(0, 0)])])

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))

        if x == 2 or y == 2:
            print("Solution Path:")
            for state in path:
                print(state)
            return

        states = [
            (4, y),       # Fill 4L jug
            (x, 3),       # Fill 3L jug
            (0, y),       # Empty 4L jug
            (x, 0),       # Empty 3L jug

            # Pour 4L → 3L
            (max(0, x - (3 - y)),
             min(3, x + y)),

            # Pour 3L → 4L
            (min(4, x + y),
             max(0, y - (4 - x)))
        ]

        for s in states:
            if s not in visited:
                queue.append((s, path + [s]))


water_jug()