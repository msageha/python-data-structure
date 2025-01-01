class BinomialNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.sibling = None

    def __repr__(self):
        return f"BinomialNode(key={self.key}, deg={self.degree})"


class BinomialHeap:
    def __init__(self):
        self.head = None

    def insert(self, key):
        temp_heap = BinomialHeap()
        node = BinomialNode(key)
        temp_heap.head = node
        self.union(temp_heap)

    def find_min(self):
        if self.head is None:
            return None
        y = None
        x = self.head
        min_val = float("inf")
        while x is not None:
            if x.key < min_val:
                min_val = x.key
                y = x
            x = x.sibling
        return y

    def extract_min(self):
        if self.head is None:
            return None
        prev_x = None
        x = self.head
        min_x = x
        prev_min_x = None
        min_val = x.key

        while x is not None:
            if x.key < min_val:
                min_val = x.key
                min_x = x
                prev_min_x = prev_x
            prev_x = x
            x = x.sibling

        if prev_min_x is None:
            self.head = min_x.sibling
        else:
            prev_min_x.sibling = min_x.sibling

        child = min_x.child
        while child is not None:
            next_child = child.sibling
            child.sibling = None
            child.parent = None
            child.sibling = self.head
            self.head = child
            child = next_child

        return min_x

    def union(self, other_heap):
        self._merge_root_lists(other_heap)
        if self.head is None:
            return
        prev_x = None
        x = self.head
        next_x = x.sibling
        while next_x is not None:
            if x.degree != next_x.degree or (
                next_x.sibling is not None and next_x.sibling.degree == x.degree
            ):
                prev_x = x
                x = next_x
            else:
                if x.key <= next_x.key:
                    x.sibling = next_x.sibling
                    self._link(next_x, x)
                else:
                    if prev_x is None:
                        self.head = next_x
                    else:
                        prev_x.sibling = next_x
                    self._link(x, next_x)
                    x = next_x
            next_x = x.sibling

    def _merge_root_lists(self, other_heap):
        self.head = self._merge_lists(self.head, other_heap.head)
        other_heap.head = None

    def _merge_lists(self, h1, h2):
        if h1 is None:
            return h2
        if h2 is None:
            return h1
        head = None
        tail = None

        while h1 and h2:
            if h1.degree <= h2.degree:
                if head is None:
                    head = h1
                    tail = h1
                else:
                    tail.sibling = h1
                    tail = h1
                h1 = h1.sibling
            else:
                if head is None:
                    head = h2
                    tail = h2
                else:
                    tail.sibling = h2
                    tail = h2
                h2 = h2.sibling

        if h1 is not None:
            if tail is None:
                head = h1
            else:
                tail.sibling = h1
        else:
            if tail is None:
                head = h2
            else:
                tail.sibling = h2
        return head

    def _link(self, y, x):
        y.parent = x
        y.sibling = x.child
        x.child = y
        x.degree += 1
