class Deque:
    def __init__(self):
        self._items = []

    def push_front(self, item):
        self._items.insert(0, item)

    def push_back(self, item):
        self._items.append(item)

    def pop_front(self):
        if self.is_empty():
            return None
        return self._items.pop(0)

    def pop_back(self):
        if self.is_empty():
            return None
        return self._items.pop()

    def front(self):
        if self.is_empty():
            return None
        return self._items[0]

    def back(self):
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)
