"""集合的实现
    """


class Array(object):
    def __init__(self, size=10, init=None):
        self._size = size
        self._items = [init] * size

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


class Slot(object):  # 表示hash数组中的一个槽
    def __init__(self, key, value) -> None:
        self.key, self.value = key, value


class HashTable(object):
    UNUSED = None  # Slot 没有被使用过
    EMPTY = Slot(None, None)  # 使用过被删除

    def __init__(self) -> None:
        self._table = Array(8, init=HashTable.UNUSED)
        self.lenght = 0

    @property
    def _load_factor(self):
        return self.lenght / float(len(self._table))

    def __len__(self):
        return self.lenght

    def _hash(self, key):
        return abs(hash(key)) % len(self._table)

    def _find_key(self, key):
        index = self._hash(key)
        _len = len(self._table)
        while self._table[index] is not HashTable.UNUSED:
            if self._table[index] is HashTable.EMPTY:
                index = (index*5 + 1) % _len  # cpython 使用一种解决hash冲出的方式
                continue
            elif self._table[index].key == key:
                return index
            else:
                index = (index*5 + 1) % _len
        return None

    def _slot_can_insert(self, index):
        return (self._table[index] is HashTable.EMPTY or self._table[index] is HashTable.UNUSED)

    def _find_slot_for_insert(self, key):
        index = self._hash(key)
        _len = len(self._table)
        while not self._slot_can_insert(index):
            index = (index*5 + 1) % _len
        return index

    def __contains__(self, key):
        index = self._find_key(key)
        return index is not None

    def add(self, key, value):
        if key in self:
            index = self._find_key(key)
            self._table[index].value = value
            return False
        else:
            index = self._find_slot_for_insert(key)
            self._table[index] = Slot(key, value)
            self.lenght += 1
            if self._load_factor >= 0.8:
                self._rehash()
            return True

    def _rehash(self):
        old_table = self._table
        newsize = len(self._table) * 2
        self._table = Array(newsize, HashTable.UNUSED)

        for slot in old_table:
            if slot is not HashTable.UNUSED and slot is not HashTable.EMPTY:
                index = self._find_slot_for_insert(slot.key)
                self._table[index] = slot
                self.lenght += 1

    def get(self, key, default=None):
        index = self._find_key(key)
        if index is None:
            return default
        else:
            return self._table[index].value

    def remove(self, key):
        index = self._find_key(key)
        if index is None:
            raise KeyError()
        value = self._table[index].value
        self.lenght -= 1
        self._table[index] = HashTable.EMPTY
        return value

    def __iter__(self):
        for slot in self._table:
            if slot not in (HashTable.EMPTY, HashTable.UNUSED):
                yield slot.key


####################################
# 下面是集合的实现
####################################

class SetADT(HashTable):

    def add(self, key):
        return super(SetADT, self).add(key, True)

    def __and__(self, other_set):
        new_set = SetADT()
        for element_a in self:
            if element_a in other_set:
                new_set.add(element_a)

        # for element_b in other_set:
        #     if element_b in self:
        #         new_set.add(element_b)

        return new_set

    def __sub__(self, other_set):
        new_set = SetADT()
        for element_a in self:
            if element_a not in other_set:
                new_set.add(element_a)

        return new_set

    def __or__(self, other_set):
        new_set = SetADT()
        for element_a in self:
            new_set.add(element_a)

        for element_b in other_set:
            new_set.add(element_b)

        return new_set


def test_setadt():
    sa = SetADT()
    sa.add(1)
    sa.add(2)
    sa.add(3)

    assert 1 in sa

    sb = SetADT()
    sb.add(3)
    sb.add(4)
    sb.add(5)

    assert sorted(list(sa & sb)) == [3]
    assert sorted(list(sa-sb)) == [1, 2]
    assert sorted(list(sa | sb)) == [1, 2, 3, 4, 5]
