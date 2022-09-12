

class BinTreeNode(object):
    def __init__(self, data, left=None, right=None) -> None:
        self.data, self.left, self.right = data, left, right


class BinTree(object):
    def __init__(self, root=None) -> None:
        self.root = root

    @classmethod
    def build_from(cls, node_list):
        node_dict = {}
        for node_data in node_list:
            data = node_data['data']
            node_dict[data] = BinTreeNode(data)  # 把所有的节点都赋值成一个bintree节点

        for node_data in node_list:
            data = node_data['data']
            node = node_dict[data]
            if node_data['is_root']:
                root = node
            node.left = node_dict.get(node_data['left'])
            node.right = node_dict.get(node_data['right'])

        return cls(root)

    def preorder_trav(self, subtree):
        """先序遍历

        Args:
            subtree (BinTree):
        """
        if subtree is not None:
            print(subtree.data)  # 递归函数里先处理根
            self.preorder_trav(subtree.left)  # 递归处理左子树
            self.preorder_trav(subtree.right)  # 递归处理右子树

    def inorder_trav(self, subtree):
        """中序遍历

        Args:
            subtree (_type_):
        """
        if subtree is not None:
            self.inorder_trav(subtree.left)
            print(subtree.data)
            self.inorder_trav(subtree.right)

    def postorder_trav(self, subtree):
        """后序遍历

        Args:
            subtree (BinTree):
        """
        if subtree is not None:
            self.postorder_trav(subtree.left)
            self.postorder_trav(subtree.right)
            print(subtree.data)

    def reverse(self, subtree):
        if subtree is not None:
            subtree.left, subtree.right = subtree.right, subtree.left
            self.reverse(subtree.left)
            self.reverse(subtree.right)


node_list = [
    {'data': 'A', 'left': 'B', 'right': 'C', 'is_root': True},
    {'data': 'B', 'left': 'D', 'right': 'E', 'is_root': False},
    {'data': 'D', 'left': None, 'right': None, 'is_root': False},
    {'data': 'E', 'left': 'H', 'right': None, 'is_root': False},
    {'data': 'H', 'left': None, 'right': None, 'is_root': False},
    {'data': 'C', 'left': 'F', 'right': 'G', 'is_root': False},
    {'data': 'F', 'left': None, 'right': None, 'is_root': False},
    {'data': 'G', 'left': 'I', 'right': 'J', 'is_root': False},
    {'data': 'I', 'left': None, 'right': None, 'is_root': False},
    {'data': 'J', 'left': None, 'right': None, 'is_root': False}
]

btree = BinTree.build_from(node_list)
btree.preorder_trav(btree.root)
