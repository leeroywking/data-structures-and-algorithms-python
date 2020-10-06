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


def test_breadth_first_no_loop():
    graph = Graph()
    spam = graph.add_vertex("spam")
    egg = graph.add_vertex("eggs")
    graph.add_edge(spam, egg, 5)
    actual = graph.breadth_first(spam)
    assert actual == [spam,egg]

def test_breadth_first_with_loop():
    graph = Graph()
    milk = graph.add_vertex("milk")
    sugar = graph.add_vertex("sugar")
    eggs = graph.add_vertex("eggs")
    flour = graph.add_vertex("flour")
    graph.add_edge(milk, flour)
    graph.add_edge(milk, eggs)
    graph.add_edge(eggs, flour)
    graph.add_edge(eggs, milk)
    graph.add_edge(flour, milk)
    graph.add_edge(flour, eggs)
    graph.add_edge(flour, sugar)
    actual = graph.breadth_first(milk)
    assert actual == [milk,flour, eggs, sugar]

def test_depth_first_pre_order():
    graph = Graph()
    milk = graph.add_vertex("milk")
    sugar = graph.add_vertex("sugar")
    eggs = graph.add_vertex("eggs")
    flour = graph.add_vertex("flour")
    graph.add_edge(milk, flour)
    graph.add_edge(milk, eggs)
    graph.add_edge(eggs, flour)
    graph.add_edge(eggs, milk)
    graph.add_edge(flour, milk)
    graph.add_edge(flour, eggs)
    graph.add_edge(flour, sugar)
    actual = graph.depth_first_pre_order(flour)
    assert actual == [flour, milk, eggs, sugar]
