"""
Question: Write a program to solve the 8-Puzzle problem using the A* Search Algorithm.
"""

import heapq

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def heuristic(state):
    distance = 0
    for i in range(9):
        value = state[i]
        if value != 0:
            goal_pos = goal.index(value)
            distance += abs(i // 3 - goal_pos // 3)
            distance += abs(i % 3 - goal_pos % 3)
    return distance

def neighbours(state):
    result = []
    zero = state.index(0)
    row, col = zero // 3, zero % 3
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        nr, nc = row + dr, col + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_zero = nr * 3 + nc
            new_state = list(state)
            new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]
            result.append(tuple(new_state))

    return result

def astar(start):
    queue = [(heuristic(start), 0, start, [start])]
    visited = set()

    while queue:
        f, g, state, path = heapq.heappop(queue)

        if state in visited: continue
        visited.add(state)

        if state == goal:
            print("Solution:")
            for step in path: print(step)
            return

        for next_state in neighbours(state):
            new_g = g + 1
            new_f = new_g + heuristic(next_state)
            heapq.heappush(queue, (new_f, new_g, next_state, path + [next_state]))

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
astar(start)
