""" Задание
Оформите последний код в функцию так, чтобы она работала с
неограниченным количеством "одновременно" выполняющихся генераторов long_process
(сейчас их три). В качестве входных данных этой функции используйте список
из целых значений, которые сейчас служат вторым параметром функции long_process.
Например, для последнего примера входным будет список [10, 100, 256]. """


def long_process(id, n):
    sum = 0
    for x in range(n):
        sum += x
        print(id, sum)
        if x < n - 1:
            yield
        else:
            yield sum


def sum_thread(some_list: list):
    R = {}
    list_thread = []
    for i, num in enumerate(some_list):
        name_thread = 'Thread N' + str(i)
        some_thread = long_process(name_thread, num)
        list_thread.append(some_thread)
        R[some_thread] = None
    for i in range(max(some_list)):
        for key in R.keys():
            if R[key] is None: R[key] = next(key)
    return R

print(sum_thread([10, 100, 256, 512, 1024]))