import unittest
from src.linkedlist.circular import CircularLinkedList


class TestCircularLinkedList(unittest.TestCase):
    def setUp(self):
        self.cll = CircularLinkedList()

    def test_push_front_and_to_list(self):
        self.cll.push_front(3)
        self.cll.push_front(2)
        self.cll.push_front(1)
        self.assertEqual(self.cll.to_list(), [1, 2, 3])

    def test_push_back_and_to_list(self):
        self.cll.push_back(1)
        self.cll.push_back(2)
        self.cll.push_back(3)
        self.assertEqual(self.cll.to_list(), [1, 2, 3])

    def test_pop_front(self):
        self.cll.push_back(1)
        self.cll.push_back(2)
        self.cll.push_back(3)
        val = self.cll.pop_front()
        self.assertEqual(val, 1)
        self.assertEqual(self.cll.to_list(), [2, 3])

    def test_pop_back(self):
        self.cll.push_back(1)
        self.cll.push_back(2)
        self.cll.push_back(3)
        val = self.cll.pop_back()
        self.assertEqual(val, 3)
        self.assertEqual(self.cll.to_list(), [1, 2])

    def test_search(self):
        self.cll.push_back(1)
        self.cll.push_back(2)
        self.cll.push_back(3)
        self.assertTrue(self.cll.search(2))
        self.assertFalse(self.cll.search(99))

    def test_remove(self):
        self.cll.push_back(1)
        self.cll.push_back(2)
        self.cll.push_back(3)
        self.assertTrue(self.cll.remove(2))
        self.assertFalse(self.cll.remove(99))
        self.assertEqual(self.cll.to_list(), [1, 3])


if __name__ == "__main__":
    unittest.main(argv=[""], verbosity=2, exit=False)
