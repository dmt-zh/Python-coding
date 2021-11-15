# Число Капрекара в произвольной системе счисления
# Напишите функцию kaprekar(n, base=10), принимающую на вход натуральное число (int для десятичной системы счисления,
# либо строку для иной) и основание системы счисления, а возвращающую:
#     True, если число является Числом Капрекара
#     False, если число НЕ является Числом Капрекара
# По умолчанию функция считает, что передаваемое число в десятичной системе счисления.


def convert(num, from_base=10, to_base=10):
    n = int(num, from_base) if isinstance(num, str) else num
    alphabet, res = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', ''
    while n > 0:
        n, m = divmod(n, to_base)
        res += alphabet[m]
    return res[::-1]


def kaprekar(n, base=10):
    num = int(convert(n, from_base=base))
    s = convert(num**2, to_base=base)
    for i in range(1, len(s)):
        if int(s[i:], base) != 0 and int(s[0:i], base) + int(s[i:], base) == num:
            return True
    return False