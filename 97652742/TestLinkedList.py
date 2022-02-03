#  File: TestLinkedList

#  Description: Our own implementation of a single linked list



class Link(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList(object):
    # create a linked list
    # you may add other attributes
    def __init__(self):
        self.first = None

    # get number of links
    def get_num_links(self):
        current = self.first
        c = 0
        while current is not None:
            c += 1
            current = current.next
        return c

    # add an item at the beginning of the list
    def insert_first(self, data):
        newLink = Link(data)
        newLink.next = self.first
        self.first = newLink

    # add an item at the end of a list
    def insert_last(self, data):
        newLink = Link(data)
        current = self.first
        while current is None:
            self.first = newLink
            return
        while current.next is not None:
            current = current.next
        current.next = newLink

    # add an item in an ordered list in ascending order
    # assume that the list is already sorted
    def insert_in_order(self, data):
        if self.first is None:
            self.insert_first(data)
            return
        elif data > self.first.data:
            newLink = Link(data)
            current = self.first
            precede = self.first
            while data > current.data:
                if current.next is None:
                    self.insert_last(data)
                    return
                else:
                    precede = current
                    current = current.next
            precede.next = newLink
            newLink.next = current

        else:
            self.insert_first(data)
            return

    # search in an unordered list, return None if not found
    def find_unordered(self, data):
        if self.first is None:
            return None
        current = self.first
        if current.data == data:
            return current
        while current.data != data:
            if current.next is None:
                return None
            current = current.next
        return current

    # Search in an ordered list, return None if not found
    def find_ordered(self, data):
        if self.first is None:
            return None
        current = self.first
        while current.data != data:
            if current.next is None:    # reached end of list
                return None
            elif current.data > data:    # reached end of order
                return None
            current = current.next
        return current

    # Delete and return the first occurrence of a Link containing data
    # from an unordered list or None if not found
    def delete_link(self, data):
        if self.first is None:
            return None
        if self.first.data == data:
            first = self.first
            self.first = self.first.next
            return first

        current = self.first.next
        prev = self.first
        while current.data != data:
            if current.next is None:
                return None
            prev = current
            current = current.next
        prev.next = current.next
        return current

    # String representation of data 10 items to a line, 2 spaces between data
    def __str__(self):
        current = self.first
        if current is None:
            return ""
        count = 0
        stringRep = ""
        if current.next is None:
            return str(current.data)

        while current is not None:
            stringRep += str(current.data)
            stringRep += "  "
            count += 1
            current = current.next
            if count == 10:
                count = 0
                stringRep += "\n"
        return stringRep

    # Copy the contents of a list and return new list
    # do not change the original list
    def copy_list(self):
        copy = LinkedList()
        current = self.first
        while current is not None:
            copy.insert_last(current.data)
            current = current.next
        return copy

    # Reverse the contents of a list and return new list
    # do not change the original list
    def reverse_list(self):
        reverse_list = LinkedList()
        current = self.first
        while current is not None:
            reverse_list.insert_first(current.data)
            current = current.next
        return reverse_list

    # Sort the contents of a list in ascending order and return new list
    # do not change the original list
    def sort_list(self):
        link_sorted = LinkedList()
        if self.is_empty():
            return link_sorted
        current = self.first
        for i in range(self.get_num_links()):
            link_sorted.insert_in_order(current.data)
            current = current.next
        return link_sorted

    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted(self):
        current = self.first
        if self.get_num_links() == 1:
            return True
        elif self.is_empty():
            return True

        for indx in range(self.get_num_links() - 1):
            if current.data > current.next.data:
                return False
            current = current.next
        return True

        # Return True if a list is empty or False otherwise

    def is_empty(self):
        if self.first is None:
            return True
        else:
            return False

    # Merge two sorted lists and return new list in ascending order
    # do not change the original lists
    def merge_list(self, other):
        merged = LinkedList()
        current1 = self.first
        current2 = other.first
        while current1 is not None:
            merged.insert_in_order(current1.data)
            current1 = current1.next

        while current2 is not None:
            merged.insert_in_order(current2.data)
            current2 = current2.next

        return merged

    # Test if two lists are equal, item by item and return True
    def is_equal(self, other):
        if self.first is None:
            if other.first is None:
                return True
            return False

        if self.get_num_links() != other.get_num_links():
            return False

        selfCurrent = self.first
        otherCurrent = other.first
        while selfCurrent.next is not None:
            if selfCurrent.data != otherCurrent.data:
                return False
            selfCurrent = selfCurrent.next
            otherCurrent = otherCurrent.next
        return True

    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    # do not change the original list
    def remove_duplicates(self):
        if self.first is None:
            return None
        cleaned = LinkedList()
        current = self.first
        while current is not None:
            if not cleaned.find_unordered(current.data):
                cleaned.insert_last(current.data)
            current = current.next
        return cleaned


def main():
    test = LinkedList()
    testa = LinkedList()

    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    print("Test for insert_first() and __str()__.")
    for idx in range(20):
        test.insert_first(idx)
    print(test)
    print()

    # Test method insert_last()
    print("Test method insert_last().")
    for i in range(10, 50):
        testa.insert_last(i)
    print(testa)
    print()

    # Test method insert_in_order()
    print("Test method insert_in_order().")
    testB = LinkedList()
    testB.insert_in_order(10)
    testB.insert_in_order(2)
    testB.insert_in_order(30)
    testB.insert_in_order(-3)
    testB.insert_in_order(100)
    print(testB)
    print()

    # Test method get_num_links()
    print("Testing get_num_links()")
    print("(List has 5 links)")
    print(testB.get_num_links())
    print()

    # Test method find_unordered()
    # Consider two cases - data is there, data is not there
    test1 = LinkedList()
    for i in range(20):
        if i % 2 == 0:
            test1.insert_first(i)
        else:
            test1.insert_last(i)
    print("Test method find_unordered()")
    print(test1.find_unordered(5))
    print(test1.find_unordered("100"))
    print()

    # Test method find_ordered()
    # Consider two cases - data is there, data is not there
    test2 = LinkedList()
    for i in range(10):
        test2.insert_last(i)
    print("Test method find_ordered()")
    print("Item in list:", test2.find_ordered(9))
    print("Item not in list:", test2.find_ordered(20))
    print()

    # Test method delete_link()
    # Consider two cases - data is there, data is not there
    print("Test method delete_link()")
    print("Original:")
    print(test2)
    print("Removed value:", test2.delete_link(3))
    print("After removal:")
    print(test2)
    print()

    # Test method copy_list()
    print("Test copy_list().")
    print(test2.copy_list())
    print()

    # Test method reverse_list()
    print("Testing reverse_list().")
    print("Original:")
    print(test)
    print("Reversed:")
    print(test.reverse_list())
    print()

    # Test method sort_list()
    print("Test sortList().")
    print(test.sort_list())
    print()

    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted
    print("Test is_sorted().")
    print(test.is_sorted())
    testa.insert_first(20)
    testa.insert_first(21)
    print(testa)
    print()

    # Test method is_empty()
    empty = LinkedList()
    print("Test is_empty()")
    print("Empty list:", empty.is_empty())
    print("Not empty:", test1.is_empty())
    print()

    # Test method merge_list()
    test3 = LinkedList()
    for i in range(10):
        if i % 2 == 1:
            test3.insert_last(i)
        else:
            test3.insert_first(i)
    test4 = LinkedList()
    for i in range(10, 20):
        if i % 2 == 1:
            test4.insert_first(i)
        else:
            test4.insert_first(i)
    print("Testing method merge_list()")
    print("List 1:")
    print(test3)
    print("List 2:")
    print(test4)
    print("Merged:")
    print(test3.merge_list(test4))
    print()

    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal
    test5 = LinkedList()
    test5.insert_first(1)
    test5.insert_first(2)
    test5.insert_first(3)
    test6 = LinkedList()
    test6.insert_first(1)
    test6.insert_first(2)
    test6.insert_first(3)
    test7 = LinkedList()
    test7.insert_last(1)
    test7.insert_last(2)
    test7.insert_last(3)
    print("Testing method is_equal()")
    print("Is true:", test5.is_equal(test6))
    print("Is false:", test5.is_equal(test7))
    print()

    # Test remove_duplicates()
    test8 = LinkedList()
    test8.insert_first(1)
    for i in range(3):
        test8.insert_last(2)
    for i in range(2):
        test8.insert_last(3)
    test8.insert_last(4)
    print("Testing method remove_duplicates()")
    print("Original:")
    print(test8)
    print("Cleaned:")
    print(test8.remove_duplicates())


if __name__ == "__main__":
    main()
