class CartesianTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class CartesianTree:
    def __init__(self, arr):
        self.root = self._build(arr)

    def _build(self, arr):
        stack = []
        for x in arr:
            node = CartesianTreeNode(x)
            last = None
            while stack and stack[-1].value > x:
                last = stack.pop()
            node.left = last
            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0] if stack else None

    def inorder(self):
        r = []

        def dfs(n):
            if n:
                dfs(n.left)
                r.append(n.value)
                dfs(n.right)

        dfs(self.root)
        return r

    def find_min(self):
        return self.root.value if self.root else None
