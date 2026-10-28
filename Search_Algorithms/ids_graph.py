def dls(graph, node, target, limit):
    if node == target: return True
    if limit <= 0: return False
    
    for neighbour in graph.get(node, []):
        if dls(graph, neighbour, target, limit - 1):
            return True
    return False

def ids(graph, start, target, max_depth):
    for limit in range(max_depth + 1):
        print(f"Searching at depth limit {limit}...")
        if dls(graph, start, target, limit):
            print(f"Target '{target}' found at depth limit {limit}!")
            return True
    print("Target not found.")
    return False

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
ids(graph, 'A', 'E', 3)