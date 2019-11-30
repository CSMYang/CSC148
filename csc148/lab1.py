""" Define your class up here. """
from typing import List


class ShopCatalogue:
    """ A class representing the catalogue of a shop. """

    def __init__(self, shop_name: str) -> None:
        """ Initializes a shop catalogue with shop_name. The shop catalogue will
        initiallly has an empty dictionary items_to_price representing each item
        to its price, and an empty dictionary item_to_quantity representing each
        item to its quantity.

        >>> s = ShopCatalogue('AppleStore')
        >>> s.shop_name
        'AppleStore'
        >>> s.items_to_price
        {}
        >>> s.item_to_quantity
        {}
        """
        self.shop_name = shop_name
        self.items_to_price = {}
        self.item_to_quantity = {}

    def add_item(self, item_name: str, item_price: float, item_quantity: int):
        """ Adds an item to the shop catalogue and set its price. If the item is
        already in the catalogue, add the quantity to it.

        >>> s = ShopCatalogue('AppleStore')
        >>> s.add_item('Samsung Galaxy', 600.0, 5)
        >>> s.item_to_quantity
        {'Samsung Galaxy': 5}
        >>> s.items_to_price
        {'Samsung Galaxy': 600.0}
        """
        if item_name not in self.items_to_price:
            self.items_to_price[item_name] = item_price
            self.item_to_quantity[item_name] = item_quantity
        else:
            self.item_to_quantity[item_name] += item_quantity

    def remove_item(self, item_name: str, item_quantity: int) -> None:
        """ Remove a certain quantity of an item in shop catalogue. If the
        item's quantity is reduced to 0, remove it from the catalogue

        >>> s = ShopCatalogue('AppleStore')
        >>> s.add_item('Apple', 1.09, 10)
        >>> s.items_to_price
        {'Apple': 1.09}
        >>> s.item_to_quantity
        {'Apple': 10}
        >>> s.remove_item('Apple', 5)
        >>> s.item_to_quantity
        {'Apple': 5}
        >>> s.remove_item('Apple', 5)
        >>> s.item_to_quantity
        {'Apple': 0}
        """
        if item_name in self.item_to_quantity and \
                self.item_to_quantity[item_name] >= item_quantity:
            self.item_to_quantity[item_name] -= item_quantity
        elif item_name not in self.item_to_quantity:
            print('This item does not exist in shop catalogue')
        else:
            print('You can only remove {} {}(s)'.format(self.item_to_quantity[
                                                        item_name], item_name))

    def __str__(self) -> str:
        """ Return the string representation of a shop catalogue. """
        if len(self.items_to_price) == 0:
            return self.shop_name + ' has no item'
        else:
            sp = self.shop_name + ' has:'
            for item in self.items_to_price:
                if self.item_to_quantity[item] > 0:
                    sp = sp + ' ' + item + ' (x{}) for {} each'.format(
                        self.item_to_quantity[item], self.items_to_price[item])
            return sp

    def get_items_below(self, price: float) -> List[str]:
        """ Return a list containing all items with a price below the price
        given.
        """
        below = []
        for item in self.items_to_price:
            if self.items_to_price[item] < price:
                below.append(item)
        return below


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config="lab_pyta.txt")
    s = ShopCatalogue("UofT Bookstore")
    s.add_item("Chips", 0.99, 3)
    assert str(s) == "UofT Bookstore has: Chips (x3) for 0.99 each"
    s.add_item("Chips", 0.99, 10)
    assert str(s) == "UofT Bookstore has: Chips (x13) for 0.99 each"
    s.add_item("Pencil", 2.50, 3)
    assert str(s) == "UofT Bookstore has: Chips (x13) for 0.99 each, Pencil \
    (x3) for 2.50 each"
    s.remove_item("Pencil", 2)
    assert str(s) == "UofT Bookstore has: Chips (x13) for 0.99 each, Pencil \
    (x1) for 2.50 each"
    s.remove_item("Pencil", 1)
    assert str(s) == "UofT Bookstore has: Chips (x13) for 0.99 each"
    s.add_item("Pop", 1.95, 3)
    s.add_item("Pencil", 2.50, 2)
    assert s.get_items_below(2.00) == ['Chips', 'Pop']
