from linked_list import LinkedList


class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self._buckets = [None] * size

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

    def update(self, key, new_value):
        hashed_key = self._hash(key)
        bucket = self._buckets[hashed_key]
        current = bucket.head
        while current:
            if current.val[0] == key:
                current.val[1] = new_value
            current = current.next_
        return None

    def get(self, key):
        try:
            hashed_key = self._hash(key)
            bucket = self._buckets[hashed_key]
            current = bucket.head
            while current:
                if current.val[0] == key:
                    return current.val[1]
                current = current.next_
            return None
        except:
            return None

    def contains(self, key):
        if self.get(key):
            return True
        else:
            return False
