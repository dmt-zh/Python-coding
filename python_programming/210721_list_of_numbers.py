# Напишите программу, на вход которой подаётся список чисел одной строкой.
# Программа должна для каждого элемента этого списка вывести сумму двух его соседей.
# Для элементов списка, являющихся крайними, одним из соседей считается элемент,
# находящий на противоположном конце этого списка. Например, если на вход подаётся список "1 3 5 6 10",
# то на выход ожидается список "13 6 9 15 7" (без кавычек).
# Если на вход пришло только одно число, надо вывести его же.
# Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.

num = [int(i) for i in input().split()]
res = []
if not len(num) > 1:
    res.append(num[0])
else:
    [res.append(num[i - 1] + num[i + 1 - len(num)]) for i in range(len(num))]
print(*res)
