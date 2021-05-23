# -*- coding: utf-8 -*-

import unittest
import LinkedList as ll


class MyTestCase(unittest.TestCase):
    def compare_list_llist(self, some_list, some_llist):
        node = some_llist.head
        for i in some_list:
            self.assertEqual(node.value, i)
            # print(i, node.value)
            node = node.next

    def test_linked_list_dell_all(self):
        test_llist = ll.LinkedList()
        self.assertEqual(None, test_llist.delete(1, all=True))

        temp_list = [11, 11, 11, 11, 12, 23, 11, 11, 34, 45, 56, 67, 11, 78, 11, 89, 11, 11, 11]
        for i in temp_list:
            test_llist.add_in_tail(ll.Node(i))
        del_item = 11
        test_llist.delete(del_item, all=True)
        temp_list = [i for i in temp_list if i != del_item]
        self.compare_list_llist(temp_list, test_llist)
        # delete all same node:
        test_llist.clean()
        for i in range(10):
            test_llist.add_in_tail(ll.Node(del_item))
        test_llist.delete(del_item, all=True)
        self.assertEqual(None, test_llist.head)
        self.assertEqual(None, test_llist.tail)
        self.assertEqual(0, test_llist.len())

    def test_linked_list_dell_one(self):
        test_llist = ll.LinkedList()
        self.assertEqual(None, test_llist.delete(1, all=False))

        temp_list = [11, 11, 11, 11, 12, 23, 11, 11, 34, 45, 56, 67, 11, 78, 11, 89, 11, 11, 11]
        for i in temp_list:
            test_llist.add_in_tail(ll.Node(i))
        del_item = 11
        test_llist.delete(del_item, all=False)
        temp_list.remove(del_item)
        self.compare_list_llist(temp_list, test_llist)

    def test_linked_list_dell_first(self):
        temp_list = [99, 11, 11, 12, 23, 11, 11, 34, 45, 56, 67, 11, 78, 11, 89, 11, 11, 11]
        test_llist = ll.LinkedList()
        for i in temp_list:
            test_llist.add_in_tail(ll.Node(i))
        del_item = 99
        test_llist.delete(del_item, all=False)
        temp_list.remove(del_item)
        self.compare_list_llist(temp_list, test_llist)

    def test_linked_list_dell_last(self):
        temp_list = [12, 23, 11, 11, 34, 45, 56, 67, 11, 78, 11, 89, 11, 99]
        test_llist = ll.LinkedList()
        for i in temp_list:
            test_llist.add_in_tail(ll.Node(i))
        del_item = 99
        test_llist.delete(del_item, all=False)
        temp_list.remove(del_item)
        self.compare_list_llist(temp_list, test_llist)
        self.assertEqual(temp_list[-1], test_llist.tail.value)

    def test_linked_list_dell_single(self):
        test_llist = ll.LinkedList()
        test_llist.add_in_tail(ll.Node(99))
        item_del = 99
        test_llist.delete(item_del, all=False)
        self.assertEqual(None, test_llist.head)
        self.assertEqual(None, test_llist.tail)

    def test_linked_list_clean(self):
        temp_list = [12, 23, 11, 11, 34, 45, 56, 67, 11, 78, 11, 89, 11, 11, 99]
        test_llist = ll.LinkedList()
        for i in temp_list:
            test_llist.add_in_tail(ll.Node(i))
        test_llist.clean()
        self.assertEqual(None, test_llist.head)
        self.assertEqual(None, test_llist.tail)

    def test_linked_list_find_all(self):
        temp_list = [12, 23, 11, 11, 34, 45, 56, 67, 11, 78, 11, 89, 11, 11, 99]
        test_llist = ll.LinkedList()
        for i in temp_list:
            test_llist.add_in_tail(ll.Node(i))
        item_find = 11
        self.assertEqual(temp_list.count(item_find), len(test_llist.find_all(item_find)))
        test_llist.clean()
        self.assertEqual(0, len(test_llist.find_all(item_find)))

    def test_linked_list_find_len(self):
        temp_list = [12, 23, 11, 11, 34, 45, 56, 67, 11, 78, 11, 89, 11, 11, 99]
        test_llist = ll.LinkedList()
        for i in temp_list:
            test_llist.add_in_tail(ll.Node(i))
        self.assertEqual(len(temp_list), test_llist.len())
        test_llist.clean()
        self.assertEqual(0, test_llist.len())

    def test_linked_list_insert(self):
        temp_list = [12, 23, 34, 45, 56, 67, 78, 89]
        test_llist = ll.LinkedList()
        for i in temp_list:
            test_llist.add_in_tail(ll.Node(i))
        # insert into begin:
        item_insert = 10
        test_llist.insert(None, ll.Node(item_insert))
        temp_list.insert(0, item_insert)
        self.compare_list_llist(temp_list, test_llist)
        self.assertEqual(temp_list[0], test_llist.head.value)
        # insert into middle:
        item_insert = 39
        test_llist.insert(test_llist.find(34), ll.Node(item_insert))
        temp_list.insert(4, item_insert)
        self.compare_list_llist(temp_list, test_llist)
        # insert into end:
        item_insert = 99
        test_llist.insert(test_llist.find(89), ll.Node(item_insert))
        temp_list.append(item_insert)
        self.compare_list_llist(temp_list, test_llist)
        self.assertEqual(temp_list[-1], test_llist.tail.value)

    def test_linked_list_addition(self):
        temp_list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
        temp_list_2 = [10, 20, 30, 40, 50, 60, 70, 80]

        temp_sum_lists = [a + b for a, b in zip(temp_list_1, temp_list_2)]

        test_llist_1 = ll.LinkedList()
        for i in temp_list_1:
            test_llist_1.add_in_tail(ll.Node(i))

        test_llist_2 = ll.LinkedList()
        for i in temp_list_2:
            test_llist_2.add_in_tail(ll.Node(i))

        test_sum_llist = test_llist_1 + test_llist_2
        self.compare_list_llist(temp_sum_lists, test_sum_llist)

        # for linked list if different length:
        test_llist_1.add_in_tail(ll.Node(9))
        test_sum_llist_2 = test_llist_1 + test_llist_2
        self.assertEqual(None, test_sum_llist_2)


if __name__ == '__main__':
    unittest.main()
