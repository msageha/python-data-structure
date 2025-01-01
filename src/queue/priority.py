import heapq


class PriorityQueue:
    """A simple Priority Queue implementation using min-heap via heapq."""

    def __init__(self):
        self._heap = []

    def push(self, item):
        """Push an item onto the priority queue."""
        heapq.heappush(self._heap, item)

    def pop(self):
        """
        Remove and return the smallest item from the priority queue.
        Return None if the queue is empty.
        """
        if self.is_empty():
            return None
        return heapq.heappop(self._heap)

    def top(self):
        """
        Return the smallest item without removing it.
        Return None if the queue is empty.
        """
        if self.is_empty():
            return None
        return self._heap[0]

    def is_empty(self):
        """Check if the priority queue is empty."""
        return len(self._heap) == 0

    def size(self):
        """Return the number of items in the priority queue."""
        return len(self._heap)
