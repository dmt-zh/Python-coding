# Обход двоичного дерева
# Построить in-order, pre-order и post-order обходы данного двоичного дерева.
# In-order обход соответствует следующей рекурсивной процедуре, получающей на вход корень v текущего поддерева:
# произвести рекурсивный вызов для v.left, напечатать v.key, произвести рекурсивный вызов для v.right. Pre-order обход:
# напечатать v.key, произвести рекурсивный вызов для v.left, произвести рекурсивный вызов для v.right. Post-order:
# произвести рекурсивный вызов для v.left, произвести рекурсивный вызов для v.right, напечатать v.key
#
# Формат входа. Первая строка содержит число вершин n. Вершины дерева пронумерованы числами от 0 до n − 1. Вершина 0
# является корнем. Каждая из следующих n строк содержит информацию о вершинах 0 , 1 , . . . , n − 1: i-я строка задаёт
# числа keyi, lefti и righti, где keyi — ключ вершины i, lefti — индекс левого сына вершины i, а righti — индекс правого
# сына вершины i. Если у вершины i нет одного или обоих сыновей, соответствующее значение равно −1.
# Формат выхода. Три строки: in-order, pre-order и post-order обходы.

# Sample Input:
# 10
# 0 7 2
# 10 -1 -1
# 20 -1 6
# 30 8 9
# 40 3 -1
# 50 -1 -1
# 60 1 -1
# 70 5 4
# 80 -1 -1
# 90 -1 -1

# Sample Output:
# 50 70 80 30 90 40 0 20 10 60
# 0 70 50 40 30 80 90 20 60 10
# 50 80 90 30 40 70 10 60 20 0

import sys

read = sys.stdin
size = int(read.readline())
tree = [tuple(map(int, read.readline().split())) for _ in range(size)]

root = 0

def in_order(root):
    if tree[root][1] > -1:
        in_order(tree[root][1])
    print(tree[root][0], end=' ')
    if tree[root][2] > -1:
        in_order(tree[root][2])

def pre_order(root):
    print(tree[root][0], end=' ')
    if tree[root][1] > -1:
        pre_order(tree[root][1])
    if tree[root][2] > -1:
        pre_order(tree[root][2])

def post_order(root):
    if tree[root][1] > -1:
        post_order(tree[root][1])
    if tree[root][2] > -1:
        post_order(tree[root][2])
    print(tree[root][0], end=' ')

in_order(root)
print()
pre_order(root)
print()
post_order(root)