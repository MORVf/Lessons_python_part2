"""Текст задания.

Вам дана последовательность строк.
Выведите строки, содержащие две буквы "z", между которыми ровно три символа.

Sample Input:
zabcz
zzz
zzxzz
zz
zxz
zzxzxxz

Sample Output:
zabcz
zzxzz

"""

__version__ = '1.0.0'
__author__ = 'Evgenii Mayorov'

import sys
import re

SUB_STRING = r'z.{3}z'

for line in sys.stdin:
    line = line.rstrip()
    if not line:
        break
    elif re.search(SUB_STRING, line) is not None:
        print(line)
