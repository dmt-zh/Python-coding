# Напишите функцию numerics(n), принимающую на вход 1 натуральное число, а возвращающую список цифр из
# которых состоит число. Если какая-то цифра встречается в исходном числе несколько раз, то и в ответе
# она должна встретиться несколько раз.

def numerics(n):
    return list(map(int, str(n)))