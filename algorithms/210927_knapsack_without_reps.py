# Задача на программирование: рюкзак
# Первая строка входа содержит целые числа 1 ≤ W ≤ 10^4 и 1 ≤ n ≤ 300 — вместимость рюкзака и число золотых слитков.
# Следующая строка содержит n целых чисел 0 ≤ w,…,w_n ≤ 10^5, задающих веса слитков. Найдите максимальный вес золота,
# который можно унести в рюкзаке.
#
# Sample Input:
# 10 3
# 1 4 8
#
# Sample Output:
# 9

weight, items = list(map(int, input().split()))
arr = list(map(int, input().split()))

def knapsack_without_reps(arr, weight, items):
    mtx = [[0 for _ in range(weight+1)] for _ in range(items+1)]

    for i in range(1, items+1):
        for j in range(1, weight+1):
            mtx[i][j] = mtx[i-1][j]
            if arr[i-1] <= j:
                mtx[i][j] = max(mtx[i][j], mtx[i-1][j - arr[i-1]] + arr[i-1])

    return mtx[items][weight]

print(knapsack_without_reps(arr, weight, items))


# Без использования матрицы
def knapsack_without_reps(arr, weight):

    prev, curr = [0] * (weight+1), [0] * (weight+1)

    for i in arr:
        prev, curr = curr, prev
        for j in range(weight+1):
            curr[j] = prev[j] if i > j else max(prev[j], prev[j-i]+i)
    return curr[-1]

print(knapsack_without_reps(arr, weight))
