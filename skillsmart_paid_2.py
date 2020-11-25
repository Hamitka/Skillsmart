"""
 Задание
1. Самостоятельно разберитесь, как сделать из класса List2 итератор с конструктором,
чтобы он работал не только начиная с 1, а с любого заданного значения, например:
for n in List2(5): # начиная с 5
    print(n)
2. Напишите версию List2 с конструктором, который получает количество N итерируемых элементов (сейчас 10),
и флажок конечности/бесконечности. В случае конечности List2 выдаёт N элементов и завершает работу,
а в случае бесконечности начинает повторно выдавать свою последовательность с самого начала.
3. Сделайте тесты для этих двух версий List2.
"""


class List2:
    def __init__(self, begin):
        self.begin = begin

    def __iter__(self):
        self.start = self.begin
        self.count = 0
        return self

    def __next__(self):
        current = self.start
        self.start = self.start * 2
        self.count += 1
        if self.count <= 10:
            return current
        raise StopIteration


class List2v2:
    def __init__(self, begin, count_end, infinity=False):
        self.begin = begin
        self.count_end = count_end
        self.infinity = infinity

    def __iter__(self):
        self.start = self.begin
        self.count = 0
        return self

    def __next__(self):
        current = self.start
        self.start = self.start * 2
        self.count += 1
        if not self.infinity:
            if self.count <= self.count_end:
                return current
        else:
            if self.count < self.count_end:
                return current
            else:
                self.count = 0
                self.start = self.begin
                return current

        raise StopIteration

# test_lst2 = List2(10)
# test_iter_lst2 = iter(test_lst2)
#
# for i in test_lst2:
#     print(i)
# next(test_iter_lst2)

# test_lst2v2 = List2v2(10, 10, True)
# test_iter_lst2v2 = iter(test_lst2v2)
#
# for i in test_iter_lst2v2:
#     print(i)

# for i in range(20):
#     print(next(test_iter_lst2v2))
