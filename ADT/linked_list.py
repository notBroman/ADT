import re
from random import randint

class _Node():
    __slots__ = '_element', 'next', 'prev'

    def __init__(self, element, next_node=None, prev_node=None):
        self._element = element
        self.next = next_node
        self.prev = prev_node

    def __del__(self):
        """ Garbage Collector for deleted Nodes"""
        self._element = None
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self._element)

class Singly_Linked_List():

    def __init__(self, values=None):
        self._tail = None
        self._head = None
        if values is not None:
            self.add_multiple(values)

    def __iter__(self):
        current = self._head
        while current:
            yield current
            current = current.next

    def __str__(self):
        values = [str(x) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        length = 0
        for element in self.__iter__():
            length += 1
        return length

    def add_end(self, value):
        newest = _Node(value)
        newest.next = None
        if self._head is None:
            self._tail = newest
            self._head = self._tail
        else:
            self._tail.next = newest
            self._tail = self._tail.next

    def add_first(self, value):
        newest = _Node(value)
        if self._head is None:
            newest.next = None
            self._head = self._tail = newest
        else:
            newest.next = self._head
            self._head = newest

    def rm_first(self):
        if self._head is None:
            raise ValueError("Value Error: No elements in Linked List")
        else:
            removed = self._head
            self._head = self._head.next
            removed.__del__() # garbage collection for node

    def add_multiple_end(self, values):
        for element in values:
            self.add_end(element)

    def add_multiple_front(self, values):
        for element in values:
            self.add_first(element)

    def generate(self, n, min_val, max_val):
        self._head = self._tail = None
        for i in range(n):
            self.add_end(randint(min_val, max_val))

def rm_dup(ll:Singly_Linked_List):
    for e in ll.__iter__():
        for e1 in ll.__iter__():
            if e1.next is e:
                e1.next = e1.next.next

if __name__ == '__main__':
    l1 = Singly_Linked_List()
    l1.generate(100, 0, 100)
    print(l1)
    l1.rm_first()
    print(l1)
