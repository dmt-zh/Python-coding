# Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
# (число повторяется столько раз, чему равно). На вход программе передаётся неотрицательное целое
# число n — столько элементов последовательности должна отобразить программа. На выходе ожидается
# последовательность чисел, записанных через пробел в одну строку.
# Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.

num = int(input())
arr1 = []
arr2 = []

for i in range(num+1):
    arr1.append([i] * i)
for j in arr1:
    if isinstance(j, list):
        for k in j:
            arr2.append(k)
print(*arr2[:num])