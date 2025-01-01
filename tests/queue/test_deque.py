import unittest
from src.queue.deque import Deque


class TestDeque(unittest.TestCase):
    def setUp(self):
        self.deque = Deque()

    def test_push_front_and_pop_front(self):
        self.deque.push_front(1)
        self.deque.push_front(2)
        self.deque.push_front(3)
        self.assertEqual(self.deque.pop_front(), 3)
        self.assertEqual(self.deque.pop_front(), 2)
        self.assertEqual(self.deque.pop_front(), 1)
        self.assertIsNone(self.deque.pop_front())

    def test_push_back_and_pop_back(self):
        self.deque.push_back(1)
        self.deque.push_back(2)
        self.deque.push_back(3)
        self.assertEqual(self.deque.pop_back(), 3)
        self.assertEqual(self.deque.pop_back(), 2)
        self.assertEqual(self.deque.pop_back(), 1)
        self.assertIsNone(self.deque.pop_back())

    def test_front_and_back(self):
        self.deque.push_back("a")
        self.deque.push_back("b")
        self.deque.push_back("c")
        self.assertEqual(self.deque.front(), "a")
        self.assertEqual(self.deque.back(), "c")

    def test_is_empty_and_size(self):
        self.assertTrue(self.deque.is_empty())
        self.assertEqual(self.deque.size(), 0)
        self.deque.push_front(10)
        self.deque.push_back(20)
        self.assertFalse(self.deque.is_empty())
        self.assertEqual(self.deque.size(), 2)


if __name__ == "__main__":
    unittest.main(argv=[""], verbosity=2, exit=False)
