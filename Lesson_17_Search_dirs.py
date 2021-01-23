"""Текст задания.

Вам дана файловая структура, состоящая из директорий и файлов.
Вам необходимо найти в данной в файловой структуре все директории, в которых есть хотя бы один файл с расширением ".py". 
Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом порядке.

"""

__all__ = ['FILE_OUT', 'DIR_START', 'lst_dirs']
__version__ = '1.0.0'
__author__ = 'Evgenii Mayorov'

import os

FILE_OUT = os.path.join("C:\\", "Documents", "file_out.txt")
DIR_START = os.path.join("C:\\", "Documents", "main")  # стартовая директория, в рамках которой будет производиться поиск
lst_dirs = []

for root_dir, dirs, files in os.walk(DIR_START):  # пробегаем все директории и поддиректории в старт. директории
    for file in files:
        if '.py' in file:
            lst_dirs += [root_dir[13::]]
            break

with open(FILE_OUT, 'w') as f_out:
    lst_dirs.sort()
    strings_concatenation = "\n".join(lst_dirs)  # конкатенируем все элементы-строки списка, соединяя их символом переноса строки
    f_out.write(strings_concatenation)
