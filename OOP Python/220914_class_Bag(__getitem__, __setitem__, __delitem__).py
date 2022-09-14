# Объявите в программе класс Bag (сумка), объекты которого создаются командой:
# bag = Bag(max_weight)
# где max_weight - максимальный суммарный вес предметов, который можно положить в сумку.

# Каждый предмет описывается классом Thing и создается командой:
# t = Thing(name, weight)
# где name - название предмета (строка); weight - вес предмета (вещественное или целочисленное значение).
# В объектах класса Thing должны автоматически формироваться локальные свойства с теми же именами: name и weight.

# В классе Bag должен быть реализован метод:
# add_thing(thing) - добавление нового объекта thing класса Thing в сумку.

# Добавление выполняется только если суммарный вес вещей не превышает параметра max_weight. Иначе,
# генерируется исключение: raise ValueError('превышен суммарный вес предметов')

# Также с объектами класса Bag должны выполняться следующие команды:
# t = bag[indx] # получение объекта класса Thing по индексу indx (в порядке добавления вещей, начиная с 0)
# bag[indx] = t # замена прежней вещи на новую t, расположенной по индексу indx
# del bag[indx] # удаление вещи из сумки, расположенной по индексу indx

# Если индекс в этих командах указывается неверно, то должно генерироваться исключение:
# raise IndexError('неверный индекс')

# Пример использования классов (эти строчки в программе не писать):
# bag = Bag(1000)
# bag.add_thing(Thing('книга', 100))
# bag.add_thing(Thing('носки', 200))
# bag.add_thing(Thing('рубашка', 500))
# bag.add_thing(Thing('ножницы', 300)) # генерируется исключение ValueError
# print(bag[2].name) # рубашка
# bag[1] = Thing('платок', 100)
# print(bag[1].name) # платок
# del bag[0]
# print(bag[0].name) # платок
# t = bag[4] # генерируется исключение IndexError




class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__bag = list()
        self.__total = 0

    def __check(self, item=False, idx=False):
        if item:
            valid_item = isinstance(item, Thing)
            valid_weight = item.weight + self.__total <= self.max_weight
            if not (valid_item and valid_weight):
                raise ValueError('превышен суммарный вес предметов')
        if idx:
            valid_idx = idx < len(self.__bag) if type(idx) == int else False
            if not valid_idx:
                raise IndexError('неверный индекс')

    def add_thing(self, thing):
        self.__check(thing)
        self.__bag.append(thing)
        self.__total += thing.weight

    def __setitem__(self, key, thing):
        self.__check(idx=key)
        self.__total -= self.__bag[key].weight
        self.__check(thing, idx=key)
        self.__bag[key] = thing
        self.__total += thing.weight

    def __getitem__(self, item):
        self.__check(idx=item)
        return self.__bag[item]

    def __delitem__(self, key):
        self.__check(idx=key)
        self.__total -= self.__bag[key].weight
        del self.__bag[key]



import shutil
shutil.copy('testing.py', '220914_class_Bag(__getitem__, __setitem__, __delitem__).py')