"""
Question: Write a program to implement the Backtracking Algorithm for solving a constraint satisfaction problem (Graph Coloring).
"""

# The graph: A complete graph where every node is connected to every other node
graph = {
    1: [2, 3, 4, 5],
    2: [1, 3, 4, 5],
    3: [1, 2, 4, 5],
    4: [1, 2, 3, 5],
    5: [1, 2, 3, 4]
}

# The nodes we need to color
nodes = [1, 2, 3, 4, 5]

# Because every node is connected to every other node (a Complete Graph),
# we must have exactly 5 different colors to solve it!
available_colors = ['Blue', 'Green', 'Yellow', 'Red', 'Purple']

# Dictionary to store our final answers (e.g., {1: 'Blue'})
node_colors = {}

def solve_csp(node_index):
    # Base Case: If we have successfully colored all 5 nodes, we are done!
    if node_index == len(nodes):
        return True
        
    # Get the current node we want to color (e.g., Node 1)
    current_node = nodes[node_index]
    
    # Try every color one by one
    for color in available_colors:
        print(f"Thinking: Trying {color} for Node {current_node}...")
        
        # Check if any neighbors already have this same color
        is_safe = True
        for neighbor in graph[current_node]:
            if neighbor in node_colors and node_colors[neighbor] == color:
                is_safe = False
                print(f"  -> Conflict! Cannot use {color} because neighbor Node {neighbor} is already {color}")
                break
                
        # If the color is safe, assign it!
        if is_safe:
            node_colors[current_node] = color
            print(f"  -> Success! Assigned {color} to Node {current_node}")
            
            # Recursively move on to the NEXT node
            if solve_csp(node_index + 1) == True:
                return True
                
            # BACKTRACK: If we hit a dead end later, undo this choice
            print(f"  -> Backtracking: Removing {color} from Node {current_node}")
            del node_colors[current_node]
            
    # If no color works, return False to trigger backtracking on the previous node
    return False

if __name__ == "__main__":
    print("Starting Backtracking Algorithm for CSP...")
    print("-" * 50)
    
    if solve_csp(0) == True:
        print("-" * 50)
        print("Final Solution Found!")
        for node in nodes:
            print(f"Node {node} is colored {node_colors[node]}")
    else:
        print("\nNo solution possible with the given colors.")
