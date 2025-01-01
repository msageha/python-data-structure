import unittest
from src.binary_tree.binary import BinaryTree


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.bt = BinaryTree()

    def test_empty_tree(self):
        self.assertIsNone(self.bt.root)
        self.assertEqual(self.bt.preorder_traversal(), [])

    def test_insert_level_order(self):
        self.bt.insert_level_order([1, 2, 3, 4, 5])
        # level-order: root=1, left=2, right=3, ...
        # preorder -> [1, 2, 4, 5, 3]
        self.assertEqual(self.bt.preorder_traversal(), [1, 2, 4, 5, 3])
        self.assertIsNotNone(self.bt.root)
        self.assertIsNotNone(self.bt.root.left)
        self.assertIsNotNone(self.bt.root.right)


if __name__ == "__main__":
    unittest.main(argv=[""], verbosity=2, exit=False)
