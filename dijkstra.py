#credit: https://www.w3schools.com/dsa/dsa_algo_graphs_dijkstra.php#:~:text=Dijkstra's%20algorithm%20finds%20the%20shortest,all%20the%20unvisited%20neighboring%20vertices.

class Graph:
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

    def dijkstra(self, start_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        distances = [float('inf')] * self.size  # Create list to store vertices
        distances[start_vertex] = 0  # Distance of start vertex is zero
        visited = [False] * self.size  # Create list to track visted vertices

        for _ in range(self.size):  # Iterates over vertices
            min_distance = float('inf')  # Initialize min distance as infinity
            u = None  # Initialize to none
            for i in range(self.size):  # Iterates over vertices
                if not visited[i] and distances[i] < min_distance:  # Checks if vertx has not been visted and distance is less than min distance
                    min_distance = distances[i]  # Update min distance
                    u = i

            if u is None:  # If no un-visited vertices are left
                break  # break

            visited[u] = True  # Mark vertex as visited

            for v in range(self.size):  # Iterate over adjacent vertices
                if self.adj_matrix[u][v] != 0 and not visited[v]:  # If edge between current and adjacent vertex
                    alt = distances[u] + self.adj_matrix[u][v]  # New distance
                    if alt < distances[v]:  # If new distance is shorter than previous distance
                        distances[v] = alt  # Update distance

        return distances  # Return list


# Given tree
g = Graph(7) # Create instance of class with 7 vertices
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')
# Adds edges with existing vertices
g.add_edge(3, 0, 4)  # D - A, weight 5
g.add_edge(3, 4, 2)  # D - E, weight 2
g.add_edge(0, 2, 3)  # A - C, weight 3
g.add_edge(0, 4, 4)  # A - E, weight 4
g.add_edge(4, 2, 4)  # E - C, weight 4
g.add_edge(4, 6, 5)  # E - G, weight 5
g.add_edge(2, 5, 5)  # C - F, weight 5
g.add_edge(2, 1, 2)  # C - B, weight 2
g.add_edge(1, 5, 2)  # B - F, weight 2
g.add_edge(6, 5, 5)  # G - F, weight 5

# Dijkstra's algorithm from D to all vertices
print("\nDijkstra's Algorithm starting from vertex D:")
distances = g.dijkstra('D')
for i, d in enumerate(distances):
    print(f"Distance from D to {g.vertex_data[i]}: {d}")

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
# Dijkstra's algorithm from Z to all vertices
print("\nDijkstra's Algorithm starting from vertex Z:")
distances = g2.dijkstra('Z')
for i, d in enumerate(distances):
    print(f"Distance from Z to {g2.vertex_data[i]}: {d}")
