"""
Assignment 2 (Set B - Q5)
Title: Performance Comparison: A* Search vs. Greedy Best First Search
Description: Implements both A* and Greedy Best First Search on the identical graph 
             to compare path optimality, path cost, and nodes expanded.
"""

import heapq
from queue import PriorityQueue

# Graph with actual edge costs
graph = {
    'S': {'A': 2, 'B': 5},
    'A': {'G': 2},
    'B': {'G': 10},
    'G': {}
}

# Heuristic values h(n) estimating distance to 'G'
# Notice B looks temptingly close (h=1), but the road from B to G is actually very expensive (cost 10)!
heuristics = {
    'S': 6,
    'A': 3,
    'B': 1,
    'G': 0
}

def run_greedy_bfs(start, goal):
    """Greedy Best First Search: f(n) = h(n)"""
    pq = PriorityQueue()
    pq.put((heuristics[start], start, [start], 0))
    visited = set()
    order = []

    while not pq.empty():
        h_val, current, path, cost = pq.get()

        if current in visited:
            continue
        visited.add(current)
        order.append(current)

        if current == goal:
            return path, cost, order

        for neighbor, edge_cost in graph[current].items():
            if neighbor not in visited:
                pq.put((heuristics[neighbor], neighbor, path + [neighbor], cost + edge_cost))

    return None, float('inf'), order

def run_astar(start, goal):
    """A* Search: f(n) = g(n) + h(n)"""
    pq = [(0 + heuristics[start], 0, start, [start])]
    visited = set()
    order = []
    best_g = {start: 0}

    while pq:
        f_val, g_val, current, path = heapq.heappop(pq)

        if current in visited:
            continue
        visited.add(current)
        order.append(current)

        if current == goal:
            return path, g_val, order

        for neighbor, edge_cost in graph[current].items():
            new_g = g_val + edge_cost
            new_f = new_g + heuristics[neighbor]
            if neighbor not in best_g or new_g < best_g[neighbor]:
                best_g[neighbor] = new_g
                heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float('inf'), order

def main():
    print("=" * 70)
    print("COMPARATIVE STUDY: A* SEARCH VS. GREEDY BEST FIRST SEARCH")
    print("=" * 70)
    print("Graph Structure and Edge Costs:")
    for src, edges in graph.items():
        if edges:
            for dst, c in edges.items():
                print(f"  {src} --(cost {c})--> {dst}")
    print("\nHeuristic Values h(n) to Goal 'G':")
    for k, v in heuristics.items():
        print(f"  h({k}) = {v}")
    print("-" * 70)

    # Run Greedy BFS
    g_path, g_cost, g_order = run_greedy_bfs('S', 'G')

    # Run A*
    a_path, a_cost, a_order = run_astar('S', 'G')

    print(f"\n{'Metric / Feature':<30} | {'Greedy Best First Search':<20} | {'A* Search Algorithm':<20}")
    print("-" * 75)
    print(f"{'Evaluation Function':<30} | {'f(n) = h(n)':<20} | {'f(n) = g(n) + h(n)':<20}")
    print(f"{'Exploration Order':<30} | {' -> '.join(g_order):<20} | {' -> '.join(a_order):<20}")
    print(f"{'Path Found':<30} | {' -> '.join(g_path):<20} | {' -> '.join(a_path):<20}")
    print(f"{'Total Path Cost':<30} | {str(g_cost):<20} | {str(a_cost):<20}")
    print(f"{'Optimal Solution?':<30} | {'NO (Sub-optimal)':<20} | {'YES (Guaranteed Optimal)':<20}")
    print("=" * 75)

    print("\nKey Insights:")
    print("1. Greedy BFS is lured by the low heuristic of 'B' (h=1), picking path S -> B -> G with high cost (15).")
    print("2. A* considers both the distance traveled g(n) and heuristic h(n), discovering optimal path S -> A -> G with low cost (4).")

if __name__ == "__main__":
    main()
