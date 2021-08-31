#           Задача на программирование: наибольший общий делитель

# По данным двум числам 1 ≤ a, b ≤ 2 * 10^9 найдите их наибольший общий делитель.
# Sample Input 1:
# 18 35

# Sample Output 1:
# 1

# Sample Input 2:
# 14159572 63967072

# Sample Output 2:
# 4

def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a >= b:
        a = a % b
        return gcd(a, b)
    if b >= a:
        b = b % a
        return gcd(a, b)


