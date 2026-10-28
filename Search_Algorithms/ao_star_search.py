"""
Assignment 2 (Set B - Q1)
Title: AO* (AND-OR Star) Search Algorithm
Description: Implements the AO* algorithm to find an optimal solution tree 
             in an AND-OR graph using heuristic evaluations and bottom-up cost updates.
"""

class AOStar:
    def __init__(self, graph, heuristics, start_node):
        self.graph = graph
        self.H = heuristics
        self.start = start_node
        self.solution_graph = {}

    def get_minimum_cost_child_node(self, node):
        """Calculates branch costs for OR/AND branches and selects the minimum."""
        minimum_cost = float('inf')
        cost_to_child_node_list_dict = {}
        cost_to_child_node_list_dict[minimum_cost] = []
        flag = True

        for node_info_list in self.graph.get(node, []):
            cost = 0
            node_list = []
            for val, weight in node_info_list:
                cost = cost + self.H[val] + weight
                node_list.append(val)

            if flag:
                minimum_cost = cost
                cost_to_child_node_list_dict[minimum_cost] = node_list
                flag = False
            else:
                if cost < minimum_cost:
                    minimum_cost = cost
                    cost_to_child_node_list_dict[minimum_cost] = node_list

        return minimum_cost, cost_to_child_node_list_dict[minimum_cost]

    def ao_star(self, node, back_tracking=False):
        """Main AO* recursive function."""
        print(f"Expanding Node: {node} (Heuristic: {self.H[node]})")

        if node in self.graph and len(self.graph[node]) > 0:
            min_cost, child_node_list = self.get_minimum_cost_child_node(node)
            print(f"  -> Best branch from {node}: {child_node_list} with total computed cost = {min_cost}")
            self.H[node] = min_cost
            self.solution_graph[node] = child_node_list

            # Recursively explore each child in the optimal branch (both children if AND branch)
            for child_node in child_node_list:
                self.ao_star(child_node, back_tracking=True)

    def print_solution(self):
        print("\n" + "=" * 55)
        print("AO* SEARCH COMPLETED - OPTIMAL SOLUTION GRAPH")
        print("=" * 55)
        print("Root Node:", self.start)
        print("Updated Heuristic / Path Costs:")
        for k in sorted(self.H.keys()):
            print(f"  Node {k}: Cost = {self.H[k]}")
        print("\nMarked Solution Tree Branches:")
        for parent, children in self.solution_graph.items():
            branch_type = "AND Branch" if len(children) > 1 else "OR Branch"
            print(f"  {parent} ---> {children}  ({branch_type})")
        print("=" * 55)

if __name__ == "__main__":
    print("=" * 55)
    print("AO* (AND-OR STAR) ALGORITHM")
    print("=" * 55)

    # Initial Heuristic values for each node
    heuristic_values = {
        'A': -1,
        'B': 4,
        'C': 2,
        'D': 3,
        'E': 6,
        'F': 8,
        'G': 2,
        'H': 0,
        'I': 0,
        'J': 0
    }

    # Graph representation:
    # Each node maps to a list of branches.
    # Each branch is a list of tuples: [(child_node, edge_weight), ...]
    # Branch with 1 tuple = OR branch (single action)
    # Branch with >1 tuples = AND branch (all sub-nodes must be solved)
    and_or_graph = {
        'A': [
            [('B', 1), ('C', 1)],  # AND branch: Solve B AND C (edge cost 1 each)
            [('D', 1)]             # OR branch: Solve D (edge cost 1)
        ],
        'B': [
            [('G', 1)],            # OR branch
            [('H', 1)]             # OR branch
        ],
        'C': [
            [('I', 1)],            # OR branch
            [('J', 1)]             # OR branch
        ],
        'D': [
            [('E', 1), ('F', 1)]   # AND branch: Solve E AND F
        ]
    }

    ao = AOStar(and_or_graph, heuristic_values, 'A')
    ao.ao_star('A')
    ao.print_solution()
