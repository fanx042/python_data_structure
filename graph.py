# -*- encoding: utf-8 -*-

"""图的遍历
    BFS: Breadth First Search
    DFS: Depdth First Search
    """
from ast import Starred
from collections import deque
from msilib.schema import Class
import queue

graph = {
    'A': ['B', 'F'],
    'B': ['C', 'I', 'G'],
    'C': ['B', 'I', 'D'],
    'D': ['C', 'I', 'G', 'H', 'E'],
    'E': ['D', 'H', 'F'],
    'F': ['A', 'G', 'E'],
    'G': ['B', 'F', 'H', 'D'],
    'H': ['G', 'D', 'E'],
    'I': ['B', 'C', 'D']
}


class Queue(object):
    def __init__(self) -> None:
        self._deque = deque()

    def push(self, value):
        self._deque.append(value)

    def pop(self):
        return self._deque.popleft()

    def __len__(self):
        return len(self._deque)


def bfs(graph, start):
    search_q = Queue()
    search_q.push(start)

    searched = set()
    while search_q:
        cur_node = search_q.pop()
        if cur_node not in searched:
            print(cur_node)
            searched.add(cur_node)
            for node in graph[cur_node]:
                search_q.push(node)


DFS_SEARCHED = set()


def dfs(graph, start):
    if start not in DFS_SEARCHED:
        print(start)
        DFS_SEARCHED.add(start)

    for node in graph[start]:
        if node not in DFS_SEARCHED:
            dfs(graph, node)


print('dfs:')
dfs(graph, 'A')


print("bfs:")
bfs(graph, 'A')
