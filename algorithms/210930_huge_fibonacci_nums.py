# Задача на программирование повышенной сложности: огромное число Фибоначчи по модулю
# Даны целые числа 1 ≤ n ≤ 10^18 и 2 ≤ m ≤ 10^5, необходимо найти остаток от деления
# n-го числа Фибоначчи на m.

def fib_mod(n, m):
    fib_arr = [0, 1]
    for i in range(2, m*6):
        fib_arr.append((fib_arr[i-2] + fib_arr[i-1]) % m)
        if fib_arr[len(fib_arr)-2] == 0 and fib_arr[len(fib_arr)-1] == 1:
            break
    return fib_arr[n % len(fib_arr[:-2])]

