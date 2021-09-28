# Задача на программирование: лестница
# Даны число 1 ≤ n ≤ 10^2 ступенек лестницы и целые числа -10^4 ≤ a_1 ,…, a_n ≤ 10^4,
# которыми помечены ступеньки. Найдите максимальную сумму, которую можно получить, идя
# по лестнице снизу вверх (от нулевой до n-й ступеньки), каждый раз поднимаясь на одну или две ступеньки.


def ladder(num, arr):
    res = [0 for _ in range(num+1)]
    for i in range(1, num+1):
        step = arr[i-1]
        res[i] = max(res[i-1], res[i-2]) + step
    return res[-1]

n = int(input().strip())
lst = list(map(int, input().split()))
print(ladder(n, lst))


# Вариант без хранения массива
def ladder(arr):
    prev, curr = 0, 0
    for step in arr:
        last, prev = prev, curr
        curr = max(last, prev) + step
    return curr
