from ADT import linked_list as ll

"""Stack Implementation using a singly linked list"""

class Stack():
    def __init__(self):
        self._data = ll.Singly_Linked_List()
        self._bot = self._data._tail
        self._top = self._data._head
        self._size = 0

    def __str__(self):
        return self._data.__str__()

    def __len__(self):
        return self._size

    def pop(self):
        if self._size == 0:
            raise IndexError("Error: the stack is empty")
        else:
            popped = self._data._head
            self._data.rm_first
            self._size -= 1
            return popped

    def push(self, element):
       self._data.add_first(element)
       self._size += 1

    def get_top(self):
        return self._data._head

if __name__ == '__main__':
    s1 = Stack()
    s1.push('(')
    s1.push('(')
    s1.push(')')

    print(s1.get_top())
