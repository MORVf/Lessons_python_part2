"""Текст задания.

Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.

Sample Input:
catcat
cat and cat
catac
cat
ccaatt

Sample Output:
catcat
cat and cat

"""

__version__ = '1.0.0'
__author__ = 'Evgenii Mayorov'

import sys
import re

SUB_STRING = r'cat'

for line in sys.stdin:
    line = line.rstrip()
    if not line:  # если пустая строка, то завершаем выполнение
        break
    elif len(re.findall(SUB_STRING, line)) >= 2:
        print(line)
