from typing import List

def shade_sort(colour_list: List[str]):
    """ Put colour_list in order "b" < "g" < "r".

    precondition: colour_list is a List[str] from {"b", "g", "r"}

    >>> list_ = ["r", "b", "g"]
    >>> shade_sort(list_)
    >>> list_ == ["b", "g", "r"]
    True

    postcondition: colour_list has same strings as before, ordered "b" < "g" < "r"
    """
    # TODO: initialize blue, green, red to be consistent with loop invariants.
    # Hint: blue, green may increase while red decreases.
    #
    # loop invariants:
    #
    # 0 <= blue <= green <= red <= len(colour_list)
    # colour_list[0 : green] + colour_list[red :] same colours as before
    # and all([c == "b" for c in colour_list[0 : blue]])
    # and all([c == "g" for c in colour_list[blue : green]])
    # and all([c == "r" for c in colour_list[red :]])
    #
    # TODO: implement loop using invariants above!
    l = colour_list
    blue = 0
    green = 0
    red = len(l)
    now = 0
    while green < red:
        last = red - 1
        if l[now] == 'b':
            l[now], l[blue] = l[blue], l[now]
            now += 1
            blue += 1
            green += 1
        elif l[now] == 'r':
            if l[last] == 'r':
                red -= 1
            l[last], l[now] = l[now], l[last]
        else:
            now += 1
            green += 1
            