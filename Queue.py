# -*- coding: utf-8 -*-

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


def rotate(queue, num_elements):
    for i in range(num_elements):
        queue.enqueue(queue.dequeue())


class Deque:
    def __init__(self):
        self.deque = []

    def addFront(self, item):
        self.deque.insert(0, item)

    def addTail(self, item):
        self.deque.append(item)

    def removeFront(self):
        if self.deque:
            return self.deque.pop(0)
        else:
            return None

    def removeTail(self):
        if self.deque:
            return self.deque.pop()
        else:
            return None

    def size(self):
        return len(self.deque)


def palindrome(some_string):
    deque = Deque()
    for i in some_string:
        if i != ' ':
            deque.addTail(i)
    while deque.size() > 1:
        if deque.removeFront() != deque.removeTail():
            return False
    return True


# print(palindrome('я иду с мечем судия'))
# print(palindrome('лёша на полке клопа нашёл'))
# print(palindrome('а роза упала на лапу азора'))
