# Объявите класс с именем ListMath, объекты которого можно создавать командами:
# lst1 = ListMath() # пустой список
# lst2 = ListMath([1, 2, -5, 7.68]) # список с начальными значениями
# В качестве значений элементов списка объекты класса ListMath должны отбирать только целые и вещественные числа,
# остальные игнорировать (если указываются в списке). Например:

# lst = ListMath([1, "abc", -5, 7.68, True]) # ListMath: [1, -5, 7.68]
# В каждом объекте класса ListMath должен быть публичный атрибут:
# lst_math - ссылка на текущий список объекта (для каждого объекта создается свой список).

# Также с объектами класса ListMath должны работать следующие операторы:
# lst = lst + 76 # сложение каждого числа списка с определенным числом
# lst = 6.5 + lst # сложение каждого числа списка с определенным числом
# lst += 76.7  # сложение каждого числа списка с определенным числом
# lst = lst - 76 # вычитание из каждого числа списка определенного числа
# lst = 7.0 - lst # вычитание из числа каждого числа списка
# lst -= 76.3
# lst = lst * 5 # умножение каждого числа списка на указанное число (в данном случае на 5)
# lst = 5 * lst # умножение каждого числа списка на указанное число (в данном случае на 5)
# lst *= 5.54
# lst = lst / 13 # деление каждого числа списка на указанное число (в данном случае на 13)
# lst = 3 / lst # деление числа на каждый элемент списка
# lst /= 13.0



import numpy as np

class ListMath:
    __VALID_TYPES = (int, float, np.int32, np.int64, np.float32, np.float64)

    def __init__(self, lst=None):
        self.lst_math = [x for x in lst if type(x) in self.__VALID_TYPES] if lst and type(lst) == list else list()

    @classmethod
    def __operand_is_valid(cls, obj):
        if not type(obj) in (int, float):
            raise ArithmeticError('Operand is not valid. Use types "int" or "float" only.')
        return True

    def __add__(self, other):
        if self.__operand_is_valid(other):
            array = np.array(self.lst_math) + other
            return ListMath(list(array))

    def __radd__(self, other):
        if self.__operand_is_valid(other):
            array = np.array(self.lst_math) + other
            return ListMath(list(array))

    def __sub__(self, other):
        if self.__operand_is_valid(other):
            array = np.array(self.lst_math) - other
            return ListMath(list(array))

    def __rsub__(self, other):
        if self.__operand_is_valid(other):
            array = other - np.array(self.lst_math)
            return ListMath(list(array))

    def __mul__(self, other):
        if self.__operand_is_valid(other):
            array = np.array(self.lst_math) * other
            return ListMath(list(array))

    def __rmul__(self, other):
        if self.__operand_is_valid(other):
            array = np.array(self.lst_math) * other
            return ListMath(list(array))

    def __truediv__(self, other):
        if self.__operand_is_valid(other):
            array = np.array(self.lst_math) / other
            return ListMath(list(array))

    def __rtruediv__(self, other):
        if self.__operand_is_valid(other):
            array = np.array(self.lst_math) / other
            return ListMath(list(array))