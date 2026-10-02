# Graph with Depth Levels:
#
# Level 0:        A
#               /   \
# Level 1:     B     C
#             / \     \
# Level 2:   D   E     F
#                ↑
#             Target

def dls(graph, node, target, limit, visited):
    if node == target:
        return True
    
    if limit <= 0:
        return False
        
    visited.add(node)
    
    for neighbour in graph.get(node, []):
        if neighbour not in visited:
            if dls(graph, neighbour, target, limit - 1, visited.copy()):
                return True
                
    return False

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
target_node = 'E'
depth_limit = 2

print(f"Searching for '{target_node}' with depth limit {depth_limit}...")
if dls(graph, 'A', target_node, depth_limit, set()):
    print("Target Found within limit!")
else:
    print("Target NOT Found within limit.")