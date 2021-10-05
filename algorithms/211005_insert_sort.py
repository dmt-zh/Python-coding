# Реализация сортировки методом вставки

import random
lst = [random.random() for _ in range(10)]

def insert_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        out = i
        while out > 0 and arr[out-1] >= temp:
            arr[out] = arr[out-1]
            out -= 1
        arr[out] = temp
    return arr

print(insert_sort(lst))


# Тестирование алгоритма на рандомных данных
def algorithm_testing(n_iter=100):
    for i in range(n_iter):
        length = random.randint(0, 1000)
        array = [random.randint(0, 1000) for _ in range(length)]
        check = array[:]
        assert insert_sort(array) == sorted(check)

algorithm_testing()