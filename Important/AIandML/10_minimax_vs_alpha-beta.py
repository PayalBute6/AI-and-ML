"""
Question: Write a program or report that compares Minimax and Alpha-Beta Pruning on the same game tree.
"""

import math

tree = {
    'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'G'],
    'D': 3, 'E': 5, 'F': 2, 'G': 9
}

def minimax(node, maximizing):
    if isinstance(tree[node], int):
        return tree[node]
    values = [minimax(child, not maximizing) for child in tree[node]]
    return max(values) if maximizing else min(values)

def alpha_beta(node, alpha, beta, maximizing):
    if isinstance(tree[node], int):
        return tree[node]

    if maximizing:
        value = -math.inf
        for child in tree[node]:
            value = max(value, alpha_beta(child, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta: break
        return value
    else:
        value = math.inf
        for child in tree[node]:
            value = min(value, alpha_beta(child, alpha, beta, True))
            beta = min(beta, value)
            if alpha >= beta: break
        return value

print("Minimax:", minimax('A', True))
print("Alpha-Beta:", alpha_beta('A', -math.inf, math.inf, True))
