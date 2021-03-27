import re

class _TreeNode():
    __slots__ = 'left_child', 'right_child', 'data', 'parent'

    def __init__(self, new_data=None):
        self.data = new_data
        self.parent = new_parent
        self.left_child = new_l_child
        self.right_child = new_r_child

    def __str__(self):
        return str(self._data)

class Binary_Tree():
    def __init__(self, new_val):
        self._root = _TreeNode(new_val)

    def preorder_trav(self, start:_TreeNode, trav:str):
        """traverses root->left->right"""
        if start:
            trav += str(start.data) + '->'
            preorder_trav(self, start.left_child, trav)
            preorder_trav(self, start.right_child, trav)
        return trav

    def inorder_trav(self, start:_TreeNode, trav:str):
        """traverses left->root->right"""
        if start:
            inorder_trav(self, start.left_child, trav)
            trav += str(start.data) + '->'
            inorder_trav(self, start.right_child, trav)

    def postorder_trav(self, start:_TreeNode, trav:str):
        """traverses left->right->root"""

    def get_root(self):
        return self._root

    def add_left(self, val):
        if self._size ==  0:
            self._root.left_child = _TreeNode(val, self._root)
        else:
            TODO

    def add_right(self, val):
        if self._size == 0:
            self._root.right_child = _TreeNode(val, self._root)
        else:
            TODO

    def rm(self):
        TODO

    def replace(self, position):
        TODO

if __name__ == '__main__':
    b1 = Binary_Tree(0)

