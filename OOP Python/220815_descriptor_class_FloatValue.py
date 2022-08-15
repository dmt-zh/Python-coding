# Объявите дескриптор данных FloatValue, который бы устанавливал и возвращал вещественные значения.
# При записи вещественного числа должна выполняться проверка на вещественный тип данных. Если проверка не проходит,
# то генерировать исключение командой: raise TypeError("Присваивать можно только вещественный тип данных.")

# Объявите класс Cell, в котором создается объект value дескриптора FloatValue. А объекты класса Cell должны создаваться командой:
# cell = Cell(начальное значение ячейки)

# Объявите класс TableSheet, с помощью которого создается таблица из N строк и M столбцов следующим образом:
# table = TableSheet(N, M)

# Каждая ячейка этой таблицы должна быть представлена объектом класса Cell, работать с вещественными числами через объект
# value (начальное значение должно быть 0.0). В каждом объекте класса TableSheet должен формироваться локальный атрибут:
# cells - список (вложенный) размером N x M, содержащий ячейки таблицы (объекты класса Cell).

# Создайте объект table класса TableSheet с размером таблицы N = 5, M = 3. Запишите в эту таблицу числа от 1.0 до 15.0 (по порядку).



import numpy as np
class FloatValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")
        setattr(instance, self.name, value)



class Cell:
    value = FloatValue()
    def __init__(self, value=0.0):
        self.value = value



class TableSheet:
    def __init__(self, n, m):
        self.cells = [[Cell() for _ in range(m)] for _ in range(n)]

    def __flatten_table(self):
        return np.concatenate(self.cells).tolist()

    @property
    def cells_values(self):
        return [cell.value for cell in self.__flatten_table()]

    @cells_values.setter
    def cells_values(self, values):
        for cell, val in zip(self.__flatten_table(), values):
            cell.value = val



table = TableSheet(5, 3)
table.cells_values = [float(n) for n in range(1, 16)]