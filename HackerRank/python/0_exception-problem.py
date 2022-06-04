# You are given two values a and b.
# Perform integer division and print a//b.

# Sample Input
# 3
# 1 0
# 2 $
# 3 1

# Sample Output
# Error Code: integer division or modulo by zero
# Error Code: invalid literal for int() with base 10: '$'
# 3

n = int(input().strip())
for _ in range(n):
    a, b = input().strip().split()
    try:
        print(int(a) // int(b))
    except ValueError as msg:
        print(f'Error Code: {msg}')
    except ZeroDivisionError:
        print(f'Error Code: integer division or modulo by zero')