"""
The Tree class you'll be provided on the midterm.
"""


class BSTree:
    """
    A class representing a Tree.

    value - The value of the root of this Tree.
    children - The subtrees of this Tree.
    """
    value: int
    left_child: BSTree
    right_child: BSTree

    def __init__(self, value: int, left_child: BSTree = None,
                 right_child: BSTree = None, parent: BSTree = None) -> None:
        """
        Initialize this Tree with the value value and children children.
        """
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent

    def path_length_from_root(self, k: int) -> int:
        """
        ...
        """
        if self.value == k:
            return 0
        elif self.value < k:
            return 1 + self.right_child.path_length_from_root(k)
        return 1 + self.left_child.path_length_from_root(k)

    def fcp(self, k: BSTree, m: BSTree) -> BSTree:
        """
        ...
        """
        if m.value >= self.value >= k.value or \
                k.value >= self.value >= m.value:
            return self.value
        elif k.value < self.value and m.value < self.value:
            return self.left_child.fcp(k, m)
        return self.right_child.fcp(k, m)

    def is_t_away(self, k: BSTree, m: BSTree, t: int) -> bool:
        """
        ...
        """
        return t == (self.path_length_from_root(k.value) +
                     self.path_length_from_root(m.value) -
                     2 * self.path_length_from_root(self.fcp(k, m)))
