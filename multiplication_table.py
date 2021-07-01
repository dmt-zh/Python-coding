# Когда Павел учился в школе, он запоминал таблицу умножения прямоугольными блоками.
# Для тренировок ему бы очень пригодилась программа, которая показывала бы блок таблицы умножения.
# Напишите программу, на вход которой даются четыре числа a, b, c и d, каждое в своей строке.
# Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a;b] на все числа отрезка [c;d].
# Числа a, b, c и d являются натуральными и не превосходят 10, a≤b, c≤d.
# Следуйте формату вывода из примера, для разделения элементов внутри строки используйте '\t' — символ табуляции.
# Заметьте, что левым столбцом и верхней строкой выводятся сами числа из заданных отрезков — заголовочные столбец и
# строка таблицы.
# Sample Input:
# 7
# 10
# 5
# 6
#
# Sample Output:
# 	 5	6
# 7	 35	42
# 8	 40	48
# 9	 45	54
# 10 50	60

a = int(input())
b = int(input())
c = int(input())
d = int(input())

for i in range(c, d + 1):
    print('\t', i, end='')
for k in range(a, b + 1):
    print('\n', k, end='')
    for j in range (c, d + 1):
        print('\t', k * j, end='')