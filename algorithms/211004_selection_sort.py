# Реализация сортировки методом выбора

import random
lst = [random.random() for _ in range(20)]

def selection_sort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

print(selection_sort(lst))


# Тестирование алгоритма на рандомных данных
def algorithm_testing(n_iter=100):
    for i in range(n_iter):
        length = random.randint(0, 1000)
        array = [random.randint(0, 1000) for _ in range(length)]
        check = array[:]
        assert selection_sort(array) == sorted(check)

algorithm_testing()