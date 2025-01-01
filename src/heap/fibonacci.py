import math


class FibNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.mark = False
        self.parent = None
        self.child = None
        self.left = self
        self.right = self

    def __repr__(self):
        return f"FibNode(key={self.key})"


class FibonacciHeap:
    def __init__(self):
        self.min = None
        self.n = 0

    def insert(self, key):
        node = FibNode(key)
        self._add_root_list(node)
        if self.min is None or node.key < self.min.key:
            self.min = node
        self.n += 1
        return node

    def find_min(self):
        return self.min

    def extract_min(self):
        z = self.min
        if z is not None:
            if z.child is not None:
                children = []
                c = z.child
                while True:
                    children.append(c)
                    c.parent = None
                    c = c.right
                    if c == z.child:
                        break
                for child in children:
                    self._add_root_list(child)
                z.child = None

            self._remove_root_list(z)
            if z == z.right:
                self.min = None
            else:
                self.min = z.right
                self._consolidate()
            self.n -= 1
        return z

    def union(self, other_heap):
        if other_heap.min is None:
            return
        if self.min is None:
            self.min = other_heap.min
            self.n = other_heap.n
        else:
            self._concatenate_root_lists(self.min, other_heap.min)
            if other_heap.min.key < self.min.key:
                self.min = other_heap.min
            self.n += other_heap.n

    def _add_root_list(self, node):
        if self.min is None:
            node.left = node
            node.right = node
        else:
            node.left = self.min.left
            node.right = self.min
            self.min.left.right = node
            self.min.left = node

    def _remove_root_list(self, node):
        if node.right == node:
            pass
        else:
            node.left.right = node.right
            node.right.left = node.left

    def _concatenate_root_lists(self, a, b):
        a_left = a.left
        b_left = b.left
        a.left = b_left
        b_left.right = a
        b.left = a_left
        a_left.right = b

    def _consolidate(self):
        array_size = int(math.log2(self.n)) + 2 if self.n > 0 else 1
        A = [None] * array_size

        root_list_nodes = []
        current = self.min
        if current is not None:
            while True:
                root_list_nodes.append(current)
                current = current.right
                if current == self.min:
                    break

        for w in root_list_nodes:
            x = w
            d = x.degree
            while A[d] is not None:
                y = A[d]
                if y.key < x.key:
                    x, y = y, x
                self._link(y, x)
                A[d] = None
                d += 1
            A[d] = x

        self.min = None
        for i in range(len(A)):
            if A[i] is not None:
                if self.min is None:
                    self.min = A[i]
                    self.min.left = self.min
                    self.min.right = self.min
                else:
                    self._add_root_list(A[i])
                    if A[i].key < self.min.key:
                        self.min = A[i]

    def _link(self, y, x):
        self._remove_root_list(y)
        y.parent = x
        if x.child is None:
            x.child = y
            y.left = y
            y.right = y
        else:
            y.left = x.child.left
            y.right = x.child
            x.child.left.right = y
            x.child.left = y
        x.degree += 1
        y.mark = False
