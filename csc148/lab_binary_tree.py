"""
The BinaryTree class for Lab 7.
"""
from typing import Any


class BinaryTree:
    """
    A class representing a BinaryTree.

    value - The value of the BinaryTree's root
    left - The root node of this BinaryTree's left subtree.
    right - The root node of this BinaryTree's right subtree.
    """
    value: Any
    left: 'BinaryTree'
    right: 'BinaryTree'

    def __init__(self, value: Any, left: 'BinaryTree' = None,
                 right: 'BinaryTree' = None) -> None:
        """
        Initialize this BinaryTree with the root value value, left subtree left,
        and right subtree right.
        """
        self.value = value
        self.left = left
        self.right = right

    # For convenience when trying to make a Tree.
    def __str__(self) -> str:
        """
        Return the string representation of this BinaryTree, such that the root
        node is at the top, and all subtrees are below it. Every line of
        the string has the same length (being padded with spaces if needed).

        >>> t1 = BinaryTree(1, BinaryTree(3, BinaryTree(4), BinaryTree(6)))
        >>> print(t1)
          1
          3
        4   6
        >>> t2 = BinaryTree(9, BinaryTree(7), BinaryTree(5))
        >>> print(t2)
          9
        7   5
        >>> t = BinaryTree(0, t1, t2)
        >>> print(t)
              0
          1       9
          3     7   5
        4   6
        """
        children = []
        if self.left:
            children.append(self.left)

        if self.right:
            children.append(self.right)

        child_strings = [str(child).split('\n') for child in children]

        # Get the maximum number of lines from a child's string
        max_lines = 0
        if child_strings:
            max_lines = max([len(child) for child in child_strings])

        # Create a list with max_lines empty lists in it
        new_string = [[] for _ in range(max_lines)]

        # Join each line of each child's string
        for i in range(max_lines):
            for child in child_strings:
                child_length = max([len(line) for line in child])

                if i < len(child):
                    padding_needed = child_length - len(child[i])
                    new_string[i].append(child[i] + " " * padding_needed)
                else:
                    # If there is no such line, just pad it with spaces
                    new_string[i].append(" " * child_length)

        # Put 3 spaces between each subtree
        new_string_joined = [(' ' * 3).join(child) for child in new_string]

        # Add in the value of the current Tree
        str_width = 0
        if new_string_joined:
            str_width = len(new_string_joined[0])

        left_padding = str_width // 2
        right_padding = (str_width - str_width // 2) - 1

        new_string_joined.insert(0, "{}{}{}".format(" " * left_padding,
                                                    self.value,
                                                    " " * right_padding))

        new_string_joined = [line.rstrip() for line in new_string_joined]

        # Return the new string
        return "\n".join(new_string_joined)

    def get_all_internal_nodes(self) -> list:
        """
        '''
        """
        if not (self.left or self.right):
            return []
        return [self.value] + sum([self.left.get_all_internal_nodes()], [])\
                + sum([self.right.get_all_internal_nodes()], [])

    def get_max_depth(self) -> int:
        """
        ...
        """
        if not (self.right or self.left):
            return 0
        return 1 + max(self.left.get_max_depth(), self.right.get_max_depth())

    def contains(self, x) -> bool:
        """
        ...
        """
        if self.value == x:
            return True
        return any([self.left.contains(x), self.right.contains(x)])

    def get_depth_of(self, x) -> int:
        """
        ...
        """
        if self.value == x:
            return 0
        elif not self.contains(x):
            return -1
        left = self.left.get_depth_of(x)
        right = self.right.get_depth_of(x)
        if left != -1:
            return left + 1
        elif right != -1:
            return right + 1

    def get_values_at_depth(self, x) -> list:
        """
        ...
        """
        if x == 0:
            return [self.value]
        return sum(self.left.get_values_at_depth(x - 1),
                   self.right.get_values_at_depth(x - 1))



if __name__ == '__main__':
    t1 = BinaryTree(1, left=BinaryTree(3))
    t2 = BinaryTree(2)
    t = BinaryTree(0, left=t1, right=t2)
