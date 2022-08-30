# Объявите класс Track (маршрут), объекты которого создаются командой:
# track = Track(start_x, start_y)
# где start_x, start_y - координаты начала маршрута (целые или вещественные числа).

# Каждый линейный сегмент маршрута определяется классом TrackLine, объекты которого создаются командой:
# line = TrackLine(to_x, to_y, max_speed)
# где to_x, to_y - координаты следующей точки маршрута (целые или вещественные числа); 
# max_speed - максимальная скорость на данном участке (целое число).

# Для формирования и работы с маршрутом в классе Track должны быть объявлены следующие методы:
# add_track(self, tr) - добавление линейного сегмента маршрута (следующей точки);
# get_tracks(self) - получение кортежа из объектов класса TrackLine.

# Также для объектов класса Track должны быть реализованные следующие операции сравнения:
# track1 == track2  # маршруты равны, если равны их длины
# track1 != track2  # маршруты не равны, если не равны их длины
# track1 > track2  # True, если длина пути для track1 больше, чем для track2
# track1 < track2  # True, если длина пути для track1 меньше, чем для track2

# И функция:
# n = len(track) # возвращает целочисленную длину маршрута (привести к типу int) для объекта track
# Создайте два маршрута track1 и track2 с координатами:

# 1-й маршрут: (0; 0), (2; 4), (5; -4) и max_speed = 100
# 2-й маршрут: (0; 1), (3; 2), (10; 8) и max_speed = 90

# Сравните их между собой на равенство. Результат сравнения сохраните в переменной res_eq.



class Track:
    def __init__(self, start_x=0, start_y=0):
        self.__track = list()
        self.start_x = start_x
        self.start_y = start_y
    
    @classmethod
    def __verify(cls, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Valid input types: int or float.')
        return True

    @classmethod
    def __object_type(cls, value):
        if not isinstance(value, Track):
            raise TypeError('Only objects of type "Track" are valid.')
        return True

    @property
    def start_x(self):
        return self.__start_x

    @start_x.setter
    def start_x(self, value):
        if self.__verify(value):
            self.__start_x = value

    @property
    def start_y(self):
        return self.__start_y

    @start_y.setter
    def start_y(self, value):
        if self.__verify(value):
            self.__start_y = value

    def add_track(self, track):
        if isinstance(track, TrackLine):
            self.__track.append(track)

    def get_tracks(self):
        return tuple(self.__track)

    def __len__(self):
        point_1 = [self.start_x] + list(map(lambda x: x.to_x, self.__track))
        point_2 = [self.start_y] + list(map(lambda y: y.to_y, self.__track))
        distance = (sum(pow(a-b, 2) for a, b in zip(point_1, point_2))) ** 0.5
        return int(distance)

    def __eq__(self, other):
        if self.__object_type(other):
            return len(self) == len(other)

    def __gt__(self, other):
        if self.__object_type(other):
            return len(self) > len(other)


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_sped = max_speed

    @classmethod
    def __verify(cls, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Invalid input type.')
        return True

    @property
    def to_x(self):
        return self.__to_x

    @to_x.setter
    def to_x(self, value):
        if self.__verify(value):
            self.__to_x = value

    @property
    def to_y(self):
        return self.__to_y

    @to_y.setter
    def to_y(self, value):
        if self.__verify(value):
            self.__to_y = value

    @property
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, value):
        if self.__verify(value) and value > 0:
            self.__max_speed = value



track1 = Track()
track2 = Track(0, 1)

track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2