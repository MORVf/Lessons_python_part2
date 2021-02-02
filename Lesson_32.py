"""Текст задания.

Вам дана последовательность строк.
Выведите строки, содержащие двоичную запись числа, кратного 3.

Двоичной записью числа называется его запись в двоичной системе счисления.

Sample Input:
0
10010
00101
01001
Not a number
1 1
0 0

Sample Output:
0
10010
01001

"""

__version__ = '1.0.0'
__author__ = 'Evgenii Mayorov'

import sys

for line in sys.stdin:
    line = line.rstrip()
    if not line:
        break
    else:
        try:
            if int(line, base=2) % 3 == 0:
                print(line)
        except ValueError:
            pass
