"""二叉查找树:BST
每一个节点包含一个key和他附带的数据，对于每个内部节点V，
所有key小于V的都存储在V的左子树；
所有key大于V的都存储在V的右子树；
如果中序遍历这颗二叉树，输出的顺序正好是有序的；
"""


class BSTnode(object):
    def __init__(self, key, value, left=None, right=None) -> None:
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BST(object):
    def __init__(self, root=None) -> None:
        self.root = root

    @classmethod
    def build_from(cls, node_list):
        cls.size = 0
        key_to_node_dict = {}
        for node_dict in node_list:
            key = node_dict['key']
            key_to_node_dict[key] = BSTnode(key, value=key)  # ! 这里的值暂时和key一致

        for node_dict in node_list:
            key = node_dict['key']
            node = key_to_node_dict[key]
            if node_dict['is_root']:
                root = node
            node.left = key_to_node_dict.get(node_dict['left'])
            node.right = key_to_node_dict.get(node_dict['right'])
            cls.size += 1
        return cls(root)

    def _bst_search(self, subtree, key):
        if subtree is None:
            return None
        elif key < subtree.key:
            return self._bst_search(subtree.left, key)
        elif key > subtree.key:
            return self._bst_search(subtree.right, key)
        else:
            return subtree

    def get(self, key, default=None):
        node = self._bst_search(self.root, key)
        if node is None:
            return default
        else:
            return node.value

    def __contains__(self, key):
        return self._bst_search(self.root, key) is not None

    def _bst_min_node(self, subtree):
        if subtree is None:
            return None
        elif subtree.left is None:  # 找到了左子树的尽头
            return subtree
        else:
            return self._bst_min_node(subtree.left)

    def bst_min(self):
        node = self._bst_min_node(self.root)
        return node.value if node else None

    def _bst_insert(self, subtree, key, value):
        """插入并且返回根节点
        """
        if subtree is None:
            subtree = BSTnode(key, value)
        elif key < subtree.key:
            subtree.left = self._bst_insert(subtree.left, key, value)
        elif key > subtree.key:
            subtree.right = self._bst_insert(subtree.right, key, value)
        return subtree

    def add(self, key, value):
        node = self._bst_search(self.root, key)
        if node is not None:
            node.value = value
            return False
        else:
            self.root = self._bst_insert(self.root, key, value)
            self.size += 1
            return True

    #! 二叉查找树节点的删除
    #! 逻辑前任与逻辑后任，表示该节点的前一个节点和后一个节点
    def _bst_delete(self, subtree, key):
        if subtree is None:
            return None
        elif key < subtree.key:
            subtree.left = self._bst_delete(subtree.left, key)
            return subtree
        elif key > subtree.key:
            subtree.right = self._bst_delete(subtree.right, key)
        else:  # 找到了要删除的节点
            if subtree.left is None and subtree.right is None:  # 叶子节点
                return None
            elif subtree.left is None or subtree.right is None:
                if subtree.left is not None:
                    return subtree.left  # 返回孩子节点，并且让他的父亲节点指过去
                else:
                    return subtree.right
            else:  # 两孩子，寻找后继节点并替换
                successor_node = self._bst_min_node(subtree.right)
                subtree.key, subtree.value = successor_node.key, successor_node.value
                subtree.right = self._bst_delete(subtree.right, key)
                return subtree

    def remove(self, key):
        assert key in self
        self.size -= 1
        return self._bst_delete(self.root, key)


node_list = [
    {'key': 60, 'left': 12, 'right': 90, 'is_root': True},
    {'key': 12, 'left': 4, 'right': 41, 'is_root': False},
    {'key': 4, 'left': 1, 'right': None, 'is_root': False},
    {'key': 1, 'left': None, 'right': None, 'is_root': False},
    {'key': 41, 'left': 29, 'right': None, 'is_root': False},
    {'key': 29, 'left': 23, 'right': 37, 'is_root': False},
    {'key': 23, 'left': None, 'right': None, 'is_root': False},
    {'key': 37, 'left': None, 'right': None, 'is_root': False},
    {'key': 90, 'left': 71, 'right': 100, 'is_root': False},
    {'key': 71, 'left': None, 'right': 84, 'is_root': False},
    {'key': 100, 'left': None, 'right': None, 'is_root': False},
    {'key': 84, 'left': None, 'right': None, 'is_root': False},
]


def test_bst():
    bst = BST.build_from(node_list)
    for node_dict in node_list:
        key = node_dict['key']
        assert bst.get(key) == key

    assert bst.size == len(node_list)

    assert bst.get(-1) == None
    assert bst.bst_min() == 1

    bst.add(0, 0)
    assert bst.bst_min() == 0

    bst.remove(12)
    assert bst.get(12) is None

    bst.remove(1)
    assert bst.get(1) is None

    bst.remove(29)
    assert bst.get(29) is None
