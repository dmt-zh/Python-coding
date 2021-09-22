# Задача на программирование: сортировка подсчётом.
# Первая строка содержит число 1 ≤ n ≤ 10^4, вторая — n натуральных чисел, не превышающих 10.
# Выведите упорядоченную по неубыванию последовательность этих чисел.

def counting_sort(arr, n):
    lst = [0 for _ in range(10)]
    res = [0 for _ in range(n)]
    for i in range(n):
        lst[arr[i] - 1] = lst[arr[i] - 1] + 1
    for j in range(1, 10):
        lst[j] = lst[j] + lst[j - 1]
    for x in range(n-1, -1, -1):
        res[lst[arr[x] - 1] - 1] = arr[x]
        lst[arr[x] - 1] = lst[arr[x] - 1] - 1
    return res

n = int(input())
lst = list(map(int, input().split()))

print(*counting_sort(lst, n))