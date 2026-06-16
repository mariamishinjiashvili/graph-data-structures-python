# Graph Data Structure Assignment (Assignment 6)

## Overview
This project implements a basic Graph Data Structure using Python dictionaries and includes several fundamental graph algorithms such as edge generation, path finding, connectivity checking, traversal methods (BFS and DFS), and minimum spanning tree algorithms (Kruskal and Prim), along with Dijkstra's shortest path algorithm.

The goal of this assignment is to understand how graphs are represented and how core graph algorithms operate.

## Graph Representation
The graph is represented using a dictionary (adjacency list):

```python
graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['d'],
    'd': []
}
```

- Keys represent vertices
- Values represent adjacent vertices (edges)

## Part 1: Graph Functions

### 1. Generate Edges
Returns a list of all edges in the graph as tuples.

**Logic:**
- Iterate through each node
- Iterate through its neighbors
- Store each connection as a tuple `(node, neighbor)`

**Output Example:**
```python
[('a', 'b'), ('a', 'c'), ('b', 'd'), ('c', 'd')]
```

### 2. Find Isolated Nodes
Finds nodes with no connections (no neighbors).

**Logic:**
- Loop through each node
- If adjacency list is empty → node is isolated

**Output Example:**
```python
['d']
```

### 3. Find Path (DFS with Backtracking)
Finds a single path from a start vertex to an end vertex.

**Logic:**
- Uses recursion (backtracking)
- Avoids revisiting nodes already in current path
- Returns first valid path found

### 4. Find All Paths
Finds all possible paths between two vertices.

**Logic:**
- Recursive DFS exploration
- Stores all valid paths in a list
- Avoids cycles by tracking visited nodes in current path

**Output Example:**
```python
[['a', 'b', 'd'], ['a', 'c', 'd']]
```

### 5. Check if Graph is Connected
Determines whether all nodes are reachable from a starting node.

**Logic:**
- Uses DFS traversal
- Tracks visited nodes in a set
- Compares visited nodes with total graph nodes

**Output:**
- `True` → connected graph
- `False` → disconnected graph

### 6. Breadth-First Search (BFS)
Traverses the graph level by level using a queue.

**Logic:**
- Visit neighbors before deeper nodes
- Uses FIFO structure

### 7. Depth-First Search (DFS)
Traverses the graph using recursion or stack.

**Logic:**
- Explore as deep as possible before backtracking

## Part 2: Graph Algorithms

### 8. Kruskal's Algorithm
Finds a Minimum Spanning Tree (MST) by selecting edges with the smallest weights while avoiding cycles.

**Steps:**
1. Sort edges by weight
2. Add smallest edge
3. Skip edges that form cycles
4. Repeat until all vertices are connected

**Time Complexity:** `O(E log E)` (E = number of edges)

### 9. Prim's Algorithm
Builds an MST by starting from a node and expanding outward using the smallest edge.

**Steps:**
1. Start from any vertex
2. Pick smallest edge connected to the tree
3. Add new vertex
4. Repeat until all vertices included

**Time Complexity:** `O(V^2)` (V = number of vertices)

### 10. Dijkstra's Algorithm
Finds the shortest path from a source node to all other nodes in a weighted graph (non-negative weights only).

**Steps:**
1. Assign initial distances (0 for source, ∞ for others)
2. Visit unvisited node with smallest distance
3. Update neighbor distances (relaxation)
4. Repeat until all nodes are processed

**Time Complexity:** `O(V^2)` or `O(E log V)` (with priority queue)

## Key Concepts Learned
- Graph representation using adjacency lists
- DFS and BFS traversal techniques
- Recursive backtracking for path finding
- Cycle detection and connectivity
- Minimum Spanning Tree algorithms (Kruskal & Prim)
- Shortest path algorithm (Dijkstra)
