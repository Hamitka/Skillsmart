"""Реализуйте с помощью рекурсии:
1. возведение числа N в степень M;
2. вычисление суммы цифр числа;
3. расчёт длины списка, для которого разрешена только одна операция удаления первого элемента pop(0);
4. проверка, является ли строка палиндромом;
5. печать только чётных значений из списка;
6. печать элементов списка с чётными индексами;
7. нахождение второго максимального числа в списке (с учётом, что максимальных может быть несколько, если они равны). """


def recursion_pow(N, M):
    """возведение числа N в степень M"""
    if M == 0:
        return 1
    elif M < 0:
        return 1 / (N * 1 / recursion_pow(N, M + 1))
    else:
        return N * recursion_pow(N, M - 1)


def recursion_sum_digit(num: int):
    """вычисление суммы цифр числа"""
    if num // 10 == 0:
        return num
    return num % 10 + recursion_sum_digit(num // 10)


def recursion_list_len(some_list):
    """расчёт длины списка, для которого разрешена только одна операция удаления первого элемента pop(0)"""
    try:
        some_list.pop(0)
    except IndexError:
        return 0
    return 1 + recursion_list_len(some_list)


def recursion_is_palindrome(some_string: str):
    """проверка, является ли строка палиндромом"""
    some_string = some_string.replace(' ', '')
    if len(some_string) <=1:
        return True
    return some_string[0] == some_string[-1] and recursion_is_palindrome(some_string[1:-1])



def recursion_print_even_value(some_list: list):
    """печать только чётных значений из списка"""
    if len(some_list) == 0:
        return
    temp = some_list.pop(0)
    if temp % 2 == 0:
        print(temp, end=' ')
    return recursion_print_even_value(some_list)

def recursion_print_even_index(some_list: list):
    """печать элементов списка с чётными индексами"""
    if len(some_list) == 0:
        return
    temp = len(some_list) - 1
    if temp % 2 == 0:
        print(some_list[temp], end=' ')
    some_list.pop(temp)
    return recursion_print_even_index(some_list)


def recursion_second_max(K):
    """нахождение второго максимального числа в списке
    (с учётом, что максимальных может быть несколько, если они равны)"""
    pass


print(set([(recursion_pow(2, i) == pow(2, i)) for i in range(-50, 50)]))

print(recursion_sum_digit(12345) == (1 + 2 + 3 + 4 + 5))

print(recursion_list_len([2, 3, 4, 5, 6, 7, 8, 9]) == len([2, 3, 4, 5, 6, 7, 8, 9]))

print(recursion_is_palindrome('а роза упала на лапу азора'))

recursion_print_even_value([1, 2, 3, 4, 5, 6, 7, 8, 9])
print()
recursion_print_even_index([1, 2, 3, 4, 5, 6, 7, 8, 9])
