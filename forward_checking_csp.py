"""
Assignment 3 (Set B - Q5)
Title: Forward Checking Algorithm for Constraint Satisfaction Problems (CSP)
Description: Implements Backtracking with Forward Checking (FC). When a variable is 
             assigned a value, conflicting values are immediately pruned from the domains 
             of all unassigned neighbors, detecting dead-ends much earlier than basic backtracking.
"""

import copy

class ForwardCheckingCSP:
    def __init__(self, variables, domains, neighbors, constraints):
        self.variables = variables          # List of variables
        self.domains = domains              # Initial domains dict: {var: list of values}
        self.neighbors = neighbors          # Graph: {var: list of neighbor vars}
        self.constraints = constraints      # Function: (v1, val1, v2, val2) -> bool
        self.backtracks = 0
        self.nodes_explored = 0

    def forward_check(self, var, val, assignment, current_domains):
        """Prunes conflicting values from unassigned neighbors of 'var'."""
        pruned = {neighbor: [] for neighbor in self.neighbors[var] if neighbor not in assignment}

        for neighbor in self.neighbors[var]:
            if neighbor not in assignment:
                valid_vals = []
                for n_val in current_domains[neighbor]:
                    if self.constraints(var, val, neighbor, n_val):
                        valid_vals.append(n_val)
                    else:
                        pruned[neighbor].append(n_val)

                # If neighbor has no remaining values in domain -> Domain Wipeout (Dead End)
                if len(valid_vals) == 0:
                    return None  # Failure

                current_domains[neighbor] = valid_vals

        return pruned

    def solve(self, assignment={}, current_domains=None):
        """Recursive backtracking with forward checking."""
        if current_domains is None:
            current_domains = copy.deepcopy(self.domains)

        self.nodes_explored += 1

        # Base case: All variables assigned
        if len(assignment) == len(self.variables):
            return assignment

        # Select next unassigned variable
        unassigned = [v for v in self.variables if v not in assignment]
        var = unassigned[0]

        print(f"\nVisiting Variable '{var}' (Current Domain: {current_domains[var]})")

        for val in list(current_domains[var]):
            print(f"  Attempting {var} = {val}...")
            assignment[var] = val

            # Perform forward checking on neighbors
            saved_domains = copy.deepcopy(current_domains)
            prune_result = self.forward_check(var, val, assignment, current_domains)

            if prune_result is not None:
                # Forward checking succeeded: domain not wiped out
                for n, pruned_items in prune_result.items():
                    if pruned_items:
                        print(f"    [Pruned] {n}'s domain had {pruned_items} removed -> Remaining: {current_domains[n]}")

                result = self.solve(assignment, current_domains)
                if result is not None:
                    return result

            # Failure / Dead-end detected: Backtrack
            self.backtracks += 1
            print(f"  <- [Forward Check Failure] Backtracking on {var} = {val}")
            del assignment[var]
            current_domains = saved_domains  # Restore domains

        return None

def main():
    print("=" * 65)
    print("BACKTRACKING WITH FORWARD CHECKING (CSP)")
    print("=" * 65)

    # 4 Regions / Nodes
    variables = ['A', 'B', 'C', 'D']

    # 3 Colors
    domains = {
        'A': ['Red', 'Green', 'Blue'],
        'B': ['Red', 'Green', 'Blue'],
        'C': ['Red', 'Green', 'Blue'],
        'D': ['Red', 'Green', 'Blue']
    }

    # Connectivity graph
    neighbors = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D'],
        'D': ['B', 'C']
    }

    def constraint(v1, val1, v2, val2):
        return val1 != val2

    fc = ForwardCheckingCSP(variables, domains, neighbors, constraint)
    solution = fc.solve()

    print("\n" + "=" * 65)
    print("FORWARD CHECKING EXECUTION SUMMARY:")
    print("=" * 65)
    if solution:
        print("Valid Solution Found:")
        for var in variables:
            print(f"  Variable {var} ---> {solution[var]}")
        print(f"\nTotal Nodes Explored: {fc.nodes_explored}")
        print(f"Total Backtracks    : {fc.backtracks}")
    else:
        print("No solution found.")
    print("=" * 65)

if __name__ == "__main__":
    main()
