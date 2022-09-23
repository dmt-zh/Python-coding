# Вам поручают разработать класс для представления маршрутов в навигаторе. Для этого требуется
# объявить класс с именем Track, объекты которого могут создаваться командами:
# tr = Track(start_x, start_y)
# tr = Track(pt1, pt2, ..., ptN)
# где start_x, start_y - начальная координата маршрута (произвольные числа);
# pt1, pt2, ..., ptN - набор из произвольного числа точек (координат) маршрута (объекты класса PointTrack).

# При передаче аргументов (start_x, start_y) координата должна представляться первым объектом класса PointTrack.
# Наборы всех точек (объектов PointTrack) должны сохраняться в локальном приватном атрибуте объекта класса Track:
# __points - список из точек (координат) маршрута.

# Далее, каждая точка (координата) должна определяться классом PointTrack, объекты которого создаются командой:
# pt = PointTrack(x, y)
# где x, y - числа (целые или вещественные).
# Если передается другой тип данных, то должно генерироваться исключение командой:
# raise TypeError('координаты должны быть числами')

# В классе PointTrack переопределите магический метод __str__, чтобы информация об объекте класса возвращалась
# в виде строки: "PointTrack: <x>, <y>". Например:
# pt = PointTrack(1, 2)
# print(pt) # PointTrack: 1, 2

# В самом классе Track должно быть свойство (property) с именем:
# points - для получения кортежа из точек маршрута.

# Также в классе Track должны быть методы:
# def add_back(self, pt) - добавление новой точки в конец маршрута (pt - объект класса PointTrack);
# def add_front(self, pt) - добавление новой точки в начало маршрута (pt - объект класса PointTrack);
# def pop_back(self) - удаление последней точки из маршрута;
# def pop_front(self) - удаление первой точки из маршрута.




class PointTrack:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def __check_value(value):
        if not isinstance(value, (float, int)):
            raise TypeError('координаты должны быть числами')

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__check_value(value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__check_value(value)
        self.__y = value

    def __str__(self):
        return f'PointTrack: {self.x}, {self.y}'


class Track:
    def __init__(self, *args):
        self.__start_x = args[0]
        self.__start_y = args[1]
        self.__points = list(args[2:])

    def add_back(self, pt):
        self.__points.append(pt)

    def add_front(self, pt):
        self.__points.insert(0, pt)

    def pop_back(self):
        self.__points.pop()

    def pop_front(self):
        self.__points.pop(0)

    @property
    def points(self):
        return tuple([self.__start_x] + [self.__start_y] + self.__points)