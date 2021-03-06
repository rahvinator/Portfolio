# linked_lists.py
"""Volume 2: Linked Lists.
<Name>
<Class>
<Date>
"""


# Problem 1
class Node:
    """A basic node class for storing data."""
    def __init__(self, data):
        """Store the data in the value attribute.
                
        Raises:
            TypeError: if data is not of type int, float, or str.
        """
        if type(data) is not int and type(data) is not float and type(data) is not str:
            raise TypeError("Data type is not int, float or str")

        self.value = data


class LinkedListNode(Node):
    """A node class for doubly linked lists. Inherits from the Node class.
    Contains references to the next and previous nodes in the linked list.
    """
    def __init__(self, data):
        """Store the data in the value attribute and initialize
        attributes for the next and previous nodes in the list.
        """
        Node.__init__(self, data)       # Use inheritance to set self.value.
        self.next = None                # Reference to the next node.
        self.prev = None                # Reference to the previous node.


# Problems 2-5
class LinkedList:
    """Doubly linked list data structure class.

    Attributes:
        head (LinkedListNode): the first node in the list.
        tail (LinkedListNode): the last node in the list.
        size (LinkedListNode): the total number of elements in the list.
    """
    def __init__(self):
        """Initialize the head and tail attributes by setting
        them to None, since the list is empty initially. Initialize size to 0.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        """Append a new node containing the data to the end of the list."""
        # Create a new node to store the input data.
        new_node = LinkedListNode(data)
        if self.head is None:
            # If the list is empty, assign the head and tail attributes to
            # new_node, since it becomes the first and last node in the list.
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            # If the list is not empty, place new_node after the tail.
            self.tail.next = new_node               # tail --> new_node
            new_node.prev = self.tail               # tail <-- new_node
            # Now the last node in the list is new_node, so reassign the tail.
            self.tail = new_node
            self.size += 1

    # Problem 2
    def find(self, data):
        """Return the first node in the list containing the data.

        Raises:
            ValueError: if the list does not contain the data.

        Examples:
            >>> l = LinkedList()
            >>> for x in ['a', 'b', 'c', 'd', 'e']:
            ...     l.append(x)
            ...
            >>> node = l.find('b')
            >>> node.value
            'b'
            >>> l.find('f')
            ValueError: <message>
        """
        nextElement = self.head
        if nextElement is None:
            raise ValueError("List is empty")
        while nextElement.value != data:
            if nextElement.next is None:
                raise ValueError("data not found in list")
            else:
                nextElement = nextElement.next

        return nextElement

    # Problem 2
    def get(self, i):
        """Return the i-th node in the list.

        Raises:
            IndexError: if i is negative or greater than or equal to the
                current number of nodes.

        Examples:
            >>> l = LinkedList()
            >>> for x in ['a', 'b', 'c', 'd', 'e']:
            ...     l.append(x)
            ...
            >>> node = l.get(3)
            >>> node.value
            'd'
            >>> l.get(5)
            IndexError: <message>
        """
        nextElement = self.head
        if i < 0:
            raise IndexError("index cannot be negative")

        if i > self.size - 1:
            raise IndexError("index out of range")

        for index in range(i):
            nextElement = nextElement.next

        return nextElement

    # Problem 3
    def __len__(self):
        """Return the number of nodes in the list.

        Examples:
            >>> l = LinkedList()
            >>> for i in (1, 3, 5):
            ...     l.append(i)
            ...
            >>> len(l)
            3
            >>> l.append(7)
            >>> len(l)
            4
        """
        return self.size

    # Problem 3
    def __str__(self):
        """String representation: the same as a standard Python list.

        Examples:
            >>> l1 = LinkedList()       |   >>> l2 = LinkedList()
            >>> for i in [1,3,5]:       |   >>> for i in ['a','b',"c"]:
            ...     l1.append(i)        |   ...     l2.append(i)
            ...                         |   ...
            >>> print(l1)               |   >>> print(l2)
            [1, 3, 5]                   |   ['a', 'b', 'c']
        """
        lst = []
        nextNode = self.head
        while nextNode is not None:
            lst.append(nextNode.value)
            nextNode = nextNode.next
        return str(lst)

    # Problem 4
    def remove(self, data):
        """Remove the first node in the list containing the data.

        Raises:
            ValueError: if the list is empty or does not contain the data.

        Examples:
            >>> print(l1)               |   >>> print(l2)
            ['a', 'e', 'i', 'o', 'u']   |   [2, 4, 6, 8]
            >>> l1.remove('i')          |   >>> l2.remove(10)
            >>> l1.remove('a')          |   ValueError: <message>
            >>> l1.remove('u')          |   >>> l3 = LinkedList()
            >>> print(l1)               |   >>> l3.remove(10)
            ['e', 'o']                  |   ValueError: <message>
        """
        if self.head is None:
            raise ValueError("List is empty")
        self.find(data)
        prev = None
        curr = self.head
        while curr:
            if curr.value == data:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
            prev = curr
            curr = curr.next
        self.size -= 1


    # Problem 5
    def insert(self, index, data):
        """Insert a node containing data into the list immediately before the
        node at the index-th location.

        Raises:
            IndexError: if index is negative or strictly greater than the
                current number of nodes.

        Examples:
            >>> print(l1)               |   >>> len(l2)
            ['b']                       |   5
            >>> l1.insert(0, 'a')       |   >>> l2.insert(6, 'z')
            >>> print(l1)               |   IndexError: <message>
            ['a', 'b']                  |
            >>> l1.insert(2, 'd')       |   >>> l3 = LinkedList()
            >>> print(l1)               |   >>> l3.insert(1, 'a')
            ['a', 'b', 'd']             |   IndexError: <message>
            >>> l1.insert(2, 'c')       |
            >>> print(l1)               |
            ['a', 'b', 'c', 'd']        |
        """


        if index < 0 or index > self.size:
            raise IndexError("index out of range")

        if index == 0:
            newNode = LinkedListNode(data)
            node = self.head
            self.head = newNode
            node.prev = newNode
            newNode.next = node

            self.size += 1

        elif index == self.size - 1:
            self.append(data)

        else:
            newNode = LinkedListNode(data)
            nodePrev = self.get(index - 1)
            nodeNext = self.get(index)
            newNode.prev = nodePrev
            newNode.next = nodeNext
            nodePrev.next = newNode
            nodeNext.prev = newNode
            self.size += 1


# Problem 6: Deque class.
class Deque(LinkedList):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def pop(self):
        if self.size == 0:
            raise ValueError("List is empty")

        temp = self.tail.value
        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1

        return temp

    def remove(*args, **kwargs):
        raise NotImplementedError("Use append() or appendleft() for insert")

    def popleft(self):
        if self.size == 0:
            raise valueError("List is empty")

        node = self.head
        self.head = node.next
        self.size -= 1

        return node.value

    def appendleft(self, data):
        newNode = LinkedListNode(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode

            self.size += 1
        else:
            node = self.head
            self.head = newNode
            node.prev = newNode
            newNode.next = node

            self.size += 1

    def insert(*args, **kwargs):
        raise NotImplementedError("Use pop() or popleft() for removal")


# Problem 7
def prob7(infile, outfile):
    """Reverse the contents of a file by line and write the results to
    another file.

    Parameters:
        infile (str): the file to read from.
        outfile (str): the file to write to.
    """
    lst = Deque()
    with open(infile, 'r') as input:
        contents = input.readlines()
    for line in contents:
        lst.appendleft(line)

    with open(outfile, 'w') as output:
        output.write(lst.popleft() + '\n')
        while lst.size > 1:
            output.write(lst.popleft())
        output.write(lst.popleft().rstrip('\n'))


"""if __name__ == "__main__":
    prob7('english.txt', 'output.txt')"""





