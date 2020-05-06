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
        print("--------------")
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
    # 1.4. Добавьте в класс LinkedList метод поиска всех узлов по конкретному значению (возвращается стандартный питоновский список найденных узлов).
    def find_all(self, val):
        listOfFind = []
        node = self.head
        while node is not None:
            if node.value == val:
                listOfFind.append(node)
                # print(node.value)
            node = node.next
        return listOfFind # здесь будет ваш код

    # 1.1. Добавьте в класс LinkedList метод удаления одного узла по его значению
    # где флажок all=False по умолчанию -- удаляем только первый нашедшийся элемент.
    # 1.2. Дополните этот метод удалением всех узлов по конкретному значению (флажок all=True).

    # я так понимаю, для удаления узла из связанного списка требуется заменить саму связь на следующий за удаляемым узел
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

    # 1.3. Добавьте в класс LinkedList метод очистки всего содержимого (создание пустого списка) -- clean()
    # Подозреваю, что достаочно "голову" списка "обнулить"
    def clean(self):
        # pass # здесь будет ваш код
        self.head = None
    # 1.5. Добавьте в класс LinkedList метод вычисления текущей длины списка -- len()
    def len(self):
        node = self.head
        i=0
        while node is not None:
            i +=1
            node = node.next
        return i # здесь будет ваш код

    # 1.6. Добавьте в класс LinkedList метод вставки узла newNode после заданного узла afterNode (из списка)
    # Если afterNode = None, добавьте новый элемент первым в списке.
    def insert(self, afterNode, newNode):
        # pass # здесь будет ваш код
        node = self.head
        newNODE= Node(newNode)
        if afterNode is None:
            newNODE.next = node
            self.head = newNODE
        else:
            while node is not None:
                if node.value == afterNode:
                    newNODE.next = node.next
                    node.next = newNODE
                    break
                node = node.next
        return None

n1 = Node(12)
n2 = Node(55)
n1.next = n2 # 12 -> 55

s_list = LinkedList()

s_list.add_in_tail(n1)
s_list.add_in_tail(Node(77))
s_list.add_in_tail(n2)
s_list.add_in_tail(Node(77))
s_list.add_in_tail(Node(318))
s_list.add_in_tail(Node(77))
s_list.add_in_tail(Node(512))
s_list.add_in_tail(Node(77))
s_list.add_in_tail(Node(777))
s_list.add_in_tail(Node(77))
s_list.add_in_tail(Node(333))
# s_list.print_all_nodes()

# nFind = s_list.find(55)
# if nFind is not None:
#     print(nFind.value)

# * 1.7. Напишите проверочные тесты для каждого из предыдущих заданий.
s_list.print_all_nodes()
print ("длина списка: ", s_list.len()) #проверяем 1.5: длина списка

nDel = s_list.delete(55, all=False) #проверяем 1.1: удаление одного узла в середине:
s_list.print_all_nodes()
print ("длина списка: ", s_list.len()) #проверяем 1.5: длина списка

nDel = s_list.delete(12, all=False) #проверяем 1.1: удаление одного узла в начале:
s_list.print_all_nodes()
print ("длина списка: ", s_list.len()) #проверяем 1.5: длина списка

nDel = s_list.delete(333, all=False) #проверяем 1.1: удаление одного узла в конце:
s_list.print_all_nodes()
print ("длина списка: ", s_list.len()) #проверяем 1.5: длина списка

nFindAll = s_list.find_all(77) #проверяем 1.4: поиска всех узлов по конкретному значению
for k in nFindAll:
    print(k.value, k.next)

nDelAll = s_list.delete(77, all=True) #проверяем 1.2: удаление всех найденных узлов:
s_list.print_all_nodes()
print ("длина списка: ", s_list.len()) #проверяем 1.5: длина списка

nInsert = s_list.insert(777, 513) #проверяем 1.6: вставка узла
s_list.print_all_nodes()
print ("длина списка: ", s_list.len()) #проверяем 1.5: длина списка

nClean = s_list.clean() #проверяем 1.3: очистка списка:
s_list.print_all_nodes()
print ("длина списка: ", s_list.len()) #проверяем 1.5: длина списка

s_list.add_in_tail(Node(88))
s_list.print_all_nodes()
print ("длина списка: ", s_list.len()) #проверяем 1.5: длина списка

nInsert = s_list.insert(None, 513) #проверяем 1.6: вставка узла если None
s_list.print_all_nodes()
print ("длина списка: ", s_list.len()) #проверяем 1.5: длина списка