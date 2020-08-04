class Karrytree:
    def __init__(self):
        self.root = None

    def show_all_vals(self):
        vals = []

        def walk(node):
            vals.append(node.value)
            if node.children:
                for child in node.children:
                    walk(child)

        walk(self.root)
        print(vals)
        return vals

    def fizzbuzz(self):
        def walk(node):
            if node.children:
                for child in node.children:
                    if child.value % 15 == 0:
                        child.value = "FizzBuzz"
                    elif child.value % 5 == 0:
                        child.value = "Buzz"
                    elif child.value % 3 == 0:
                        child.value = "Fizz"
        walk(self.root)


class KarryNode:
    def __init__(self, value):
        self.children = []
        self.value = value

