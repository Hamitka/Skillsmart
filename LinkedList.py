# -*- coding: utf-8 -*-

class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        return [] # здесь будет ваш код

    def delete(self, val, all=False):
        while self.head.value == val:
            self.head = self.head.next
            if not all:
                return None

        node = self.head
        node_prev = None
        while node is not None:
            if node.value == val:
                node_prev.next = node.next
                if not all:
                    return None
            else:
                node_prev = node
            node = node.next
        return None

    def clean(self):
        pass # здесь будет ваш код

    def len(self):
        return 0 # здесь будет ваш код

    def insert(self, afterNode, newNode):
        pass # здесь будет ваш код