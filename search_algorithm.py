"""线性查找与二分查找
"""

number_list = [0, 1, 2, 3, 4, 5, 6, 7]


def linear_search(value, iterable):
    for index, val in enumerate(iterable):
        if val == value:
            return index

    return -1


def linear_search_v2(predicate, iterable):
    for index, val in enumerate(iterable):
        if predicate(val):
            return index

    return -1


assert linear_search_v2(lambda x: x == 3, number_list) == 3


def linear_saerch_recusive(array, value):
    if len(array) == 0:
        return -1
    index = len(array) - 1
    if array[index] == value:
        return index
    return linear_saerch_recusive(array[:index], value)


assert linear_saerch_recusive(number_list, 2) == 2
assert linear_saerch_recusive(number_list, -1) == -1


# 二分查找
def binary_search(sorted_array, value):
    if sorted_array is None:
        return -1

    begin = 0
    end = len(sorted_array) - 1

    while begin <= end:
        mid = int((begin + end) / 2)
        if sorted_array[mid] == value:
            return mid
        elif sorted_array[mid] > value:
            end = mid - 1
        else:
            begin = begin + 1

    return -1


def test_binary_search():
    a = list(range(10))

    assert binary_search(a, 2) == 2
    assert binary_search(a, 11) == -1
