"""Текст задания.

Вам дана последовательность строк.
В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
Буквой считается символ из группы \w.

Sample Input:
this is a text
"this' !is. ?n1ce,

Sample Output:
htis si a etxt
"htis' !si. ?1nce,

"""

__version__ = '1.0.0'
__author__ = 'Evgenii Mayorov'

import sys
import re

SUB_STRING = r'\b(\w)(\w)'

for line in sys.stdin:
    line = line.rstrip()
    if not line:
        break
    else:
        line = re.sub(SUB_STRING, r'\2\1', line)
        print(line)
