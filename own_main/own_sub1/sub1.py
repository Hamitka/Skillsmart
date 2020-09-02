"""5. Задание
Сформируйте собственный небольшой пакет и импортируйте из какого-нибудь модуля произвольную функцию. """

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


# list_child = [random.choice([Daughter(), Son()]) for _ in range(10)]
#
# [i.say() for i in list_child]

#а то именно в выводе надо объячнить?
