"""3. Задания
3.1. Программно создайте 10 файлов с именами 1.txt, 2.txt, ..., 10.txt,
и в каждый запишите три случайных числа, каждое с новой строки.

3.2. Напишите программу, которая получает на вход два случайных числа от 1 до 10,
по этим числам открывает два соответствующих файла из задания выше, и возвращает сумму шести чисел (содержимое обоих файлов).
Обрабатывайте ситуацию, когда содержимое файла неполно или испорчено. """

import random
path = 'some_files/'
# for i in  range(1, 11):
#     with open(path + str(i) + '.txt', 'w') as file:
#         for i in range(3):
#             file.write(str(random.randint(1, 100000))+'\n')

lst_in = []
for k in range(2):
    j = random.randint(1, 2)
    print('try to open file: ', j, '.txt', sep='')
    with open(path + str(j) + '.txt') as file:
        for data in file:
            lst_in += [data.strip()]
lst_out = []

#Обрабатывайте ситуацию, когда содержимое файла неполно или испорчено.
try:
    for i in range(6):
        lst_out += [int(lst_in[i])]
except IndexError:
    print ('more than 6 numbers')
except ValueError:
    print('\'', lst_in[i], '\'', 'is not numeric')
else:
    if len(lst_out) < 6:
        print('less than 6 numbers')
    elif len(lst_in) > 6:
        print ('more than 6 numbers after second file')
    else:
        print('sum of int values in two random files:', sum(lst_out))



