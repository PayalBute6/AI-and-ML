"""
Assignment 3 (Set A - Q4)
Title: Domain Reduction Technique in Constraint Satisfaction Problems (CSP)
Description: Demonstrates how unary and binary constraints prune/reduce the domain of 
             variables before or during search, drastically shrinking the state space.
"""

def print_domains(title, domains):
    print(f"\n{title}:")
    for var, dom in domains.items():
        print(f"  Domain({var}) = {sorted(list(dom))}")

def domain_reduction_demo():
    print("=" * 65)
    print("DOMAIN REDUCTION TECHNIQUE IN CSP")
    print("=" * 65)

    # Step 1: Initialize variables and initial domains
    variables = ['X', 'Y', 'Z']
    domains = {
        'X': {1, 2, 3, 4, 5},
        'Y': {1, 2, 3, 4, 5},
        'Z': {1, 2, 3, 4, 5}
    }

    print_domains("Step 1: Initial Variable Domains", domains)

    print("\nConstraints to satisfy:")
    print("  1. Unary Constraint  : Z <= 4")
    print("  2. Binary Constraint : Y < Z")
    print("  3. Binary Constraint : X < Y")
    print("  4. Binary Constraint : X + Y == 5")
    print("-" * 65)

    # Step 2: Apply Unary constraint: Z <= 4
    pruned_z = {v for v in domains['Z'] if not (v <= 4)}
    domains['Z'] -= pruned_z
    print(f"Applying 'Z <= 4' -> Pruned from Z: {pruned_z}")
    print_domains("After Unary Constraint on Z", domains)

    # Step 3: Apply Binary constraint: Y < Z
    # For every y in Y, there must exist at least one z in Z such that y < z
    pruned_y = {y for y in domains['Y'] if not any(y < z for z in domains['Z'])}
    domains['Y'] -= pruned_y
    print(f"\nApplying 'Y < Z' -> Pruned from Y: {pruned_y}")
    print_domains("After reducing domain of Y", domains)

    # Step 4: Apply Binary constraint: X < Y
    # For every x in X, there must exist at least one y in Y such that x < y
    pruned_x = {x for x in domains['X'] if not any(x < y for y in domains['Y'])}
    domains['X'] -= pruned_x
    print(f"\nApplying 'X < Y' -> Pruned from X: {pruned_x}")
    print_domains("After reducing domain of X", domains)

    # Step 5: Apply Binary constraint: X + Y == 5
    # Value x is valid only if (5 - x) is in domain of Y
    pruned_xy = {x for x in domains['X'] if (5 - x) not in domains['Y']}
    domains['X'] -= pruned_xy
    print(f"\nApplying 'X + Y == 5' -> Pruned from X: {pruned_xy}")

    # Re-check Y with updated X
    pruned_yx = {y for y in domains['Y'] if (5 - y) not in domains['X']}
    domains['Y'] -= pruned_yx
    print(f"Propagating to Y: Pruned from Y: {pruned_yx}")

    # Re-check Z with updated Y (Y < Z)
    pruned_zy = {z for z in domains['Z'] if not any(y < z for y in domains['Y'])}
    domains['Z'] -= pruned_zy
    print(f"Propagating to Z: Pruned from Z: {pruned_zy}")

    print("=" * 65)
    print_domains("FINAL REDUCED DOMAINS (Consistent CSP)", domains)
    print("=" * 65)

    print("\nResulting Valid Solutions from Reduced Domains:")
    solution_count = 0
    for x in domains['X']:
        for y in domains['Y']:
            for z in domains['Z']:
                if x < y and y < z and (x + y == 5) and z <= 4:
                    solution_count += 1
                    print(f"  Solution {solution_count}: X = {x}, Y = {y}, Z = {z}")
    print("=" * 65)

if __name__ == "__main__":
    domain_reduction_demo()
