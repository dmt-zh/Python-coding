# Необходимо объявить класс Bag (рюкзак), объекты которого будут создаваться командой:
# bag = Bag(max_weight)
# где max_weight - максимальный суммарный вес вещей, который выдерживает рюкзак (целое число).

# В каждом объекте этого класса должен создаваться локальный приватный атрибут:
# __things - список вещей в рюкзаке (изначально список пуст).

# Сам же класс Bag должен иметь объект-свойство:
# things - для доступа к локальному приватному атрибуту __things (только для считывания, не записи).

# Также в классе Bag должны быть реализованы следующие методы:
# add_thing(self, thing) - добавление нового предмета в рюкзак (добавление возможно, если суммарный вес (max_weight)
# не будет превышен, иначе добавление не происходит);
# remove_thing(self, indx) - удаление предмета по индексу списка __things;
# get_total_weight(self) - возвращает суммарный вес предметов в рюкзаке.

# Каждая вещь описывается как объект класса Thing и создается командой:
# t = Thing(название, вес)
# где название - наименование предмета (строка); вес - вес предмета (целое или вещественное число).

# В каждом объекте класса Thing должны формироваться локальные атрибуты:
# name - наименование предмета;
# weight - вес предмета.




class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self, max_weight=0):
        self.max_weight = max_weight
        self.__things = list()

    @property
    def things(self):
        return self.__things

    def add_thing(self, item):
        if self.get_total_weight() + item.weight <= self.max_weight:
            self.__things.append(item)

    def remove_thing(self, indx):
        self.__things.pop(indx)

    def get_total_weight(self):
        return sum(map(lambda x: x.weight, self.__things))