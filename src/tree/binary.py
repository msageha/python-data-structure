class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_level_order(self, arr):
        if not arr:
            return

        nodes = [BinaryTreeNode(val) if val is not None else None for val in arr]

        for i in range(len(nodes)):
            if nodes[i] is not None:
                left_index = 2 * i + 1
                right_index = 2 * i + 2
                if left_index < len(nodes):
                    nodes[i].left = nodes[left_index]
                if right_index < len(nodes):
                    nodes[i].right = nodes[right_index]

        self.root = nodes[0]

    def preorder_traversal(self):
        result = []

        def dfs(node):
            if node is not None:
                result.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(self.root)
        return result
