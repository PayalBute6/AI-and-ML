from collections import deque

def is_valid(m_left, c_left):
    m_right, c_right = 3 - m_left, 3 - c_left
    if m_left > 0 and m_left < c_left: return False
    if m_right > 0 and m_right < c_right: return False
    return True

def solve():
    initial = (3, 3, 0)
    goal = (0, 0, 1)
    queue = deque([(initial, [initial])])
    visited = set()
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    while queue:
        (m_left, c_left, boat), path = queue.popleft()

        if (m_left, c_left, boat) in visited: continue
        visited.add((m_left, c_left, boat))

        if (m_left, c_left, boat) == goal:
            print("Solution:"); 
            for s in path: print(s)
            return

        for m, c in moves:
            if boat == 0:
                new_m, new_c, new_boat = m_left - m, c_left - c, 1
            else:
                new_m, new_c, new_boat = m_left + m, c_left + c, 0

            if 0 <= new_m <= 3 and 0 <= new_c <= 3:
                if is_valid(new_m, new_c):
                    new_state = (new_m, new_c, new_boat)
                    if new_state not in visited:
                        queue.append((new_state, path + [new_state]))
solve()