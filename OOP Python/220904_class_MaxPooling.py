# В нейронных сетях использую операцию под названием Max Pooling. Суть ее состоит в сканировании 
# прямоугольной таблицы чисел (матрицы) окном определенного размера (обычно, 2x2 элемента) и выбора
# наибольшего значения в пределах этого окна.
# Или, если окна выходят за пределы матрицы, то они пропускаются (игнорируются).

# Мы повторим эту процедуру. Для этого в программе нужно объявить класс с именем MaxPooling, 
# объекты которого создаются командой: mp = MaxPooling(step=(2, 2), size=(2,2))
# где step - шаг смещения окна по горизонтали и вертикали; size - размер окна по горизонтали и вертикали.

# Параметры step и size по умолчанию должны принимать кортеж со значениями (2, 2).
# Для выполнения операции Max Pooling используется команда:
# res = mp(matrix)
# где matrix - прямоугольная таблица чисел; res - ссылка на результат обработки таблицы matrix 
# (должна создаваться новая таблица чисел.

# Прямоугольную таблицу чисел следует описывать вложенными списками. Если при сканировании таблицы часть
# окна выходит за ее пределы, то эти данные отбрасывать (не учитывать все окно).

# Если matrix не является прямоугольной таблицей или содержит хотя бы одно не числовое значение, то 
# должно генерироваться исключение командой: raise ValueError("Неверный формат для первого параметра matrix.")

# Пример использования класса:
# mp = MaxPooling(step=(2, 2), size=(2,2))
# res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])    # [[6, 8], [9, 7]]




import numpy as np
from itertools import product

class MaxPooling:
    __VALID_TYPES = (int, float, np.int32, np.int64, np.float32, np.float64)

    def __init__(self, step=(2, 2), size=(2, 2)):
        self._step = step
        self._size = size

    @classmethod
    def __matrix_is_valid(cls, mtx):
        numbers_only = all(all(type(x) in cls.__VALID_TYPES for x in arr) for arr in mtx)
        correct_shape = len(set(len(arr) for arr in mtx)) == 1
        if numbers_only and correct_shape:
            return np.array(mtx)
        else:
            raise ValueError("Неверный формат для первого параметра matrix.")
        
    def __call__(self, matrix, *args, **kwds):
        mtx = self.__matrix_is_valid(matrix)
        max_elements = []

        indexes_rows = tuple((i, i+self._size[0]) for i in range(0, mtx.shape[0], self._step[0]))
        indexes_cols = tuple((j, j+self._size[1]) for j in range(0, mtx.shape[1], self._step[1]))

        for indx_row, indx_col in product(indexes_rows, indexes_cols):
            sub_mtx = mtx[indx_row[0]:indx_row[1], indx_col[0]:indx_col[1]]
            if sub_mtx.shape == self._size:
                max_elements.append(sub_mtx.max())

        try:
            return np.array(max_elements).reshape(len(indexes_cols), len(indexes_rows)).tolist()
        except:
            return max_elements