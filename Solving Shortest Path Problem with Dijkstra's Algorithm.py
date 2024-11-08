import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = {}

    def add_edge(self, source, destination, weight):
        if source in self.vertices and destination in self.vertices:
            self.vertices[source][destination] = weight
            self.vertices[destination][source] = weight  # For undirected graph

    def get_neighbors(self, vertex):
        if vertex in self.vertices:
            return self.vertices[vertex]
        else:
            return {}

    def dijktra(self, starting_node):
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[starting_node] = 0
        queue = [(0, starting_node)]

        while queue:
            value, vertex = heapq.heappop(queue)
            if value > distances[vertex]:
                continue
            for neighbor, n_value in self.vertices[vertex].items():
                distance = n_value + value
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))

        return distances

graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_edge('A', 'B', 5)
graph.add_edge('B', 'C', 6)
graph.add_edge('A', 'C', 10)

print(graph.dijktra('A'))

"""
Dijksta's algorithm works in O((V + E) log V) time. 
This is due to the fact that the algorithm scales due to the amount of both nodes and edges with connections
to each neighbor needing to be tested for shorter distances.

The space complexity for this particular algorithm is O(V^2). This is because for each vertex, we are storing
the data for the distance to each other vertex.
"""
