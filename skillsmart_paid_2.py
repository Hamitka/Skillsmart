""" Задание
Напишите функцию, которая получает на вход два параметра:
имя файла архива и расширение файла, сканирует текущий каталог в поисках файлов с подходящим расширением,
и добавляет их в архив (исходно этот архив не существует). """
import os.path


def extfiletozip(zip_name: str, extention: str) -> bool:
    lst_files = []
    for root_fir_files in os.walk(os.getcwd()):
        for file in root_fir_files[2]:
            if os.path.splitext(file)[1] == extention and os.path.isfile(file):
                lst_files += [root_fir_files[0] + '\\' + file]
    print (*lst_files, sep='\n')
    return True


extfiletozip('test.zip', '.py')
# from zipfile import ZipFile
#
# with ZipFile('test.zip') as ziptest:
#     print(ziptest.testzip())
#     print(ziptest.namelist())
#     with ziptest.open('skillsmart_LinkedList2.py') as file:
#         print(file.read())
