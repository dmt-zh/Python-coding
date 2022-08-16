# Вам требуется сформировать класс PathLines для описания маршрутов, состоящих из линейных сегментов.
# При этом каждый линейный сегмент предполагается задавать отдельным классом LineTo. Объекты этого класса
# будут формироваться командой: line = LineTo(x, y)
# где x, y - следующая координата линейного участка (начало маршрута из точки 0, 0).

# В каждом объекте класса LineTo должны формироваться локальные атрибуты:
# x, y - для хранения координат конца линии (начало определяется по координатам предыдущего объекта).

# Объекты класса PathLines должны создаваться командами:
# p = PathLines()                   # начало маршрута из точки 0, 0
# p = PathLines(line1, line2, ...)  # начало маршрута из точки 0, 0
# где line1, line2, ... - объекты класса LineTo.

# Сам же класс PathLines должен иметь следующие методы:
# get_path() - возвращает список из объектов класса LineTo (если объектов нет, то пустой список);
# get_length() - возвращает суммарную длину пути (сумма длин всех линейных сегментов);
# add_line(self, line) - добавление нового линейного сегмента (объекта класса LineTo) в конец маршрута.

# Пояснение: суммарный маршрут - это сумма длин всех линейных сегментов, а длина каждого линейного сегмента
# определяется как евклидовое расстояние по формуле: L = sqrt((x1-x0)^2 + (y1-y0)^2)
# где x0, y0 - предыдущая точка маршрута; x1, y1 - текущая точка маршрута.


class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PathLines:
    def __init__(self, *args):
        self.__path = list((LineTo(0, 0), ) + args)

    def get_path(self):
        return self.__path[1:]

    def get_length(self):
        distance = 0
        lst = self.__path
        for i in range(1, len(lst)):
            distance += ((lst[i].x - lst[i - 1].x) ** 2 + (lst[i].y - lst[i - 1].y) ** 2) ** 0.5
        return distance

    def add_line(self, line):
        self.__path.append(line)



p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
print(p.get_length())
# 73.5917360311745