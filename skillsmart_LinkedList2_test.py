# 2.9. Напишите проверочные тесты для каждого из предыдущих заданий.
import unittest
import logging
import skillsmart_LinkedList2 as ll2

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%m-%y %H:%M:%S', level=logging.INFO)

class MyTestCase(unittest.TestCase):
    def test_LinkedList2_add_in_tail(self):
        testList2 = ll2.LinkedList2()
        testNode2 = ll2.Node(11)
        testList2.add_in_tail(testNode2)
        testList2.add_in_tail(ll2.Node(22))

        self.assertEqual(testList2.head.value, 11)
        self.assertEqual(testList2.tail.value, 22)

    def test_LinkedList2_find_last(self):
        testList2 = ll2.LinkedList2()
        testList2.add_in_tail(ll2.Node(11))
        testList2.add_in_tail(ll2.Node(22))
        testList2.add_in_tail(ll2.Node(33))

        self.assertEqual(testList2.find(11), testList2.head)
        # print (f"{testList2.find(11)} -find, {testList2.head} -head")

        self.assertEqual(testList2.find(33), testList2.tail)
        # print (f"{testList2.find(33)} -find, {testList2.tail} -tail")

        self.assertEqual(testList2.find(44), None)

    def test_LinkedList2_find_all(self):
        testList2 = ll2.LinkedList2()
        self.assertEqual(len(testList2.find_all(22)), 0)

        testList2.add_in_tail(ll2.Node(22))
        testList2.add_in_tail(ll2.Node(11))
        testList2.add_in_tail(ll2.Node(22))
        testList2.add_in_tail(ll2.Node(33))
        testList2.add_in_tail(ll2.Node(22))
        testList2.add_in_tail(ll2.Node(33))
        testList2.add_in_tail(ll2.Node(44))
        testList2.add_in_tail(ll2.Node(22))

        self.assertEqual(len(testList2.find_all(22)), 4)

    def test_LinkedList2_delete_last(self):
        testList2 = ll2.LinkedList2()
        testList2.add_in_tail(ll2.Node(22))
        testList2.add_in_tail(ll2.Node(11))
        testList2.add_in_tail(ll2.Node(22))
        testList2.add_in_tail(ll2.Node(55))
        testList2.add_in_tail(ll2.Node(22))
        testList2.add_in_tail(ll2.Node(33))
        testList2.add_in_tail(ll2.Node(44))
        testList2.add_in_tail(ll2.Node(22))

        testList2.delete(22)
        self.assertEqual(testList2.tail.value, 44)
        self.assertEqual(testList2.tail.prev.value, 33)
        self.assertEqual(testList2.tail.prev.prev.value, 22)
        self.assertEqual(testList2.tail.prev.prev.prev.value, 55)
        self.assertEqual(testList2.tail.prev.prev.prev.prev.value, 22)
        self.assertEqual(testList2.tail.prev.prev.prev.prev.prev.value, 11)
        self.assertEqual(testList2.tail.prev.prev.prev.prev.prev.prev.value, 22)
        self.assertEqual(testList2.head.value, 22)

    def test_LinkedList2_delete_all(self):
        testList2 = ll2.LinkedList2()
        testList2.delete(22)
        testList2.delete(22, True)
        testList2.add_in_tail(ll2.Node(22))
        testList2.add_in_tail(ll2.Node(11))
        testList2.add_in_tail(ll2.Node(22))
        testList2.add_in_tail(ll2.Node(55))
        testList2.add_in_tail(ll2.Node(22))
        testList2.add_in_tail(ll2.Node(33))
        testList2.add_in_tail(ll2.Node(44))
        testList2.add_in_tail(ll2.Node(22))

        testList2.delete(22, True)
        self.assertEqual(testList2.tail.value, 44)
        self.assertEqual(testList2.tail.prev.value, 33)
        self.assertEqual(testList2.tail.prev.prev.value, 55)
        self.assertEqual(testList2.tail.prev.prev.prev.value, 11)
        self.assertEqual(testList2.head.value, 11)

    def test_LinkedList2_clean_and_len(self):
        testList2 = ll2.LinkedList2()
        self.assertEqual(testList2.len(), 0)
        testList2.add_in_tail(ll2.Node(22))
        testList2.add_in_tail(ll2.Node(11))
        testList2.add_in_tail(ll2.Node(22))
        testList2.add_in_tail(ll2.Node(55))
        testList2.add_in_tail(ll2.Node(22))
        testList2.add_in_tail(ll2.Node(33))
        testList2.add_in_tail(ll2.Node(44))
        testList2.add_in_tail(ll2.Node(22))
        self.assertEqual(testList2.len(), 8)

        testList2.clean()
        self.assertEqual(testList2.tail, None)
        self.assertEqual(testList2.head, None)
        self.assertEqual(testList2.len(), 0)

    def test_LinkedList2_insert_v2(self):
        testList2 = ll2.LinkedList2()
        testList2.add_in_tail(ll2.Node(66))
        testList2.add_in_tail(ll2.Node(55))
        testList2.add_in_tail(ll2.Node(44))
        self.assertEqual(testList2.find(66), testList2.head)

        testList2.clean()
        testList2.add_in_tail(ll2.Node(77))
        self.assertEqual(testList2.find(77), testList2.head)

        testList2.clean()
        testList2.insert(None, ll2.Node(88))
        testList2.print_forward_and_back()
        # print (f'one Node {testList2.head.value} {testList2.head.next} {testList2.tail.value}')
        self.assertEqual(testList2.find(88), testList2.head)
        self.assertEqual(testList2.head.value, 88)
        self.assertEqual(testList2.tail.value, 88)

        testList2.insert(None, ll2.Node(99))
        testList2.print_forward_and_back()
        # print (f'two Node {testList2.head.value} {testList2.head.next.value} {testList2.tail.value}')
        self.assertEqual(testList2.find(99), testList2.tail)
        self.assertEqual(testList2.find(99), testList2.head.next)
        self.assertEqual(testList2.find(88), testList2.tail.prev)
        self.assertEqual(testList2.head.value, 88)
        self.assertEqual(testList2.head.next.value, 99)
        self.assertEqual(testList2.tail.value, 99)
        self.assertEqual(testList2.tail.prev.value, 88)

        testList2.insert(None, ll2.Node(111))
        testList2.print_forward_and_back()
        # print (f'three Node {testList2.head.value} {testList2.head.next.value} {testList2.tail.value}')
        self.assertEqual(testList2.find(111), testList2.tail)
        self.assertEqual(testList2.head.value, 88)
        self.assertEqual(testList2.head.next.value, 99)
        self.assertEqual(testList2.head.next.next.value, 111)
        self.assertEqual(testList2.tail.value, 111)
        self.assertEqual(testList2.tail.prev.value, 99)
        self.assertEqual(testList2.tail.prev.prev.value, 88)

        testList2.insert(None, ll2.Node(122))
        testList2.print_forward_and_back()

        testList2.insert(testList2.find(88), ll2.Node(90))
        testList2.print_forward_and_back()
        # self.assertEqual(testList2.head.value, 88)
        # self.assertEqual(testList2.head.next.value, 90)
        # self.assertEqual(testList2.head.next.next.value, 99)
        # self.assertEqual(testList2.head.next.next.next.value, 111)
        # self.assertEqual(testList2.head.next.next.next.next, None)
        # self.assertEqual(testList2.tail.next, None)
        # self.assertEqual(testList2.tail.value, 111)
        # self.assertEqual(testList2.tail.prev.value, 99)
        # self.assertEqual(testList2.tail.prev.prev.value, 90)
        # self.assertEqual(testList2.tail.prev.prev.prev.value, 88)

        testList2.insert(testList2.find(99), ll2.Node(101))
        testList2.print_forward_and_back()

        testList2.insert(testList2.find(122), ll2.Node(133))
        testList2.print_forward_and_back()

    def test_LinkedList2_add_in_head(self):
        testList2 = ll2.LinkedList2()
        testList2.add_in_tail(ll2.Node(66))
        testList2.add_in_tail(ll2.Node(55))
        testList2.add_in_tail(ll2.Node(44))

        testList2.print_forward_and_back()
        testList2.add_in_head(ll2.Node(77))
        testList2.print_forward_and_back()

        self.assertEqual(testList2.head, testList2.find(77))
        self.assertEqual(testList2.head.next, testList2.find(77).next)

if __name__ == '__main__':
    unittest.main()
