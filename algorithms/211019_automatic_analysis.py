# Автоматический анализ программ
# Проверить, можно ли присвоить переменным целые значения, чтобы выполнить заданные равенства вида
# x_i = x_j и неравенства вида x_p != x_q.

# Формат входа. Первая строка содержит числа n, e, d. Каждая из следующих e строк содержит два числа i и j
# и задаёт равенство x_i = x_j. Каждая из следующих d строк содержит два числа i и j и задаёт неравенство
# x_i != x_j. Переменные индексируются с 1: x_1, . . . , x_n.

# Формат выхода. Выведите 1, если переменным x_1, . . . , x_n можно присвоить целые значения, чтобы все равенства
# и неравенства выполнились. В противном случае выведите 0.
# Ограничения. 1 ≤ n ≤ 105; 0 ≤ e, d; e + d ≤ 2 · 10^5; 1 ≤ i, j ≤ n.

# Sample Input 1:
# 4 6 0
# 1 2
# 1 3
# 1 4
# 2 3
# 2 4
# 3 4

# Sample Output 1:
# 1

# Sample Input 2:
# 4 6 1
# 1 2
# 1 3
# 1 4
# 2 3
# 2 4
# 3 4
# 1 2

# Sample Output 2:
# 0


n, e, d = list(map(int, input().split()))
digits = [list(map(int, input().split())) for _ in range(e + d)]

parent = [i for i in range(n + 1)]


def find(i):
    if i != parent[i]:
        parent[i] = find(parent[i])
    return parent[i]


def union(set_one, set_two):
    set_one = find(set_one)
    set_two = find(set_two)

    if set_one != set_two:
        parent[set_two] = parent[set_one]


for sets in range(e):
    union(*digits[sets])
if d > 0:
    for sets in range(e, d + e):
        a = find(digits[sets][0])
        b = find(digits[sets][1])
        if a == b:
            break
    print(0 if a == b else 1)
else:
    print(1)