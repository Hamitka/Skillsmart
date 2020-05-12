import unittest
import skillsmart_LinkedList

class MyTestCase(unittest.TestCase):

    def test_linkedList_delete_all_False_first(self):
        testList = skillsmart_LinkedList.LinkedList()
        testNode = skillsmart_LinkedList.Node(88)
        testList.add_in_tail(testNode)
        testList.add_in_tail(skillsmart_LinkedList.Node(66))
        testList.add_in_tail(skillsmart_LinkedList.Node(22))
        testList.add_in_tail(skillsmart_LinkedList.Node(44))
        testList.add_in_tail(skillsmart_LinkedList.Node(33))
        testList.add_in_tail(skillsmart_LinkedList.Node(22))
        testList.add_in_tail(skillsmart_LinkedList.Node(88))
        testList.add_in_tail(skillsmart_LinkedList.Node(77))

        testList.delete(88)
        self.assertEqual(testList.head.value, 66)
        self.assertEqual(testList.head.next.value, 22)
        self.assertEqual(testList.head.next.next.value, 44)
        self.assertEqual(testList.head.next.next.next.value, 33)
        self.assertEqual(testList.head.next.next.next.next.value, 22)
        self.assertEqual(testList.head.next.next.next.next.next.value, 88)
        self.assertEqual(testList.head.next.next.next.next.next.next.value, 77)
        self.assertEqual(testList.head.next.next.next.next.next.next.next, None)

    def test_linkedList_delete_all_False_midle(self):
        testList = skillsmart_LinkedList.LinkedList()
        testNode = skillsmart_LinkedList.Node(88)
        testList.add_in_tail(testNode)
        testList.add_in_tail(skillsmart_LinkedList.Node(66))
        testList.add_in_tail(skillsmart_LinkedList.Node(22))
        testList.add_in_tail(skillsmart_LinkedList.Node(44))
        testList.add_in_tail(skillsmart_LinkedList.Node(33))
        testList.add_in_tail(skillsmart_LinkedList.Node(22))
        testList.add_in_tail(skillsmart_LinkedList.Node(88))
        testList.add_in_tail(skillsmart_LinkedList.Node(77))

        testList.delete(22)
        self.assertEqual(testList.head.value, 88)
        self.assertEqual(testList.head.next.value, 66)
        self.assertEqual(testList.head.next.next.value, 44)
        self.assertEqual(testList.head.next.next.next.value, 33)
        self.assertEqual(testList.head.next.next.next.next.value, 22)
        self.assertEqual(testList.head.next.next.next.next.next.value, 88)
        self.assertEqual(testList.head.next.next.next.next.next.next.value, 77)
        self.assertEqual(testList.head.next.next.next.next.next.next.next, None)

    def test_linkedList_delete_all_True(self):
        testList = skillsmart_LinkedList.LinkedList()
        testNode = skillsmart_LinkedList.Node(88)
        testList.add_in_tail(testNode)
        testList.add_in_tail(skillsmart_LinkedList.Node(66))
        testList.add_in_tail(skillsmart_LinkedList.Node(22))
        testList.add_in_tail(skillsmart_LinkedList.Node(44))
        testList.add_in_tail(skillsmart_LinkedList.Node(33))
        testList.add_in_tail(skillsmart_LinkedList.Node(22))
        testList.add_in_tail(skillsmart_LinkedList.Node(88))
        testList.add_in_tail(skillsmart_LinkedList.Node(77))

        testList.delete(88, True)
        self.assertEqual(testList.head.value, 66)
        self.assertEqual(testList.head.next.value, 22)
        self.assertEqual(testList.head.next.next.value, 44)
        self.assertEqual(testList.head.next.next.next.value, 33)
        self.assertEqual(testList.head.next.next.next.next.value, 22)
        self.assertEqual(testList.head.next.next.next.next.next.value, 77)
        self.assertEqual(testList.head.next.next.next.next.next.next, None)

    def test_linkedList_delete_all_True_last(self):
        testList = skillsmart_LinkedList.LinkedList()
        testNode = skillsmart_LinkedList.Node(88)
        testList.add_in_tail(testNode)
        testList.add_in_tail(skillsmart_LinkedList.Node(66))
        testList.add_in_tail(skillsmart_LinkedList.Node(22))
        testList.add_in_tail(skillsmart_LinkedList.Node(77))
        testList.add_in_tail(skillsmart_LinkedList.Node(77))
        testList.add_in_tail(skillsmart_LinkedList.Node(77))
        testList.add_in_tail(skillsmart_LinkedList.Node(77))

        testList.delete(77, True)

        # testList.print_all_nodes()
        self.assertEqual(testList.head.value, 88)
        self.assertEqual(testList.head.next.value, 66)
        self.assertEqual(testList.head.next.next.value, 22)
        self.assertEqual(testList.head.next.next.next, None)
        self.assertEqual(testList.tail.value, 22)
        self.assertEqual(testList.tail.next, None)
        # print ("tail:", testList.tail.value)
        # self.assertEqual(testList.head.next.next.next, None)

    def test_linkedList_delete_all_True_all_same(self):
        testList = skillsmart_LinkedList.LinkedList()
        testNode = skillsmart_LinkedList.Node(77)
        testList.add_in_tail(testNode)
        testList.add_in_tail(skillsmart_LinkedList.Node(77))
        testList.add_in_tail(skillsmart_LinkedList.Node(77))
        testList.add_in_tail(skillsmart_LinkedList.Node(77))
        testList.add_in_tail(skillsmart_LinkedList.Node(77))

        testList.delete(77, True)

        # testList.print_all_nodes()
        self.assertEqual(testList.head, None)

    def test_linkedList_delete_all_True_not_in_list(self):
        testList = skillsmart_LinkedList.LinkedList()
        testNode = skillsmart_LinkedList.Node(88)
        testList.add_in_tail(testNode)

        testList.delete(77, True)
        self.assertEqual(testList.head.value, 88)

    def test_linkedList_delete_all_True_one_link(self):
        testList = skillsmart_LinkedList.LinkedList()
        testList.add_in_tail(skillsmart_LinkedList.Node(99))

        testList.delete(99, True)
        self.assertEqual(testList.head, None)

if __name__ == '__main__':
    unittest.main()
