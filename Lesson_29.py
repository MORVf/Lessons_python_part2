"""Текст задания.

Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
Буквой считается символ из группы \w.

Sample Input:
attraction
buzzzz

Sample Output:
atraction
buz

"""

__version__ = '1.0.0'
__author__ = 'Evgenii Mayorov'

import sys
import re

SUB_STRING = r'(\w)(\1+)'

for line in sys.stdin:
    line = line.rstrip()
    if not line:
        break
    else:
        line = re.sub(SUB_STRING, r'\1', line)
        print(line)
