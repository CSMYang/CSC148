from typing import Any, Union

"""
Final exam practice
"""


class Food:
    """
    A class representing foods.
    """

    def __init__(self, name: str, exp_date: str, quantity: int = 0) -> None:
        """
        Initializes a food with name name, quantity quantity and expiration date
        exp_date.
        """
        self.name = name
        self.quantity = quantity
        self.expiration_date = exp_date

    def __str__(self) -> str:
        """
        Returns a string representation of food.
        """
        return "{}: {}. Best before {}".format(self.name, self.quantity,
                                               self.expiration_date)

    def __eq__(self, other) -> bool:
        """
        Returns True if self has the same name and expiration date as other.
        """
        if not isinstance(self, other):
            return False
        return self.name == other.name and \
               self.expiration_date == other.expiration_date


class Storage:
    """
    A class representing storages
    """

    def __init__(self, max_capacity: int) -> None:
        """
        Initializes a storage
        """
        self._content = []
        self.capacity = max_capacity

    def get_num(self) -> int:
        """
        Return the number of items stored in the storage
        """
        return len(self._content)

    def store(self, item) -> bool:
        """
        Store an item into the storage. Returns True if successfully stored,
        otherwise False.
        """
        if self.get_num() < self.capacity:
            self._content.append(item)
            return True
        return False

    def remove(self):
        """
        Remove and return an item from the storage.
        """
        raise NotImplementedError

    def __str__(self) -> str:
        """
        Returns a string representation of current storage.
        """
        if not self._content:
            return "The storage has no item inside."
        s = "The storage has:"
        for item in self._content:
            s += " "
            s += str(item)
        s += '.'
        return s

    def __eq__(self, other) -> bool:
        """
        Return True if self has the same item as the other.
        """
        if not isinstance(self, other):
            return False
        for item in self._content:
            if item not in other._content:
                return False
        return True


class Fridge(Storage):
    """
    A class representing fridges
    """

    def __init__(self, max_capacity: int) -> None:
        """
        ...
        """
        super().__init__(max_capacity)

    def store(self, item: Food) -> bool:
        """
        Stores a food inside a fridge
        """
        if not isinstance(item, Food) or self.get_num() >= self.capacity:
            return False
        for foods in self._content:
            if item == foods:
                foods.quantity += 1
                return True
        self._content.append(item)
        return True


def get_all_elements(l: Any) -> list:
    """
    ...
    """
    if not isinstance(l, list):
        return [l]
    return sum([get_all_elements(item) for item in l], [])


def get_most_common(l: list) -> Any:
    """
    ...
    """
    elements = get_all_elements(l)
    s = {}
    for item in elements:
        if item not in s:
            s[item] = 0
        s[item] += 1
    item_to_return = elements[0]
    for key in s:
        if s[key] > s[item_to_return]:
            item_to_return = key
    return item_to_return
