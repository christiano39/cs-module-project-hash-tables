class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"HashEntry({repr(self.key)},{repr(self.value)})"


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        if capacity < MIN_CAPACITY:
            capacity = MIN_CAPACITY
        
        self.storage = [None] * capacity
        self.capacity = capacity
        self.count_of_items = 0

    def print_ht(self):
        for i in range(len(self.storage)):
            if self.storage[i] is None:
                print('None')
            else:
                string = ""
                cur = self.storage[i]
                while cur is not None:
                    string += f"({cur.key}, {cur.value}) "
                    if cur.next is not None:
                        string += "-> "
                    cur = cur.next
                print(string)



    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.storage)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        num_slots = self.get_num_slots()
        return self.count_of_items / num_slots


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for c in key:
            hash = ((hash << 5) + hash) + ord(c) & 0xFFFFFFFF
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)

        if self.storage[index] is None:
            self.storage[index] = HashTableEntry(key, value)
        else: 
            current = self.storage[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next

            new_entry = HashTableEntry(key, value)
            new_entry.next = self.storage[index]
            self.storage[index] = new_entry
        self.count_of_items += 1

        lf = self.get_load_factor()
        if lf > 0.7:
                num_slots = self.get_num_slots()
                self.resize(num_slots * 2)





    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)

        if self.storage[index] == None:
            print('Key does not exist')
            return None

        if self.storage[index].key == key:
            new_head = self.storage[index].next
            old_head = self.storage[index]
            self.storage[index].next = None
            self.storage[index] = new_head
            self.count_of_items -= 1
            return old_head.value

        else: 
            prev = self.storage[index]
            current = self.storage[index].next
            while current is not None:
                if current.key == key:
                    prev.next = current.next
                    current.next == None
                    self.count_of_items -= 1
                    return current.value
                prev = prev.next
                current = current.next
                
            print('Key does not exist')
            return None



    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        if not self.storage[index]:
            return None
        else:
            current = self.storage[index]
            while current:
                if current.key == key:
                    return current.value
                current = current.next
            return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        old_storage = self.storage
        self.storage = [None] * new_capacity
        self.capacity = new_capacity
        self.count_of_items = 0

        for node in old_storage:
            while node is not None:
                self.put(node.key, node.value)
                node = node.next




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