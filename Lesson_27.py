"""Текст задания.

Вам дана последовательность строк.
Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).

Sample Input:
blabla is a tandem repetition
123123 is good too
go go
aaa

Sample Output:
blabla is a tandem repetition
123123 is good too

"""

__version__ = '1.0.0'
__author__ = 'Evgenii Mayorov'

import sys
import re
 
SUB_STRING = r'\b(\w+)\1\b'

for line in sys.stdin:
    line = line.rstrip()
    if not line:
        break
    elif re.match(SUB_STRING, line) is not None:
        print(line)
