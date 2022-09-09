# Объявите класс с именем Triangle, объекты которого создаются командой:
# tr = Triangle(a, b, c)
# где a, b, c - длины сторон треугольника (числа: целые или вещественные). В классе Triangle объявите
# следующие дескрипторы данных: a, b, c - для записи и считывания длин сторон треугольника.

# При записи нового значения нужно проверять, что присваивается положительное число (целое или вещественное).
# Иначе, генерируется исключение командой:
# raise ValueError("длины сторон треугольника должны быть положительными числами")
# Также нужно проверять, что все три стороны a, b, c могут образовывать стороны треугольника. То есть, должны
# выполняться условия: a < b+c; b < a+c; c < a+b
# Иначе генерируется исключение командой: raise ValueError("с указанными длинами нельзя образовать треугольник")

# Наконец, с объектами класса Triangle должны выполняться функции:
# len(tr) - возвращает периметр треугольника, приведенный к целому значению с помощью функции int();
# tr() - возвращает площадь треугольника (можно вычислить по формуле Герона:
# s = sqrt(p * (p-a) * (p-b) * (p-c)), где p - полупериметр треугольника).




class BaseCoordinate:
    def __set_name__(self, owner, name):
        self.__name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.__name, None)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        setattr(instance, self.__name, value)


class Triangle:
    a, b, c = BaseCoordinate(), BaseCoordinate(), BaseCoordinate()
    def __init__(self, a, b, c):
        if self.__check_triangle_sides(a, b, c):
            self.a, self.b, self.c = a, b, c

    @classmethod
    def __check_triangle_sides(cls, a, b, c):
        if not all([a < b+c, b < a+c, c < a+b]):
            raise ValueError("с указанными длинами нельзя образовать треугольник")
        return True

    def __len__(self):
        return int(sum([self.a, self.b, self.c]))

    def __call__(self):
        p = self.__len__() * 0.5
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5