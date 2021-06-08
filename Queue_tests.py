# -*- coding: utf-8 -*-

import unittest
import Queue_my


class MyTestCase(unittest.TestCase):
    def test_deque(self):
        deque = Queue_my.Deque()
        deque.addTail(7)
        self.assertEqual(1, deque.size())
        deque.addTail(8)
        self.assertEqual(2, deque.size())
        deque.addTail(9)
        self.assertEqual(3, deque.size())
        deque.addFront(3)
        self.assertEqual(4, deque.size())
        deque.addFront(2)
        self.assertEqual(5, deque.size())
        deque.addFront(1)
        self.assertEqual(6, deque.size())

        self.assertEqual(9, deque.removeTail())
        self.assertEqual(1, deque.removeFront())
        self.assertEqual(4, deque.size())

        self.assertEqual(8, deque.removeTail())
        self.assertEqual(2, deque.removeFront())
        self.assertEqual(2, deque.size())

        self.assertEqual(7, deque.removeTail())
        self.assertEqual(3, deque.removeFront())
        self.assertEqual(0, deque.size())







if __name__ == '__main__':
    unittest.main()
