class BinarySearchTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = BinarySearchTreeNode(val)
            return

        current = self.root
        while True:
            if val < current.val:
                if current.left is None:
                    current.left = BinarySearchTreeNode(val)
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = BinarySearchTreeNode(val)
                    break
                current = current.right

    def search(self, val):
        current = self.root
        while current:
            if current.val == val:
                return True
            elif val < current.val:
                current = current.left
            else:
                current = current.right
        return False

    def remove(self, val):
        self.root, deleted = self._remove_rec(self.root, val)
        return deleted

    def _remove_rec(self, node, val):
        if node is None:
            return node, False

        if val < node.val:
            node.left, deleted = self._remove_rec(node.left, val)
        elif val > node.val:
            node.right, deleted = self._remove_rec(node.right, val)
        else:
            deleted = True
            if node.left is None:
                return node.right, True
            elif node.right is None:
                return node.left, True
            else:
                min_node = self._find_min(node.right)
                node.val = min_node.val
                node.right, _ = self._remove_rec(node.right, min_node.val)

        return node, deleted

    def _find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def inorder_traversal(self):
        result = []

        def dfs(n):
            if n is not None:
                dfs(n.left)
                result.append(n.val)
                dfs(n.right)

        dfs(self.root)
        return result
