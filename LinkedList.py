"""链式结构：
    内存不连续，无法下标访问
    """


class Node(object):  # 单链表
    def __init__(self, value=None, next=None) -> None:
        self.value, self.next = value, next

    def __str__(self) -> str:
        return f"<Node: value: {self.value}, next: {self.next}"

    __repr__ = __str__


class LinkedList(object):
    def __init__(self, maxsize=None) -> None:
        self.maxsize = maxsize
        self.root = Node()
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('Full')
        node = Node(value)
        tailnode = self.tail
        if tailnode is None:
            self.root.next = node
        else:
            tailnode.next = node
        self.tail = node
        self.length += 1

    def appendLeft(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('Full')

        headnode = self.root.next
        node = Node(value)
        self.root.next = node
        node.next = headnode
        self.length += 1

    def iter_node(self):
        curnode = self.root.next
        while curnode is not self.tail:
            yield curnode
            curnode = curnode.next
        yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def remove(self, value):
        prevnode = self.root
        curnode = self.root.next
        for curnode in self.iter_node():
            if curnode.value == value:
                prevnode.next = curnode.next
                if curnode is self.tail:  # NOTE: 注意更新 tail
                    self.tail = prevnode
                del curnode
                self.length -= 1
                return 1  # 表明删除成功
            else:  # NOTE: 更新 prevnode
                prevnode = curnode
        return -1  # 表示删除失败

    def find(self, value):
        index = 0
        for node in self.iter_node():
            if node.value == value:
                return index
            index += 1
        return -1

    def popleft(self):  # popleft 抛出headnode
        if self.root.next is None:
            raise Exception('pop from empty linkedlist')
        headnode = self.root.next
        self.root.next = headnode.next
        self.length -= 1
        value = headnode.value
        del headnode
        return value

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None
        self.length = 0


def test_linked_list():
    ll = LinkedList()
    ll.append(0)
    ll.append(1)
    ll.append(2)

    assert len(ll) == 3
    assert ll.find(2) == 2
    assert ll.find(3) == -1

    ll.remove(0)
    assert len(ll) == 2
    assert ll.find(0) == -1

    assert list(ll) == [1, 2]

    ll.appendLeft(0)
    assert list(ll) == [0, 1, 2]
    assert len(ll) == 3

    headvalue = ll.popleft()
    assert headvalue == 0
    assert len(ll) == 2
    assert list(ll) == [1, 2]

    ll.clear()
    assert len(ll) == 0
