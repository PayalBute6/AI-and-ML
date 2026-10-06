"""
Question: Write a program to build a Knowledge Base using logical rules and facts.
"""

# Knowledge Base using Facts and Rules

# Facts
facts = {
    "bird": True,
    "has_feathers": True
}

# Rules
rules = {
    "bird": "can_fly"
}

# Display facts
print("Facts in Knowledge Base:")

for fact in facts:
    print("-", fact)

# Apply rule
if "bird" in facts and facts["bird"] == True:
    conclusion = rules["bird"]

    print("\nApplying Rule:")
    print("If bird then can_fly")

    print("\nConclusion:")
    print("The bird", conclusion)
