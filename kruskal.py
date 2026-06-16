#credit: https://www.w3schools.com/dsa/dsa_algo_mst_kruskal.php

class Graph:  # Define class
    def __init__(self, size):  # Define constructor that takes in instance and size of graph
        self.size = size  # Assigns size to the size of that instance
        self.edges = []  # Creates empty list
        self.vertex_data = [''] * size  # Creates list depending on the size of graph

    def add_edge(self, u, v, weight):  # Define function to add an edge, u: start vertex,v: end vertex, weight between them
        if 0 <= u < self.size and 0 <= v < self.size:  # Checks if vertices are within given range of graph
            self.edges.append((u, v, weight))  # Adds edge to list

    def add_vertex_data(self, vertex, data):  # Define function that adds vertex value
        if 0 <= vertex < self.size:  # Checks if vertex is within graph range
            self.vertex_data[vertex] = data  # Assigns value at given vertex index

    def find(self, parent, i):  # Define function to find vertex
        if parent[i] == i:  # Check if equal
            return i  # Returns value
        return self.find(parent, parent[i])  # Recalls function recursively

    def union(self, parent, rank, x, y):  # Define function
        xroot = self.find(parent, x)  # Finds parent of x
        yroot = self.find(parent, y)  # Finds parent of y
        if rank[xroot] < rank[yroot]:  # If statement that checks root of x is less than root of y
            parent[xroot] = yroot  # Update parent of y
        elif rank[xroot] > rank[yroot]:  # If statement that checks root of y is less than root of x
            parent[yroot] = xroot  # Update parent of x
        else:  # Are equal
            parent[yroot] = xroot  # Update parent of x
            rank[xroot] += 1  # Increment rank

    def kruskals_algorithm(self):  # Define function
        result = []  # Create empty list
        i = 0  # Edge counter

        self.edges = sorted(self.edges, key=lambda item: item[2])  # Sort edges in non-decreasing order

        parent, rank = [], []  # Initialize list to use for union function

        for node in range(self.size):  # Iterates ove each vertex in graph
            parent.append(node)  # Points to itself
            rank.append(0)  # Initial rank is 0

        while i < len(self.edges):  # Iterates over each edge
            u, v, weight = self.edges[i]  # Edge information
            i += 1  # Move to next edge

            x = self.find(parent, u)  # Find the root
            y = self.find(parent, v)  # Find the root
            if x != y:  # If sets are not equal
                result.append((u, v, weight))  # Add edge
                self.union(parent, rank, x, y)  # Merge sets

        print("Edge \tWeight")  # Print edge with their weights
        for u, v, weight in result:
            print(f"{self.vertex_data[u]}-{self.vertex_data[v]} \t{weight}")

# Given tree
g = Graph(7)  # Create instance of class
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')
# Adds edges with existing vertices
g.add_edge(0, 1, 4)  # A-B,  4
g.add_edge(0, 6, 10)  # A-G, 10
g.add_edge(0, 2, 9)  # A-C,  9
g.add_edge(1, 2, 8)  # B-C,  8
g.add_edge(2, 3, 5)  # C-D,  5
g.add_edge(2, 4, 2)  # C-E,  2
g.add_edge(2, 6, 7)  # C-G,  7
g.add_edge(3, 4, 3)  # D-E,  3
g.add_edge(3, 5, 7)  # D-F,  7
g.add_edge(4, 6, 6)  # E-G,  6
g.add_edge(5, 6, 11)  # F-G, 11

print("Kruskal's Algorithm MST:")
g.kruskals_algorithm()
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
print("Kruskal's Algorithm MST:")
g2.kruskals_algorithm()
