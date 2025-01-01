import unittest
from src.queue import Queue


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue_and_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 3)
        self.assertIsNone(self.queue.dequeue())  # Empty queue -> None

    def test_front(self):
        self.queue.enqueue("x")
        self.assertEqual(self.queue.front(), "x")
        self.queue.enqueue("y")
        self.assertEqual(self.queue.front(), "x")  # front remains 'x'
        self.queue.dequeue()
        self.assertEqual(self.queue.front(), "y")

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(10)
        self.assertFalse(self.queue.is_empty())

    def test_size(self):
        self.assertEqual(self.queue.size(), 0)
        self.queue.enqueue("a")
        self.queue.enqueue("b")
        self.assertEqual(self.queue.size(), 2)
        self.queue.dequeue()
        self.assertEqual(self.queue.size(), 1)


if __name__ == "__main__":
    unittest.main(argv=[""], verbosity=2, exit=False)
