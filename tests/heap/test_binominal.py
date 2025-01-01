import unittest
from src.heap.binomial import BinomialHeap


class TestBinomialHeap(unittest.TestCase):
    def setUp(self):
        self.bh = BinomialHeap()

    def test_insert_and_find_min(self):
        self.bh.insert(10)
        self.bh.insert(3)
        self.bh.insert(5)
        min_node = self.bh.find_min()
        self.assertIsNotNone(min_node)
        self.assertEqual(min_node.key, 3)

    def test_extract_min(self):
        self.bh.insert(7)
        self.bh.insert(2)
        self.bh.insert(9)
        min_node = self.bh.extract_min()
        self.assertEqual(min_node.key, 2)
        new_min = self.bh.find_min()
        self.assertIn(new_min.key, [7, 9])

    def test_union(self):
        bh2 = BinomialHeap()
        self.bh.insert(1)
        self.bh.insert(4)
        bh2.insert(2)
        bh2.insert(3)
        self.bh.union(bh2)
        # union後の最小
        min_node = self.bh.find_min()
        self.assertEqual(min_node.key, 1)


if __name__ == "__main__":
    unittest.main(argv=[""], verbosity=2, exit=False)
