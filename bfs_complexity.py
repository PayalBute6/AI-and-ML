# Q5. Set B: Write a program to analyze the time and space complexity of BFS.
from collections import deque
import time

def generate_tree(branching_factor, depth):
    """Generates a perfect tree with given branching factor and depth."""
    graph = {}
    nodes = 1
    
    def build(current_node, current_depth):
        nonlocal nodes
        graph[current_node] = []
        if current_depth < depth:
            for _ in range(branching_factor):
                nodes += 1
                child = f"Node_{nodes}"
                graph[current_node].append(child)
                build(child, current_depth + 1)
                
    build("Root", 0)
    return graph, nodes

def analyze_bfs_complexity(graph, start):
    """
    Runs BFS and tracks:
    1. Nodes visited (representing Time Complexity)
    2. Max queue size (representing Space Complexity)
    """
    queue = deque([start])
    visited = set([start])
    
    nodes_visited = 0
    max_queue_size = 0
    
    start_time = time.time()
    
    while queue:
        # Track maximum space used by queue
        if len(queue) > max_queue_size:
            max_queue_size = len(queue)
            
        vertex = queue.popleft()
        nodes_visited += 1 # Track time complexity
        
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    end_time = time.time()
    
    return nodes_visited, max_queue_size, end_time - start_time

if __name__ == "__main__":
    print("BFS Complexity Analysis (Time and Space)\n")
    print(f"{'Branching (b)':<15} | {'Depth (d)':<10} | {'Total Nodes Visited (Time)':<28} | {'Max Queue (Space)':<20} | {'Time (s)'}")
    print("-" * 95)
    
    # We will test BFS with different branching factors and depths
    test_cases = [
        (2, 5),   # b=2, d=5
        (2, 10),  # b=2, d=10
        (3, 5),   # b=3, d=5
        (3, 8),   # b=3, d=8
        (4, 5)    # b=4, d=5
    ]
    
    for b, d in test_cases:
        # 1. Generate a tree of the given size
        graph, total_nodes = generate_tree(b, d)
        
        # 2. Run BFS and record metrics
        nodes_visited, max_q, t = analyze_bfs_complexity(graph, "Root")
        
        # 3. Print the metrics for this configuration
        print(f"{b:<15} | {d:<10} | {nodes_visited:<28} | {max_q:<20} | {t:.5f}")
        
    print("\n--- Conclusion ---")
    print("Time Complexity: O(b^d)  - The total nodes visited grows exponentially with depth.")
    print("Space Complexity: O(b^d) - The max queue size equals the number of leaf nodes at the widest level, which also grows exponentially.")
