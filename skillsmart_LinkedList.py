# В классе Node будут два элемента: value (само данное) и next -- "связь", по сути указатель на следующий узел.
# Если данный узел финальный, поле next будет хранить None.
class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

# Поле head -- это по сути указатель на узел-голову списка,
# а поле tail -- это указатель на завершающий узел.
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
        while node != None:
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

    # 1.1. Добавьте в класс LinkedList метод удаления одного узла по его значению
    # где флажок all=False по умолчанию -- удаляем только первый нашедшийся элемент.
    # 1.2. Дополните этот метод удалением всех узлов по конкретному значению (флажок all=True).
    def delete(self, val, all=False):
        # pass # здесь будет ваш код
        if self.head is None:
            print("LinkedList is empty")
        elif (self.head.value == val) and not all:
            self.head = self.head.next
        elif (self.head.value == val) and all:
            while self.head.value == val:
                self.head = self.head.next

        node = self.head.next
        previous = self.head
        while node is not None:
            if node.value == val:
                # print("candidate for del", node.value)
                previous.next = node.next
                if not all:
                    break
            previous = node
            node = node.next
        return None

    def clean(self):
        pass # здесь будет ваш код

    def len(self):
        return 0 # здесь будет ваш код

    def insert(self, afterNode, newNode):
        pass # здесь будет ваш код

n1 = Node(12)
n2 = Node(55)
n1.next = n2 # 12 -> 55

s_list = LinkedList()
s_list.add_in_tail(Node(77))
s_list.add_in_tail(Node(77))
s_list.add_in_tail(n1)
s_list.add_in_tail(n2)
s_list.add_in_tail(Node(77))
s_list.add_in_tail(Node(318))
s_list.add_in_tail(Node(77))
s_list.add_in_tail(Node(512))
s_list.add_in_tail(Node(77))
s_list.add_in_tail(Node(777))
s_list.add_in_tail(Node(77))
# s_list.print_all_nodes()

# nf = s_list.find(55)
# if nf is not None:
#     print(nf.value)
nd = s_list.delete(77, all=False)
s_list.print_all_nodes()
