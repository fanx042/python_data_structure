# -*- encoding: utf-8 -*-

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

##########################################
# Priority Queue
##########################################


class PriorityQueue(object):
    def __init__(self, maxsize) -> None:
        self.maxsize = maxsize
        self._maxheap = MaxHeap(maxsize)

    def push(self, priority, value):
        entry = (priority, value)
        self._maxheap.add(entry)

    def pop(self, with_priority=False):
        entry = self._maxheap.extract()
        if with_priority:
            return entry   # return a tuple
        else:
            return entry[-1]

    def is_empty(self):
        return len(self._maxheap) == 0


def test_priority_queue():
    size = 5
    pq = PriorityQueue(size)
    pq.push(5, 'purple')
    pq.push(0, 'white')
    pq.push(3, 'organge')
    pq.push(1, 'black')

    res = []
    while not pq.is_empty():
        res.append(pq.pop())

    assert res == ['purple', 'organge', 'black', 'white']
