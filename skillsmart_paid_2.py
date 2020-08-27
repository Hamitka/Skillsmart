# -*- coding: utf8 -*-
"""3. Задание
Подготовьте иерархию из трёх классов -- один родительский, и два наследника. В родительском классе сделайте метод, условно, foo(), а в дочерних классах переопределите его. В каждой из трёх реализаций foo() выводите в консоль что-то оригинальное, чтобы можно было различить, для какого класса foo() вызывается.
Создайте список из 10 объектов, где будут случайно перемешаны 10 объектов двух дочерних классов, и в цикле, не зная где какой объект, вызывайте foo().
Не забывайте, что объекты обычным присваиванием не копируются.
Почему получится такой вывод? """

import random


class Parent:
    def say(self):
        print('Im the BOSS')


class Daughter(Parent):
    def say(self):
        print('Im daughter')


class Son(Parent):
    def say(self):
        print('Im son')


list_child = [random.choice([Daughter(), Son()]) for _ in range(10)]

[i.say() for i in list_child]

#а то именно в выводе надо объячнить?