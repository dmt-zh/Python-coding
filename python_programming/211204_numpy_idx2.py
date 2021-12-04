# На вход подаётся 2 набора целых чисел. Создайте вектор V такой, что он будет содержать числа из 1 набора, делящиеся
# нацело на предпоследнее число из 2 набора и разделённые на это число. Если таких чисел не найдётся, то вектор V будет
# пустым (т.е. не будет содержать элементов).

# Sample Input 1:
# 1, 2, 3, 4, 5, 6
# 1, 2, 3, 4

# Sample Output 1:
# V[<class 'numpy.ndarray'>]: [1. 2.]

# Sample Input 2:
# 1, 2
# 10, 10

# Sample Output 2:
# V[<class 'numpy.ndarray'>]: []


import numpy as np

v1 = np.fromstring(input(), dtype=int, sep=', ')
v2 = np.fromstring(input(), dtype=int, sep=', ')

V = v1[v1 % v2[-2] == 0] / v2[-2]