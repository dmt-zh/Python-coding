# Объявите класс с именем Rect (прямоугольник), объекты которого создаются командой:
# r = Rect(x, y, width, height)
# где x, y - координаты верхнего левого угла (любые числа);
# width, height - ширина и высота прямоугольника (положительные числа).

# В каждом объекте класса Rect должны формироваться локальные атрибуты с именами: _x, _y, _width, _height и
# соответствующими значениями. Если переданные аргументы x, y (не числа) и width, height не положительные числа,
# то генерировать исключение командой: raise ValueError('некорректные координаты и параметры прямоугольника')

# В классе Rect реализовать метод:
# def is_collision(self, rect): ...

# который проверяет пересечение текущего прямоугольника с другим (с объектом rect). Если прямоугольники пересекаются,
# то должно генерироваться исключение командой: raise TypeError('прямоугольники пересекаются')

# Сформировать в программе несколько объектов класса Rect со следующими значениями:
# 0; 0; 5; 3
# 6; 0; 3; 5
# 3; 2; 4; 4
# 0; 8; 8; 1

# Сохранить их в списке lst_rect. На основе списка lst_rect сформировать еще один список lst_not_collision, в котором
# должны быть объекты rect не пересекающиеся ни с какими другими объектами в списке lst_rect.



class Rect:
    def __init__(self, x, y, w, h):
        self._x, self._y = x, y
        self._width = w
        self._height = h
        self._sides = (x, y, w, h)

    def __setattr__(self, key, value):
        if key in ('_x', '_y'):
            if not type(value) in (int, float):
                raise ValueError('некорректные координаты и параметры прямоугольника')
        if key in ('_width', '_height'):
            if not type(value) in (int, float) or value <= 0:
                raise ValueError('некорректные координаты и параметры прямоугольника')

        object.__setattr__(self, key, value)

    def is_collision(self, rect):
        if isinstance(rect, Rect):
            h_sides = self._x + self._width < rect._x or rect._x + rect._width < self._x
            v_sides = self._y + self._height < rect._y or rect._y + rect._height < self._y
            if not (h_sides or v_sides):
                raise TypeError('прямоугольники пересекаются')

    def __repr__(self):
        return f"{self._sides}"


lst_rect = [Rect(0, 0, 5, 3), Rect(6, 0, 3, 5), Rect(3, 2, 4, 4), Rect(0, 8, 8, 1)]

lst_not_collision = []
for rect in lst_rect:
    try:
        any(rect.is_collision(r) for r in lst_rect if rect != r)
    except TypeError:
        continue
    else:
        lst_not_collision.append(rect)
