# Хеширование цепочками.
# Ваша цель в данной задаче — реализовать такую схему, используя таблицу с m ячейками и полиномиальной хеш-функцией
# на строках:
#         ∣s∣−1
# h(S) = ((∑  S[i](x**i)) %p ) %m
#         i=0

# где S[i] — ASCII-код i-го символа строки S, p = 1 000 000 007 — простое число, а x = 263. Ваша программа должна
# поддерживать следующие
# типы запросов:
# • add string: добавить строку string в таблицу. Если такая строка уже есть, проигнорировать запрос;
# • del string: удалить строку string из таблицы. Если такой строки нет, проигнорировать запрос;
# • find string: вывести «yes» или «no» в зависимости от того, есть в таблице строка string или нет;
# • check i: вывести i-й список (используя пробел в качестве разделителя); если i-й список пуст, вывести пустую строку.
# При добавлении строки в цепочку, строка должна добавляться в начало цепочки.

# Формат входа. Первая строка размер хеш-таблицы m. Следующая строка содержит количество запросов n. Каждая из последую-
# щих n строк содержит запрос одного из перечисленных выше четырёх типов.
# Формат выхода. Для каждого из запросов типа find и check выведите результат в отдельной строке.

# Sample Input 2:
# 4
# 8
# add test
# add test
# find test
# del test
# find test
# find Test
# add Test
# find Test

# Sample Output 2:
# yes
# no
# no
# yes


import sys

read = sys.stdin
m = int(read.readline())
size = int(read.readline())
p = 1000000007
x = {i: pow(263, i, p) for i in range(1, 16)}

linked = [[] for _ in range(m)]


def string_hash(strng):
    for polynom, char in enumerate(strng):
        if polynom == 0:
            hashing = ord(char)
        else:
            hashing = hashing + ord(char) * x[polynom]
    hashing = (hashing % p) % m
    return hashing

for _ in range(size):
    line = read.readline().strip().split()
    if line[0].startswith('add'):
        hash_ = string_hash(line[1])
        if line[1] not in linked[hash_]:
            linked[hash_].insert(0, line[1])

    if line[0].startswith('check'):
        print(*linked[int(line[1])])

    if line[0].startswith('find'):
        print('yes' if line[1] in linked[string_hash(line[1])] else 'no')

    if line[0].startswith('del'):
        hash_ = string_hash(line[1])
        if line[1] in linked[hash_]:
            linked[hash_].remove(line[1])