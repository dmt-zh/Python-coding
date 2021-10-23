# Проверка более общего свойства дерева поиска.
# Нужно проверить общее свойство. Дереву разрешается содержать равные ключи, но они всегда должны находиться в
# правом под дереве. Формально, двоичное дерево называется деревом поиска, если для любой вершины её ключ больше
# всех ключей из её левого под дерева и не меньше всех ключей из правого поддерева.

# Sample Input:
# 3
# 2 1 2
# 1 -1 -1
# 3 -1 -1

# Sample Output:
# CORRECT

import sys

read = sys.stdin
size = int(read.readline())

tree = [tuple(map(int, read.readline().split())) for _ in range(size)]
inf = float('inf')

def in_order(root, prev=-inf):
    stack = []
    while tree and root > -1 or stack:
        if root > -1:
            stack.append(root)
            if tree[tree[root][1]][0] == tree[root][0] and tree[root][1] > -1:
                return 'INCORRECT'
            root = tree[root][1]
        else:
            root = stack.pop()
            if prev > tree[root][0]:
                return 'INCORRECT'
            prev = tree[root][0]
            root = tree[root][2]
    return 'CORRECT'

print(in_order(0))