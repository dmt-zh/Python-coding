# You are given a positive integer N.
# Your task is to print a palindromic triangle of size N.
# You can't take more than two lines. The first line (a for-statement) is already written for you.
# You have to complete the code using exactly one print statement.

# Note:
# Using anything related to strings will give a score of 0.
# Using more than one for-statement will give a score of 0.

# Sample Input
# 5

# Sample Output
# 1
# 121
# 12321
# 1234321
# 123454321


for i in range(1, int(input()) + 1):
    print(((10 ** i - 1) // 9) ** 2)