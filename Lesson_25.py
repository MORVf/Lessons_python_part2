"""Текст задания.

Вам дана последовательность строк.
В каждой строке замените все вхождения подстроки "human" на подстроку "computer" 
и выведите полученные строки.

Sample Input:
I need to understand the human mind
humanity

Sample Output:
I need to understand the computer mind
computerity

"""

__version__ == '1.0.0'
__author__ = 'Evgenii Mayorov'

import sys
import re

SUB_STRING = r'human'

for line in sys.stdin:
    line = line.rstrip()
    if not line:
        break
    else:
        line = re.sub(SUB_STRING, 'computer', line)
        print(line)
