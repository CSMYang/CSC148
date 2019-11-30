"""
The BattleQueue class for A1.

A BattleQueue is a queue that lets our game know in what order various
characters are going to attack. The method headers and descriptions have all
been provided for you, but the implementation will depend on you.

You must replace the 'Any's in the type annotations as well as add in
the constructors for the docstring examples.
"""
# To put a class name without importing it, just wrap the name in ''s.
# For example:
# add(self, character: 'Something') -> None:
#
# If there are multiple return types, import Union and use that. For example:
# Union[str, bool]
from typing import Union


class BattleQueue:
    """
    A class representing a BattleQueue.
    """

    def __init__(self) -> None:
        """
        Initialize this BattleQueue.

        >>> bq = BattleQueue()
        >>> bq.is_empty()
        True
        """
        self._content = []

    def add(self, character: "Characters") -> None:
        """
        Add character to this BattleQueue.

        >>> bq = BattleQueue()
        >>> from a1_playstyle import ManualPlaystyle
        >>> ps = ManualPlaystyle(bq)
        >>> from a1_characters import Mage
        >>> c = Mage('Alex', bq, ps)
        >>> bq.add(c)
        >>> bq.is_empty()
        False
        """
        self._content.append(character)

    def remove(self) -> "Characters":
        """
        Remove and return the character at the front of this BattleQueue.

        >>> bq = BattleQueue()
        >>> from a1_playstyle import ManualPlaystyle
        >>> ps = ManualPlaystyle(bq)
        >>> from a1_characters import Rogue
        >>> c = Rogue('Sophia', bq, ps)
        >>> bq.add(c)
        >>> bq.remove()
        Sophia (Rogue): 100/100
        >>> bq.is_empty()
        True
        """
        i = 0
        while i < len(self._content) and \
                not self._content[i].get_available_actions():
            i += 1
        return self._content.pop(i)

    def is_empty(self) -> bool:
        """
        Return whether this BattleQueue is empty (i.e. has no players or
        has no players that can perform any actions).

        >>> bq = BattleQueue()
        >>> bq.is_empty()
        True
        """
        if not self._content:
            return True
        for character in self._content:
            if character.get_available_actions():
                return False
        return True

    def peek(self) -> None:
        """
        Return the character at the front of this BattleQueue but does not
        remove them.

        >>> bq = BattleQueue()
        >>> from a1_playstyle import ManualPlaystyle
        >>> ps = ManualPlaystyle(bq)
        >>> from a1_characters import Rogue
        >>> c = Rogue('Sophia', bq, ps)
        >>> bq.add(c)
        >>> bq.peek()
        Sophia (Rogue): 100/100
        >>> bq.is_empty()
        False
        """
        i = 0
        while i < len(self._content) and \
                not self._content[i].get_available_actions():
            i += 1
        return self._content[i]

    def is_over(self) -> bool:
        """
        Return whether the game being carried out in this BattleQueue is over
        or not.

        A game is considered over if:
            - Both players have no skills that they can use.
            - One player has 0 HP
            or
            - The BattleQueue is empty.

        >>> bq = BattleQueue()
        >>> bq.is_over()
        True

        >>> from a1_playstyle import ManualPlaystyle
        >>> ps = ManualPlaystyle(bq)
        >>> from a1_characters import Rogue
        >>> c = Rogue('Sophia', bq, ps)
        >>> bq.add(c)
        >>> bq.is_over()
        False
        """
        if self.is_empty():
            return True
        if self.peek().get_hp() == 0 or self.peek().enemy.get_hp() == 0:
            return True
        if not (self.peek().get_available_actions() or
                self.peek().enemy.get_available_actions()):
            return True
        return False

    def get_winner(self) -> Union["Characters", None]:
        """
        Return the winner of the game being carried out in this BattleQueue
        if the game is over. If the game is not over or if there is no winner
        (i.e. there's a tie), return None.

        >>> bq = BattleQueue()
        >>> bq.get_winner()
        """
        if self.is_over():
            if self.peek().get_hp() == 0:
                return self.peek().enemy
            elif self.peek().enemy.get_hp() == 0:
                return self.peek()
        return None


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config='a1_pyta.txt')
