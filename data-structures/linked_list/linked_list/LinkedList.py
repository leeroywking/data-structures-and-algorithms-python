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

        newNode = Node(val, self.head)
        self.head = newNode
        self.length += 1

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
        current = self.head
        last = None
        if self.head.val == val:
            newNode = Node(newVal, self.head)
            self.head = newNode
            return

        while current != None:
            if current.val == val:
                newNode = Node(newVal, current)
                last.next_ = newNode
                return
            else:
                last = current
                current = current.next_
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
        if kth_from_start > self.length:
            raise KeyError
        else:
            current = self.head
            for i in range(kth_from_start):
                current = current.next_
            return current.val

    def length_it(self):
        counter = -0
        current = self.head
        while current:
            current = current.next_
            counter += 1
        return counter

    @staticmethod
    def merge_lls(ll1: dict, ll2: dict) -> dict:
        """Static method accepts two linked lists and zips the nodes together before returning the zipped list WARNING: this is a mutating function to achieve O(1) space complexity

        Args:
            ll1 (LinkedList): [first linked list]
            ll2 (LinkedList): [second linked list]

        Returns:
            LinkedList: [long linked list]
        """
        current1 = ll1.head
        current2 = ll2.head
        print(current1)
        print(current2)
        if current1 == None and current2 == None:
            return ll1
        if current1 == None:
            return ll2
        if current2 == None:
            return ll1

        while current1.next_ and current2.next_:
            holder = current1.next_
            holder2 = current2.next_
            current1.next_ = current2
            current2.next_ = holder
            current1 = holder
            current2 = holder2

        if not current2.next_:
            holder = current1.next_
            current1.next_ = current2
            current2.next_ = holder
        else:
            current1.next_ = current2
        ll1.length = ll1.length_it()
        return ll1
