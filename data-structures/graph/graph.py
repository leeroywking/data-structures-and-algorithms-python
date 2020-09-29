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

    def breadth_first(self, starting_node):
        visited_vertex = []
        vertex_to_visit = []
        def walk(curr_vertex):
            nonlocal visited_vertex
            nonlocal vertex_to_visit
            visited_vertex.append(curr_vertex)
            for edge in self.adjacency_list[curr_vertex]:
                print("in the loop")
                if (edge.vertex not in visited_vertex) and (edge.vertex not in vertex_to_visit):
                    print("in the if",  visited_vertex)
                    vertex_to_visit.append(edge.vertex)
                else:
                    print(" in the else")
                    pass
  
        vertex_to_visit.append(starting_node)

        while len(vertex_to_visit):
            first = vertex_to_visit.pop(0)
            walk(first)

        return visited_vertex
        
    

class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex, weight = 1):
        self.vertex = vertex
        self.weight = weight
        

if __name__ == "__main__":
    graph = Graph()
    milk = graph.add_vertex("milk")
    eggs = graph.add_vertex("eggs")
    flour = graph.add_vertex("flour")
    graph.add_edge(milk, flour)
    graph.add_edge(milk, eggs)
    graph.add_edge(eggs, flour)
    graph.add_edge(eggs, milk)
    graph.add_edge(flour, milk)
    graph.add_edge(flour, eggs)
    actual = graph.breadth_first(milk)
    assert actual == [milk, eggs, flour]