class GameNode:
    """
    Represents a single state (node) in our game tree.
    """
    def __init__(self, name, score=None):
        self.name = name           
        self.score = score         
        self.children = []         
        
    def add_child(self, child_node):
        self.children.append(child_node)

def alpha_beta_search(node, depth, alpha, beta, is_max_player):
    """
    Evaluates the game tree using Minimax with Alpha-Beta Pruning.
    """
    # 1. Base Case: If it's a leaf node, return its score
    if not node.children:
        print(f"{'    ' * depth}Leaf {node.name} -> returns {node.score}")
        return node.score

    if is_max_player:
        best_score = -float('inf')
        print(f"{'    ' * depth}MAX evaluating {node.name} (alpha={alpha}, beta={beta})")
        
        for child in node.children:
            score = alpha_beta_search(child, depth + 1, alpha, beta, False)
            best_score = max(best_score, score)
            
            # Update Alpha (the best MAX can guarantee so far)
            alpha = max(alpha, best_score)
            
            # Pruning condition
            if beta <= alpha:
                print(f"{'    ' * (depth+1)}[PRUNED] Stop exploring {node.name}'s remaining children! (beta {beta} <= alpha {alpha})")
                break
                
        print(f"{'    ' * depth}-> MAX chooses {best_score} for {node.name}")
        return best_score
        
    else:
        best_score = float('inf')
        print(f"{'    ' * depth}MIN evaluating {node.name} (alpha={alpha}, beta={beta})")
        
        for child in node.children:
            score = alpha_beta_search(child, depth + 1, alpha, beta, True)
            best_score = min(best_score, score)
            
            # Update Beta (the lowest MIN can guarantee so far)
            beta = min(beta, best_score)
            
            # Pruning condition
            if beta <= alpha:
                print(f"{'    ' * (depth+1)}[PRUNED] Stop exploring {node.name}'s remaining children! (beta {beta} <= alpha {alpha})")
                break
                
        print(f"{'    ' * depth}-> MIN chooses {best_score} for {node.name}")
        return best_score

if __name__ == "__main__":
    # Build the game tree exactly from the image
    #
    #                 Root (MAX)
    #               /     |      \
    #          A(MIN)   B(MIN)   C(MIN)
    #         /   \     /    \    /   \
    #        3     5   2      9  0     7
    
    # Root
    root = GameNode("Root")
    
    # Level 1
    a = GameNode("A")
    b = GameNode("B")
    c = GameNode("C")
    root.add_child(a)
    root.add_child(b)
    root.add_child(c)
    
    # Level 2 (Leaves)
    a.add_child(GameNode("Leaf 3", score=3))
    a.add_child(GameNode("Leaf 5", score=5))
    
    b.add_child(GameNode("Leaf 2", score=2))
    b.add_child(GameNode("Leaf 9", score=9))
    
    c.add_child(GameNode("Leaf 0", score=0))
    c.add_child(GameNode("Leaf 7", score=7))
    
    print("Starting Alpha-Beta Pruning Algorithm...")
    print("=" * 60)
    
    # Initial call: Depth 0, Alpha = -infinity, Beta = infinity, Maximizing Player = True
    final_score = alpha_beta_search(root, 0, -float('inf'), float('inf'), True)
    
    print("=" * 60)
    print(f"Final Optimal Score: {final_score}")
