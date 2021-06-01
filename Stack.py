# -*- coding: utf-8 -*-

class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.stack:
            return self.stack.pop(0)
        else:
            return None

    def push(self, value):
        self.stack.insert(0, value)

    def peek(self):
        if self.stack:
            return self.stack[0]
        else:
            return None


def bracket_sequence(some_string: str):
    bracket_stack = Stack()
    for i in some_string:
        bracket_stack.push(i)

    result = 0
    while bracket_stack.size() > 0:
        temp = bracket_stack.pop()
        if temp == '(' and result == 0:
            return False
        elif temp == ')':
            result += 1
        elif temp == '(':
            result -= 1

    return True if result == 0 else False
