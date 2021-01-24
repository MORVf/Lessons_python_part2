"""Текст задания.

Вам дана последовательность строк.
Выведите строки, содержащие обратный слеш "\".

Sample Input:
\w denotes word character
No slashes here

Sample Output:
\w denotes word character

"""

__version__ = '1.0.0'
__author__ = 'Evgenii Mayorov'

import sys
import re

SUB_STRING = r'\\'

for line in sys.stdin:
    line = line.rstrip()
    if not line:
        break
    elif re.search(SUB_STRING, line) is not None:
        print(line)
