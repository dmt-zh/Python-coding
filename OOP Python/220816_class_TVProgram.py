# Необходимо написать программу для представления и управления расписанием телевизионного вещания.
# Для этого нужно объявить класс TVProgram, объекты которого создаются командой:
# pr = TVProgram(название канала) где название канала - это строка с названием телеканала.

# В каждом объекте класса TVProgram должен формироваться локальный атрибут:
# items - список из телепередач (изначально список пуст).

# В самом классе TVProgram должны быть реализованы следующие методы:
# add_telecast(self, tl) - добавление новой телепередачи в список items;
# remove_telecast(self, indx) - удаление телепередачи по ее порядковому номеру (атрибуту __id, см. далее).

# Каждая телепередача должна описываться классом Telecast, объекты которого создаются командой:
# tl = Telecast(порядковый номер, название, длительность)
# где порядковый номер - номер телепередачи в сетке вещания (от 1 и далее); название - наименование телепередачи;
# длительность - время телепередачи (в секундах - целое число).

# Соответственно, в каждом объекте класса Telecast должны формироваться локальные приватные атрибуты:
# __id - порядковый номер (целое число);
# __name - наименование телепередачи (строка);
# __duration - длительность телепередачи в секундах (целое число).

# Для работы с этими приватными атрибутами в классе Telecast должны быть объявлены соответствующие объекты-свойства (property):
# uid - для записи и считывания из локального атрибута __id;
# name - для записи и считывания из локального атрибута __name;
# duration - для записи и считывания из локального атрибута __duration.



class TVProgram:
    def __init__(self, title=None):
        self.title = title
        self.items = list()

    def add_telecast(self, tl):
        self.items.append(tl)

    def remove_telecast(self, indx):
        title_to_delete = None
        for item in self.items:
            if item.uid == indx:
                title_to_delete = item
                break
        self.items.remove(title_to_delete)


class Telecast:
    def __init__(self, tl_id, tl_name, tl_duration):
        self.uid = tl_id
        self.name = tl_name
        self.duration = tl_duration

    def __check_input(self, data, digits=True):
        if digits:
            return type(data) == int and data > 0
        else:
            return type(data) == str and len(data) > 0

    @property
    def uid(self):
        return self.__id

    @uid.setter
    def uid(self, value):
        if self.__check_input(value):
            self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, tl_name):
        if self.__check_input(tl_name, digits=False):
            self.__name = tl_name

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        if self.__check_input(value):
            self.__duration = value