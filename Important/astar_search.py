def a_star():
    # Define the graph with edge costs
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'D': 2, 'E': 5},
        'C': {'F': 3},
        'D': {'G': 3},
        'E': {'G': 1},
        'F': {'G': 2},
        'G': {}
    }
    
    # Define the heuristic values (h)
    h = {'A': 6, 'B': 5, 'C': 4, 'D': 3, 'E': 2, 'F': 2, 'G': 0}
    
    # List stores items like: (f_value, current_node, path_so_far, g_value)
    # For starting node A: f = g(0) + h(6) = 6
    open_list = [(6, 'A', ['A'], 0)]
    
    print("Tracing Path...")
    
    while len(open_list) > 0:
        # Sort the list so the lowest f_value is always at the start (index 0)
        open_list.sort(key=lambda x: x[0])
        
        # Take the node with the lowest f_value
        f_val, current, path, g_val = open_list.pop(0)
        
        print(f"Visiting {current} (f={f_val})")
        
        # Stop if we reached the goal 'G'
        if current == 'G':
            print("-" * 20)
            print("Goal Reached!")
            print("Shortest Path:", " -> ".join(path))
            print("Total Cost:", g_val)
            break
            
        # Add all neighbors to the list
        for neighbor, cost in graph[current].items():
            new_g = g_val + cost           # Cost from start to neighbor
            new_f = new_g + h[neighbor]    # new g + heuristic
            new_path = path + [neighbor]   # add neighbor to path
            
            # Add to our list to be evaluated later
            open_list.append((new_f, neighbor, new_path, new_g))

if __name__ == "__main__":
    a_star()
