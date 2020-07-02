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
