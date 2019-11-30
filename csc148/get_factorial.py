from typing import Union, List

def get_factorial(x: int) -> int:
    if x == 1:
        return 1
    return x * get_factorial(x - 1)

def get_max(x: Union[int, List]) -> int:
    if isinstance(x, int):
        return x
    result = []
    for item in x:
        result.append(get_max(item))
    return max(result)

def count_occurrences(x: Union[int, List], value: int) -> int:
    count = 0
    if isinstance(x, int) and x != value:
        return 0
    elif isinstance(x, int) and x == value:
        return 1
    for item in x:
        count = count + count_occurrences(item)
    return count
