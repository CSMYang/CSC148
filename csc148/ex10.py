"""
Implement the add(key, value) method for our HashTable class.

The HashTable should use chaining, and it shouldn't grow in size (e.g.
we can have a very bad/unbalanced hash table).

If a key already exists in the hash table, its value should be replaced.

Use HashTable.get_hash(key) to get the hash values. Assume the key will always
be a string.
"""
from typing import Any


class HashTable:
    """
    A class representing a HashTable.
    """

    def __init__(self) -> None:
        """
        Initialize this HashTable with 4 buckets.
        """
        self._content = [[], [], [], []]

    def __str__(self) -> str:
        """
        Print out this HashTable and all of its contents.

        >>> print(HashTable())
        0: []
        1: []
        2: []
        3: []
        >>> h = HashTable()
        >>> h.add('a', 'b')
        >>> print(h)
        0: []
        1: [('a', 'b')]
        2: []
        3: []
        """
        strings = []
        for i in range(len(self._content)):
            strings.append("{}: {}".format(i, self._content[i]))
        return "\n".join(strings)

    def get_hash(self, key: str) -> int:
        """
        Return the hashed value of key.

        >>> h = HashTable()
        >>> h.get_hash('a')
        97
        """
        if key == '':
            return 3

        return ord(key[0]) * len(key)

    def insert(self, key: str, value: Any) -> None:
        """
        Insert (key, value) into this HashTable using self.get_hash() as the
        hash function.

        >>> h = HashTable()
        >>> h.insert('a', 'b')
        >>> print(h)
        0: []
        1: [('a', 'b')]
        2: []
        3: []
        """
        index = self.get_hash(key) % 4
        if not self._content[index]:
            self._content[index].append((key, value))
        else:
            n = None
            for i in range(len(self._content[index])):
                if self._content[index][i][0] == key:
                    n = i
            if n:
                self._content[index].insert(n, (key, value))
                self._content[index].pop(n + 1)
            else:
                self._content[index].append((key, value))



if __name__ == '__main__':
    ht = HashTable()
    ht.insert('a', 'b')

    assert str(ht) == "0: []\n1: [('a', 'b')]\n2: []\n3: []"

    ht.insert('apple', 'bee')
    assert str(ht) == "0: []\n1: [('a', 'b'), ('apple', 'bee')]\n2: []\n3: []"

    ht.insert('apple', 'juice')
    assert str(ht) == "0: []\n1: [('a', 'b'), ('apple', 'juice')]\n2: []\n3: []"

    ht.insert('d', 'cat')
    assert str(ht) == ("0: [('d', 'cat')]\n1: [('a', 'b'), " +
                       "('apple', 'juice')]\n2: []\n3: []")

    ht.insert('yes', 'no')
    assert str(ht) == ("0: [('d', 'cat')]\n1: [('a', 'b'), " +
                       "('apple', 'juice')]\n2: []\n3: [('yes', 'no')]")

    import python_ta

    python_ta.check_all(config='ex8_pyta.txt')
