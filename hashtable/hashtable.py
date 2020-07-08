class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.entry_count = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return (self.entry_count / self.capacity)

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # hash = offset_basis
        # for each octet_of_data to be hashed
        #  hash = hash xor octet_of_data
        #  hash = hash * FNV_prime
        # return hash

        hash = 14695981039346656037
        for x in key:
            hash = hash ^ ord(x)
            hash = (hash * 1099511628211)
        return hash

    def djb2(self, key):
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.fnv1(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here

        self.int_put(key, value, self.storage)
        load_factor = self.get_load_factor()

        self.entry_count += 1
        if load_factor > 0.7:
            self.resize(self.capacity * 2)

    def int_put(self, key, value, table):
        index = self.hash_index(key)
        node = table[index]
        new_node = HashTableEntry(key, value)

        # if the key of the index matches that of the new_node
        # check if an entry already exists
        if node == None:
            # if not, insert (and increment entry count)
            node = new_node

        # otherwise, grab the current nodes value and move it over
        else:
            prev_node = node
            new_node.next = prev_node
        # then insert new_node into the "head"
            node = new_node

        # resize if the current table is too small

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        node = self.storage[index]
        # while the node exists and the keys don't match, go through the LL
        if node:
            prev = None
            while node:
                if node.key == key:
                    if prev:
                        prev.next = node.next

            print(f'There is nothing here!')
        else:
            node = None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        i = self.hash_index(key)
        node = self.storage[i]
        if node is None:
            return None
        if node.key == key:
            return node.value
        while node.next:
            node = node.next
            if node.key == key:
                return node.value
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        new_table = [None] * new_capacity
        self.capacity = new_capacity

        for i in self.storage:
            if i is None:
                continue
            # assign index to a new variable for readability
            node = i
            while node.next:
                node = node.next
                self.put(node.key, node.value)
            self.put(i.key, i.value)
        self.storage = new_table

    def pp(self):
        """
        outputs the table in the following form:
          {
              0 => [{key: key1, value: value1}]
              1 => []
              ...
              n => [{key: keyn1, value: valuen1}, {key: keyn2, value: valuen2}
          }
        """
        for idx, node in enumerate(self.storage):
            if node is None:
                print(f"{idx} => []")
                continue
            print(f"{idx} => [", end="")
            # index = i
            print(f"{{key: {node.key}, value: {node.value}}}", end="")
            while node.next:
                node = node.next
                print(f"{{key: {node.key}, value: {node.value}}}", end="")
            print(f"]")


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    ht.pp()

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
