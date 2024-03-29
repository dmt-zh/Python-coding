# Объявите в программе класс Triangle, объекты которого создаются командой:
# tr = Triangle(a, b, c)
# где a, b, c - длины сторон треугольника (любые положительные числа).

# В каждом объекте класса Triangle должны формироваться локальные атрибуты _a, _b, _c с соответствующими значениями.
# Если в качестве хотя бы одной величины a, b, c передается не числовое значение, или меньше либо равно нулю, то
# должно генерироваться исключение командой:
# raise TypeError('стороны треугольника должны быть положительными числами')

# Если из переданных значений a, b, c нельзя составить треугольник (условие: каждая сторона должна быть меньше суммы
# двух других), то генерировать исключение командой:
# raise ValueError('из указанных длин сторон нельзя составить треугольник')

# Затем, на основе следующего набора данных:
# input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]
# необходимо сформировать объекты класса Triangle, но только в том случае, если не возникло никаких исключений.
# Все созданные объекты представить в виде списка с именем lst_tr.



class Triangle:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
        self.__check_triangle(a, b, c)

    def __setattr__(self, key, value):
        if type(value) not in (int, float) or value <= 0:
            raise TypeError('стороны треугольника должны быть положительными числами')
        object.__setattr__(self, key, value)

    @staticmethod
    def __check_triangle(a, b, c):
        if not all([a < b+c, b < a+c, c < a+b]):
            raise ValueError('из указанных длин сторон нельзя составить треугольник')

    def __repr__(self):
        return f'({self._a}, {self._b}, {self._c})'


input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 4), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]

lst_tr = []
for data in input_data:
    try:
        tr = Triangle(*data)
        lst_tr.append(tr)
    except:
        continue