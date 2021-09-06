# Первая строка содержит количество предметов 1 ≤ n ≤ 10^31 и вместимость рюкзака 0 ≤ W ≤ 2 * 10^6.
# Каждая из следующих nn строк задаёт стоимость 0 ≤ ci ≤ 2 * 10^6 и объём 0 ≤ wi ≤ 2 * 10^6 предмета
# (n, W, ci, wi — целые числа). Выведите максимальную стоимость частей предметов (от каждого предмета
# можно отделить любую часть, стоимость и объём при этом пропорционально уменьшатся), помещающихся в
# данный рюкзак, с точностью не менее трёх знаков после запятой.

# Sample Input:
# 3 50
# 60 20
# 100 50
# 120 30

# Sample Output:
# 180.000

import sys

n, volume = list(map(int, input().split()))
lst = [list(map(int, line.split())) for line in sys.stdin]

sack = []
items = reversed(sorted(lst, key=lambda x: x[0]/x[1]))

for item in items:
    weight = item[1]
    cost = item[0]
    if volume < weight:
        sack.append(volume * (cost/weight))
        volume -= volume
    else:
        sack.append(cost)
        volume -= weight
        n -= 1

print(f'{sum(sack):.3f}')