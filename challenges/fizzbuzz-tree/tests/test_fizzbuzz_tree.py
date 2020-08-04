from fizzbuzz_tree import __version__
from fizzbuzz_tree.karrytree import KarryNode, Karrytree


def test_version():
    assert __version__ == "0.1.0"


def test_wiring():
    assert KarryNode, Karrytree


def test_fizzbuzz():
    tree = Karrytree()
    nodes = []
    for i in range(2, 100):
        nodes.append(KarryNode(i))
    tree.root = KarryNode(1)
    for node in nodes:
        tree.root.children.append(node)
    tree.fizzbuzz()
    assert tree.show_all_vals() == ["FizzBuzz" if i%15 ==0  else "Fizz" if i%3==0 else "Buzz" if i%5==0 else i for i in range(1,100)]
