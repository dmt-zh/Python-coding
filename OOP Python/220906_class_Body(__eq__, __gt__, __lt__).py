# Необходимо объявить класс Body (тело), объекты которого создаются командой:

# body = Body(name, ro, volume)
# где name - название тела (строка); ro - плотность тела (число: вещественное или целочисленное); 
# volume - объем тела  (число: вещественное или целочисленное).

# Для объектов класса Body должны быть реализованы операторы сравнения:
# body1 > body2  # True, если масса тела body1 больше массы тела body2
# body1 == body2 # True, если масса тела body1 равна массе тела body2
# body1 < 10     # True, если масса тела body1 меньше 10
# body2 == 5     # True, если масса тела body2 равна 5

# Масса тела вычисляется по формуле: m = ro * volume




import math
class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume
        self.mass = self.ro * self.volume

    def __eq__(self, other):
        mass = other.mass if isinstance(other, Body) else other
        return math.isclose(self.mass, mass)

    def __gt__(self, other):
        mass = other.mass if isinstance(other, Body) else other
        return self.mass > mass

    def __lt__(self, other):
        mass = other.mass if isinstance(other, Body) else other
        return self.mass < mass