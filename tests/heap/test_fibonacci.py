import unittest
from src.heap.fibonacci import FibonacciHeap


class TestFibonacciHeap(unittest.TestCase):
    def setUp(self):
        self.fh = FibonacciHeap()

    def test_insert_and_find_min(self):
        self.fh.insert(5)
        self.fh.insert(3)
        self.fh.insert(8)
        min_node = self.fh.find_min()
        self.assertIsNotNone(min_node)
        self.assertEqual(min_node.key, 3)

    def test_extract_min(self):
        self.fh.insert(10)
        self.fh.insert(2)
        self.fh.insert(15)
        min_node = self.fh.extract_min()  # 2
        self.assertEqual(min_node.key, 2)
        new_min = self.fh.find_min()
        # 新しい min は 10 か 15
        self.assertIn(new_min.key, [10, 15])
        self.assertEqual(self.fh.n, 2)

    def test_union(self):
        fh2 = FibonacciHeap()
        self.fh.insert(1)
        self.fh.insert(3)
        fh2.insert(2)
        fh2.insert(4)
        self.fh.union(fh2)
        self.assertEqual(self.fh.n, 4)
        self.assertEqual(self.fh.find_min().key, 1)


if __name__ == "__main__":
    unittest.main(argv=[""], verbosity=2, exit=False)
