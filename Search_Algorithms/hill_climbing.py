"""
Assignment 2 (Set A - Q4)
Title: Hill Climbing Algorithm for Function Optimization
Description: Demonstrates the Hill Climbing search algorithm to find the maximum value
             of a simple objective function f(x) = -(x - 5)^2 + 25 (Peak at x = 5, f(5) = 25).
"""

def objective_function(x):
    """Simple concave objective function: f(x) = -(x - 5)^2 + 25."""
    return -(x - 5) ** 2 + 25

def get_neighbors(x, step_size=0.5):
    """Generates neighboring points to the left and right."""
    return [round(x - step_size, 2), round(x + step_size, 2)]

def hill_climbing(start_x, step_size=0.5, max_iterations=50):
    print("=" * 60)
    print("STEEPEST-ASCENT HILL CLIMBING ALGORITHM")
    print("=" * 60)
    print("Objective Function: f(x) = -(x - 5)^2 + 25")
    print(f"Starting Point    : x = {start_x}, f(x) = {objective_function(start_x)}")
    print(f"Step Size (dx)    : {step_size}")
    print("-" * 60)

    current_x = start_x
    current_val = objective_function(current_x)

    iteration = 1
    while iteration <= max_iterations:
        neighbors = get_neighbors(current_x, step_size)
        
        # Evaluate all neighbors
        best_neighbor = None
        best_val = current_val

        print(f"Iteration {iteration:02d}: Current x = {current_x:.2f}, f(x) = {current_val:.4f}")
        for n in neighbors:
            n_val = objective_function(n)
            print(f"    Evaluating Neighbor x = {n:.2f} -> f(x) = {n_val:.4f}")
            if n_val > best_val:
                best_val = n_val
                best_neighbor = n

        # Check termination condition: Peak reached (no neighbor is better)
        if best_neighbor is None or best_val <= current_val:
            print("-" * 60)
            print(f"Peak Reached! No better neighboring state found.")
            break

        # Move to the best neighbor
        print(f"  --> Moving from x = {current_x:.2f} to x = {best_neighbor:.2f} (Improvement: +{best_val - current_val:.4f})")
        current_x = best_neighbor
        current_val = best_val
        iteration += 1

    print("=" * 60)
    print("HILL CLIMBING COMPLETED")
    print(f"Maximum found at: x = {current_x:.2f}")
    print(f"Maximum value   : f(x) = {current_val:.4f}")
    print("=" * 60)
    return current_x, current_val

if __name__ == "__main__":
    # Starting away from the peak (e.g., at x = 0.0)
    initial_x = 0.0
    hill_climbing(initial_x, step_size=0.5)
