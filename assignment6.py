# CMPSC 462 Assignment 6
# Mariami Shinjiashvili
import sys
class Graph:
    def generate_edges(self, graph):
        edges = []
        for node in graph:
            for neighbour in graph[node]:
                edges.append((node, neighbour))
        return edges


    # Function to calculate isolated nodes of a given graph
    def find_isolated_nodes(self, graph):
        """ returns a list of isolated nodes. """
        isolated = []
        for node in graph:
            if not graph[node]:
                isolated += node
        return isolated
    #Function to find a path from a start vertex to an end vertex
    def find_path(self, graph, start_vertex, end_vertex, path=None):
        """ find a path from start_vertex to end_vertex in graph """
        if path == None:
            path = []
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(graph, vertex,end_vertex,path)
                if extended_path:
                    return extended_path
        return None
    # The algorithm uses an important technique called backtracking: it tries each possibility in turn until it finds a solution.


    # Function to find all the paths between a start vertex to an end vertex
    def find_all_paths(self, graph, start_vertex, end_vertex, path=[]):
        """ find all paths from start_vertex to
            end_vertex in graph """
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(graph, vertex,end_vertex,path)
                for p in extended_paths:
                    paths.append(p)
        return paths
    '''
    A graph is said to be connected if every pair of vertices in the graph is connected.
    The example graph on the right side is a connected graph.
    It possible to determine with a simple algorithm whether a graph is connected:
    Choose an arbitrary node x of the graph G as the starting point
    Determine the set A of all the nodes which can be reached from x.
    If A is equal to the set of nodes of G, the graph is connected; otherwise it is
    disconnected.
    '''


    # Function to check if a graph is a connected graph.
    def is_connected(self, graph, vertices_encountered=None,start_vertex=None):
        """ determines if the graph is connected """
        if vertices_encountered is None:
            vertices_encountered = set()
        vertices = list(graph.keys()) # "list" necessary in Python 3
        if not start_vertex:
            # choose a vertex from graph as a starting point
            start_vertex = vertices[0]
        vertices_encountered.add(start_vertex)
        if len(vertices_encountered) != len(vertices):
            for vertex in graph[start_vertex]:
                if vertex not in vertices_encountered:
                    if self.is_connected(graph, vertices_encountered, vertex):
                        return True
        else:
            return True
        return False
    '''
    references:
    https://www.python-course.eu/graphs_python.php
    https://www.python.org/doc/essays/graphs/
    '''


    def bfs(self, graph, node): # Define function
        visited = []  # Create list to tacl visited vertices
        queue = []  # Create list ti implement queue
        visited.append(node)  # Adds node to list
        queue.append(node)  # Adds node to list

        while queue:  # Creating loop to visit each node
            m = queue.pop(0)  # Removes first element in list
            for neighbour in graph[m]:  # For each value of key in graph
                if neighbour not in visited:  # If value is not in list
                    visited.append(neighbour)  # Add value to list
                    queue.append(neighbour)  # Add value to list
        return visited  # Return visited list as that list did not remove elements and simply kept track

    visited = []  # Initilize empty list
    def dfs(self, graph, node):  # Define function
        if node not in self.visited:  # If node not in previously created list
            self.visited.append(node)  # Add node to list
            for neighbour in graph[node]:  # For each value of key in graph
                self.dfs(graph, neighbour)  # Recall function for each value
        return self.visited  # Return list that continues all visted vertices

graph0 = { "a" : ['b','c'],
"b" : ['c', 'd'],
"c" : ['d'],
"d" : ['c'],
"e" : ['f'],
"f" : []
}
graph1 = { "a" : ["d","f"],
"b" : ["c"],
"c" : ["b", "c", "d", "e"],
"d" : ["a", "c"],
"e" : ["c"],
"f" : ["a"]
}
graph2 = { "a" : ["d","f"],
"b" : ["c","b"],
"c" : ["b", "c", "d", "e"],
"d" : ["a", "c"],
"e" : ["c"],
"f" : ["a"]
}

graph=Graph()
print(graph.generate_edges(graph1))
print(graph.find_isolated_nodes(graph1))
print(graph.find_path(graph1, 'a','e'))
print(graph.find_all_paths(graph1, 'a','e'))
print(graph.is_connected(graph1))
print("Visited nodes in bfs:", graph.bfs(graph1,"a"))
print("Visited nodes in dfs:", graph.dfs(graph1,"a"))
