# Объявите класс Line, объекты которого создаются командой:
# line = Line(x1, y1, x2, y2)
# где x1, y1, x2, y2 - координаты начала линии (x1, y1) и координаты конца линии (x2, y2).
# Могут быть произвольными числами. В объектах класса Line должны создаваться соответствующие
# локальные атрибуты с именами x1, y1, x2, y2.

# В классе Line определить магический метод __len__() так, чтобы функция:
# bool(line)
# возвращала False, если длина линии меньше 1.




import math
class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = float(x1)
        self.x2 = float(x2)
        self.y1 = float(y1)
        self.y2 = float(y2)

    def __len__(self):
        len_line = math.hypot(self.x1 - self.x2, self.y1 - self.y2)
        return math.ceil(len_line)

    def __bool__(self):
        return len(self) >= 1



import shutil
shutil.copy('testing.py', '220912_class_Line(__bool__).py')