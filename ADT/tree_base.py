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

    def __del__(self):
        """ DO NOT USE INCOMPLETE/INCORRECT CODE """
        if self.is_root():
            # mistake in structruing need to check for children always
            # dont check for parent if node is root
            pass
        else:
            """ Node has right and left child """
            if self.left_child is not None and self.right_child is not None:
                if self is self.parent.left_child:
                    # implement logic to replace self correctly
                elif self is self.parent.right_child:
                    # implement logic to replace self correctly

            """ Node only has left child """
            elif self.left_child is not None and self.right_child is None:
                # node is parents left child
                if self is self.parent.left_child:
                    self.left_child.parent = self.parent
                    self.parent.left_child = self.left_child
                # node is parents right child
                elif self is self.parent.right_child:
                    self.left_child.parent = self.parent
                    self.parent.right_child = self.left_child
                # in case something goes wrong
                else:
                    print("case not accounted for")
                    break

            """ Node only has right child """
            elif self.left_child is None and self.right_child is not None:
                # node is parents left child
                if self is self.parent.left_child:
                    self.right_child.parent = self.parent
                    self.parent.left_child = self.right_child
                # node is parents right child
                elif self is self.parent.right_child:
                    self.right_child.parent = self.parent
                    self.parent.right_child = self.right_child
                # in case something goes wrong
                else:
                    print("case not accounted for")
                    break

        self.data = None
        self.parent = None
        self.left_child = None
        self.right_child = None

class Binary_Tree():
    def __init__(self, new_val):
        self._root = _TreeNode(new_val)

    def preorder_trav(self, start:_TreeNode, travd:str):
        """traverses root->left->right"""
        if start:
            travd += str(start.data) + '->'
            preorder_trav(self, start.left_child, travd)
            preorder_trav(self, start.right_child, travd)
        else:
            return travd

    def inorder_trav(self, start:_TreeNode, travd:str):
        """traverses left->root->right"""
        if start:
            inorder_trav(self, start.left_child, travd)
            travd += str(start.data) + '->'
            inorder_trav(self, start.right_child, travd)
        else:
            return travd

    def postorder_trav(self, start:_TreeNode, travd:str):
        """traverses left->right->root"""
        if start:
            postorder_trav(self, start.left_child, travd)
            postorder_trav(self, start.right_child, travd)
            travd += str(start.data) + '->'
        else:
            return travd

    def get_root(self):
        return self._root

    def add_left(self, val, parent:_TreeNode):
        """ return 1 -> success | return 0 -> failure """
        if type(parent) is _TreeNode:
            parent.left_child = _TreeNode(val)
            parent.left_child.parent = parent
            return 1
        else:
            return 0

    def add_right(self, val, parent:_TreeNode):
        """ return 1 -> success | return 0 -> failure"""
        if type(parent) is _TreeNode:
            parent.right_child = _TreeNode(val)
            parent.right_child.parent = parent
            return 1
        else:
            return 0

    def rm(self):
        TODO

if __name__ == '__main__':
    b1 = Binary_Tree(0)

