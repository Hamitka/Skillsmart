# -*- coding: utf-8 -*-

import unittest
import LinkedList as ll


class MyTestCase(unittest.TestCase):
    def test_linked_list_dell_all(self):
        temp_list = [11, 11, 11, 11, 12, 23, 11, 11, 34, 45, 56, 67, 11, 78, 11, 89, 11, 11, 11]
        test_llist = ll.LinkedList()
        for i in temp_list:
            test_llist.add_in_tail(ll.Node(i))
        del_item = 11
        test_llist.delete(del_item, True)
        temp_list = [i for i in temp_list if i != del_item]
        node = test_llist.head
        for i in temp_list:
            self.assertEqual(i, node.value)
            print(i, node.value)
            node = node.next


if __name__ == '__main__':
    unittest.main()