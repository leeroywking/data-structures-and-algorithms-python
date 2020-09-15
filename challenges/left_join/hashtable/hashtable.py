from hashtable.linked_list import LinkedList


class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self._buckets = [None] * size
        self.current = 0

    def _hash(self, key):
        # Get the ascii value of each char in the key
        hash_total = 0

        for c in key:
            # sum char's
            hash_total += ord(c)

        # multiple by some prime number for this example
        # modulo by size
        return (hash_total * 199) % self.size

    def add(self, key, value):
        hashed_key = self._hash(key)

        if not self._buckets[hashed_key]:
            self._buckets[hashed_key] = LinkedList()

        self._buckets[hashed_key].append([key, value])

    def get(self, key):
        hashed_key = self._hash(key)

        bucket = self._buckets[hashed_key]

        try:
            current = bucket.head
            while current:
                if current.val[0] == key:
                    return current.val[1]
        except AttributeError:
            pass
        return None

    def contains(self, key):
        if self.get(key):
            return True
        else: 
            return False

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.size <= self.current:
            self.current = 0
            raise StopIteration
        else:
            output = self._buckets[self.current]
            self.current += 1
            return output
