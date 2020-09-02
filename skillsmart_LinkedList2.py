class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


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

    # 2.1. Добавьте в класс LinkedList2 метод поиска первого узла по его значению.
    def find(self, val):
        # return None # здесь будет ваш код
        if self.head is None:
            # print("LinkedList is empty")
            return None
        node = self.head
        while node:
            if node.value == val:
                return node
            node = node.next
        return None

    # 2.2. Добавьте в класс LinkedList2 метод поиска всех узлов по конкретному значению (возвращается список найденных узлов).
    def find_all(self, val):
        listOfFind = []
        if self.head is None:
            # print("LinkedList is empty")
            return listOfFind
        node = self.head
        while node is not None:
            if node.value == val:
                listOfFind.append(node)
            node = node.next
        return listOfFind  # здесь будет ваш код

    # 2.3. Добавьте в класс LinkedList2 метод удаления одного узла по его значению.
    # где флажок all=False по умолчанию -- удаляем только первый нашедшийся элемент.
    # 2.4. Дополните этот метод удалением всех узлов по конкретному значению (флажок all=True).
    def delete(self, val, all=False):
        # pass # здесь будет ваш
        i = 0
        if self.head is None:
            # print("LinkedList is empty")
            return None
        if self.head.value == val:
            while self.head.value == val:
                self.head = self.head.next
                i += 1
                if not all:
                    if self.head is None:
                        self.tail = None
                    return None
                if self.head is None:
                    self.tail = None
                    return None
            node = self.head
            nodeNext = self.head.next
            while nodeNext:
                if nodeNext.value == val:
                    node.next = nodeNext.next
                    nodeNext = nodeNext.next
                    i += 1
                    if not all:
                        return None
                else:
                    # nodePrev = node
                    node = node.next
                    nodeNext = nodeNext.next
                if node.nodeNext is None:
                    self.tail = node
        if i == 0:
            pass
            # print("this value is not in LinkedList")
        return None

    # 2.7. Добавьте в класс LinkedList2 метод очистки всего содержимого (создание пустого списка) -- clean()
    def clean(self):
        # pass # здесь будет ваш код
        if self.head is None:
            # print("LinkedList is already empty")
            pass
        else:
            self.head = None
            self.tail = None

    # 2.8. Добавьте в класс LinkedList2 метод вычисления текущей длины списка -- len()
    def len(self):
        node = self.head
        i = 0
        while node is not None:
            i += 1
            node = node.next
        return i  # здесь будет ваш код

    # 2.5. Добавьте в класс LinkedList2 метод вставки узла после заданного узла.
    # Если afterNode = None и список пустой, добавьте новый элемент первым в списке.
    # Если afterNode = None и список непустой, добавьте новый элемент последним в списке.
    def insert(self, afterNode, newNode):
        # pass # здесь будет ваш код
        node = self.tail
        if afterNode is None and node is None:
            self.head = newNode
            newNode.next = None
            newNode.prev = None
            self.tail = newNode
            return None
        elif afterNode is None and node is not None:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            return None
        else:
            if self.tail == afterNode:
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode
                return None
            while node:
                if node == afterNode:
                    newNode.next = node.next
                    node.next = newNode
                    # print(f"---{newNode.value}")
                    newNode.prev = node
                    # print(f"--{newNode.prev.value}")
                    return None
                node = node.prev

    # 2.6. Добавьте в класс LinkedList2 метод вставки узла самым первым элементом.
    def add_in_head(self, newNode):
        # pass  # здесь будет ваш код
        node = self.head
        self.head = newNode
        newNode.next = node
        node.prev = newNode

    def print_forward_and_back(self):
        node = self.head
        print("→", end=" ")
        while node:
            print(node.value, end=" ")
            node = node.next

        node = self.tail
        print("←", end=" ")
        while node:
            print(node.value, end=" ")
            node = node.prev
        print("")
