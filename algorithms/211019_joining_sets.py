# Объединение таблиц
# Ваша цель в данной задаче — реализовать симуляцию объединения таблиц в базе данных. В базе данных есть n таблиц,
# пронумерованных от 1 до n, над одним и тем же множеством столбцов (атрибутов). Каждая таблица содержит либо реальные
# записи в таблице, либо символьную ссылку на другую таблицу. Изначально все таблицы содержат реальные записи, и i-я
# таблица содержит r_i записей. Ваша цель — обработать m запросов типа ( destination_i, source_i).

# 1. Рассмотрим таблицу с номером destinationi. Пройдясь по цепочке символьных ссылок, найдём номер реальной таблицы,
# на которую ссылается эта таблица: пока таблица destination_i содержит символическую ссылку: destination_i ← symlink(destination_i)
# 2. Сделаем то же самое с таблицей source_i.
# 3. Теперь таблицы destinationi и sourcei содержат реальные записи. Если destination_i != source_i, скопируем все
# записи из таблицы source_i в таблицу destination_i, очистим таблицу source_i и пропишем в неё символическую ссылку
# на таблицу destination_i.
# 4. Выведем максимальный размер среди всех n таблиц. Размером таблицы называется число строк в ней. Если таблица содержит
# символическую ссылку, считаем её размер равным нулю.

# Формат входа. Первая строка содержит числа n и m — число таблиц и число запросов, соответственно. Вторая строка
# содержит n целых чисел r 1, .. . ,r_n — размеры таблиц. Каждая из последующих m строк содержит два номера таблиц
# destination_i и source_i, которые необходимо объединить.

# Формат выхода. Для каждого из m запросов выведите максимальный размер таблицы после соответствующего объединения.

# Sample Input:
# 5 5
# 1 1 1 1 1
# 3 5
# 2 4
# 1 4
# 5 4
# 5 3

# Sample Output:
# 2
# 2
# 3
# 5
# 5


n, m = list(map(int, input().split()))
tables = list(map(int, input().split()))
requests = [list(map(int, input().split())) for _ in range(m)]


parent = [i for i in range(n)]
max_size = max(tables)


def find(i):
    if i != parent[i]:
        parent[i] = find(parent[i])
    return parent[i]


def union(set_one, set_two):

    global max_size
    set_one = find(set_one - 1)
    set_two = find(set_two - 1)

    if set_one != set_two:
        parent[set_two] = parent[set_one]
        tables[set_one] += tables[set_two]

    if tables[set_one] > max_size:
        max_size = tables[set_one]
    return max_size


for sets in requests:
    print(union(*sets))