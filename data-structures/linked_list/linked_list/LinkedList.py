from linked_list.Node import Node


class LinkedList:
    """
    Instatniates a Linked LIst which expises the following methods, insert, includes
    """

    def __init__(self):
        self.head = None

    def __repr__(self):
        """
        repr function
        """
        output = []
        current = self.head
        while current != None:
            output.append(current.val)
            current = current.next_
        return str(output)

    def __str__(self):
        """
        str function
        """
        output = ""
        current = self.head
        while current != None:
            output += "{ "
            output += str(current.val)
            output += " } -> "
            current = current.next_
        output += "NULL"
        return output

    def insert(self, val: int):
        """
        insert takes an integetr
        """
        if self.head == None:
            self.head = Node(val)
        else:
            newNode = Node(val, self.head)
            self.head = newNode

    def includes(self, val: int):
        """
        returns a boolean if the passed in int exists in linked list or not
        """
        current = self.head
        while current != None:
            if current.val == val:
                return True
            current = current.next_
        return False
