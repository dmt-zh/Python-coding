# Построение кучи. Переставить элементы заданного массива чисел так, чтобы он удовлетворял
# свойству мин-кучи.
# Вход. Массив чисел A[0 . . . n−1].
#
# A[i] ≤ A[2i + 2] для всех i. Чтобы превратить данный массив в кучу, необходимо произвести
# несколько обменов его элементов. Обменом мы называем базовую операцию, которая меняет местами
# элементы A[i] и A[j]. Ваша цель в данной задаче — преобразовать заданный массив в кучу за
# линейное количество обменов.
#
# Формат выхода. Первая строка выхода должна содержать число обменов m, которое должно удовлетворять
# неравенству 0 ≤ m ≤ 4n. Каждая из последующихm строк должна задавать обмен двух элементов массива A.
# Каждый обмен задаётся парой различных индексов 0 ≤ i != j ≤ n − 1. После применения всех обменов в
# указанном порядке массив должен превратиться в мин-кучу, то есть для всех 0 ≤ i ≤ n − 1 должны выполняться
# следующие два условия:
# • если 2i + 1 ≤ n − 1, то A[i] < A[2i + 1].
# • если 2i + 2 ≤ n − 1, то A[i] < A[2i + 2].

# Sample Input 1:
# 6
# 0 1 2 3 4 5

# Sample Output 1:
# 0

# Sample Input 2:
# 6
# 7 6 5 4 3 2

# Sample Output 2:
# 4
# 2 5
# 1 4
# 0 2
# 2 5

size = int(input())
arr = list(map(int, input().split()))

res = []

def build_heap(arr, size):
    for i in range((size-1)//2, -1, -1):
        sift_down(i, size)

def sift_down(i, size):
    max_index = i
    left_child = 2*i + 1
    right_child = 2*i + 2
    if left_child <= size-1 and arr[left_child] < arr[max_index]:
        max_index = left_child
    if right_child <= size-1 and arr[right_child] < arr[max_index]:
        max_index = right_child
    if i != max_index:
        arr[i], arr[max_index] = arr[max_index], arr[i]
        res.append(f'{i} {max_index}')
        sift_down(max_index, size)

build_heap(arr, n)
print(len(res))
print(*res, sep='\n')

