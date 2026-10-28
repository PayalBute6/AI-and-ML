"""
Assignment 3 (Set B - Q2)
Title: Graph Coloring Problem using Backtracking Algorithm
Description: Solves the m-Coloring graph problem using CSP backtracking where vertices 
             are assigned colors such that no two adjacent vertices share the same color.
"""

class GraphColoring:
    def __init__(self, vertices, edges, num_colors):
        self.vertices = vertices
        self.num_vertices = len(vertices)
        self.edges = edges
        self.m = num_colors
        self.color_names = ["None", "Red", "Green", "Blue", "Yellow"]
        self.colors = [0] * self.num_vertices

        # Construct adjacency matrix
        self.adj_matrix = [[0] * self.num_vertices for _ in range(self.num_vertices)]
        for u, v in edges:
            i, j = vertices.index(u), vertices.index(v)
            self.adj_matrix[i][j] = 1
            self.adj_matrix[j][i] = 1

    def is_safe(self, v_idx, c):
        """Check if any adjacent vertex already has color 'c'."""
        for i in range(self.num_vertices):
            if self.adj_matrix[v_idx][i] == 1 and self.colors[i] == c:
                return False
        return True

    def solve(self, v_idx=0):
        """Recursive backtracking solver."""
        if v_idx == self.num_vertices:
            return True

        for c in range(1, self.m + 1):
            if self.is_safe(v_idx, c):
                self.colors[v_idx] = c
                print(f"Vertex '{self.vertices[v_idx]}' assigned color {self.color_names[c]}")

                if self.solve(v_idx + 1):
                    return True

                # Backtrack
                print(f"  [Conflict] Backtracking: Uncoloring Vertex '{self.vertices[v_idx]}'")
                self.colors[v_idx] = 0

        return False

    def print_result(self):
        print("=" * 60)
        print(f"GRAPH COLORING SOLUTION (Using {self.m} Colors)")
        print("=" * 60)
        for i, vertex in enumerate(self.vertices):
            print(f"  Vertex {vertex}  --->  Color: {self.color_names[self.colors[i]]}")
        print("-" * 60)
        print("Edge Constraints Verification:")
        for u, v in self.edges:
            c1 = self.color_names[self.colors[self.vertices.index(u)]]
            c2 = self.color_names[self.colors[self.vertices.index(v)]]
            print(f"  Edge ({u} - {v}): {c1} != {c2} -> Valid")
        print("=" * 60)

def main():
    print("=" * 60)
    print("GRAPH COLORING CSP SOLVER")
    print("=" * 60)

    # Vertices and undirected edges
    vertices = ['A', 'B', 'C', 'D', 'E']
    edges = [
        ('A', 'B'), ('A', 'C'), ('A', 'D'),
        ('B', 'C'), ('B', 'E'),
        ('C', 'D'), ('C', 'E'),
        ('D', 'E')
    ]
    num_colors = 3  # Try coloring with 3 colors

    print(f"Vertices   : {vertices}")
    print(f"Edges      : {edges}")
    print(f"Max Colors : {num_colors}")
    print("-" * 60)

    gc = GraphColoring(vertices, edges, num_colors)
    if gc.solve(0):
        gc.print_result()
    else:
        print(f"No valid coloring possible with {num_colors} colors.")

if __name__ == "__main__":
    main()
