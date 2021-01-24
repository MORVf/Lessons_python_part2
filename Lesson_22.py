"""Текст задания.

Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве слова.

Sample Input:
cat
catapult and cat
catcat
concat
Cat
"cat"
!cat?

Sample Output:
cat
catapult and cat
"cat"
!cat?

"""

__version__ = '1.0.0'
__author__ = 'Evgenii Mayorov'

import sys
import re

SUB_STRING = r'\bcat\b'

for line in sys.stdin:
    line = line.rstrip()
    if not line:
        break
    elif re.search(SUB_STRING, line) is not None:
        print(line)
