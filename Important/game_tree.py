class GameNode:
    """
    Represents a single state (node) in our two-player game tree.
    """
    def __init__(self, name, score=None, is_max_player=True):
        self.name = name           # Name of the node (e.g., "A", "B", "Root")
        self.score = score         # The value of this board state (only leaves have this initially)
        self.is_max_player = is_max_player # True if it's Player 1's turn (MAX), False if Player 2 (MIN)
        self.children = []         # Possible moves from this state
        
    def add_child(self, child_node):
        self.children.append(child_node)

def solve_minimax(node, depth=0):
    """
    Evaluates the game tree using the Minimax algorithm.
    """
    # 1. Base Case: If it's a leaf node (the game is over), return its final score
    if not node.children:
        print(f"{'    ' * depth}Leaf {node.name} reached: Score is {node.score}")
        return node.score

    player_type = "MAX (P1)" if node.is_max_player else "MIN (P2)"
    print(f"{'    ' * depth}{player_type} is thinking at Node {node.name}...")
    
    # 2. If it's the MAX player's turn (they want the HIGHEST score)
    if node.is_max_player:
        best_score = -float('inf') # Start with the lowest possible score
        
        for child in node.children:
            score = solve_minimax(child, depth + 1)
            best_score = max(best_score, score) # Pick the highest one
            
        print(f"{'    ' * depth}-> MAX chooses the highest: {best_score} for Node {node.name}")
        node.score = best_score
        return best_score
        
    # 3. If it's the MIN player's turn (they want the LOWEST score)
    else:
        best_score = float('inf') # Start with the highest possible score
        
        for child in node.children:
            score = solve_minimax(child, depth + 1)
            best_score = min(best_score, score) # Pick the lowest one
            
        print(f"{'    ' * depth}-> MIN chooses the lowest: {best_score} for Node {node.name}")
        node.score = best_score
        return best_score

if __name__ == "__main__":
    # ==========================================
    # Let's build a classic two-player Game Tree
    # ==========================================
    # 
    #          MAX (Root)
    #          /        \
    #      MIN (B)      MIN (C)
    #      /    \       /     \
    #    D(3)  E(5)   F(2)   G(9) 
    #
    
    # Level 0 (Root): MAX Player's Turn
    root = GameNode("Root (A)", is_max_player=True)
    
    # Level 1: MIN Player's Turn
    b = GameNode("B", is_max_player=False)
    c = GameNode("C", is_max_player=False)
    root.add_child(b)
    root.add_child(c)
    
    # Level 2 (Leaves): Final Scores of the board
    b.add_child(GameNode("D", score=3))
    b.add_child(GameNode("E", score=5))
    
    c.add_child(GameNode("F", score=2))
    c.add_child(GameNode("G", score=9))
    
    print("Starting Game Tree Evaluation...\n")
    print("-" * 50)
    
    # Run the Minimax algorithm
    final_score = solve_minimax(root)
    
    print("-" * 50)
    print(f"Result: The MAX player can guarantee a final score of {final_score}!")
