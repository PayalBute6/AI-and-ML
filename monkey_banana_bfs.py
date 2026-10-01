# A very simple Breadth-First Search (BFS) for the Monkey Banana Problem
# Target: Monkey gets the banana.

# State: (monkey_position, monkey_on_box, box_position, has_banana)
initial_state = ('door', False, 'window', False)

# The queue stores paths (a path is a list of states we've visited)
queue = [[initial_state]]
visited = set([initial_state])

print("Searching for a solution...\n")

while len(queue) > 0:
    path = queue.pop(0)          # Get the first path from the queue
    current_state = path[-1]     # Get the last state in that path
    
    monkey_pos = current_state[0]
    on_box = current_state[1]
    box_pos = current_state[2]
    has_banana = current_state[3]
    
    # If we reached our goal (monkey has the banana)
    if has_banana == True:
        print("Solution found!")
        print("Here are the steps:")
        for step in path:
            print(f"Monkey at: {step[0]:<7} | On box: {str(step[1]):<5} | Box at: {step[2]:<7} | Has banana: {str(step[3])}")
        break
        
    # Generate all possible next states from the current state
    next_states = []
    
    # 1. Grasp banana (if monkey is on the box at the center)
    if monkey_pos == 'center' and on_box == True and box_pos == 'center' and has_banana == False:
        next_states.append(('center', True, 'center', True))
        
    # 2. Climb box (if monkey is at the exact same location as the box)
    if monkey_pos == box_pos and on_box == False:
        next_states.append((monkey_pos, True, box_pos, False))
        
    # 3. Push box to different locations (if monkey is next to the box)
    if monkey_pos == box_pos and on_box == False:
        for new_pos in ['door', 'window', 'center']:
            if new_pos != box_pos:
                next_states.append((new_pos, False, new_pos, False))
                
    # 4. Walk to different locations (if monkey is not on the box)
    if on_box == False:
        for new_pos in ['door', 'window', 'center']:
            if new_pos != monkey_pos:
                next_states.append((new_pos, False, box_pos, False))
                
    # Check the new states. If we haven't seen them before, add them to the queue!
    for state in next_states:
        if state not in visited:
            visited.add(state)
            
            # Create a new path that includes this new state and add it to the queue
            new_path = path + [state]
            queue.append(new_path)
