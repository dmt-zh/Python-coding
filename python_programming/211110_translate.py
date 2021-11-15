# Напишите функцию перевода числа из десятичной системы счисления в систему с основанием n.
# Функция translate должна принимать 2 параметра:
#     обязательный (исходное целое число в десятичной системе счисления);
#     необязательный, по-умолчанию 2 (основание новой системы счисления, в которую переводится число).


def translate(n, base=2):
    binary = ''
    while n != 0:
        binary += str(n % base)
        n //= base
    return binary[::-1]