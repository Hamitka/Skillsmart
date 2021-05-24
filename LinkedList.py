# -*- coding: utf-8 -*-

class Node:

    def __init__(self, v):
        self.value = v
        self.prev = None
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
        """
        1.4. Добавьте в класс LinkedList метод поиска всех узлов по конкретному значению
        (возвращается стандартный питоновский список найденных узлов).
        """
        result = []
        node = self.head
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def delete(self, val, all=False):
        """
        1.1. Добавьте в класс LinkedList метод удаления одного узла по его значению
        где флажок all=False по умолчанию -- удаляем только первый нашедшийся элемент.
        1.2. Дополните этот метод удалением всех узлов по конкретному значению (флажок all=True).
        """
        while self.head and self.head.value == val:
            self.head = self.head.next
            if self.head is None: self.tail = None
            if not all:
                return None

        node = self.head
        node_prev = None
        while node is not None:
            if node.value == val:
                node_prev.next = node.next
                if self.head is None: self.tail = None
                if node == self.tail: self.tail = node_prev
                if not all:
                    return None
            else:
                node_prev = node
            node = node.next
        return None

    def clean(self):
        """
        1.3. Добавьте в класс LinkedList метод очистки всего содержимого
        (создание пустого списка) -- clean()
        """
        self.__init__()

    def len(self):
        """
        1.5. Добавьте в класс LinkedList метод вычисления текущей длины списка -- len()
        """
        i = 0
        node = self.head
        while node is not None:
            i += 1
            node = node.next
        return i

    def insert(self, afterNode, newNode):
        """
        1.6. Добавьте в класс LinkedList метод вставки узла newNode после заданного узла afterNode (из списка)
        Если afterNode = None, добавьте новый элемент первым в списке.
        """
        if self.head is None:
            self.add_in_tail(newNode)
            return None
        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
            return None
        node = self.head
        while node is not None:
            if node == afterNode:
                newNode.next = node.next
                node.next = newNode
                if node == self.tail: self.tail = newNode
                return None
            node = node.next

    def __add__(self, other):
        if self.len() == other.len():
            result = LinkedList()
            node_self, node_other = self.head, other.head
            while node_self:
                result.add_in_tail(Node(node_self.value + node_other.value))
                node_self, node_other = node_self.next, node_other.next
            return result
        return None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def print_all_nodes_reverse(self):
        node = self.tail
        while node is not None:
            print(node.value)
            node = node.prev

    def print_all_nodes_both_row(self):
        node = self.head
        while node is not None:
            print(node.value, end=' ')
            node = node.next
        print()
        print('-' * 8)
        node = self.tail
        while node is not None:
            print(node.value, end=' ')
            node = node.prev
        print()

    def find(self, val):
        """
        2.1. Добавьте в класс LinkedList2 метод поиска первого узла по его значению.
        """
        node = self.head
        while node:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        """
        2.2. Добавьте в класс LinkedList2 метод поиска всех узлов по конкретному значению
        (возвращается список найденных узлов).
        """
        result = []
        node = self.head
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def delete(self, val, all=False):
        """
        2.3. Добавьте в класс LinkedList2 метод удаления одного узла по его значению.
        где флажок all=False по умолчанию -- удаляем только первый нашедшийся элемент.
        2.4. Дополните этот метод удалением всех узлов по конкретному значению (флажок all=True).
        """
        while self.head and self.head.value == val:
            self.head = self.head.next
            if self.head: self.head.prev = None
            if self.head is None: self.tail = None
            if not all:
                return None

        node = self.head
        while node is not None:
            if node.value == val:
                node.prev.next = node.next
                if node.next: node.next.prev = node.prev
                if self.head is None: self.tail = None
                if node == self.tail: self.tail = node.prev
                if not all:
                    return None

            node = node.next
        return None

    def clean(self):
        """
        2.7. Добавьте в класс LinkedList2 метод очистки всего содержимого
        (создание пустого списка) -- clean()
        """
        self.__init__()

    def len(self):
        """
        2.8. Добавьте в класс LinkedList2 метод вычисления текущей длины списка -- len()
        """
        i = 0
        node = self.head
        while node is not None:
            i += 1
            node = node.next
        return i

    def len_reverse(self):
        i = 0
        node = self.tail
        while node is not None:
            i += 1
            node = node.prev
        return i

    def insert(self, afterNode, newNode):
        """
        2.5. Добавьте в класс LinkedList2 метод вставки узла после заданного узла.
        Если afterNode = None и список пустой, добавьте новый элемент первым в списке.
        Если afterNode = None и список непустой, добавьте новый элемент последним в списке.
        """
        if self.head is None or afterNode is None:
            self.add_in_tail(newNode)
            return None
        node = self.head
        while node is not None:
            if node == afterNode:

                newNode.next = node.next
                newNode.prev = node
                if node.next: node.next.prev = newNode
                node.next = newNode
                if node == self.tail: self.tail = newNode
                return None
            node = node.next

    def add_in_head(self, item):
        """
        2.6. Добавьте в класс LinkedList2 метод вставки узла самым первым элементом.
        """
        if self.head is None:
            self.tail = item
            item.prev = None
            item.next = None
        else:
            self.head.prev = item
            item.next = self.head
        self.head = item

