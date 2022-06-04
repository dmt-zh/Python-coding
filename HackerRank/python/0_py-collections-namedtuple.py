# Dr. John Wesley has a spreadsheet containing a list of student's ID, MARKS, CLASS and NAME.
# Your task is to help Dr. Wesley calculate the average marks of the students.

# Sample Input
# 5
# ID         MARKS      NAME       CLASS
# 1          97         Raymond    7
# 2          50         Steven     4
# 3          91         Adrian     9
# 4          72         Stewart    5
# 5          80         Peter      6

# Sample Output
# 78.00

from collections import namedtuple
n = int(input().strip())
col_names = ' '.join(input().strip().split())
STUDENT = namedtuple('Student', col_names)

acc = 0
for _ in range(n):
    info = [int(i) if i.isdigit() else i for i in input().split()]
    std = STUDENT(*info)
    acc += std.MARKS

print(f'{acc/n:.2f}')