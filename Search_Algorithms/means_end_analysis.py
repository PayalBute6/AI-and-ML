"""
Assignment 2 (Set A - Q5)
Title: Means-End Analysis (MEA) for Goal-Based Problem Solving
Description: Implements Means-End Analysis where an AI agent detects differences 
             between the current state and goal state, selects suitable operators (means) 
             to eliminate the differences, and recursively satisfies preconditions until 
             the target goal is achieved.
"""

# Available Operators with their Preconditions and Effects (Additions & Deletions)
OPERATORS = [
    {
        "action": "Walk to Door",
        "preconditions": {"robot_at": "Hall"},
        "add": {"robot_at": "Door"},
        "delete": ["robot_at"]
    },
    {
        "action": "Unlock Door",
        "preconditions": {"robot_at": "Door", "has_key": True, "door_locked": True},
        "add": {"door_locked": False},
        "delete": ["door_locked"]
    },
    {
        "action": "Open Door",
        "preconditions": {"robot_at": "Door", "door_locked": False, "door_open": False},
        "add": {"door_open": True},
        "delete": ["door_open"]
    },
    {
        "action": "Enter Target Room",
        "preconditions": {"robot_at": "Door", "door_open": True},
        "add": {"robot_at": "Target Room"},
        "delete": ["robot_at"]
    }
]

def find_difference(current_state, goal_state):
    """Identifies attributes where current state does not match goal state."""
    diff = {}
    for key, val in goal_state.items():
        if current_state.get(key) != val:
            diff[key] = val
    return diff

def select_operator_for_difference(diff):
    """Finds an operator whose effect (add list) produces a needed attribute in diff."""
    for key, val in diff.items():
        for op in OPERATORS:
            if key in op["add"] and op["add"][key] == val:
                return op
    return None

def apply_operator(state, op):
    """Applies an operator's delete and add lists to update the world state."""
    new_state = state.copy()
    for del_key in op["delete"]:
        if del_key in new_state:
            del new_state[del_key]
    for add_key, add_val in op["add"].items():
        new_state[add_key] = add_val
    return new_state

def means_end_analysis(current_state, goal_state, plan=None):
    """Recursive MEA solver: transforms current state into goal state."""
    if plan is None:
        plan = []

    # Step 1: Detect differences
    diff = find_difference(current_state, goal_state)
    if not diff:
        return plan, current_state

    # Step 2: Select operator to reduce difference
    op = select_operator_for_difference(diff)
    if not op:
        print(f"Error: Cannot find operator to resolve differences: {diff}")
        return None, current_state

    print(f"\n[Detected Difference]   : {diff}")
    print(f"[Selected Means/Action] : '{op['action']}'")

    # Step 3: Check preconditions of chosen operator
    precond_diff = find_difference(current_state, op["preconditions"])
    if precond_diff:
        print(f"  --> Preconditions unmet: {precond_diff}. Recursively solving sub-goals...")
        sub_plan, current_state = means_end_analysis(current_state, op["preconditions"], plan)
        if sub_plan is None:
            return None, current_state

    # Step 4: Execute operator once preconditions are met
    print(f">>> EXECUTING ACTION: {op['action']}")
    current_state = apply_operator(current_state, op)
    plan.append(op["action"])

    # Step 5: Continue towards remaining goal differences
    return means_end_analysis(current_state, goal_state, plan)

if __name__ == "__main__":
    print("=" * 65)
    print("MEANS-END ANALYSIS (MEA): ROBOT REACHING TARGET ROOM")
    print("=" * 65)

    # Starting state of the world
    initial_state = {
        "robot_at": "Hall",
        "has_key": True,
        "door_locked": True,
        "door_open": False
    }

    # Desired goal state
    goal_state = {
        "robot_at": "Target Room"
    }

    print("Initial State :", initial_state)
    print("Goal State    :", goal_state)
    print("-" * 65)

    plan, final_state = means_end_analysis(initial_state, goal_state)

    print("\n" + "=" * 65)
    print("FINAL MEA SOLUTION PLAN:")
    print("=" * 65)
    for idx, action in enumerate(plan, 1):
        print(f"  Step {idx}: {action}")
    print("\nFinal World State:")
    for k, v in final_state.items():
        print(f"  {k}: {v}")
    print("=" * 65)
