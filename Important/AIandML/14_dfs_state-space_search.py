"""
Question: Write a program to solve a state-space search problem using DFS. Start vertex - 1.
"""

graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2, 5, 6],
    5: [3, 4, 6],
    6: [4, 5]
}

def dfs_state_space(graph, start):
    visited = set()
    stack = [start]
    traversal = []

    print("Starting DFS State-Space Search...")
    
    while stack:
        node = stack.pop()
        
        if node not in visited:
            visited.add(node)
            traversal.append(str(node))
            print(f"Visited: {node}")
            
            # To ensure standard numerical visit order, we sort in reverse before pushing
            neighbors = sorted(graph[node], reverse=True)
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
                    
    print("-" * 30)
    print("Final DFS Traversal Path:")
    print(" -> ".join(traversal))

if __name__ == "__main__":
    dfs_state_space(graph, 1)
