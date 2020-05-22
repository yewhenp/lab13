"""
Module for Tree class
"""


class Tree:
    """
    Tree class
    """
    def __init__(self, root_value):
        self.root = root_value
        self.childs = []

    def add(self, value):
        """
        (Tree, obj) -> None
        adds object as a root`s child
        """
        self.childs.append(value)

    def get_childs(self):
        """
        Tree -> obj
        Returns children
        """
        return self.childs

    def get_root(self):
        """
        Tree -> obj
        Returns root value
        """
        return self.root
