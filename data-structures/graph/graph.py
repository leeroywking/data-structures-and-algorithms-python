class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, value):
        vertex = Vertex(value)
        self.adjacency_list[vertex] = []
        return vertex

    def add_edge(self, start, end, weight= 1):
        if start not in self.adjacency_list:
            raise KeyError("Start Vertex not in graph")
        if end not in self.adjacency_list:
            raise KeyError("End Vertex not in the graph")

        edge = Edge(end, weight)
        adjacencies = self.adjacency_list[start]
        adjacencies.append(edge)

    def size(self):
        return len(self.adjacency_list)

    

class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex, weight = 1):
        self.vertex = vertex
        self.weight = weight
        