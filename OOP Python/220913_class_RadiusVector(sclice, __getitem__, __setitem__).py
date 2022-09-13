# Объявите в программе класс с именем RadiusVector (радиус-вектор), объекты которого создаются командой:
# v = RadiusVector(x1, x2,..., xN)
# где x1, x2,..., xN - координаты радиус-вектора (числа: целые или вещественные).

# В каждом объекте класса RadiusVector должен быть локальный атрибут:
# coords - список из координат радиус-вектора.

# Для доступа к отдельным координатам, реализовать следующий функционал:
# coord = v[i] # получение значения i-й координаты (целое число, отсчет с нуля)
# coords_1 = v[start:stop] # получение среза (набора) координат в виде кортежа
# coords_2 = v[start:stop:step] # получение среза (набора) координат в виде кортежа
# v[i] = value # изменение i-й координаты
# v[start:stop] = [val_1, val_2, ...] # изменение сразу нескольких координат
# v[start:stop:step] = [val_1, val_2, ...] # изменение сразу нескольких координат




class RadiusVector:
    def __init__(self, *coords):
        self.coords = list(coords)

    def __getitem__(self, item):
        if type(item) == int:
            return self.coords[item]
        return tuple(self.coords[item])

    def __setitem__(self, key, value):
        self.coords[key] = value