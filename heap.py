# -*- coding: UTF-8 -*-
"""堆与堆排序
    """
"""
    最大堆，对于每个非叶子节点V，V的值都比他的两个孩子大。称为最大堆特性。最大堆
    里的根总是存储最大值，最小的值存储在叶节点。
    最小堆：和最大堆相反，每个非叶子节点V的孩子节点的值都比他大。
    """
'''
    由于完全二叉树的特点，树不会有间隙。对于数组里的一个下表i,我们可以得到它的父亲和
    孩子节点对应的下标
'''

'''
parent = int((i-1) / 2)
left = 2*i + 1
right = 2*i + 2
'''

##################################
# 最大堆的实现
##################################


class Array(object):
    def __init__(self, size=10):
        self._size = size
        self._items = [None] * size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item


class MaxHeap(object):
    def __init__(self, maxsize=None) -> None:
        self.maxsize = maxsize
        self._elements = Array(maxsize)
        self._count = 0

    def __len__(self):
        return self._count

    def add(self, value):
        if self._count >= self.maxsize:
            raise Exception('full')

        self._elements[self._count] = value
        self._count += 1
        self._siftup(self._count-1)

    def _siftup(self, idx):
        if idx > 0:
            parent = int((idx-1)/2)
            if self._elements[idx] > self._elements[parent]:
                self._elements[idx], self._elements[parent] = self._elements[parent], self._elements[idx]
                self._siftup(parent)

    def extract(self):
        if self._count <= 0:
            raise Exception('empty')

        value = self._elements[0]
        #! original step:
        self._count -= 1
        self._elements[0] = self._elements[self._count]
        self._siftdown(0)
        return value

    def _siftdown(self, ndx):
        left = 2 * ndx + 1
        right = 2 * ndx + 2
        largest = ndx

        if (left < self._count and  # ! 有左孩子
            self._elements[left] > self._elements[largest] and
                self._elements[left] >= self._elements[right]):  # ! 左孩子 > 右孩子
            largest = left
        elif right < self._count and self._elements[right] >= self._elements[largest]:
            largest = right

        if largest != ndx:
            self._elements[ndx], self._elements[largest] = self._elements[largest], self._elements[ndx]
            self._siftdown(largest)


def test_heap():
    n = 5
    h = MaxHeap(n)
    for i in range(n):
        h.add(i)
    # print(h._elements._items)
    for i in reversed(range(n)):
        print(i)
        assert i == h.extract()
        # print(h._elements._items)


test_heap()
