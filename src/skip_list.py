import random


class SkipListNode:
    def __init__(self, key, level):
        self.key = key
        self.forward = [None] * (level + 1)


class SkipList:
    def __init__(self, maxLevel=16, p=0.5):
        self.maxLevel = maxLevel
        self.p = p
        self.level = 0
        self.header = SkipListNode(-float("inf"), self.maxLevel)

    def randomLevel(self):
        lvl = 0
        while random.random() < self.p and lvl < self.maxLevel:
            lvl += 1
        return lvl

    def search(self, key):
        current = self.header
        for i in reversed(range(self.level + 1)):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
        current = current.forward[0]
        if current and current.key == key:
            return True
        return False

    def insert(self, key):
        update = [None] * (self.maxLevel + 1)
        current = self.header
        for i in reversed(range(self.level + 1)):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current
        current = current.forward[0]
        if current and current.key == key:
            return
        lvl = self.randomLevel()
        if lvl > self.level:
            for i in range(self.level + 1, lvl + 1):
                update[i] = self.header
            self.level = lvl
        n = SkipListNode(key, lvl)
        for i in range(lvl + 1):
            n.forward[i] = update[i].forward[i]
            update[i].forward[i] = n

    def remove(self, key):
        update = [None] * (self.maxLevel + 1)
        current = self.header
        for i in reversed(range(self.level + 1)):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current
        current = current.forward[0]
        if current and current.key == key:
            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]
            while self.level > 0 and self.header.forward[self.level] is None:
                self.level -= 1
