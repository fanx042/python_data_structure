
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


class FullError(Exception):
    pass


class ArrayQueue(object):  # 用数组实现的队列
    def __init__(self, maxsize=None) -> None:
        self.maxsize = maxsize
        self.array = Array(maxsize)
        self.head = 0
        self.tail = 0

    def push(self, value):
        if len(self) >= self.maxsize:
            raise FullError('Queue Full')

        self.array[self.head % self.maxsize] = value
        self.head += 1

    def pop(self):
        value = self.array[self.tail % self.maxsize]
        self.tail += 1
        return value

    def __len__(self):
        return self.head - self.tail


def test_array():
    size = 20
    a = Array(size)

    a[0] = 1
    assert a[0] == 1

    a.clear()
    assert a[0] is None
