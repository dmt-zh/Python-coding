# In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools.
# You are given a string S. Suppose a character 'c' occurs consecutively X times in the string.
# Replace these consecutive occurrences of the character 'c' with (X, c) in the string.

# Sample Input
# 1222311

# Sample Output
# (1, 1) (3, 2) (1, 3) (2, 1)

from itertools import groupby
s = input().strip()
print(*[(len([i for i in iter_item]), int(item)) for item, iter_item in groupby(s)])