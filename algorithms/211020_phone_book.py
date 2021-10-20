# Телефонная книга
# Реализовать структуру данных, эффективно обрабатывающую запросы вида add number name, del number и find number.
# Вход. Последовательность запросов вида add number name, del number и find number, где number — телефонный номер,
# содержащий не более семи знаков, а name — короткая строка.
# Выход. Для каждого запроса find number выведите соответствующее имя или сообщите, что такой записи нет.

# Sample Input 1:
# 12
# add 911 police
# add 76213 Mom
# add 17239 Bob
# find 76213
# find 910
# find 911
# del 910
# del 911
# find 911
# find 76213
# add 76213 daddy
# find 76213

# Sample Output 1:
# Mom
# not found
# police
# not found
# Mom
# daddy

import sys

book = {}
read = sys.stdin
size = int(read.readline())

for _ in range(size):
    line = read.readline().strip().split()
    if line[0].startswith('add'):
        book[line[1]] = line[2]
    elif line[0].startswith('find'):
        print(book[line[1]] if line[1] in book else 'not found')
    elif line[0].startswith('del'):
        if line[1] in book:
            del book[line[1]]
