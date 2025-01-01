class SuffixArray:
    def __init__(self, s):
        self.s = s
        self.n = len(s)
        self.sa = [i for i in range(self.n)]
        self.rank = [ord(c) for c in s]
        self.temp = [0] * self.n
        k = 1
        while k < self.n:
            self.sa.sort(
                key=lambda x: (self.rank[x], self.rank[x + k] if x + k < self.n else -1)
            )
            self.temp[self.sa[0]] = 0
            for i in range(1, self.n):
                self.temp[self.sa[i]] = self.temp[self.sa[i - 1]]
                if (
                    self.rank[self.sa[i]],
                    self.rank[self.sa[i] + k] if self.sa[i] + k < self.n else -1,
                ) > (
                    self.rank[self.sa[i - 1]],
                    self.rank[self.sa[i - 1] + k]
                    if self.sa[i - 1] + k < self.n
                    else -1,
                ):
                    self.temp[self.sa[i]] += 1
            self.rank, self.temp = self.temp, self.rank
            k <<= 1
            if self.rank[self.sa[-1]] == self.n - 1:
                break

    def search(self, pattern):
        left, right = 0, self.n
        while left < right:
            mid = (left + right) // 2
            if self.s[self.sa[mid] :].startswith(pattern):
                right = mid
            elif self.s[self.sa[mid] :] < pattern:
                left = mid + 1
            else:
                right = mid
        start = left
        left, right = 0, self.n
        while left < right:
            mid = (left + right) // 2
            if pattern < self.s[self.sa[mid] : self.sa[mid] + len(pattern)]:
                right = mid
            else:
                left = mid + 1
        return range(start, left)
