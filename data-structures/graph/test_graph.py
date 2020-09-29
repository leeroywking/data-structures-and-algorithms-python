import pytest
from graph import Graph, Vertex


def test_add_graph():
    graph = Graph()
    assert graph


def test_add_vertex():
    graph = Graph()
    vertex = graph.add_vertex("spam")
    assert vertex.value == "spam"


def test_add_edge():
    graph = Graph()
    spam = graph.add_vertex("spam")
    egg = graph.add_vertex("eggs")
    graph.add_edge(spam, egg)
    assert True


def test_add_edge_leo_test():
    graph = Graph()
    start = graph.add_vertex("start_v")
    end = graph.add_vertex("end_v")
    graph.add_edge(start, end)
    assert graph.adjacency_list[start][0].vertex == end


def test_add_edge_test_size_pass():
    graph = Graph()
    spam = graph.add_vertex("spam")
    egg = graph.add_vertex("eggs")
    graph.add_edge(spam, egg, 5)
    assert len(graph.adjacency_list) == 2
    assert graph.adjacency_list[spam][0].weight == 5


def test_add_edge_test_size_fall():
    graph = Graph()
    spam = graph.add_vertex("spam")
    egg = graph.add_vertex("eggs")
    graph.add_edge(spam, egg)
    assert len(graph.adjacency_list) != 3
