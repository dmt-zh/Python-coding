# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.

import sys
import re
pattern = r'cat'

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'cat'
    if len(re.findall(pattern, line)) >= 2:
        print(line)

