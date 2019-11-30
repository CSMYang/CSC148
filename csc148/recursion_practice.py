from typing import Union, List


def get_all_elements(x: Union[int, List]) -> List:
    """
    Return all the elements contained in x as a List.
    """
    if isinstance(x, int):
        return [x]
    elif x == []:
        return []
    list_of_elements = []
    for elements in x:
        list_of_elements.extend(get_all_elements(elements))
    return list_of_elements


def passes_condition(f, x: Union[int, List]) -> List:
    """
    Return a list of elements in x that passes function f.
    """
    if isinstance(x, int) and f(x):
        return [x]
    elif isinstance(x, int) and not f(x):
        return []
    list_of_elements = get_all_elements(x)
    list_of_passes = []
    for elements in list_of_elements:
        list_of_passes.extend(passes_condition(f, elements))
    return list_of_passes


def count_number_of_lists(x: Union[List, int]) -> int:
    """
    Return the number of nested lists of x.
    """
    if isinstance(x, int):
        return 0
    return 1 + sum([count_number_of_lists(sublist) for sublist in x])


def get_all_elements2(x: object) -> List:
    """
    Return a list of all objects contained in x.
    """
    if not isinstance(x, List):
        return [x]
    list_of_elements = []
    for elements in x:
        list_of_elements.extend(get_all_elements2(elements))
    return list_of_elements


def get_nth_fibonacci(num: int) -> int:
    """
    Return the nth number of fibonacci sequences.
    """
    if num == 1 or num == 2:
        return 1
    return get_nth_fibonacci(num - 1) + get_nth_fibonacci(num - 2)


def count_odd(x: Union[int, List]) -> int:
    """
    Return an int representing number of odd numbers in x.
    """
    if isinstance(x, int) and x % 2 == 0:
        return 1
    elif isinstance(x, int) and x % 2 != 0:
        return 0
    return sum([count_odd(item) for item in x])


def get_values_linked_list(x: 'LinkedList') -> List:
    """
    Return a list of values of a linkedlist.
    """
    if x is None:
        return []
    return [x.value] + get_values_linked_list(x.next_)


def count_elements_in(x: Union[int, list], y: List[int]) -> int:
    """
    ...
    """
    if isinstance(x, int):
        if x in y:
            return 1
        return 0
    return sum(count_elements_in(element, y) for element in x)


def sum_at_depth(x: Union[int, list], y: int) -> int:
    """
    ...
    """
    if isinstance(x, int) and y == 0:
        return x
    return sum(sum_at_depth(num, y - 1) for num in x)


def return_values_with_type(x, y) -> list:
    """
    ...
    """
    if not isinstance(x, list):
        return [x] if isinstance(x, y) else []
    return sum([return_values_with_type(items, y) for items in (x, [])])


def get_max(x: Union[int, list]) -> int:
    """
    ...
    """
    if isinstance(x, int):
        return x
    return max(get_max(items) for items in x)


def get_min(x: Union[int, list]) -> int:
    """
    ...
    """
    if isinstance(x, int):
        return x
    return min(get_min(items) for items in x)


def all_true(x: Union[bool, list]) -> bool:
    """
    ...
    """
    if isinstance(x, bool):
        return x
    return all([all_true(item) for item in x])


def any_true(x: Union[bool, list]) -> bool:
    """
    ...
    """
    if isinstance(x, bool):
        return x
    return any([any_true(item) for item in x])
