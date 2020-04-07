# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.key}: {self.value}"


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        
        index = self._hash_mod(key)

        # If the list is None, add key and value
        
        if self.storage[index] is None:
            self.storage[index] = LinkedPair(key, value)

        item = self.storage[index]

        # While a node exists, check if the node's key matches key then store value
        # If not, go to the next node and store key and value when next is no longer true
        
        while item:
            if item.key == key:
                item.value = value
                break
            elif item.next:
                item = item.next
            else:
                item.next = LinkedPair(key, value)
                break

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''

        # While loop checks if key in storage matches unwanted key.
        # If the key matches, change node to None and break.
        # If the key is not found, print error message.

        index = self._hash_mod(key)

        if self.storage[index] is not None:
            item = self.storage[index]

            while True:
                if item.next:
                    item = item.next
                else:
                    self.storage[index] = None
                    break
        else:
            print("Key is not found")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''

        index = self._hash_mod(key)
        item = self.storage[index]

        # If linked list is no nodes, return None

        if item is None:
            return None

        # While the key for the node is true, loop
        # If the key is found, return the node's value
        # Else, return None

        while item.key:
            if item.key == key:
                return item.value
            elif item.next is not None:
                item = item.next
            else:
                return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''

        # Double capacity

        storage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity

        # Loops through self.storage then uses the insert function to
        # copy elements into new data structure

        for item in storage:
            if item:
                current = item

                while True:
                    self.insert(current.key, current.value)

                    if current.next:
                        current = current.next
                    else:
                        break


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
