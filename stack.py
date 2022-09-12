
'''双端循环链表
'''


class Node(object):
    def __init__(self, value=None, prev=None, next=None):
        self.prev, self.value, self.next = prev, value, next


class CircualDoubleLinkedList(object):
    def __init__(self, maxsize=None) -> None:
        self.maxsize = maxsize
        node = Node()
        node.next, node.prev = node, node
        self.root = node
        self.length = 0

    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev

    def append(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('Full')

        node = Node(value)
        tailnode = self.tailnode()

        tailnode.next = node
        node.prev = tailnode

        node.next = self.root
        self.root.prev = node
        self.length += 1

    def appendleft(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('Full')

        node = Node(value)
        if self.root.next is self.root:  # empty
            node.mext = self.root
            node.prev = self.root
            self.root.next = node
            self.root.prev = node
        else:
            node.prev = self.root
            headnode = self.root.next
            node.next = headnode
            headnode.prev = node
            self.root.next = node
        self.length += 1

    def remove(self, node):  # node is not value
        if node is self.root:
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1
        return node

    def iter_node(self):
        if self.root.next == self.root:
            return
        curnode = self.root.next
        while curnode.next is not self.root:
            yield curnode
            curnode = curnode.next
        yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node_reverse(self):
        if self.root.prev is self.root:
            return
        curnode = self.root.prev
        while curnode.prev is not self.root:
            yield curnode
            curnode = curnode.prev
        yield curnode

####################################################
# 分割线，下面是栈的实现
####################################################


class Deque(CircualDoubleLinkedList):
    def pop(self):
        if len(self) == 0:
            raise Exception('empty')

        tailnode = self.tailnode()
        value = tailnode.value
        self.remove(tailnode)
        return value

    def popleft(self):
        if len(self) == 0:
            raise Exception('empty')

        headnode = self.headnode()
        value = headnode.value()
        self.remove(headnode)
        return value


class Stack(object):
    def __init__(self) -> None:
        self.deque = Deque()

    def push(self, value):
        return self.deque.append(value)

    def pop(self):
        return self.deque.pop()

    def __len__(self):
        return len(self.deque)

    def is_empty(self):
        return len(self) == 0


def test_stakc():
    s = Stack()
    s.push(0)
    s.push(1)
    s.push(2)

    assert len(s) == 3
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.pop() == 0

    assert s.is_empty()
