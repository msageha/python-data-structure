import unittest
from src.linkedlist.singly import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):
    def setUp(self):
        self.sll = SinglyLinkedList()

    def test_push_front_and_to_list(self):
        self.sll.push_front(3)
        self.sll.push_front(2)
        self.sll.push_front(1)
        self.assertEqual(self.sll.to_list(), [1, 2, 3])

    def test_push_back_and_to_list(self):
        self.sll.push_back(1)
        self.sll.push_back(2)
        self.sll.push_back(3)
        self.assertEqual(self.sll.to_list(), [1, 2, 3])

    def test_pop_front(self):
        self.sll.push_back(1)
        self.sll.push_back(2)
        self.sll.push_back(3)
        val = self.sll.pop_front()
        self.assertEqual(val, 1)
        self.assertEqual(self.sll.to_list(), [2, 3])

    def test_pop_back(self):
        self.sll.push_back(1)
        self.sll.push_back(2)
        self.sll.push_back(3)
        val = self.sll.pop_back()
        self.assertEqual(val, 3)
        self.assertEqual(self.sll.to_list(), [1, 2])

    def test_search(self):
        self.sll.push_back(1)
        self.sll.push_back(2)
        self.sll.push_back(3)
        self.assertTrue(self.sll.search(2))
        self.assertFalse(self.sll.search(99))

    def test_remove(self):
        self.sll.push_back(1)
        self.sll.push_back(2)
        self.sll.push_back(3)
        self.assertTrue(self.sll.remove(2))
        self.assertFalse(self.sll.remove(99))
        self.assertEqual(self.sll.to_list(), [1, 3])


if __name__ == "__main__":
    unittest.main(argv=[""], verbosity=2, exit=False)
