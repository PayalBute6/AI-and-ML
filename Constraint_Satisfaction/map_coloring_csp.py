"""
Assignment 3 (Set A - Q1)
Title: Map Coloring Problem using CSP (Constraint Satisfaction Problem)
Description: Colors adjacent geographical regions using CSP backtracking such that 
             no two adjacent territories share the same color.
"""

# Variables (Regions of the Map)
regions = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']

# Adjacency list representing borders between regions (Binary Constraints)
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q':  ['NT', 'SA', 'NSW'],
    'NSW': ['SA', 'Q', 'V'],
    'V':   ['SA', 'NSW'],
    'T':   []  # Tasmania is an island with no land borders
}

# Domains: Available colors
colors = ['Red', 'Green', 'Blue']

def is_safe(region, color, assignment):
    """Check if assigning 'color' to 'region' satisfies all adjacency constraints."""
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack_map_coloring(assignment={}):
    """Recursive CSP backtracking algorithm."""
    # Base case: All variables are assigned
    if len(assignment) == len(regions):
        return assignment

    # Select an unassigned variable
    unassigned = [r for r in regions if r not in assignment]
    current_region = unassigned[0]

    for color in colors:
        if is_safe(current_region, color, assignment):
            # Assign color
            assignment[current_region] = color
            print(f"Assigning '{color}' to region '{current_region}'")

            result = backtrack_map_coloring(assignment)
            if result is not None:
                return result

            # Backtrack
            print(f"  [Conflict/Dead-end] Backtracking from region '{current_region}' (Removing {color})")
            del assignment[current_region]

    return None

def main():
    print("=" * 60)
    print("MAP COLORING PROBLEM USING CSP APPROACH")
    print("=" * 60)
    print(f"Variables (Regions) : {regions}")
    print(f"Domain (Colors)     : {colors}")
    print("-" * 60)

    solution = backtrack_map_coloring()

    print("=" * 60)
    if solution:
        print("SOLUTION FOUND (All Constraints Satisfied):")
        for region in regions:
            print(f"  Region {region:<5} ---> Color: {solution[region]}")
        print("-" * 60)
        print("Constraint Verification:")
        valid = True
        for r, adj_list in neighbors.items():
            for adj in adj_list:
                if solution[r] == solution[adj]:
                    valid = False
                    print(f"  Conflict between {r} and {adj}!")
        if valid:
            print("  All adjacent region constraints verified successfully!")
    else:
        print("No valid coloring exists with the given colors.")
    print("=" * 60)

if __name__ == "__main__":
    main()
