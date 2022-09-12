from collections import deque


def fact(n):
    if n == 0:  # 递归出口
        return 1
    else:
        return fact(n-1) * n


def print_num_recu(n):
    if n > 0:
        print(n)
        print_num_recu(n-1)


# print_num_recu(19)


class Stack():
    def __init__(self) -> None:
        self._deque = deque()

    def push(self, value):
        return self._deque.append(value)

    def pop(self):
        return self._deque.pop()

    def is_empty(self):
        return len(self._deque) == 0


# 模拟递归入栈和出栈的操作1
def print_num_use_stack(n):
    s = Stack()
    while n > 0:
        s.push(n)
        n -= 1

    while not s.is_empty():
        print(s.pop())


# print_num_use_stack(10)
# print(fact(10))
