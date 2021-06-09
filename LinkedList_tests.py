# -*- coding: utf-8 -*-

import unittest
import LinkedList as ll


class MyTestCase(unittest.TestCase):
    def compare_list_llist(self, some_list, some_llist):
        node = some_llist.head
        for i in some_list:
            self.assertEqual(i, node.value)
            # print(i, node.value)
            node = node.next

    def test_linked_list_del_all(self):
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

    def test_linked_list_del_one(self):
        test_llist = ll.LinkedList()
        self.assertEqual(None, test_llist.delete(1, all=False))

        temp_list = [11, 11, 11, 11, 12, 23, 11, 11, 34, 45, 56, 67, 11, 78, 11, 89, 11, 11, 11]
        for i in temp_list:
            test_llist.add_in_tail(ll.Node(i))
        del_item = 11
        test_llist.delete(del_item, all=False)
        temp_list.remove(del_item)
        self.compare_list_llist(temp_list, test_llist)

    def test_linked_list_del_first(self):
        temp_list = [99, 11, 11, 12, 23, 11, 11, 34, 45, 56, 67, 11, 78, 11, 89, 11, 11, 11]
        test_llist = ll.LinkedList()
        for i in temp_list:
            test_llist.add_in_tail(ll.Node(i))
        del_item = 99
        test_llist.delete(del_item, all=False)
        temp_list.remove(del_item)
        self.compare_list_llist(temp_list, test_llist)

    def test_linked_list_del_last(self):
        temp_list = [12, 23, 11, 11, 34, 45, 56, 67, 11, 78, 11, 89, 11, 99]
        test_llist = ll.LinkedList()
        for i in temp_list:
            test_llist.add_in_tail(ll.Node(i))
        del_item = 99
        test_llist.delete(del_item, all=False)
        temp_list.remove(del_item)
        self.compare_list_llist(temp_list, test_llist)
        self.assertEqual(temp_list[-1], test_llist.tail.value)

    def test_linked_list_del_single(self):
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
        # insert into empty linked list:
        test_llist.clean()
        test_llist.insert(test_llist.find(89), ll.Node(item_insert))
        self.assertEqual(item_insert, test_llist.head.value)
        self.assertEqual(item_insert, test_llist.tail.value)

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


