import math
import hashlib


class BloomFilter:
    def __init__(self, capacity, error_rate=0.001):
        self.capacity = capacity
        self.error_rate = error_rate
        self.size = self._optimal_size(capacity, error_rate)
        self.hash_count = self._optimal_hash_count(self.size, capacity)
        self.bit_array = [0] * (self.size)

    def _hashes(self, item):
        md5 = int(hashlib.md5(item.encode("utf-8")).hexdigest(), 16)
        sha1 = int(hashlib.sha1(item.encode("utf-8")).hexdigest(), 16)
        for i in range(self.hash_count):
            yield (md5 + i * sha1) % self.size

    def add(self, item):
        for h in self._hashes(item):
            self.bit_array[h] = 1

    def __contains__(self, item):
        for h in self._hashes(item):
            if self.bit_array[h] == 0:
                return False
        return True

    def _optimal_size(self, n, p):
        return int(-n * math.log(p) / (math.log(2) ** 2))

    def _optimal_hash_count(self, m, n):
        return max(1, int(round(m / n * math.log(2))))
