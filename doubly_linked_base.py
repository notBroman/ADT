class _Node():
    __slots__ = '_elemnt', 'next', 'prev'

    def __init__(self, element, next_node=None, prev_node=None):
        self._element = element
        self.next = next_node
        self.prev = prev_node

    def __del__(self):
        """ Garbage Collector for deleted Nodes """
        self._element = None
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self._element)

class _Doubly_Linked_Base():
    """ Implementation of Doubly Linked List ADT """
    def __init__(self):
        """ Initialize list with special node for head and tail """
        self.__head = _Node(None)
        self.__tail = _Node(None)
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        self._size = 0

    def __iter__(self):
        current = self.__head.next
        while current is not self.__tail.prev:
            yield current
            current = current.next

    def __str__(self):
        values = [str(e) for e in self]
        return ' -> '.join(values)

    def __len__(self):
        return self._size

    def add_between(self, value, predecessor:_Node, successor:_Node):
        newest = _Node(value, successor, predecessor)
        predecessor.next = newest
        successor.prev = newest
        self._size += 1
        return newest

    def rm_node(self, node:_Node):
        if self._size == 0:
            raise IndexError("Index Error: no elements in list")
        else:
            predecessor = node.prev
            successor = node.next
            predecessor.next = successor
            successor.prev = predecessor
            self._size -= 1
            element = node._element
            node.__del__()
            return element

if __name__ == '__main__':
    print('1')
