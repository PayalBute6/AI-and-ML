# A very simple Breadth-First Search (BFS) for the 4-Gallon and 3-Gallon Water Jug Problem
# Target: Measure exactly 2 gallons.

# We start with both jugs empty.
# The queue stores paths (a path is a list of states we've visited)
queue = [[(0, 0)]]  
visited = set([(0, 0)])

print("Searching for a solution...\n")

while len(queue) > 0:
    path = queue.pop(0)       # Get the first path from the queue
    j1, j2 = path[-1]         # Get the last state in that path (current jug amounts)
    
    # If we reached our goal (2 gallons in either jug)
    if j1 == 2 or j2 == 2:
        print("Solution found!")
        print("Here are the steps (Jug 1, Jug 2):")
        for step in path:
            print(f"Jug 1: {step[0]} gal | Jug 2: {step[1]} gal")
        break
        
    # Generate all possible next states from the current (j1, j2)
    next_states = [
        (4, j2),  # 1. Fill Jug 1 completely
        (j1, 3),  # 2. Fill Jug 2 completely
        (0, j2),  # 3. Empty Jug 1 completely
        (j1, 0),  # 4. Empty Jug 2 completely
        
        # 5. Pour from Jug 1 to Jug 2
        # We pour either all of Jug 1, or just enough to fill Jug 2 (whichever is smaller)
        (j1 - min(j1, 3 - j2), j2 + min(j1, 3 - j2)),
        
        # 6. Pour from Jug 2 to Jug 1
        # We pour either all of Jug 2, or just enough to fill Jug 1 (whichever is smaller)
        (j1 + min(j2, 4 - j1), j2 - min(j2, 4 - j1))
    ]
    
    # Check the new states. If we haven't seen them before, add them to the queue!
    for state in next_states:
        if state not in visited:
            visited.add(state)
            
            # Create a new path that includes this new state and add it to the queue
            new_path = path + [state]
            queue.append(new_path)
