"""4. Задания
4.1. Напишите функцию, которая возвращает два списка: все файлы в текущем каталоге, включая файлы из его подкаталогов произвольной вложенности,
и все каталоги в текущем каталоге, включая подкаталоги произвольной вложенности.

4.2. Напишите функцию, которая удаляет каталог (возможно, непустой) и все файлы внутри него.
Если внутри каталога есть подкаталоги, ничего удалять не надо. """
import os
def dir_all(dir=os.getcwd()):
    if not os.path.isdir(dir):
        return None, 'No such directory'
    lst_files, lst_dir = [], []
    for i in os.walk(dir):
        for k in i[2]:
            lst_files += [i[0]+'\\'+ k]
        for k in i[1]:
            lst_dir += [i[0]+'\\'+ k]
    return lst_files, lst_dir

def delenddir(dir):
    lst_of_files, lst_of_dir = dir_all(dir)
    if len(lst_of_dir) > 0:
        return None, 'is some dir in dir'
    for f in lst_of_files:
        os.remove(f)
    os.rmdir(dir)


# print(dir_all('own_main\\test'))
delenddir('own_main\\test')