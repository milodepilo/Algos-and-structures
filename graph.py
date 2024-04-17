class Graph:
    def __init__(self):
        self.graph = {}  # Initializes an empty dictionary to store graph vertices and their edges.

    def add_edge(self, u, v):
        # Adds an edge between vertex u and vertex v. The graph is undirected.
        if u in self.graph.keys():
            self.graph[u].add(v)  # Adds v to the adjacency set of u.
        else:
            self.graph[u] = set([v])  # Creates a new set if u is not in the graph.

        if v in self.graph.keys():
            self.graph[v].add(u)  # Since the graph is undirected, add u to v's adjacency set.
        else:
            self.graph[v] = set([u])  # Creates a new set for v if v is not in the graph.

    def __repr__(self):
        # Provides a human-readable representation of the graph.
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result

    def depth_first_search(self, start_vertex):
        # Performs a depth-first search (DFS) starting from start_vertex.
        visited = []  # List to keep track of visited nodes.
        self.depth_first_search_r(visited, start_vertex)
        return visited

    def depth_first_search_r(self, visited, current_vertex):
        # Helper recursive function for DFS.
        visited.append(current_vertex)  # Marks the current vertex as visited.
        sorted_neibo = sorted(self.graph[current_vertex])  # Sorts neighbors for consistent traversal order.
        for neibo in sorted_neibo:
            if neibo not in visited:
                self.depth_first_search_r(visited, neibo)  # Recursively visits unvisited neighbors.

    def breadth_first_search(self, v):
        # Performs a breadth-first search (BFS) starting from vertex v.
        visited = []  # List to keep track of visited nodes.
        to_visit = [v]  # Queue to manage nodes to visit.
        while len(to_visit) > 0:
            current = to_visit.pop(0)  # Dequeues the first element for visiting.
            visited.append(current)  # Marks it as visited.
            sorted_neighbours = sorted(self.graph[current])  # Sorts neighbors for consistent traversal order.
            for nb in sorted_neighbours:
                if nb not in visited and nb not in to_visit:
                    to_visit.append(nb)  # Enqueues unvisited neighbors.
        return visited
