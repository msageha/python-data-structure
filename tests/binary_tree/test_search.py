import unittest
from src.binary_tree.search import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_insert_and_search(self):
        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(2)
        self.bst.insert(4)
        self.assertTrue(self.bst.search(3))
        self.assertTrue(self.bst.search(4))
        self.assertFalse(self.bst.search(10))

    def test_inorder_traversal(self):
        values = [5, 3, 7, 2, 4, 6, 8]
        for v in values:
            self.bst.insert(v)
        # Inorder -> [2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(self.bst.inorder_traversal(), sorted(values))

    def test_remove(self):
        for v in [5, 3, 7, 2, 4, 6, 8]:
            self.bst.insert(v)
        # 削除: 7
        self.assertTrue(self.bst.remove(7))
        self.assertFalse(self.bst.search(7))
        # 削除: 存在しない値
        self.assertFalse(self.bst.remove(10))
        # 削除後の inorder
        self.assertEqual(self.bst.inorder_traversal(), [2, 3, 4, 5, 6, 8])


if __name__ == "__main__":
    unittest.main(argv=[""], verbosity=2, exit=False)
