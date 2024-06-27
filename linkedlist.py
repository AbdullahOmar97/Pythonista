class Node:
    """
    Node class for a singly linked list.

    Attributes:
    - data: Data stored in the node.
    - next: Reference to the next node in the linked list.
    """

    def __init__(self, data=None):
        """
        Initialize a node with data.

        Args:
        - data: Data to be stored in the node.
        """
        self.data = data
        self.next = None

class LinkedList:
    """
    Singly linked list implementation.

    Methods:
    - append(data): Append a new node with data at the end of the list.
    - __iter__(): Iterator to iterate over nodes in the list.
    - __str__(): String representation of the linked list.
    - __len__(): Returns the number of nodes in the linked list.
    - __getitem__(index): Access node data at a specific index.

    Attributes:
    - head: Reference to the first node in the list.
    """

    def __init__(self):
        """
        Initialize an empty linked list with head set to None.
        """
        self.head = None

    def append(self, data):
        """
        Append a new node with the given data at the end of the linked list.

        Args:
        - data: Data to be stored in the new node.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def __iter__(self):
        """
        Iterator to iterate over nodes in the linked list.
        Yields:
        - Data stored in each node.
        """
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __str__(self):
        """
        String representation of the linked list.

        Returns:
        - String representation of the linked list, showing its elements in order.
        """
        return ' -> '.join(str(item) for item in self)

    def __len__(self):
        """
        Returns the number of nodes in the linked list.

        Returns:
        - Number of nodes in the linked list.
        """
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __getitem__(self, index):
        """
        Access node data at a specific index in the linked list.

        Args:
        - index: Index of the node to access.

        Returns:
        - Data stored in the node at the given index.

        Raises:
        - IndexError if the index is out of range.
        """
        if index < 0:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
        if current is None:
            raise IndexError("Index out of range")
        return current.data
