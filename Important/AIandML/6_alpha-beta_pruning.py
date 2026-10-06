"""
Question: Write a program to implement Alpha-Beta Pruning for optimizing the Minimax search process.
"""

import math


def alpha_beta(node, depth, alpha, beta, maximizing):

    # Leaf node
    if depth == 0:
        return node

    if maximizing:

        best = -math.inf

        for child in node:

            value = alpha_beta(
                child,
                depth - 1,
                alpha,
                beta,
                False
            )

            best = max(best, value)
            alpha = max(alpha, best)

            # Pruning
            if alpha >= beta:
                break

        return best

    else:

        best = math.inf

        for child in node:

            value = alpha_beta(
                child,
                depth - 1,
                alpha,
                beta,
                True
            )

            best = min(best, value)
            beta = min(beta, best)

            # Pruning
            if alpha >= beta:
                break

        return best


# Game tree
tree = [
    [3, 5],
    [2, 9],
    [0, 7]
]

# Root is MAX
result = alpha_beta(
    tree,
    2,
    -math.inf,
    math.inf,
    True
)

print("Best value:", result)
