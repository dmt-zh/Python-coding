# Числа Фибоначчи.
# Дано целое число 1 ≤ n ≤ 40, необходимо вычислить n-е число Фибоначчи (напомним, что F_0=0, F_1=1 и
# F_n = F_{n-1} + F_{n-2} при n ≥ 2).

def fib(n):
    if n <= 1:
        return n
    else:
        fib_arr = [0, 1,]
        for i in range(n):
            fib_arr.append(fib_arr[i] + fib_arr[i + 1])
        return fib_arr[n]

def main():
    n = int(input())
    print(fib(n))

if __name__ == "__main__":
    main()



# Реализация через математическу формулу:
def fibonacci(num):
    from math import sqrt
    if num <= 1:
        return num
    else:
        return round(1/sqrt(5) * ((1 + sqrt(5))/2)**num)
