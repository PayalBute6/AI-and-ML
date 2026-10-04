from collections import deque

def bfs_traversal(graph, start_node):
    """
    Performs Breadth-First Search (BFS) on a graph.
    """
    # Queue for BFS, start by adding the starting node
    queue = deque([start_node])
    
    # Set to keep track of visited nodes (so we don't visit them twice)
    visited = set([start_node])
    
    # List to store the final traversal order
    traversal_order = []
    
    print("Starting BFS Traversal...")
    
    while queue:
        # Get the next node from the FRONT of the queue
        current_node = queue.popleft()
        
        # Add it to our final traversal list
        traversal_order.append(current_node)
        print(f"\nVisiting Node: {current_node}")
        
        # Look at all the neighbors connected to this node
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                # Mark as visited and add to the BACK of the queue
                visited.add(neighbor)
                queue.append(neighbor)
                print(f"  -> Discovered Node {neighbor}, adding to the queue.")
                
    return traversal_order

if __name__ == "__main__":
    # Define the graph based exactly on your image
    # It's a perfect binary tree from 1 to 15
    graph = {
        1: [2, 3],
        2: [4, 5],
        3: [6, 7],
        4: [8, 9],
        5: [10, 11],
        6: [12, 13],
        7: [14, 15],
        8: [], 
        9: [], 
        10: [], 
        11: [], 
        12: [], 
        13: [], 
        14: [], 
        15: []
    }
    
    print("=" * 50)
    result = bfs_traversal(graph, 1)
    
    print("=" * 50)
    print("Final BFS Traversal Order:")
    # Convert numbers to strings and join them with arrows
    print(" -> ".join(map(str, result)))
