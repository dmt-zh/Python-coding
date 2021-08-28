# Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку
# значения, которые встречаются в нём более одного раза.
# Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
# Sample Input 1:       Sample Input 2:
# 4 8 0 3 4 2 0 3       10
# Sample Output 1:      Sample Output 2:
# 0 3 4

arr = [int(i) for i in input().split()]

from collections import Counter
cnt = Counter(arr)
[print(k) for k, v in cnt.items() if v > 1]
