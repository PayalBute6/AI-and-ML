"""
Assignment 2 (Set B - Q3)
Title: Route-Finding Problem using Heuristic Search (A* Algorithm)
Description: Solves a realistic road navigation problem to find the shortest driving 
             route from Pune to Mumbai using actual highway distances and straight-line 
             heuristic distances.
"""

import heapq

# Highway network: connected cities with actual driving distance (in km)
road_network = {
    'Pune': {'Lonavala': 65, 'Ahmednagar': 120, 'Satara': 110},
    'Lonavala': {'Pune': 65, 'Mumbai': 85},
    'Ahmednagar': {'Pune': 120, 'Nashik': 155, 'Aurangabad': 115},
    'Satara': {'Pune': 110, 'Kolhapur': 120},
    'Nashik': {'Ahmednagar': 155, 'Mumbai': 165, 'Thane': 150},
    'Aurangabad': {'Ahmednagar': 115, 'Nashik': 190},
    'Kolhapur': {'Satara': 120},
    'Thane': {'Nashik': 150, 'Mumbai': 25},
    'Mumbai': {}
}

# Heuristic: Straight-Line (Aerial) Distance estimate to Destination 'Mumbai' (in km)
aerial_heuristic_to_mumbai = {
    'Pune': 120,
    'Lonavala': 70,
    'Ahmednagar': 210,
    'Satara': 190,
    'Nashik': 140,
    'Aurangabad': 275,
    'Kolhapur': 300,
    'Thane': 25,
    'Mumbai': 0
}

def find_shortest_route(origin, destination):
    print("=" * 65)
    print("AI ROUTE-FINDING NAVIGATION SYSTEM (A* SEARCH)")
    print("=" * 65)
    print(f"Origin City      : {origin}")
    print(f"Destination City : {destination}")
    print("-" * 65)

    # Priority queue stores tuples: (f_score, g_cost, current_city, route_path)
    # f(n) = g(n) [actual km traveled] + h(n) [estimated straight-line km to destination]
    start_f = 0 + aerial_heuristic_to_mumbai[origin]
    pq = [(start_f, 0, origin, [origin])]
    
    best_g = {origin: 0}
    visited = set()

    step = 1
    while pq:
        f_cost, g_cost, current_city, path = heapq.heappop(pq)

        if current_city in visited:
            continue
        visited.add(current_city)

        h_val = aerial_heuristic_to_mumbai[current_city]
        print(f"Step {step}: Visiting '{current_city}' | Traveled: {g_cost} km, Aerial Est: {h_val} km, Total f={f_cost}")
        step += 1

        if current_city == destination:
            print("=" * 65)
            print("OPTIMAL ROUTE FOUND!")
            print(f"Navigation Path : {' -> '.join(path)}")
            print(f"Total Road Distance: {g_cost} km")
            print("=" * 65)
            return path, g_cost

        for neighbor, distance in road_network[current_city].items():
            new_g = g_cost + distance
            new_f = new_g + aerial_heuristic_to_mumbai[neighbor]

            if neighbor not in best_g or new_g < best_g[neighbor]:
                best_g[neighbor] = new_g
                heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))

    print("No route exists to destination.")
    return None, float('inf')

if __name__ == "__main__":
    start_city = 'Pune'
    target_city = 'Mumbai'
    find_shortest_route(start_city, target_city)
