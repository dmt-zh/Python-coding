# Напишите функцию luka(L0, L1, n), которая принимает на вход параметры: L0, L1 - 0й и 1й члены
# последовательности соответственно n - номер числа из последовательности, которое необходимо вернуть

# Sample Input 1:
# 42 13 0

# Sample Output 1:
# 42

# Sample Input 2:
# 12345 67890 5

# Sample Output 2:
# 376485

def luka(L0, L1, n):
    if n < 2:
        return L0 if n == 0 else L1
    else:
        for i in range(n):
            L0, L1 = L1, L1 + L0
    return L0