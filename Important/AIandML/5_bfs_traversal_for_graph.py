"""
Question: Write a program to implement Breadth First Search (BFS) traversal for a graph.
"""

from collections import deque

def bfs_traversal(graph, start_node):
    queue = deque([start_node])
    visited = set([start_node])
    traversal_order = []
    
    print("Starting BFS Traversal...")
    
    while queue:
        current_node = queue.popleft()
        traversal_order.append(current_node)
        print(f"\\nVisiting Node: {current_node}")
        
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                print(f"  -> Discovered Node {neighbor}, adding to the queue.")
                
    return traversal_order

# Define the graph based exactly on the image (perfect binary tree 1 to 15)
graph = {
    1: [2, 3], 2: [4, 5], 3: [6, 7], 4: [8, 9], 5: [10, 11],
    6: [12, 13], 7: [14, 15], 8: [], 9: [], 10: [], 11: [],
    12: [], 13: [], 14: [], 15: []
}

print("=" * 50)
result = bfs_traversal(graph, 1)

print("=" * 50)
print("Final BFS Traversal Order:")
print(" -> ".join(map(str, result)))
