# Реализуйте декоратор reverse_args, который передает все позиционные аргументы в декорируемую функцию func в обратном порядке.

# Примечание. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

# Sample Input 1:
# @reverse_args
# def power(a, n):
#     return a ** n
# print(power(2, 3))

# Sample Output 1:
# 9


# Sample Input 2:
# @reverse_args
# def concat(a, b, c):
#     return a + b + c  
# print(concat('apple', 'cherry', 'melon'))

# Sample Output 2:
# meloncherryapple


def reverse_args(func):
    def wrapper(*args, **kwargs):
        return func(*args[::-1], **kwargs)
    return wrapper