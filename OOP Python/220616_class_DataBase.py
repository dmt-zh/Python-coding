# Из входного потока читаются строки данных с помощью команды:
# lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
# в формате: id, name, old, salary (записанные через пробел). Например:
# 1 Сергей 35 120000
# 2 Федор 23 12000
# 3 Иван 13 1200
# ...

# Необходимо в класс DataBase:
# class DataBase:
#     lst_data = []
#     FIELDS = ('id', 'name', 'old', 'salary')
# добавить два метода:
# insert(self, data) - для добавления в список lst_data новых данных из переданного списка строк data;
# select(self, a, b) - возвращает список из элементов списка lst_data в диапазоне [a; b] (включительно) по их индексам
# (граница b может превышать длину списка).

# Каждая запись в списке lst_data должна быть представлена словарем (добавление с помощью метода insert) в формате:
# {'id': 'номер', 'name': 'имя', 'old': 'возраст', 'salary': 'зарплата'}

# Например:
# {'id': '1', 'name': 'Сергей', 'old': '35', 'salary': '120000'}

# Примечание: в этой задаче число элементов в строке (разделенных пробелом) всегда совпадает с числом полей в коллекции FIELDS.


import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, arrs):
        for line in lst_in:
            values = line.strip().split()
            self.lst_data.append(dict(zip(self.FIELDS, values)))


    def select(self, a, b):
        for i in range(a, b + 1):
            return self.lst_data[a:b + 1]



db = DataBase()
db.insert(lst_in)
