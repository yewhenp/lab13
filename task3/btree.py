"""
Module for self-created small Binary Tree
"""

from btnode import BinaryTreeNode


class BinaryTree:
    """
    Class for self-created small Binary Tree
    """
    def __init__(self, root_value):
        self.root = BinaryTreeNode(root_value)
        self.left = None
        self.right = None

    def add_left(self, value):
        """
        (BinaryTree, BinaryTree/obj) -> None
        Adds left object to tree
        """
        self.left = value

    def add_right(self, value):
        """
        (BinaryTree, obj) -> None
        Adds right object to tree
        """
        self.right = value

    def get_left(self):
        """
        BinaryTree -> BinaryTree/obj/None
        Returns left object
        """
        return self.left

    def get_right(self):
        """
        BinaryTree -> BinaryTree/obj/None
        Returns right object
        """
        return self.right

    def get_root(self):
        """
        BinaryTree -> obj
        Returns root object
        """
        return self.root.root()
