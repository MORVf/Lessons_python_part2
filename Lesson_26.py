"""Текст задания.

Вам дана последовательность строк.
В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" 
(регистр не важен), на слово "argh".

Sample Input:
There’ll be no more "Aaaaaaaaaaaaaaa"
AaAaAaA AaAaAaA

Sample Output:
There’ll be no more "argh"
argh AaAaAaA

"""

__version__ = '1.0.0'
__author__ = 'Evgenii Mayorov'

import sys
import re

SUB_STRING = r'\b[Aa]+\b'

for line in sys.stdin:
    line = line.rstrip()
    if not line:
        break
    elif re.findall(SUB_STRING, line) is not None:
        line = re.sub(SUB_STRING, 'argh', line, count=1)
        print(line)
