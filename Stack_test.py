import unittest
import Stack


class MyTestCase(unittest.TestCase):
    def test_stack_size(self):
        stack = Stack.Stack()
        self.assertEqual(0, stack.size())
        stack.push(1)
        self.assertEqual(1, stack.size())
        stack.push(2)
        self.assertEqual(2, stack.size())

    def test_stack_push_pop_peek(self):
        stack = Stack.Stack()
        self.assertEqual(None, stack.pop())
        stack.push(1)
        self.assertEqual(1, stack.peek())
        stack.push(2)
        self.assertEqual(2, stack.peek())
        self.assertEqual(2, stack.pop())
        self.assertEqual(1, stack.pop())
        self.assertEqual(None, stack.pop())


if __name__ == '__main__':
    unittest.main()
