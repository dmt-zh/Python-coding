# Максимум в скользящем окне
# Найти максимум в каждом окне размера m данного массива чисел A[1 . . . n].
# Вход. Массив чисел A[1 . . . n] и число 1 ≤ m ≤ n.
# Выход. Максимум подмассива A[i...i + m − 1] для всех 1 ≤ i ≤ n − m + 1.

import numpy as np
n = int(input())
arr = np.array([int(x) for x in input().split()])
m = int(input())


res = []

for i in range(n - m + 1):
    res.append(arr[i:i + m].max())
print(*res)