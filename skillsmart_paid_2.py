"""3. Задания
3.1. Программно создайте 10 файлов с именами 1.txt, 2.txt, ..., 10.txt,
и в каждый запишите три случайных числа, каждое с новой строки.

3.2. Напишите программу, которая получает на вход два случайных числа от 1 до 10,
по этим числам открывает два соответствующих файла из задания выше, и возвращает сумму шести чисел (содержимое обоих файлов).
Обрабатывайте ситуацию, когда содержимое файла неполно или испорчено. """

import random
path = 'some_files/'
for i in  range(1, 11):
    with open(path + str(i) + '.txt', 'w') as file:
        for i in range(3):
            file.write(str(random.randint(1, 100000))+'\n')

lst_in = []
for k in range(2):
    j = random.randint(1, 10)
    print('try to open file: ', j, '.txt', sep='')
    with open(path + str(j) + '.txt') as file:
        for data in file:
            lst_in += [int(i) for i in [data.strip()] if i.isdigit()]

#считается за?:
#Обрабатывайте ситуацию, когда содержимое файла неполно или испорчено
if len(lst_in) !=6:
    print('--attention, in both file there are not 6 int values in total--')
print ('sum of int values in two random files:', sum(lst_in))

