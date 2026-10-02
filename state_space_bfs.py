from collections import deque

state_space = {
    'Start': ['State_1', 'State_2'],
    'State_1': ['State_3', 'State_4'],
    'State_2': ['State_5', 'Goal'],
    'State_3': [],
    'State_4': ['Goal'],
    'State_5': [],
    'Goal': []
}

def bfs_search(initial_state, goal_state):
    visited = set()
    queue = deque([(initial_state, [initial_state])])
    
    while queue:
        current_state, path = queue.popleft()
        
        if current_state in visited: continue
        visited.add(current_state)
        
        if current_state == goal_state:
            print("Goal Found! Path:", " -> ".join(path))
            return
            
        for next_state in state_space.get(current_state, []):
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))

bfs_search('Start', 'Goal')