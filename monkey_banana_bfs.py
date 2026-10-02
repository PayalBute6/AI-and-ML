from collections import deque 
 
# BFS for Monkey Banana Problem 
queue = deque(["Monkey at Door"]) 
visited = [] 
while queue: 
    state = queue.popleft() 
 
    if state not in visited: 
        visited.append(state) 
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
            print("\nGoal : Banana Obtained!") 
            break