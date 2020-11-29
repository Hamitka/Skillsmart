""" Задание
Напишите функцию, которая получает на вход большой список вещественных чисел
(например, 10 тысяч элементов, сгенерируйте их случайным образом),
и количество процессов (целое число), которое должно просуммировать этот массив по кусочкам.

Например, задано количество процессов -- 10 и список из 100 000 элементов.
Функция запускает 10 процессов, каждый из которых суммирует свой участок списка
(по 10 000 элементов), суммирует их результаты и возвращает итоговую сумму всего списка.
Не используйте в решении join().
Проверьте корректность работы функции,
сравнив её результат с результатом обычного суммирования массива циклом. """
from random import random
from threading import Thread
import time


def lst_sum(some_list, name='', result=None):
    sum = 0
    for v in some_list:
        sum += v
        # print(name)
        # time.sleep(.00005)
    if result is not None:
        result[name] = sum
    return sum


def lst_sum_thread(some_list, num_thread):
    result_dct = {}
    size_part = len(some_list) // num_thread
    list_of_list = [some_list[i:i + size_part] for i in range(0, len(some_list), size_part)]
    for i, lst in enumerate(list_of_list):
        name = 'Thread N' + str(i)
        some_thread = Thread(target=lst_sum, name=name, args=(lst, name, result_dct))
        some_thread.start()
        # print ('%s is start' % (name))
    # print(result_dct)
    sum_total = lst_sum(list(result_dct.values()))
    return sum_total

list_float = [random() for _ in range(100000)]

print(lst_sum_thread(list_float, 10), sum(list_float))
print(lst_sum_thread(list_float, 10) == sum(list_float))
