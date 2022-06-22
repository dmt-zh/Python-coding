# Объявите три класса геометрических фигур: Line, Rect, Ellipse. Должна быть возможность создавать объекты каждого
# класса следующими командами:
# g1 = Line(a, b, c, d)
# g2 = Rect(a, b, c, d)
# g3 = Ellipse(a, b, c, d)
# Здесь в качестве аргументов a, b, c, d передаются координаты верхнего правого и нижнего левого углов (произвольные числа).
# В каждом объекте координаты должны сохраняться в локальных свойствах sp (верхний правый угол) и ep (нижний левый) в виде
# кортежей (a, b) и (c, d) соответственно.

# Сформируйте 217 объектов этих классов: для каждого текущего объекта класс выбирается случайно (или Line, или Rect, или Ellipse).
# Координаты также генерируются случайным образом (числовые значения). Все объекты сохраните в списке elements.
# В списке elements обнулите координаты объектов только для класса Line.


import random

class Figure:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Line(Figure):
    pass

class Rect(Figure):
    pass

class Ellipse(Figure):
    pass


elements = []

for _ in range(217):
    cls = random.choice((Line, Rect, Ellipse))
    coords = [random.randint(0, 10) for _ in range(4)]
    elements.append(cls(*coords))

for elem in elements:
    if isinstance(elem, Line):
        elem.sp = elem.ep = 0, 0