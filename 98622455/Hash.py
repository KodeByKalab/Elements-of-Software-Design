#  File: Hash.py

#  Description: Implement a cache with hash table and linked list


import sys

# A class to represent a LinkedList node
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

# A class to represent a LinkedList
class LinkedList:
    def __init__(self):
        self.first = None

    # we want to always add this item at the front
    def insert_first(self, data):
        node = Node(data)
        node.next = self.first
        self.first = node

# A hash table mimicking a cache
class HashingCache:
    def __init__(self, size):
        self.con = [None for i in range(size)]

    # Return the size of the hash table
    def size(self):
        return len(self.con)

    # Return the hash index given a number to be hashed
    # DO NOT MODIFY THIS HASH FUNCTION
    def hash_idx(self, num):
        return num % len(self.con)

    # Input: a number to be hashed. Place this item in the table 
    # at the desired place
    # Output: n/a
    def hash(self, num):
        idx = self.hash_idx(num)
        ##print("idx")
        ##print(idx)
        if(self.con[idx] == None):
            self.con[idx] = LinkedList()
        self.con[idx].insert_first(num)

        return

    # Input: a number to be found in the cache. If the number is
    # in cache, bring it to the front of the linked list at its 
    # index.
    # Output: the node found, or None if it is not in cache
    def find(self, num):

        idx = self.hash_idx(num)
        if (self.con[idx] == None):
            return None
            
        if(self.con[idx].first != None):
            curr = self.con[idx].first
            if(self.con[idx].first.data == num):
                return self.con[idx].first
            while (curr.next != None):
                if(curr.next.data == num):
                    temp = curr.next
                    curr.next = curr.next.next
                    self.con[idx].insert_first(num)
                    return temp
        return None

    # Helper function to print out the hash table
    # DO NOT MODIFY THIS FUNCTION
    def __str__(self):
        res = '['

        for i in range(self.size() - 1):
            if (self.con[i] == None):
                res += 'None, '
            else:
                curr = self.con[i].first
                while (curr != None and curr.next != None):
                    res += str(curr.data) + '->'
                    curr = curr.next

                # last item
                if (curr != None):
                    res += str(curr.data) + ', '
        # print last item
        if (self.con[-1] == None):
            res += 'None'
        else:
            curr = self.con[-1].first
            while (curr != None and curr.next != None):
                res += str(curr.data) + '->'
                curr = curr.next

            # last item
            if (curr != None):
                res += str(curr.data)
        res += ']'
        return res

def main():

    size = int(sys.stdin.readline())


    n = int(sys.stdin.readline())
    cache = HashingCache(size)

    for i in range(n):
        cache.hash(int(sys.stdin.readline()))
    print(cache)

    m = int(sys.stdin.readline())
    for i in range(m):
        cache.find(int(sys.stdin.readline()))

    print(cache)

if __name__ == "__main__":
    main()
