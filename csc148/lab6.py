"""
The Tree class for Lab 6.
"""
from typing import Any, List


class Tree:
    """
    A class representing a Tree.

    value - The value of the Tree's root
    children - The root nodes of the children of this Tree.
    """
    value: Any
    children: List['Tree']

    def __init__(self, value: Any, children: List['Tree'] = None) -> None:
        """
        Initialize this Tree with the root value value and children children.
        """
        self.value = value

        # We make this a copy of the list children, in case it gets modified
        # at some point elsewhere.
        self.children = children[:] if children else []

    # For convenience when trying to make a Tree.
    def __str__(self) -> str:
        """
        Return the string representation of this Tree, such that the root
        node is at the top, and all subtrees are below it. Every line of
        the string has the same length (being padded with spaces if needed).

        >>> t1 = Tree(1, [Tree(3, [Tree(4), Tree(6)])])
        >>> print(t1)
          1
          3
        4   6
        >>> t2 = Tree(2, [Tree(8)])
        >>> print(t2)
        2
        8
        >>> t3 = Tree(9, [Tree(7), Tree(5)])
        >>> print(t3)
          9
        7   5
        >>> children = [t1, t2, t3]
        >>> t = Tree(0, children)
        >>> print(t)
                0
          1     2     9
          3     8   7   5
        4   6
        """
        child_strings = [str(child).split('\n') for child in self.children]

        # Get the maximum number of lines from a child's string
        max_lines = 0
        if child_strings:
            max_lines = max([len(child) for child in child_strings])

        # Create a list with max_lines empty lists in it
        new_string = [[] for _ in range(max_lines)]

        # Join each line of each child's string
        for i in range(max_lines):
            for child in child_strings:
                if i < len(child):
                    new_string[i].append(child[i])
                else:
                    # If there is no such line, just pad it with spaces
                    new_string[i].append(" " * len(child[0]))

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

        # Return the new string
        return "\n".join(new_string_joined)

    def count_occurence(self, x) -> int:
        """
        Returns the number of occurence of x in a tree.
        """
        count_root = 1 if self.value == x else 0
        return sum([child.count_occurence(x) for child in self.children]) + \
               count_root

    def get_internal_nodes(self) -> list:
        """
        Return a list of values of all nodes those are not leafs.
        """
        if not self.children:
            return []
        return [self.value] + sum([child.get_internal_nodes() for child in
                                   self.children], [])

    def get_depth_of(self, x) -> int:
        """
        Return the depth of value x in tree.
        """
        if self.value == x or not self.contain(x):
            return 0
        return 1 + sum([child.get_depth_of(x) for child in self.children])

    def contain(self, x) -> bool:
        """
        Return True iff x is in this tree.
        """
        if self.value == x:
            return True
        return any([child.contain(x) for child in self.children])

    def get_values_at_depth(self, x) -> list:
        """
        Return a list of all values at depth x.
        """
        if x == 0:
            return [self.value]
        return sum([child.get_values_at_depth(x) for child in self.children],
                   [])

    def get_max_branching_factor(self) -> int:
        """
        Return the maximum branching factor of a tree
        """
        if not self.children:
            return 0
        return 1 + max([child.get_max_branching_factor() for child in
                        self.children])

    def copy(self) -> 'Tree':
        """
        Return a copy of the tree.
        """
        return Tree(self.value, sum([child.copy for child in self.children],
                                    []))


if __name__ == '__main__':
    t1 = Tree(1, [Tree(3)])
    t2 = Tree(2)
    t = Tree(0, [t1, t2])
