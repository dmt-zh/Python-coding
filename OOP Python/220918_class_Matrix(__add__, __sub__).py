# Объявите класс Matrix (матрица) для операций с матрицами. Объекты этого класса должны создаваться командой:
# m1 = Matrix(rows, cols, fill_value)
# где rows, cols - число строк и столбцов матрицы; fill_value - заполняемое начальное значение элементов матрицы
# (должно быть число: целое или вещественное). Если в качестве аргументов передаются не числа, то генерировать
# исключение: raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')

# Также объекты можно создавать командой:
# m2 = Matrix(list2D)
# где list2D - двумерный список (прямоугольный), состоящий из чисел (целых или вещественных). Если список list2D
# не прямоугольный, или хотя бы один из его элементов не число, то генерировать исключение командой:
# raise TypeError('список должен быть прямоугольным, состоящим из чисел')

# Для объектов класса Matrix должны выполняться следующие команды:
# matrix = Matrix(4, 5, 0)
# res = matrix[0, 0] # возвращается первый элемент матрицы
# matrix[indx1, indx2] = value # элементу матрицы с индексами (indx1, indx2) присваивается новое значение

# Если в результате присвоения тип данных не соответствует числу, то генерировать исключение командой:
# raise TypeError('значения матрицы должны быть числами')

# Если указываются недопустимые индексы матрицы (должны быть целыми числами от 0 и до размеров матрицы),
# то генерировать исключение:
# raise IndexError('недопустимые значения индексов')

# Также с объектами класса Matrix должны выполняться операторы:
# matrix = m1 + m2 # сложение соответствующих значений элементов матриц m1 и m2
# matrix = m1 + 10 # прибавление числа ко всем элементам матрицы m1
# matrix = m1 - m2 # вычитание соответствующих значений элементов матриц m1 и m2
# matrix = m1 - 10 # вычитание числа из всех элементов матрицы m1

# Во всех этих операция должна формироваться новая матрица с соответствующими значениями. Если размеры матриц
# не совпадают (разные хотя бы по одной оси), то генерировать исключение командой:
# raise ValueError('операции возможны только с матрицами равных размеров')



import numpy as np

class Matrix:
    __VALID_TYPES = (int, float, np.int32, np.int64, np.float32, np.float64)
    def __init__(self, *args):
        if type(args[0]) in (np.ndarray, list):
            self.__check_matrix(args[0])
            self.array = np.array(args[0])
            self.rows = len(args[0])
            self.cols = len(args[0][0])
        else:
            self.rows = args[0]
            self.cols = args[1]
            self.fill_value = args[2]
            self.array = np.array([[self.fill_value for _ in range(self.cols)] for _ in range(self.rows)])

    def __check_matrix(self, mtx):
        col_size = len(mtx[0])
        valid_cols = all(len(lst) == col_size for lst in mtx)
        valid_types = all(type(elem) in self.__VALID_TYPES for lst in mtx for elem in lst)
        if not (valid_types and valid_cols):
            raise TypeError('список должен быть прямоугольным, состоящим из чисел')

    def __check_indexes(self, r, c):
        valid_row_indx = 0 <= r < self.rows and type(r) == int
        valid_col_indx = 0 <= c < self.cols and type(c) == int
        if not (valid_row_indx and valid_col_indx):
            raise IndexError('недопустимые значения индексов')

    def __check_dimentions(self, other):
        if self.array.shape != other.array.shape:
            raise ValueError('операции возможны только с матрицами равных размеров')

    def __check_value(self, value):
        if type(value) not in self.__VALID_TYPES:
            raise TypeError('значения матрицы должны быть числами')

    def __getitem__(self, item):
        row, col = item
        self.__check_indexes(row, col)
        return self.array[row][col]

    def __setitem__(self, key, value):
        row, col = key
        self.__check_indexes(row, col)
        self.__check_value(value)
        self.array[row][col] = value

    def __add__(self, other):
        if not isinstance(other, Matrix):
            return Matrix(self.array + other)
        self.__check_dimentions(other)
        return Matrix(self.array + other.array)

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            return Matrix(self.array - other)
        self.__check_dimentions(other)
        return Matrix(self.array - other.array)