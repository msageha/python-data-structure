import unittest
from src.binary_tree.avl import AVLTree


class TestAVLTree(unittest.TestCase):
    def setUp(self):
        self.avl = AVLTree()

    def test_insert_and_search(self):
        values = [10, 20, 5, 6, 8, 15, 30]
        for v in values:
            self.avl.insert(v)

        self.assertTrue(self.avl.search(10))
        self.assertTrue(self.avl.search(30))
        self.assertFalse(self.avl.search(999))

    def test_inorder_balance(self):
        for v in [20, 10, 5, 4, 3, 2, 1]:
            self.avl.insert(v)
        self.assertEqual(self.avl.inorder_traversal(), [1, 2, 3, 4, 5, 10, 20])


if __name__ == "__main__":
    unittest.main(argv=[""], verbosity=2, exit=False)