class MyTestCase2(unittest.TestCase):
    def compare_list_llist(self, some_list, some_llist):
        node = some_llist.head
        for i in some_list:
            self.assertEqual(i, node.value)
            # print(i, node.value)
            node = node.next

    def compare_list_llist_reverse(self, some_list, some_llist):
        node = some_llist.tail
        for i in some_list[::-1]:
            self.assertEqual(i, node.value)
            # print(i, node.value)
            node = node.prev

    def common_tests(self, some_list, some_llist):
        self.compare_list_llist(some_list, some_llist)
        self.compare_list_llist_reverse(some_list, some_llist)
        self.assertEqual(len(some_list), some_llist.len())
        self.assertEqual(len(some_list), some_llist.len_reverse())

    def test_linked_list2_del_all(self):
        test_llist = ll.LinkedList2()
        self.assertEqual(None, test_llist.delete(1, all=True))

        temp_list = [11, 11, 11, 11, 12, 23, 11, 11, 34, 45, 56, 67, 11, 78, 11, 89, 11, 11, 11]
        for i in temp_list:
            test_llist.add_in_tail(ll.Node(i))
        del_item = 11
        test_llist.delete(del_item, all=True)
        # test_llist.print_all_nodes_both_row()
        temp_list = [i for i in temp_list if i != del_item]
        self.common_tests(temp_list, test_llist)

        # delete all same node:
        test_llist.clean()
        for i in range(10):
            test_llist.add_in_tail(ll.Node(del_item))
        test_llist.delete(del_item, all=True)
        self.assertEqual(None, test_llist.head)
        self.assertEqual(None, test_llist.tail)
        self.assertEqual(0, test_llist.len())
        self.assertEqual(0, test_llist.len_reverse())

    def test_linked_list2_del_one(self):
        test_llist = ll.LinkedList2()
        self.assertEqual(None, test_llist.delete(1, all=False))

        temp_list = [11, 11, 11, 11, 12, 23, 11, 11, 34, 45, 56, 67, 11, 78, 11, 89, 11, 11, 11]
        for i in temp_list:
            test_llist.add_in_tail(ll.Node(i))
        del_item = 11
        test_llist.delete(del_item, all=False)
        temp_list.remove(del_item)
        # test_llist.print_all_nodes_both_row()
        self.common_tests(temp_list, test_llist)

    def test_linked_list2_del_first(self):
        temp_list = [99, 11, 11, 12, 23, 11, 11, 34, 45, 56, 67, 11, 78, 11, 89, 11, 11, 11]
        test_llist = ll.LinkedList2()
        for i in temp_list:
            test_llist.add_in_tail(ll.Node(i))
        del_item = 99
        test_llist.delete(del_item, all=False)
        temp_list.remove(del_item)
        self.common_tests(temp_list, test_llist)

    def test_linked_list2_del_last(self):
        temp_list = [12, 23, 11, 11, 34, 45, 56, 67, 11, 78, 11, 89, 11, 99]
        test_llist = ll.LinkedList2()
        for i in temp_list:
            test_llist.add_in_tail(ll.Node(i))
        del_item = 99
        test_llist.delete(del_item, all=False)
        temp_list.remove(del_item)
        self.common_tests(temp_list, test_llist)
        self.assertEqual(temp_list[-1], test_llist.tail.value)

    def test_linked_list2_del_single(self):
        test_llist = ll.LinkedList2()
        test_llist.add_in_tail(ll.Node(99))
        item_del = 99
        test_llist.delete(item_del, all=False)
        self.assertEqual(None, test_llist.head)
        self.assertEqual(None, test_llist.tail)

    def test_linked_list2_insert(self):
        temp_list = [12, 23, 34, 45, 56, 67, 78, 89]
        test_llist2 = ll.LinkedList2()
        for i in temp_list:
            test_llist2.add_in_tail(ll.Node(i))
        # test_llist2.print_all_nodes_both_row()

        # insert into end:
        item_insert = 10
        test_llist2.insert(None, ll.Node(item_insert))
        temp_list.append(item_insert)
        # test_llist2.print_all_nodes_both_row()
        self.common_tests(temp_list, test_llist2)
        self.assertEqual(temp_list[-1], test_llist2.tail.value)

        # insert into middle:
        item_insert = 39
        test_llist2.insert(test_llist2.find(34), ll.Node(item_insert))
        temp_list.insert(3, item_insert)
        # test_llist2.print_all_nodes_both_row()
        self.common_tests(temp_list, test_llist2)

        # insert into end:
        item_insert = 99
        test_llist2.insert(test_llist2.find(10), ll.Node(item_insert))
        temp_list.append(item_insert)
        self.common_tests(temp_list, test_llist2)
        self.assertEqual(temp_list[-1], test_llist2.tail.value)

        # insert into empty linked list:
        test_llist2.clean()
        test_llist2.insert(test_llist2.find(89), ll.Node(item_insert))
        self.assertEqual(item_insert, test_llist2.head.value)
        self.assertEqual(item_insert, test_llist2.tail.value)

    def test_linked_list2_add_in_head(self):
        temp_list = [12, 23, 34, 45, 56, 67, 78, 89]
        test_llist2 = ll.LinkedList2()
        for i in temp_list:
            test_llist2.add_in_tail(ll.Node(i))
        item_head = 10
        temp_list.insert(0, item_head)
        test_llist2.add_in_head(ll.Node(item_head))
        # test_llist2.print_all_nodes_both_row()
        self.common_tests(temp_list, test_llist2)


class MyTestCaseOrderList(unittest.TestCase):

    def test_order_list_add(self):
        order_list = ll.OrderedList(True)
        for i in range(3):
            order_list.add(i)
        self.assertEqual(0, order_list.head.value)
        self.assertEqual(2, order_list.tail.value)
        order_list.add(10)
        self.assertEqual(10, order_list.tail.value)
        order_list.add(5)
        order_list.add(8)
        order_list.add(7)
        order_list.add(9)
        order_list.add(3)
        order_list.add(6)
        order_list.add(4)
        node = order_list.head
        for i in range(11):
            self.assertEqual(i, node.value)
            node = node.next
        order_list.add(-1)
        order_list.add(-2)
        print([i.value for i in order_list.get_all()])
        print(f'compare: {order_list.compare(order_list.head.value, order_list.tail.value)}')

        order_list.clean(False)
        for i in range(11):
            order_list.add(i)
        order_list.add(11)
        order_list.add(-1)
        print([i.value for i in order_list.get_all()])
        print(f'compare: {order_list.compare(order_list.head.value, order_list.tail.value)}')

    def test_order_list_add_string(self):
        order_list = ll.OrderedStringList(True)
        for i in 'qwertyuiop':
            order_list.add(i)
        print([i.value for i in order_list.get_all()])
        print(f'compare: {order_list.compare(order_list.head.value, order_list.tail.value)}')

        order_list.clean(False)
        for i in 'qwertyuiop':
            order_list.add(i)
        print([i.value for i in order_list.get_all()])
        print(f'compare: {order_list.compare(order_list.head.value, order_list.tail.value)}')
        order_list.delete('i')
        print([i.value for i in order_list.get_all()])


if __name__ == '__main__':
    unittest.main()
