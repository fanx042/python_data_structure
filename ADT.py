
from array import array


class Bag(object):
    def __init__(self, maxsize=50) -> None:
        self.maxsize = maxsize
        self._items = list()

    def add(self, item):
        if len(self) > self.maxsize:
            raise Exception("Bag is Full")
        self._items.append(item)

    def remove(self, item):
        self._items.remove(item)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        for item in self._items:
            yield item


def test_bag():
    bag = Bag()
    bag.add(1)
    bag.add(2)
    bag.add(3)

    assert len(bag) == 3

    bag.remove(3)
    assert len(bag) == 2

    for i in bag:
        print(i)


test_bag()


"""
线性结构：内存连续和下标访问
"""

arr = array('u', 'asdf')

print(arr[0], arr[1])

'''
单一数据类型
'''
