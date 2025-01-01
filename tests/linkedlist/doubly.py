import unittest
from src.linkedlist.doubly import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.dll = DoublyLinkedList()

    def test_push_front_and_to_list(self):
        self.dll.push_front(3)
        self.dll.push_front(2)
        self.dll.push_front(1)
        self.assertEqual(self.dll.to_list(), [1, 2, 3])

    def test_push_back_and_to_list(self):
        self.dll.push_back(1)
        self.dll.push_back(2)
        self.dll.push_back(3)
        self.assertEqual(self.dll.to_list(), [1, 2, 3])

    def test_pop_front(self):
        self.dll.push_back(1)
        self.dll.push_back(2)
        self.dll.push_back(3)
        val = self.dll.pop_front()
        self.assertEqual(val, 1)
        self.assertEqual(self.dll.to_list(), [2, 3])

    def test_pop_back(self):
        self.dll.push_back(1)
        self.dll.push_back(2)
        self.dll.push_back(3)
        val = self.dll.pop_back()
        self.assertEqual(val, 3)
        self.assertEqual(self.dll.to_list(), [1, 2])

    def test_search(self):
        self.dll.push_back(1)
        self.dll.push_back(2)
        self.dll.push_back(3)
        self.assertTrue(self.dll.search(2))
        self.assertFalse(self.dll.search(99))

    def test_remove(self):
        self.dll.push_back(1)
        self.dll.push_back(2)
        self.dll.push_back(3)
        self.assertTrue(self.dll.remove(2))
        self.assertFalse(self.dll.remove(99))
        self.assertEqual(self.dll.to_list(), [1, 3])


if __name__ == "__main__":
    unittest.main(argv=[""], verbosity=2, exit=False)
