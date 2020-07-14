from stacks_and_queues import __version__
from stacks_and_queues.stacks_and_queues import Stack, Queue
import pytest


def test_version():
    assert __version__ == "0.1.0"


def test_stack_top():
    stack1 = Stack()
    assert stack1.top == None


def test_stack_push():
    stack2 = Stack()
    stack2.push(0)
    assert stack2.top.val == 0


def test_stack_pop():
    stack3 = Stack()
    stack3.push(0)
    assert stack3.pop() == 0
    assert stack3.top == None


def test_stack_pop_exception():
    stack4 = Stack()
    with pytest.raises(Exception) as excep:
        stack4.pop()
        assert "EmptyStack" in excep


def test_stack_peek():
    stack5 = Stack()
    stack5.push(5)
    assert stack5.peek() == 5
    assert stack5.top.val == 5


def test_stack_is_empty():
    stack6 = Stack()
    assert stack6.is_empty() == True
    stack6.push(5)
    assert stack6.is_empty() == False


# ---------------Queues-------------------------------------------------------


def test_queue_front():
    queue1 = Queue()
    assert queue1.front == None


def test_queue_enqueue():
    queue2 = Queue()
    queue2.enqueue(0)
    assert queue2.back.val == 0


def test_queue_dequeue():
    queue3 = Queue()
    queue3.enqueue(5)
    assert queue3.dequeue() == 5
    assert queue3.back == None


def test_queue_dequeue_exception():
    queue4 = Queue()
    with pytest.raises(Exception) as excep:
        queue4.dequeue()
        assert "EmptyQueue" in excep


def test_queue_peek():
    queue5 = Queue()
    queue5.enqueue(5)
    assert queue5.peek() == 5
    assert queue5.back.val == 5
    assert queue5.front.val == 5


def test_queue_peek_exception():
    queue6 = Queue()
    with pytest.raises(Exception) as excep:
        queue6.peek()
        assert "EmptyQueue" in excep


def test_queue_isEmpty():
    queue7 = Queue()
    assert queue7.is_empty() == True
    queue7.enqueue(5)
    assert queue7.is_empty() == False

def test_stack_str():
    stack9 = Stack()
    stack9.push(5)
    assert str(stack9) == "[5]"

def test_queue_str():
    queue9 = Queue()
    queue9.enqueue(5)
    assert str(queue9) == "[5]"

def test_queue_object():
    queue10 = Queue()
    obj = {"name":"Steven"}
    queue10.enqueue(obj)
    assert queue10.dequeue() == {'name': 'Steven'}

def test_enqueue_dequeue_multiple():
    queue11 = Queue()
    queue11.enqueue(1)
    queue11.enqueue(5)
    queue11.dequeue()
    assert queue11.dequeue() == 5