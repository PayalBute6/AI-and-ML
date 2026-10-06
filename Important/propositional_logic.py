import itertools

# ==========================================
# 1. Define Propositional Logic Operators
# ==========================================
def AND(p, q):
    return p and q

def OR(p, q):
    return p or q

def NOT(p):
    return not p

def IMPLIES(p, q):
    # In logic, P -> Q is exactly the same as (NOT P) OR Q
    return (not p) or q

def EQUIV(p, q):
    # P <-> Q means P and Q must have the exact same truth value
    return p == q

# ==========================================
# 2. Logic Evaluator Engine
# ==========================================
def evaluate_expression(variables, values, expression_func):
    """
    Pairs the variables with their True/False values and evaluates the logic.
    """
    # Create a dictionary. For example: {'P': True, 'Q': False}
    assignment = dict(zip(variables, values))
    
    # Run the expression with these values and return the boolean result
    return expression_func(assignment)

def generate_truth_table(variables, expression_func, expression_name):
    """
    Generates every possible True/False combination and prints a Truth Table.
    """
    print(f"\nTruth Table for: {expression_name}")
    print("-" * (len(expression_name) + 20))
    
    # Print Header (e.g., "P | Q | Result")
    header_cols = variables + ["Result"]
    header = " | ".join(header_cols)
    print(header)
    print("-" * len(header))
    
    # itertools.product generates all True/False combos for N variables
    combinations = list(itertools.product([True, False], repeat=len(variables)))
    
    for values in combinations:
        # Get the result for this specific combination
        result = evaluate_expression(variables, values, expression_func)
        
        # Format it nicely with 'T' and 'F' instead of 'True' and 'False'
        row_str = " | ".join(['T' if v else 'F' for v in values])
        res_str = 'T' if result else 'F'
        
        print(f"{row_str} |   {res_str}")

# ==========================================
# 3. Main Program & Examples
# ==========================================
if __name__ == "__main__":
    print("PROPOSITIONAL LOGIC EVALUATOR")
    print("=" * 30)

    # --- Example 1 ---
    # Expression: P AND (NOT Q)
    vars_1 = ['P', 'Q']
    # Define the logic using our operators. v['P'] gets the truth value of P
    def expr_1(v): return AND(v['P'], NOT(v['Q']))
    
    generate_truth_table(vars_1, expr_1, "P AND (NOT Q)")
    
    # --- Example 2 ---
    # Expression: (P OR Q) IMPLIES R
    vars_2 = ['P', 'Q', 'R']
    def expr_2(v): return IMPLIES(OR(v['P'], v['Q']), v['R'])
    
    generate_truth_table(vars_2, expr_2, "(P OR Q) IMPLIES R")
    
    # --- Example 3 (Checking De Morgan's Law) ---
    # Law: NOT(P AND Q) is equivalent to (NOT P) OR (NOT Q)
    vars_3 = ['P', 'Q']
    def expr_3(v): 
        left_side = NOT(AND(v['P'], v['Q']))
        right_side = OR(NOT(v['P']), NOT(v['Q']))
        return EQUIV(left_side, right_side)
        
    generate_truth_table(vars_3, expr_3, "NOT(P AND Q) <-> (NOT P) OR (NOT Q)")
    print("\n(Notice how the result is all T's. This means it's a Tautology, proving the law is true!)")
