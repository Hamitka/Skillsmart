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
