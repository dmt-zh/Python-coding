# Объявите класс с именем DataBase (база данных - БД), объекты которого создаются командой:
# db = DataBase(path)
# где path - путь к файлу с данными БД (строка).

# Также в классе DataBase нужно объявить следующие методы:
# write(self, record) - для добавления новой записи в БД, представленной объектом record;
# read(self, pk) - чтение записи из БД (возвращает объект Record) по ее уникальному идентификатору
# pk (уникальное целое положительное число); запись ищется в значениях словаря (см. ниже)

# Каждая запись БД должна описываться классом Record, а объекты этого класса создаваться командой:
# record = Record(fio, descr, old)
# где fio - ФИО некоторого человека (строка); descr - характеристика человека (строка); 
# old - возраст человека (целое число).

# В каждом объекте класса Record должны формироваться следующие локальные атрибуты:
# pk - уникальный идентификатор записи (число: целое, положительное); формируется автоматически при 
# создании каждого нового объекта;
# fio - ФИО человека (строка);
# descr - характеристика человека (строка);
# old - возраст человека (целое число).

# Реализовать для объектов класса Record вычисление хэша по атрибутам: fio и old (без учета регистра). 
# Если они одинаковы для разных записей, то и хэши должны получаться равными. Также для объектов класса 
# Record  с одинаковыми хэшами оператор == должен выдавать значение True, а с разными хэшами - False.

# Хранить записи в БД следует в виде словаря dict_db (атрибут объекта db класса DataBase), ключами которого 
# являются объекты класса Record, а значениями список из объектов с равными хэшами:
# dict_db[rec1] = [rec1, rec2, ..., recN] где rec1, rec2, ..., recN - объекты класса Record с одинаковыми хэшами.

# Для наполнения БД прочитайте строки из входного потока с помощью команды:
# lst_in = list(map(str.strip, sys.stdin.readlines()))



import sys
from itertools import chain

class DataBase:
    def __init__(self, path=None):
        self.path = path
        self.dict_db = {}

    def write(self, record):
        self.dict_db.setdefault(hash(record), []).append(record)

    def read(self, pk):
        values = chain(*self.dict_db.values())
        for record in values:
            if record.pk == pk:
                return record


class Record:
    __acc = 0

    def __new__(cls, *arg, **kwargs):
        cls.__acc += 1
        return super().__new__(cls)

    def __init__(self, fio, descr, old):
        self.fio = fio
        self.descr = descr
        self.old = old
        self.pk = self.__acc

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other):
        return hash(self) == hash(other)



db = DataBase()
lst_in = list(map(str.strip, sys.stdin.readlines()))

for row in lst_in:
    name, desc, age = list(map(str.strip, row.split(';')))
    db.write(Record(name, desc, int(age)))