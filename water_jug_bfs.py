from collections import deque

def water_jug():
    visited = set()
    queue = deque([((0, 0), [(0, 0)])])

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) in visited: continue
        visited.add((x, y))

        if x == 2 or y == 2:
            print("Solution Path:")
            for state in path: print(state)
            return

        states = [
            (4, y), (x, 3), (0, y), (x, 0),
            (max(0, x - (3 - y)), min(3, x + y)),
            (min(4, x + y), max(0, y - (4 - x)))
        ]

        for s in states:
            if s not in visited:
                queue.append((s, path + [s]))

water_jug()