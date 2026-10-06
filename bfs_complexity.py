import time
from collections import deque

def generate_tree(branch_factor, depth):
    graph = {}
    nodes = 1
    def build(node, d):
        nonlocal nodes
        graph[node] = []
        if d < depth:
            for _ in range(branch_factor):
                nodes += 1
                child = f"N{nodes}"
                graph[node].append(child)
                build(child, d + 1)
    build("Root", 0)
    return graph, nodes

def measure_bfs(graph, start):
    queue = deque([start])
    visited = set([start])
    max_q = 0
    start_t = time.time()
    
    while queue:
        max_q = max(max_q, len(queue))
        node = queue.popleft()
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                
    end_t = time.time()
    return (end_t - start_t), max_q

b, d = 3, 5
graph, total = generate_tree(b, d)
time_taken, max_space = measure_bfs(graph, "Root")

print(f"Nodes: {total}")
print(f"Time (seconds): {time_taken:.5f}")
print(f"Space (Max Queue Size): {max_space}")