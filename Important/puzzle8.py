import heapq

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)


# Calculate Manhattan distance
def heuristic(state):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            goal_index = goal.index(state[i])

            distance += abs(i // 3 - goal_index // 3)
            distance += abs(i % 3 - goal_index % 3)

    return distance


# Generate possible moves
def moves(state):
    result = []

    zero = state.index(0)
    row = zero // 3
    col = zero % 3

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:

        r = row + dr
        c = col + dc

        if 0 <= r < 3 and 0 <= c < 3:

            new_zero = r * 3 + c

            new_state = list(state)

            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            result.append(tuple(new_state))

    return result


# A* Search
def astar(start):

    queue = [(heuristic(start), 0, start, [start])]
    visited = set()

    while queue:

        f, cost, state, path = heapq.heappop(queue)

        if state in visited:
            continue

        visited.add(state)

        if state == goal:

            print("Solution:")

            for s in path:
                print(s[0:3])
                print(s[3:6])
                print(s[6:9])
                print()

            return

        for next_state in moves(state):

            new_cost = cost + 1
            f = new_cost + heuristic(next_state)

            heapq.heappush(
                queue,
                (f, new_cost, next_state, path + [next_state])
            )


# Starting state
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

astar(start)