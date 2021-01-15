'''
Вам дана файловая структура, состоящая из директорий и файлов.
Вам необходимо найти в данной в файловой структуре все директории, в которых есть хотя бы один файл с расширением ".py". 
Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом порядке.
'''

import os

file_out = os.path.join("C:\\", "Documents", "file_out.txt")  # выходной файл, куда будут записываться директории
dir_start = os.path.join("C:\\", "Documents", "main")  # стартовая директория, в рамках которой будет производиться поиск
lst_dirs = []  # список найденных директорий

for root_dir, dirs, files in os.walk(dir_start):  # пробегаем все директории и поддиректории в старт. директории
    for file in files:  # проверяем все файлы в директории
        if '.py' in file:  # если нашли хотя бы один файл с раширение .py, то
            lst_dirs += [root_dir[13::]]  # добавляем директорию в список
            break  # выходим из цикла

with open(file_out, 'w') as f_out:
    lst_dirs.sort()  # сортируем полученный список лексикографически
    strings_concatenation = "\n".join(lst_dirs)  # конкатенируем все элементы-строки списка, соединяя их символом переноса строки
    f_out.write(strings_concatenation)  # записываем в выходной файл полученную строку