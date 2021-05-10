class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes, data and the link to the next node in the list
    """

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data


class LinkedList:
    """
    Singly linked list
    """

    def __init__(self):
        self.head = None

    def search(self, key):
        """
        Search for 1st node containing data that matches the key
        Returns the node or None if not found

        Time: O(n)
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """
        Inserts new node at index position
        Insertion takes O(1)
        Finding node takes O(n)
        Time: O(n)
        """
        if index == 0:
            self.add(data)
            return

        if index > 0:
            new = Node(data)
            position = index
            current = self.head

            while position > 1:
                # stop loop 1 before the index position
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
                return current
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
                return current
            else:
                previous = current
                current = current.next_node

    def is_empty(self):
        return self.head is None

    def size(self):
        """
        Returns number of nodes in list
        Takes O(n) time
        """
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.next_node
        return count

    def add(self, data):
        """
        Adds new node to head of linked list containing data
        Time: O(n)
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1

            return current

    def __repr__(self):
        """
        Returns a string representation of the list.
        Takes O(n) time
        """

        nodes = []
        current = self.head

        while current  != None:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node

        return " -> ".join(nodes)


'''
class Node:
    """
    An object for storing a single node in a linked list

    Attributes:
        data: Data stored in node
        next_node: Reference to next node in linked list
    """

    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return "<Node data: %s>" % self.data

class SinglyLinkedList:
    """
    Linear data structure that stores values in nodes. The list maintains a reference to the first node, also called head. Each node points to the next node in the list

    Attributes:
        head: The head node of the list
    """

    def __init__(self):
        self.head = None
        # Maintaining a count attribute allows for len() to be implemented in
        # constant time
        self.__count = 0

    def is_empty(self):
        """
        Determines if the linked list is empty
        Takes O(1) time
        """

        return self.head is None

    def __len__(self):
        """
        Returns the length of the linked list
        Takesn O(1) time
        """

        return self.__count
'''
