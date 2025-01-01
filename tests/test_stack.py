import unittest
from src.stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push_and_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        self.assertIsNone(self.stack.pop())  # Empty stack -> None

    def test_top(self):
        self.stack.push(10)
        self.assertEqual(self.stack.top(), 10)
        self.assertEqual(self.stack.pop(), 10)
        self.assertIsNone(self.stack.top())

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(100)
        self.assertFalse(self.stack.is_empty())

    def test_size(self):
        self.assertEqual(self.stack.size(), 0)
        self.stack.push("a")
        self.stack.push("b")
        self.assertEqual(self.stack.size(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 1)


if __name__ == "__main__":
    unittest.main(argv=[""], verbosity=2, exit=False)
