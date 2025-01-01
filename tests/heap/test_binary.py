import unittest
from src.heap.binary import BinaryHeap


class TestBinaryHeap(unittest.TestCase):
    def setUp(self):
        self.bh = BinaryHeap()

    def test_insert_and_find_min(self):
        self.bh.insert(5)
        self.bh.insert(3)
        self.bh.insert(8)
        self.assertEqual(self.bh.find_min(), 3)

    def test_extract_min(self):
        self.bh.insert(4)
        self.bh.insert(2)
        self.bh.insert(6)
        self.bh.insert(1)
        self.assertEqual(self.bh.extract_min(), 1)
        self.assertEqual(self.bh.extract_min(), 2)
        self.assertEqual(self.bh.extract_min(), 4)
        self.assertEqual(self.bh.extract_min(), 6)
        self.assertIsNone(self.bh.extract_min())  # 空

    def test_is_empty_and_size(self):
        self.assertTrue(self.bh.is_empty())
        self.assertEqual(self.bh.size(), 0)
        self.bh.insert(10)
        self.bh.insert(20)
        self.assertFalse(self.bh.is_empty())
        self.assertEqual(self.bh.size(), 2)


if __name__ == "__main__":
    unittest.main(argv=[""], verbosity=2, exit=False)
