from typing import List


def shade_sort(colour_list: List[str]) -> None:
    """ Put colour_list in order "b" < "g" < "r".

    precondition: colour_list is a List[str] from {"b", "g", "r"}

    >>> list_ = ["r", "b", "g"]
    >>> shade_sort(list_)
    >>> list_ == ["b", "g", "r"]
    True

    postcondition: colour_list has same strings as before, ordered "b" < "g" <
    "r"
    """
    # Hint: blue, green may increase while red decreases.
    #
    # loop invariants:
    #
    # 0 <= blue <= green <= red <= len(colour_list)
    # colour_list[0 : green] + colour_list[red :] same colours as before
    # and all([c == "b" for c in colour_list[0 : blue]])
    # and all([c == "g" for c in colour_list[blue : green]])
    # and all([c == "r" for c in colour_list[red :]])
    blue = 0
    green = 0
    red = len(colour_list)
    for i in range(len(colour_list)):
        if colour_list[i] == "b":
            colour_list[i], colour_list[blue] = \
                colour_list[blue], colour_list[i]
            blue += 1
            green += 1
    j = red - 1
    while j >= green:
        if colour_list[j] == 'r':
            colour_list[j], colour_list[red - 1] =\
                colour_list[red - 1], colour_list[j]
            red -= 1
        j -= 1


def four_shade_sort(colour_list: List[str]) -> None:
    """
    Put colour_List in order "b" < "g" < "r" < "y".

    precondition: colour_list is a List[str] from {"b", "g", "r", "y"}
    """
    # loop invariants:
    #
    # 0 <= blue <= green <= red <= yellow <= len(colour_list)
    # colour_list[0 : green] + colour_list[yellow :] same colours as before
    # and all([c == "b" for c in colour_list[0 : blue]])
    # and all([c == "g" for c in colour_list[blue : green]])
    # and all([c == "r" for c in colour_list[red : yellow]])
    # and all([c == "r" for c in colour_list[yellow :]])
    blue, green, red, yellow = 0, 0, len(colour_list), len(colour_list)
    for i in range(len(colour_list)):
        if colour_list[i] == "b":
            colour_list[i], colour_list[blue] = \
                colour_list[blue], colour_list[i]
            blue += 1
            green += 1
    j = yellow - 1
    while j >= green:
        if colour_list[j] == 'y':
            colour_list[j], colour_list[yellow - 1] = \
                colour_list[yellow - 1], colour_list[j]
            yellow -= 1
            red -= 1
        j -= 1
    p = green
    while p < red:
        if colour_list[p] == 'g':
            colour_list[p], colour_list[green] = \
                colour_list[green], colour_list[p]
            green += 1
        p += 1
