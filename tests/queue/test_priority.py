import unittest
from src.queue.priority import PriorityQueue


class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.pq = PriorityQueue()

    def test_push_and_pop(self):
        self.pq.push(5)
        self.pq.push(3)
        self.pq.push(8)
        self.pq.push(1)
        self.assertEqual(self.pq.pop(), 1)
        self.assertEqual(self.pq.pop(), 3)
        self.assertEqual(self.pq.pop(), 5)
        self.assertEqual(self.pq.pop(), 8)
        self.assertIsNone(self.pq.pop())

    def test_top(self):
        self.pq.push(10)
        self.pq.push(4)
        self.assertEqual(self.pq.top(), 4)
        self.assertEqual(self.pq.pop(), 4)
        self.assertEqual(self.pq.top(), 10)
        self.pq.pop()
        self.assertIsNone(self.pq.top())

    def test_is_empty_and_size(self):
        self.assertTrue(self.pq.is_empty())
        self.assertEqual(self.pq.size(), 0)
        self.pq.push(2)
        self.pq.push(7)
        self.assertFalse(self.pq.is_empty())
        self.assertEqual(self.pq.size(), 2)
        self.pq.pop()
        self.assertEqual(self.pq.size(), 1)


if __name__ == "__main__":
    unittest.main(argv=[""], verbosity=2, exit=False)
