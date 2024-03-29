"""Given already-sorted lists, `a` and `b`, return sorted list of both.

You may not use sorted() or .sort().

Check edge cases of empty lists:

    >>> sort_ab([], [])
    []

    >>> sort_ab([1, 2,3], [])
    [1, 2, 3]

    >>> sort_ab([], [1, 2, 3])
    [1, 2, 3]

Check:

    >>> sort_ab([1, 3, 5, 7], [2, 6, 8, 10])
    [1, 2, 3, 5, 6, 7, 8, 10]
"""


def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().
    """

    new_list = []

    ia = 0
    ib = 0

    for num in a:
        if num < b[ib]:
            ia += 1
            new_list.append(num)
        elif num == b[ib]:
            new_list.append(num)
            new_list.append(num)
            ia += 1
            ib += 1
        else:
            new_list.append(b[ib])
            ib += 1


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE A MERGE CHAMPION!!\n")
