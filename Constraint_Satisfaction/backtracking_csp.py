"""
Assignment 3 (Set A - Q2)
Title: General Backtracking Algorithm for Constraint Satisfaction Problems (CSP)
Description: Implements a generalized CSP backtracking solver with variables, domains, 
             and arbitrary binary constraints, tracing variable assignment and backtracking steps.
"""

class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables      # List of variable names
        self.domains = domains          # Dict of {var: [possible_values]}
        self.constraints = constraints  # Function constraint(var1, val1, var2, val2) -> bool
        self.backtracks = 0
        self.assignments_count = 0

    def is_consistent(self, var, val, assignment):
        """Check if assigning val to var violates any constraint with currently assigned variables."""
        for other_var, other_val in assignment.items():
            if not self.constraints(var, val, other_var, other_val):
                return False
        return True

    def backtrack(self, assignment={}):
        """Standard recursive backtracking algorithm for CSP."""
        if len(assignment) == len(self.variables):
            return assignment

        # Select an unassigned variable
        unassigned_vars = [v for v in self.variables if v not in assignment]
        var = unassigned_vars[0]

        for val in self.domains[var]:
            self.assignments_count += 1
            print(f"Trying assignment: {var} = {val}")

            if self.is_consistent(var, val, assignment):
                assignment[var] = val
                print(f"  -> Valid! {var} = {val} placed into assignment.")

                result = self.backtrack(assignment)
                if result is not None:
                    return result

                # Backtrack
                self.backtracks += 1
                print(f"  <- [Dead End] Backtracking: removing {var} = {val}")
                del assignment[var]
            else:
                print(f"  -> Conflict detected! Value '{val}' violates constraints for {var}.")

        return None

def task_scheduling_demo():
    print("=" * 65)
    print("GENERAL CSP BACKTRACKING SOLVER: EXAM SCHEDULING")
    print("=" * 65)
    
    # 4 Exam courses that need time slots
    variables = ['Math', 'Physics', 'Chemistry', 'Biology']

    # Available time slots (1, 2, 3)
    domains = {
        'Math': [1, 2],
        'Physics': [1, 2, 3],
        'Chemistry': [2, 3],
        'Biology': [1, 2, 3]
    }

    # Mutual conflict constraints (Students share these subjects, so they CANNOT be at the same time slot)
    conflicts = {
        ('Math', 'Physics'), ('Physics', 'Math'),
        ('Physics', 'Chemistry'), ('Chemistry', 'Physics'),
        ('Chemistry', 'Biology'), ('Biology', 'Chemistry'),
        ('Math', 'Biology'), ('Biology', 'Math')
    }

    def constraint_function(var1, val1, var2, val2):
        if (var1, var2) in conflicts or (var2, var1) in conflicts:
            return val1 != val2  # Conflicting courses must have different time slots
        return True

    csp = CSP(variables, domains, constraint_function)
    solution = csp.backtrack({})

    print("=" * 65)
    if solution:
        print("OPTIMAL SOLUTION FOUND:")
        for var, slot in solution.items():
            print(f"  Course: {var:<12} ---> Assigned Slot: Time-Slot {slot}")
        print(f"\nTotal Assignment Attempts: {csp.assignments_count}")
        print(f"Total Backtrack Steps    : {csp.backtracks}")
    else:
        print("No valid assignment found satisfying all constraints.")
    print("=" * 65)

if __name__ == "__main__":
    task_scheduling_demo()
