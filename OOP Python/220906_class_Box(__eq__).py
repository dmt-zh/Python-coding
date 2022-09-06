# Объявите в программе класс с именем Box (ящик), объекты которого должны создаваться командой:
# box = Box()

# А сам класс иметь следующие методы:
# add_thing(self, obj) - добавление предмета obj (объект другого класса Thing) в ящик;
# get_things(self) - получение списка объектов ящика.

# Для описания предметов необходимо объявить еще один класс Thing. Объекты этого класса должны 
# создаваться командой:
# obj = Thing(name, mass)
# где name - название предмета (строка); mass - масса предмета (число: целое или вещественное).

# Объекты класса Thing должны поддерживать операторы сравнения:
# obj1 == obj2
# obj1 != obj2
# Предметы считаются равными, если у них одинаковые названия name (без учета регистра) и массы mass.

# Также объекты класса Box должны поддерживать аналогичные операторы сравнения:
# box1 == box2
# box1 != box2
# Ящики считаются равными, если одинаковы их содержимое (для каждого объекта класса Thing одного
# ящика и можно найти ровно один равный объект из второго ящика).




import math
class Box:
    def __init__(self):
        self.__things = list()

    def add_thing(self, obj):
        if isinstance(obj, Thing):
            self.__things.append(obj)

    def get_things(self):
        return self.__things

    def __eq__(self, other):
        return sorted(self.get_things()) == sorted(other.get_things())


class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        same_names = self.name.lower() == other.name.lower()
        same_mass = math.isclose(self.mass, other.mass)
        return same_mass and same_names

    def __lt__(self, other):
        if isinstance(other, Thing):
            return self.mass < other.mass