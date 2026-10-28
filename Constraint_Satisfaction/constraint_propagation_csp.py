"""
Assignment 3 (Set B - Q4)
Title: Constraint Propagation in CSP using AC-3 (Arc Consistency) Algorithm
Description: Demonstrates Constraint Propagation using the AC-3 algorithm where 
             inconsistencies between connected variables propagate through the network, 
             pruning invalid domain values without search.
"""

from collections import deque

class AC3ConstraintPropagation:
    def __init__(self, variables, domains, neighbors, constraints):
        self.variables = variables          # List of variables
        self.domains = {v: list(d) for v, d in domains.items()}  # Domains dictionary
        self.neighbors = neighbors          # Graph adjacency: {var: [neighbor_vars]}
        self.constraints = constraints      # Function: (var1, val1, var2, val2) -> bool

    def revise(self, xi, xj):
        """Revises domain of Xi with respect to Xj. Returns True if domain was pruned."""
        revised = False
        to_remove = []

        for x_val in self.domains[xi]:
            # Check if there exists ANY y_val in domain of Xj that satisfies the constraint
            satisfies_any = any(self.constraints(xi, x_val, xj, y_val) for y_val in self.domains[xj])
            if not satisfies_any:
                to_remove.append(x_val)
                revised = True

        if revised:
            for val in to_remove:
                self.domains[xi].remove(val)
            print(f"  [Revision] Pruned value(s) {to_remove} from Domain({xi}) based on Arc ({xi} -> {xj})")

        return revised

    def ac3(self):
        """AC-3 Arc Consistency Algorithm."""
        print("=" * 65)
        print("CONSTRAINT PROPAGATION VIA AC-3 ALGORITHM")
        print("=" * 65)
        print("Initial Domains:")
        for v in self.variables:
            print(f"  {v}: {self.domains[v]}")
        print("-" * 65)

        # Initialize queue with all directed arcs in the CSP
        queue = deque()
        for xi in self.variables:
            for xj in self.neighbors.get(xi, []):
                queue.append((xi, xj))

        step = 1
        while queue:
            xi, xj = queue.popleft()

            if self.revise(xi, xj):
                print(f"Step {step:02d}: Arc ({xi}, {xj}) revised. Updated Domain({xi}) = {self.domains[xi]}")
                step += 1

                # If domain is emptied, problem is unsolvable
                if len(self.domains[xi]) == 0:
                    print(f"Domain({xi}) became empty! CSP has no solution.")
                    return False

                # Propagate: Re-enqueue all incoming arcs (Xk, Xi) except (Xj, Xi)
                for xk in self.neighbors.get(xi, []):
                    if xk != xj and (xk, xi) not in queue:
                        queue.append((xk, xi))
                        print(f"    --> Re-enqueued arc ({xk}, {xi}) for propagation")

        print("=" * 65)
        print("ARC CONSISTENCY REACHED (No more values violate constraints):")
        for v in self.variables:
            print(f"  {v}: {self.domains[v]}")
        print("=" * 65)
        return True

def demo():
    # Variables representing 3 connected entities
    variables = ['A', 'B', 'C']

    # Initial Domains
    domains = {
        'A': [1, 2, 3],
        'B': [1, 2, 3],
        'C': [1, 2, 3]
    }

    # Neighbor graph (Edges)
    neighbors = {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B']
    }

    # Binary constraints:
    # 1. A must be strictly greater than B (A > B)
    # 2. B must equal C (B == C)
    # 3. A + C must equal 4 (A + C == 4)
    def constraints(v1, val1, v2, val2):
        if (v1, v2) == ('A', 'B'): return val1 > val2
        if (v1, v2) == ('B', 'A'): return val2 > val1
        if (v1, v2) in [('B', 'C'), ('C', 'B')]: return val1 == val2
        if (v1, v2) in [('A', 'C'), ('C', 'A')]: return val1 + val2 == 4
        return True

    propagator = AC3ConstraintPropagation(variables, domains, neighbors, constraints)
    propagator.ac3()

if __name__ == "__main__":
    demo()
