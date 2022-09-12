
from LinkedList import Node, LinkedList


class FullError(Exception):
    pass


class EmptyError(Exception):
    pass


class Queue(object):
    def __init__(self, maxsize=None) -> None:
        self.maxsize = maxsize
        self._item_linked_list = LinkedList()

    def __len__(self):
        return (len(self._item_linked_list))

    def push(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise FullError('Queue Full')

        return self._item_linked_list.append(value)

    def pop(self):
        if len(self) == 0:
            raise EmptyError('Queue Empty')

        return self._item_linked_list.popleft()


class DeQueue(object):
    def __init__(self, maxsize=None) -> None:
        self.maxsize = maxsize


def test_queue():
    q = Queue()
    q.push(0)
    q.push(1)
    q.push(2)

    assert len(q) == 3

    assert q.pop() == 0
    assert q.pop() == 1
    assert q.pop() == 2
