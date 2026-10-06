"""
Question: Write a program to implement Breadth First Search (BFS) for the Monkey Banana Problem.
"""

from collections import deque

queue = deque(["Monkey at Door"])
visited = set()

while queue:
    state = queue.popleft()

    if state in visited:
        continue

    visited.add(state)
    print(state)

    if state == "Monkey at Door":
        queue.append("Monkey at Box")
    elif state == "Monkey at Box":
        queue.append("Box Under Banana")
    elif state == "Box Under Banana":
        queue.append("Monkey Climbs Box")
    elif state == "Monkey Climbs Box":
        queue.append("Monkey Gets Banana")
    elif state == "Monkey Gets Banana":
        print("Goal: Banana Obtained!")
        break
