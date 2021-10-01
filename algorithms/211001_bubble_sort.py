# Реализация алгоритма пузырьковой сортировки

import random
lst = [random.randint(0, 10) for _ in range(20)]

def bubble_sort(arr):
    out = len(arr)
    while out > 1:
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        out -= 1
    return arr

print(bubble_sort(lst))


# Тестирование алгоритма на рандомных данных
def algorithm_testing(n_iter=100):
    for i in range(n_iter):
        length = random.randint(0, 1000)
        array = [random.randint(0, 1000) for _ in range(length)]
        check = array[:]
        assert bubble_sort(array) == sorted(check)

algorithm_testing()
