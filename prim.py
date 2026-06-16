#credit: https://www.w3schools.com/dsa/dsa_algo_mst_prim.php

class Graph:  # Define class
    def __init__(self, size):  # Define constructor
        self.adj_matrix = [[0] * size for _ in range(size)]  # Matrix with everything initialized to 0
        self.size = size  # Assigns size to size of that instance
        self.vertex_data = [''] * size  # Creates list depending on the size of graph

    def add_edge(self, u, v, weight):  # Define function
        if 0 <= u < self.size and 0 <= v < self.size:  # Checks if vertices are within given range of graph
            self.adj_matrix[u][v] = weight  # Assigns weight depending on passed parameter
            self.adj_matrix[v][u] = weight  # Assigns weight depending on passed parameter  # For undirected graph

    def add_vertex_data(self, vertex, data):  # Define function to add vertex
        if 0 <= vertex < self.size:  # Checks if vertex are within given range of graph
            self.vertex_data[vertex] = data   # Assigns value at given vertex index

    def prims_algorithm(self):  # Define function
        in_mst = [False] * self.size  # Create list to keep track of vertices
        key_values = [float('inf')] * self.size  # Key value for each vertex
        parents = [-1] * self.size  # Stores the parent of each vertex

        key_values[0] = 0  # Key value of start vertex to 0

        print("Edge \tWeight")
        for _ in range(self.size):  # Iterate of eav vertex
            u = min((v for v in range(self.size) if not in_mst[v]), key=lambda v: key_values[v])  # Find vertex with min key valu that is no the list

            in_mst[u] = True  # Mark vertex as true

            if parents[u] != -1:  # If vertex has a parent
                print(f"{self.vertex_data[parents[u]]}-{self.vertex_data[u]} \t{self.adj_matrix[u][parents[u]]}")

            for v in range(self.size):  # Iterates over vertices
                if 0 < self.adj_matrix[u][v] < key_values[v] and not in_mst[v]:  # If not in the list
                    key_values[v] = self.adj_matrix[u][v]  # Update key value of v
                    parents[v] = u  # Assigns parent of v to u

# Given tree
g = Graph(8) # Create instance of class
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')
g.add_vertex_data(7, 'H')
# Adds edges with existing vertices
g.add_edge(0, 1, 4)  # A - B
g.add_edge(0, 3, 3)  # A - D
g.add_edge(1, 2, 3)  # B - C
g.add_edge(1, 3, 5)  # B - D
g.add_edge(1, 4, 6)  # B - E
g.add_edge(2, 4, 4)  # C - E
g.add_edge(2, 7, 2)  # C - H
g.add_edge(3, 4, 7)  # D - E
g.add_edge(3, 5, 4)  # D - F
g.add_edge(4, 5, 5)  # E - F
g.add_edge(4, 6, 3)  # E - G
g.add_edge(5, 6, 7)  # F - G
g.add_edge(6, 7, 5)  # G - H

print("Prim's Algorithm MST:")
g.prims_algorithm()

g2 = Graph(6)  # Create instance of class with 6 vertices
g2.add_vertex_data(0, 'X')
g2.add_vertex_data(1, 'Y')
g2.add_vertex_data(2, 'Z')
g2.add_vertex_data(3, 'W')
g2.add_vertex_data(4, 'U')
g2.add_vertex_data(5, 'V')

# Adds edges with existing vertices
g2.add_edge(0, 1, 5)  # X - Y
g2.add_edge(0, 2, 4)  # X - Z
g2.add_edge(1, 2, 3)  # Y - Z
g2.add_edge(1, 3, 7)  # Y - W
g2.add_edge(2, 3, 2)  # Z - W
g2.add_edge(2, 4, 6)  # Z - U
g2.add_edge(3, 4, 8)  # W - U
g2.add_edge(3, 5, 9)  # W - V
g2.add_edge(4, 5, 3)  # U - V
print("Prim's Algorithm MST:")
g2.prims_algorithm()
