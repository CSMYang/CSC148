"""
Provided is a LinkedList and LinkedListNode class.

Implement the LinkedList method 'swap_front_back'.
"""

from typing import Union, Any


class LinkedListNode:
    """
    A Node to be used in a LinkedList.

    next_ - The successor to this LinkedListNode
    value - The data represented by this LinkedListNode.
    """
    next_: Union["LinkedListNode", None]
    value: object

    def __init__(self, value: object,
                 next_: Union["LinkedListNode", None] = None) -> None:
        """
        Initialize this LinkedListNode with the value value and successor next.

        >>> LinkedListNode(3).value
        3
        >>> LinkedListNode(3).next_ == None
        True
        """
        self.value = value
        self.next_ = next_

    def __str__(self) -> str:
        """
        Return a string representation of this LinkedListNode.

        >>> print(LinkedListNode(3))
        3 ->
        """
        return "{} -> ".format(self.value)


class LinkedList:
    """
    Collection of LinkedListNodes.

    front - first node of this LinkedList
    back - last node of this LinkedList
    size - the number of nodes in this LinkedList (>= 0)
    """
    front: Union[LinkedListNode, None]
    back: Union[LinkedListNode, None]
    size: int

    def __init__(self) -> None:
        """
        Initialize an empty LinkedList.

        >>> lnk = LinkedList()
        >>> lnk.size
        0
        """
        self.front = None
        self.back = None
        self.size = 0

    def prepend(self, value: Any) -> None:
        """
        Insert value to the start of this LinkedList (before self.front).

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> print(lnk)
        1 -> 0 -> |
        """
        self.front = LinkedListNode(value, self.front)
        if self.back is None:
            self.back = self.front
        self.size += 1

    def __str__(self) -> str:
        """
        Return a string representation of this LinkedList.

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> print(lnk)
        1 -> 0 -> |
        """
        cur_node = self.front
        result = ''
        while cur_node is not None:
            result += str(cur_node)
            cur_node = cur_node.next_
        return result + '|'

    def swap_front_back(self) -> None:
        """
        Swap the LinkedListNodes of the front and back of this linked list.

        Do not create any new LinkedListNodes.
        Do not swap the values of the LinkedListNodes.

        >>> lnk = LinkedList()
        >>> lnk.prepend(3)
        >>> lnk.prepend(2)
        >>> lnk.prepend(1)
        >>> print(lnk)
        1 -> 2 -> 3 -> |
        >>> front_id = id(lnk.front)
        >>> back_id = id(lnk.back)
        >>> lnk.swap_front_back()
        >>> print(lnk)
        3 -> 2 -> 1 -> |
        >>> front_id == id(lnk.back)
        True
        >>> back_id == id(lnk.front)
        True
        """
        if self.size > 1:
            previous_node, current_node = None, self.front
            self.back = current_node
            while current_node.next_ is not None:
                previous_node = current_node
                current_node = current_node.next_
            previous_node.next_ = self.front
            previous_node.next_.next_ = None
            self.front = current_node
            self.front.next_ = previous_node



if __name__ == '__main__':
    lnk = LinkedList()
    lnk.prepend(3)
    lnk.prepend(2)
    lnk.prepend(1)

    front_id = id(lnk.front)
    back_id = id(lnk.back)
    lnk.swap_front_back()

    assert str(lnk) == "3 -> 2 -> 1 -> |"
    assert front_id == id(lnk.back)
    assert back_id == id(lnk.front)

    lnk2 = LinkedList()
    lnk2.prepend(2)
    lnk2.prepend(1)

    front_id2 = id(lnk2.front)
    back_id2 = id(lnk2.back)
    lnk2.swap_front_back()

    assert str(lnk2) == "2 -> 1 -> |"

    assert front_id2 == id(lnk2.back)
    assert back_id2 == id(lnk2.front)

    import python_ta

    python_ta.check_all(config="ex4_pyta.txt")
