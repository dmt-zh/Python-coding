# Объявите в программе класс Vector, объекты которого создаются командой:
# v = Vector(x1, x2, x3,..., xN)
# где x1, x2, x3,..., xN - координаты вектора (числа: целые или вещественные).

# С каждым объектом класса Vector должны выполняться операторы:
# v1 + v2 # суммирование соответствующих координат векторов
# v1 - v2 # вычитание соответствующих координат векторов
# v1 * v2 # умножение соответствующих координат векторов

# v1 += 10 # прибавление ко всем координатам вектора числа 10
# v1 -= 10 # вычитание из всех координат вектора числа 10
# v1 += v2
# v2 -= v1

# v1 == v2 # True, если соответствующие координаты векторов равны
# v1 != v2 # True, если хотя бы одна пара координат векторов не совпадает

# При реализации бинарных операторов +, -, * следует создавать новые объекты класса Vector с новыми
# (вычисленными) координатами. При реализации операторов +=, -= координаты меняются в текущем объекте,
# не создавая новый.

# Если число координат (размерность) векторов v1 и v2 не совпадает, то при операторах +, -, * должно
# генерироваться исключение командой: raise ArithmeticError('размерности векторов не совпадают').




import operator as op

class Vector:
    def __init__(self, *coords):
        self.coords = list(coords)

    @staticmethod
    def __check_vector(vec):
        if not isinstance(vec, Vector):
            raise TypeError('операнд должен принадлежать классу Vector')

    def __valid__dimensions(self, other):
        self.__check_vector(other)
        if len(self.coords) != len(other.coords):
            raise ArithmeticError('размерности векторов не совпадают')

    def __make_operation(self, other, func, vector=True):
        if type(other) in (int, float):
            new_coords = (func(coord, other) for coord in self.coords)
            self.coords = (*new_coords,)
        else:
            self.__check_vector(other)
            self.__valid__dimensions(other)
            new_coords = (func(coord1, coord2) for coord1, coord2 in zip(self.coords, other.coords))
        return Vector(*new_coords) if vector else self

    def __add__(self, other):
        return self.__make_operation(other, op.add)

    def __iadd__(self, other):
        return self.__make_operation(other, op.add, vector=False)

    def __sub__(self, other):
        return self.__make_operation(other, op.sub)

    def __isub__(self, other):
        return self.__make_operation(other, op.sub, vector=False)

    def __mul__(self, other):
        return self.__make_operation(other, op.mul)

    def __eq__(self, other):
        self.__check_vector(other)
        self.__valid__dimensions(other)
        return all(x == y for x, y in zip(self.coords, other.coords))