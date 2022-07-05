# You are given a string S.
# Your task is to find the first occurrence of an alphanumeric character
# in S(read from left to right) that has consecutive repetitions.

# Sample Input
# ..12345678910111213141516171820212223

# Sample Output
# 1

# Explanation
# .. is the first repeating character, but it is not alphanumeric.
# 1 is the first (from left to right) alphanumeric repeating character of the string in the substring 111.


import re
s = input().strip()
try:
    print(re.search(r'([0-9a-zA-Z]+)\1', s).group(1))
except:
    print(-1)