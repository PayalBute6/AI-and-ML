"""
Question: Write a program to implement the Backward Chaining inference mechanism.
"""

facts = {"rain"}

rules = {
    "wet_ground": ["rain"],
    "slippery": ["wet_ground"],
    "dangerous": ["slippery"]
}

def backward_chaining(goal):
    if goal in facts:
        return True
    if goal not in rules:
        return False

    for condition in rules[goal]:
        if backward_chaining(condition):
            facts.add(goal)
            return True

    return False

goal = "dangerous"
if backward_chaining(goal):
    print("Goal proved:", goal)
else:
    print("Goal cannot be proved")
