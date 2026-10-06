# The graph: which nodes are connected to each other
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

# The nodes we need to color
nodes = ['A', 'B', 'C', 'D']

# The colors we are allowed to use
available_colors = ['Red', 'Green', 'Blue']

# This dictionary will store our answers (e.g., {'A': 'Red'})
node_colors = {}

def solve(node_index):
    # Base Case: If we have colored all 4 nodes, we are done!
    if node_index == len(nodes):
        return True
        
    # Get the current node we are trying to color (e.g., 'A')
    current_node = nodes[node_index]
    
    # Try every color one by one
    for color in available_colors:
        print(f"Thinking: Trying {color} for {current_node}...")
        
        # Check if any neighbors already have this same color
        is_safe = True
        for neighbor in graph[current_node]:
            # If the neighbor is already colored, and it's the same color we are trying -> Not Safe
            if neighbor in node_colors and node_colors[neighbor] == color:
                is_safe = False
                print(f"  -> Conflict! Cannot use {color} because neighbor {neighbor} is already {color}")
                break # Stop checking other neighbors
                
        # If it is safe, let's assign the color!
        if is_safe:
            node_colors[current_node] = color
            print(f"  -> Success! Assigned {color} to {current_node}")
            
            # Now, recursively move on to the NEXT node
            if solve(node_index + 1) == True:
                return True # Everything worked out perfectly!
                
            # If we reached here, it means the color we picked caused a dead end later on.
            # So, we BACKTRACK by undoing our choice.
            print(f"  -> Backtracking: Removing {color} from {current_node} and trying a different color.")
            del node_colors[current_node]
            
    # If we tried all colors and none worked, return False so the previous node can pick a new color
    return False

if __name__ == "__main__":
    print("Starting Map Coloring...")
    print("-" * 30)
    
    # Start solving from the 0th node (which is 'A')
    if solve(0) == True:
        print("-" * 30)
        print("Final Solution:")
        for node in nodes:
            print(f"Node {node} is colored {node_colors[node]}")
    else:
        print("\nNo solution possible!")
