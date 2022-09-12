from operator import truediv
import random
from wsgiref.validate import PartialIteratorWrapper


def bubble_sort(seq):
    n = len(seq)
    for i in range(n-1):
        print(seq)
        for j in range(n-1-i):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]

        print(seq)


def select_sort(seq):
    n = len(seq)
    for i in range(n-1):
        print(seq)
        min_idx = i
        for j in range(i+1, n):
            if seq[j] < seq[min_idx]:
                min_idx = j
        if min_idx != i:
            seq[min_idx], seq[i] = seq[i], seq[min_idx]

    print(seq)


def insertion_sort(seq):
    n = len(seq)
    for i in range(1, n):
        print(seq)
        value = seq[i]
        pos = i
        while pos > 0 and value < seq[pos-1]:
            seq[pos] = seq[pos-1]
            pos -= 1
        seq[pos] = value
    print(seq)


def merge_sort(seq):
    if len(seq) <= 1:
        return seq
    else:
        mid = int(len(seq) / 2)
        left_half = merge_sort(seq[:mid])
        right_half = merge_sort(seq[mid:])
        new_seq = merge_sorted_list(left_half, right_half)
        return new_seq


def merge_sorted_list(sorted_a, sorted_b):
    len_a, len_b = len(sorted_a), len(sorted_b)
    a = b = 0
    new_sorted_list = list()

    while a < len_a and b < len_b:
        if sorted_a[a] < sorted_b[b]:
            new_sorted_list.append(sorted_a[a])
            a += 1
        else:
            new_sorted_list.append(sorted_b[b])
            b += 1

    while a < len_a:
        new_sorted_list.append(sorted_a[a])
        a += 1

    while b < len_b:
        new_sorted_list.append(sorted_b[b])
        b += 1

    return new_sorted_list


#! quick sort
def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot_index = 0
        pivot = array[pivot_index]
        less_part = [i for i in array[pivot_index+1:] if i <= pivot]
        great_part = [i for i in array[pivot_index+1:] if i > pivot]
        return quick_sort(less_part) + [pivot] + quick_sort(great_part)


def partition(array, beg, end):
    pivot_index = beg
    pivot = array[pivot_index]

    left = pivot_index + 1
    right = end - 1

    while True:
        while left <= right and array[left] < pivot:
            left += 1
        while right >= left and array[right] > pivot:
            right -= 1

        if left > right:
            break
        else:
            array[left], array[right] = array[right], array[left]

    array[pivot_index], array[right] = array[right], array[pivot_index]
    return right


def quick_sort_inplace(array, beg, end):
    if beg < end:
        pivot = partition(array, beg, end)
        quick_sort_inplace(array, beg, pivot)
        quick_sort_inplace(array, pivot+1, end)


################################################
# test
################################################


def test_quick_sort():
    seq = list(range(10))
    random.shuffle(seq)
    print(quick_sort(seq))


def test_merge_sort():
    seq = list(range(10))
    random.shuffle(seq)
    print(seq)
    print(merge_sort(seq))


def test_select_sort():
    seq = list(range(10))
    random.shuffle(seq)
    select_sort(seq)


def test_bubble_sort():
    seq = list(range(10))
    random.shuffle(seq)
    bubble_sort(seq)


def test_insertion_sort():
    seq = list(range(10))
    random.shuffle(seq)
    insertion_sort(seq)


def test_partition():
    l = [4, 3, 63, 2]
    assert partition(l, 0, len(l)) == 2
    l = [1, 2, 3, 4]
    assert partition(l, 0, len(l)) == 0


def test_quick_sort_inplace():
    seq = list(range(10))
    random.shuffle(seq)
    print(seq)
    quick_sort_inplace(seq, 0, len(seq))
    print(seq)


test_quick_sort_inplace()
