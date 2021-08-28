# Напишите программу, которая считывает строку с числом n, которое задаёт количество чисел,
# которые нужно считать. Далее считывает n строк с числами xi, по одному числу в каждой строке.
# Итого будет n+1 строк. При считывании числа xi программа должна на отдельной строке вывести значение f(xi).
# Функция f(x) уже реализована и доступна для вызова.
# Функция вычисляется достаточно долго и зависит только от переданного аргумента x.
# Для того, чтобы уложиться в ограничение по времени, нужно избежать повторного вычисления значений.
# Sample Input:
# 5
# 5
# 12
# 9
# 20
# 12

# Sample Output:
# 11
# 41
# 47
# 61
# 41

num = int(input())
ins = ''
lst = []

while len(lst) < num:
    ins = str(input())
    lst += [int(i) for i in ins.split()]

d = {}

for i in lst:
    if i in d.keys():
        print(d[i])
    else:
        d[i] = f(i)
        print(d[i])