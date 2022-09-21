# Вам поручено организовать представление объектов для продажи в риэлтерских агентствах.
# Для этого в программе нужно объявить базовый класс SellItem, объекты которого создаются командой:
# item = SellItem(name, price)
# где name - название объекта продажи (строка);
# price - цена продажи (число: целое или вещественное).

# Каждые конкретные типы объектов описываются следующими классами, унаследованные от базового SellItem:
# House - дома;
# Flat - квартиры;
# Land - земельные участки.

# Объекты этих классов создаются командами:
# house = House(name, price, material, square)
# flat = Flat(name, price, size, rooms)
# land = Land(name, price, square)

# В каждом объекте этих классов должны формироваться соответствующие локальные атрибуты: name, price и т.д.
# Формирование атрибутов name и price должно выполняться в инициализаторе базового класса.

# Далее, объявить еще один класс с именем Agency, объекты которого создаются командой:
# ag = Agency(name)
# где name - название агентства (строка).

# В классе Agency объявить следующие методы:
# add_object(obj) - добавление нового объекта недвижимости для продажи (один из объектов классов: House, Flat, Land);
# remove_object(obj) - удаление объекта obj из списка объектов для продажи;
# get_objects() - возвращает список из всех объектов для продажи.



class SellItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class House(SellItem):
    def __init__(self, name, price, material, square):
        super().__init__(name, price)
        self.material = material
        self.square = square


class Flat(SellItem):
    def __init__(self, name, price, size, rooms):
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms


class Land(SellItem):
    def __init__(self, name, price, square):
        super().__init__(name, price)
        self.square = square


class Agency:
    def __init__(self, name):
        self.name = name
        self.__base = list()

    def add_object(self, obj):
        if isinstance(obj, (House, Land, Flat)):
            self.__base.append(obj)

    def remove_object(self, obj):
        if obj in self.__base:
            self.__base.remove(obj)

    def get_objects(self):
        return self.__base