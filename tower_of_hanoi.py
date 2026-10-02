from collections import deque

def get_successors(state):
    successors = []
    # State represents 3 pegs A, B, C as lists of disk sizes
    for i in range(3):
        if not state[i]: continue
        disk = state[i][-1]
        
        for j in range(3):
            if i == j: continue
            # Can place if peg is empty or top disk is larger
            if not state[j] or state[j][-1] > disk:
                new_state = list(list(peg) for peg in state)
                new_state[i].pop()
                new_state[j].append(disk)
                successors.append(tuple(tuple(peg) for peg in new_state))
    return successors

def solve_hanoi():
    initial = ((3, 2, 1), (), ())
    goal = ((), (), (3, 2, 1))
    
    queue = deque([(initial, [initial])])
    visited = {initial}
    
    while queue:
        state, path = queue.popleft()
        if state == goal:
            print(f"Solution Found in {len(path)-1} steps!")
            for p in path: print(p)
            return
            
        for succ in get_successors(state):
            if succ not in visited:
                visited.add(succ)
                queue.append((succ, path + [succ]))

solve_hanoi()