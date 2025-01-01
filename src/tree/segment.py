class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.size = 1
        while self.size < self.n:
            self.size <<= 1
        self.tree = [0] * (self.size << 1)
        self.lazy = [0] * (self.size << 1)
        for i in range(self.n):
            self.tree[self.size + i] = arr[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[(i << 1) + 1]

    def _apply(self, idx, value, length):
        self.tree[idx] += value * length
        if idx < self.size:
            self.lazy[idx] += value

    def _push_down(self, idx, length):
        if self.lazy[idx] != 0:
            l = idx << 1
            r = l + 1
            mid = length >> 1
            self._apply(l, self.lazy[idx], mid)
            self._apply(r, self.lazy[idx], length - mid)
            self.lazy[idx] = 0

    def _update(self, left, right, value, idx, start, end):
        if left > end or right < start:
            return
        if left <= start and end <= right:
            self._apply(idx, value, end - start + 1)
            return
        self._push_down(idx, end - start + 1)
        mid = (start + end) >> 1
        self._update(left, right, value, idx << 1, start, mid)
        self._update(left, right, value, (idx << 1) + 1, mid + 1, end)
        self.tree[idx] = self.tree[idx << 1] + self.tree[(idx << 1) + 1]

    def update(self, left, right, value):
        self._update(left, right, value, 1, 0, self.size - 1)

    def _query(self, left, right, idx, start, end):
        if left > end or right < start:
            return 0
        if left <= start and end <= right:
            return self.tree[idx]
        self._push_down(idx, end - start + 1)
        mid = (start + end) >> 1
        s1 = self._query(left, right, idx << 1, start, mid)
        s2 = self._query(left, right, (idx << 1) + 1, mid + 1, end)
        return s1 + s2

    def query(self, left, right):
        return self._query(left, right, 1, 0, self.size - 1)
