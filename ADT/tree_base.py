import re

class _TreeNode():
    __slots__ = 'left_child', 'right_child', 'data', 'parent', 'pos'

    def __init__(self, new_data=None, new_parent=None:_TreeNode, new_r_child=None:_TreeNode, new_l_child=None:_TreeNode):
        self.data = new_data
        self.parent = new_parent
        self.left_child = new_l_child
        self.right_child = new_r_child
        self.pos = None

    def __str__(self):
        return str(self._data)

class Binary_Tree():
    def __init__(self, new_val=None):
        self._root = _TreeNode(new_val)
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        TODO
        # traversal method

    def get_root(self):
        return self._root

    def add_left(self, val):
        if self._size ==  0:
            self._root.left_child = _TreeNode(val, self._root)

    def add_right(self, val):
        TODO

    def rm(self):
        TODO

    def replace(self, position):
        TODO

if __name__ == '__main__':
    b1 = Binary_Tree(0)

