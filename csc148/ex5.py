"""
Implement the get_all_evens() method below.
"""

from typing import Union, List


def get_all_evens(x: Union[list, int]) -> List[int]:
    """
    Return a list of all of the even ints in x or in any sublists within x.

    Order doesn't matter.
    """
    list_of_evens = []
    if isinstance(x, int) and x % 2 == 0:
        return [x]
    elif x == [] or (isinstance(x, int) and x % 2 != 0):
        return []
    for item in x:
        list_of_evens.extend(get_all_evens(item))
    return list_of_evens


if __name__ == '__main__':
    single_int = 1
    assert get_all_evens(single_int) == []

    lst = [1, 2, 3, 4]
    assert sorted(get_all_evens(lst)) == [2, 4]

    nested_lst = [1, [2, 3, [4]], [[4], 6]]
    assert sorted(get_all_evens(nested_lst)) == [2, 4, 4, 6]

    import python_ta

    python_ta.check_all(config="ex5_pyta.txt")
