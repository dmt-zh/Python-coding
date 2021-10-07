# Вычислить высоту данного дерева.
# Вход:
# Корневое дерево с вершинами{0, ... , n−1}, заданное как последовательность parent0, ..., parentn−1,
# где parenti—родитель i-й вершины.

# Формата входа:
# Первая строка содержит натуральное число n. Вторая строка содержит n целых неотрицательных чисел
# parent0, ..., parentn−1. Для каждого 0 ≤ i ≤ n−1, parenti—родитель вершины i; если parenti = -1,
# то i является корнем. Гарантируется, что корень ровно один. Гарантируется, что данная последовательность задаёт дерево.
#
# Выход:
# Высота дерева.
# Ограничения: 1 ≤ n ≤ 10^5.


# Sample Input:
# 10
# 9 7 5 5 2 9 9 9 2 -1

# Sample Output:
# 4



import sys
sys.setrecursionlimit(20000)

n = int(input().strip())
data = list(map(int, input().split()))

tree = {}

for num, leaf in enumerate(data):
    if leaf in tree:
        tree[leaf] += [num]
    else:
        tree[leaf] = [num]

def tree_height(root):
    height = 1
    for child in tree[root]:
        if child in tree:
            height = max(height, 1+tree_height(child))
    return height

print(tree_height(-1))


