from itertools import chain, combinations
from typing import List


def power_set(iterable):
    """
    ...
    """
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s) + 1))


"""def closure(elems, fds):
    
    Find closure for given functional dependencies.
    Args:
        elems <list>            Elements in question for closure
        fds <list of tuples>    Tuples of x -> b in form ([x1,x2,x3], [y1,y2])
    Returns:
        set of elements under closure.
    
    unused = set(fds)
    closures = set(elems)
    for i in range(0, len(fds)):
        if fds[i % len(fds)][0] in closure:
            unused.remove(fds[i % len(fds)])
            closures.add(fds[i % len(fds)][1])

    return closures"""


def fd_projector(attributes: List[str], fds: dict) -> dict:
    """
    ...
    """
    to_ret = dict()
    all_combinations = list(power_set(attributes))
    list_of_str = []
    for combination in all_combinations:
        current_str = ''
        for character in combination:
            current_str += character
        list_of_str.append(current_str)

    for str in list_of_str:
        closure = ''

    return to_ret
