# Задача на программирование: точки и отрезки
# В первой строке задано два целых числа 1 ≤ n ≤ 50000 и 1 ≤ m ≤ 50000 — количество отрезков и точек на прямой,
# соответственно. Следующие n строк содержат по два целых числа a_i и b_i (a_i ≤ b_i) — координаты концов отрезков.
# Последняя строка содержит m целых чисел — координаты точек. Все координаты не превышают 10^8 по модулю. Точка
# считается принадлежащей отрезку, если она находится внутри него или на границе. Для каждой точки в порядке появления
# во вводе выведите, скольким отрезкам она принадлежит.


import bisect

n, m = list(map(int, input().split()))
l, r = map(sorted, zip(*(map(int, input().split()) for _ in range(n))))
points = list(map(int, input().split()))

print(*[bisect.bisect_right(l, point) - bisect.bisect_left(r, point) for point in points])




def quick_sort(A, low, high):
    while low < high:
        pivot = partition(A, low, high)
        quick_sort(A, low, pivot-1)
        low = pivot + 1

def partition(A, low, high):
    pivot = low
    swap(A, pivot, high)
    for i in range(low, high):
        if A[i] <= A[high]:
            swap(A, i, low)
            low += 1
    swap(A, low, high)
    return low

def swap(A, dex1, dex2):
    temp = A[dex1]
    A[dex1] = A[dex2]
    A[dex2] = temp

quick_sort(l, 0, len(l)-1)
quick_sort(r, 0, len(r)-1)

print(*[bisect.bisect_right(l, point) - bisect.bisect_left(r, point) for point in points])
