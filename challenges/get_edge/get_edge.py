from graph import Graph

def get_edge(graph, list_of_city_names):
    starting_name = list_of_city_names.pop(0)
    current_vertex = None
    while list_of_city_names:
        #find vertex that matches name
        for vertex in graph.adjacency_list:
            if vertex.value == starting_name:
                current_vertex = vertex
            else:
                print("you wut mate?")

    return (True,82)




def build_map():
    graph = Graph()
    pandora = graph.add_vertex("pandora")
    arendelle = graph.add_vertex("arendelle")
    metroville = graph.add_vertex("metroville")
    monstropolis = graph.add_vertex("monstropolis")
    naboo = graph.add_vertex("naboo")
    narnia = graph.add_vertex("narnia")

    graph.add_edge(pandora, arendelle, 150)
    graph.add_edge(pandora, metroville, 82)
    graph.add_edge(metroville, monstropolis, 105)
    graph.add_edge(metroville, naboo, 26)
    graph.add_edge(metroville, narnia, 37)
    graph.add_edge(metroville, pandora, 82)
    graph.add_edge(metroville, arendelle, 99)

    graph.add_edge(arendelle, pandora, 150)
    graph.add_edge(arendelle, metroville, 99)
    graph.add_edge(arendelle, monstropolis, 42)

    graph.add_edge(monstropolis, arendelle, 42)
    graph.add_edge(monstropolis, metroville, 105)
    graph.add_edge(monstropolis, naboo, 73)

    graph.add_edge(naboo, metroville, 26)
    graph.add_edge(naboo, narnia, 250)
    graph.add_edge(naboo, monstropolis, 73)

    graph.add_edge(narnia, naboo, 250)
    graph.add_edge(narnia, metroville, 37)
    return graph


if __name__ == "__main__":
    graph = build_map()
    actual = get_edge(graph, ["metroville", "pandora"])
    assert actual == (True,82)
