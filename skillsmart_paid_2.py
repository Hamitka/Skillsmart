""" Задание
Напишите функцию, которая получает на вход два параметра:
имя файла архива и расширение файла, сканирует текущий каталог в поисках файлов с подходящим расширением,
и добавляет их в архив (исходно этот архив не существует). """
import os.path
from zipfile import ZipFile


def extfiletozip(zip_name: str, extention: str) -> bool:
    """create new zip file with all files in current directory and given extension"""
    lst_files = []
    for root_dir_files in os.walk(os.getcwd()):
        for file in root_dir_files[2]:
            if os.path.splitext(file)[1] == extention and os.path.isfile(file):
                lst_files += [file]
    if not lst_files:
        return False
    # print (*lst_files, sep='\n')
    with ZipFile(zip_name, 'w') as filezip:
        for f in lst_files:
            filezip.write(f)
    return True


extfiletozip('test.zip', '.py')
