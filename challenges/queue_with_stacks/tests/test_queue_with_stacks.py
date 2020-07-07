from queue_with_stacks import __version__
from queue_with_stacks.queue_with_stacks import PsuedoQueue


def test_version():
    assert __version__ == '0.1.0'

def test_wiring():
    assert PsuedoQueue
    assert PsuedoQueue()

def test_enqueue_1():
    pq = PsuedoQueue()
    pq.enqueue(5)
    assert pq.stack1.peek() == 5

def test_enqueue_multiple():
    pq2 = PsuedoQueue()
    pq2.enqueue(5)
    pq2.enqueue(8)
    assert pq2.stack1.peek() == 5

def test_dequeue_single():
    pq3 = PsuedoQueue()
    pq3.enqueue(5)
    assert pq3.dequeue() == 5

def test_dequeue_multiple():
    pq4 = PsuedoQueue()
    pq4.enqueue(1)
    pq4.enqueue(2)
    pq4.enqueue(3)
    assert pq4.dequeue() == 1
    assert pq4.dequeue() == 2
    assert pq4.dequeue() == 3
    