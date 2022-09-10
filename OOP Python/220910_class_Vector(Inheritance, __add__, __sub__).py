# Объявите в программе класс Vector, объекты которого создаются командой:
# v = Vector(x1, x2, ..., xN)
# где x1, x2, ..., xN - координаты радиус-вектора (числа: целые или вещественные).

# С объектами этого класса должны выполняться команды:
# v1 = Vector(1, 2, 3)
# v2 = Vector(3, 4, 5)
# v = v1 + v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
# v = v1 - v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами

# Если размерности векторов v1 и v2 не совпадают, то генерировать исключение:
# raise TypeError('размерности векторов не совпадают')
# В самом классе Vector объявите метод с именем get_coords, который возвращает кортеж из текущих координат вектора.
# На основе класса Vector объявите дочерний класс VectorInt для работы с целочисленными координатами:
# v = VectorInt(1, 2, 3, 4)
# v = VectorInt(1, 0.2, 3, 4) # ошибка: генерируется исключение raise ValueError('координаты должны быть целыми числами')

# При операциях сложения и вычитания с объектом класса VectorInt:
# v = v1 + v2  # v1 - объект класса VectorInt
# v = v1 - v2  # v1 - объект класса VectorInt
# должен формироваться объект v как объект класса Vector, если хотя бы одна координата является вещественной.
# Иначе, v должен быть объектом класса VectorInt.




class Vector:
    _valid_types = (int, float)

    def __init__(self, *args):
        self.__check_coords(args)
        self.__coords = args

    def get_coords(self):
        return tuple(self.__coords)

    def __check_coords(self, values):
        if not all(type(x) in self._valid_types for x in values):
            raise ValueError('неверный тип координат')

    @staticmethod
    def __check_vector(vec):
        if not isinstance(vec, Vector):
            raise TypeError('операнд должен принадлежать классу Vector или его дочернему классу')

    def __valid__dimensions(self, other):
        self.__check_vector(other)
        if len(self.__coords) != len(other.get_coords()):
            raise TypeError('размерности векторов не совпадают')

    def __make_vector(self, coords):
        try:
            return self.__class__(*coords)
        except ValueError:
            return Vector(*coords)

    def __add__(self, other):
        self.__check_vector(other)
        self.__valid__dimensions(other)

        new_coords = tuple(x + y for x, y in zip(self.__coords, other.get_coords()))
        return self.__make_vector(new_coords)

    def __sub__(self, other):
        self.__check_vector(other)
        self.__valid__dimensions(other)

        new_coords = tuple(x - y for x, y in zip(self.__coords, other.get_coords()))
        return self.__make_vector(new_coords)


class VectorInt(Vector):
    _valid_types = (int,)
