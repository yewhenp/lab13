"""
Module for tic-tac-toe Board and BinaryTree generation
"""

import copy
import random
from btree import BinaryTree


class Board:
    """
    Class for tic-tac-toe Board
    """
    def __init__(self):
        self._board = [[None, None, None],
                       [None, None, None],
                       [None, None, None]]
        self._num_of_moves = 0
        self._moves_left = [
            (0, 0), (0, 1), (0, 2),
            (1, 0), (1, 1), (1, 2),
            (2, 0), (2, 1), (2, 2)
        ]
        self._last_moves = []

    def __str__(self):
        """
        Board -> str
        String representation pf Board
        """
        line_to_return = ""
        line_to_return += "_" * 7 + "\n"

        for row in range(3):
            for col in range(3):
                if self._board[row][col]:
                    line_to_return += "|" + self._board[row][col]
                else:
                    line_to_return += "| "
            line_to_return += "|\n" + "_" * 7 + "\n"

        return line_to_return

    def _check_figure(self, figure):
        """
        (Board, str) -> True
        Checks if there is a winning situation on Board for figure (x, o)
        """
        # checking rows
        for row in range(3):
            if self._board[row][0] == self._board[row][1] == self._board[row][2] == figure:
                return True

        # checking col
        for col in range(3):
            if self._board[0][col] == self._board[1][col] == self._board[2][col] == figure:
                return True

        # checking diag
        if self._board[0][0] == self._board[1][1] == self._board[2][2] == figure:
            return True
        if self._board[0][2] == self._board[1][1] == self._board[2][0] == figure:
            return True

        return False

    def make_move(self, figure, row, col):
        """
        (Board, str, int, int) -> bool
        Makes move
        """
        if (row, col) not in self._moves_left:
            print("Error")
            return False

        self._board[row][col] = figure
        self._moves_left.remove((row, col))

        self._num_of_moves += 1
        return True

    def check_situation(self):
        """
        Board - (int, srt/None)
        Checks situation on the Board
        """
        if self._check_figure('x'):
            return 0, 'x'
        if self._check_figure('o'):
            return 0, 'o'
        if self._num_of_moves < 9:
            return 1, None
        return 0, None

    def _recursive_tree(self, tree):
        """
        (Board, BinaryTree) -> BinaryTree
        Builds game BinaryTree
        """
        set_of_moves = set()

        try:
            set_of_moves.add(random.choice(self._moves_left))
        except IndexError:
            return tree

        if len(self._moves_left) > 1:
            while len(set_of_moves) < 2:
                set_of_moves.add(random.choice(self._moves_left))

        set_of_moves = list(set_of_moves)
        self._last_moves = copy.deepcopy(set_of_moves)

        flag = False
        for move in set_of_moves:
            boaard = copy.deepcopy(self)
            if boaard._num_of_moves % 2 == 1:
                boaard.make_move('o', move[0], move[1])
            else:
                boaard.make_move('x', move[0], move[1])

            if flag:
                tree.add_right(boaard._recursive_tree(BinaryTree(boaard)))
            else:
                flag = True
                tree.add_left(boaard._recursive_tree(BinaryTree(boaard)))

        return tree

    def _recursive_calculation(self, tree):
        """
        (Board, BinaryTree) -> int
        Calculate the win power of tree
        """
        if tree.get_left() and tree.get_right():
            return self._recursive_calculation(tree.get_left()) + \
                   self._recursive_calculation(tree.get_right())
        if tree.get_left():
            return self._recursive_calculation(tree.get_left())
        if tree.get_right():
            return self._recursive_calculation(tree.get_right())

        state = tree.get_root().check_situation()

        if state[0] == 0:
            if state[1] == 'x':
                return -1
            if state[1] == '0':
                return 1
            return 0

    def _tree_generator(self):
        """
        Board -> (int, int)
        Generates the best move of 2 random
        """
        tree = BinaryTree(self._board)

        board = copy.deepcopy(self)
        tree = board._recursive_tree(tree)

        left_variant = self._recursive_calculation(tree.get_left())
        right_variant = self._recursive_calculation(tree.get_right())

        if left_variant > right_variant:
            return board._last_moves[0]
        return board._last_moves[1]

    def make_computer_move(self):
        """
        Board -> None
        Makes the move for computer
        """
        move = self._tree_generator()
        self.make_move('o', move[0], move[1])
