from linked_list.Node import Node


class LinkedList:
    """
    Instatniates a Linked LIst which expises the following methods, insert, includes
    """

    def __init__(self):
        self.head = None
        self.length = 0

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
        self.length +=1

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

    def append(self, val: int):
        """
        adds a new node to the linked list at the end of the list
        """
        if self.head == None:
            self.head = Node(val)
        else:
            current = self.head
            while current.next_ != None:
                current = current.next_
            current.next_ = Node(val)
        self.length += 1

    def insert_before(self, val: int, newVal: int):
        """
        adds a new node to the ll before the 'val' node
        """
        try:
            current = self.head
            while current.next_ != None:
                if current.next_.val == val:
                    break
                current = current.next_
            newNode = Node(newVal, current.next_)
            current.next_ = newNode
            self.length += 1
            return "Success"
        except: 
            raise KeyError


    def insert_after(self, val: int, newVal: int):
        """
        adds a new node to the ll after the 'val' node
        """
        current = self.head
        while current != None:
            if current.val == val:
                newNode = Node(newVal, current.next_)
                current.next_ = newNode
                self.length += 1
                return "Success"
            current = current.next_
        raise KeyError

    def kth_from_end(self, k):
        kth_from_start = self.length - k
        if kth_from_start  > self.length:
            raise KeyError
        else:
            current = self.head
            for i in range(kth_from_start):
                current = current.next_
            return current.val
