# Число называется простым, если оно делится только на 1 и само себя. Напишите функцию is_prime(n),
# проверяющую простое ли число. Если число простое, функция должна вернуть True, иначе False
# (логическое значение, не строку!).

# Sample Input:
# 7, 15, 99, 103

# Sample Output:
# True False False True


def is_prime(x):
    if x in [0, 1]:
        return True
    if x >= 2:
        cnt = 0
        for num in range(2, int(x**0.5) + 1):
            while x % num == 0:
                cnt += 1
                x //= num
        if x != 1:
            cnt += 1
    return False if cnt >= 2 else True
