# В программе необходимо реализовать таблицу TableValues.
# Каждая ячейка таблицы должна быть представлена классом Cell. Объекты этого класса создаются командой:
# cell = Cell(data)
# где data - данные в ячейке. В каждом объекте класса Cell должен формироваться локальный приватный
# атрибут __data с соответствующим значением. Для работы с ним в классе Cell должно быть
# объект-свойство (property):
# data - для записи и считывания информации из атрибута __data.

# Сам класс TableValues представляет таблицу в целом, объекты которого создаются командой:
# table = TableValues(rows, cols, type_data)
# где rows, cols - число строк и столбцов таблицы; type_data - тип данных ячейки (int - по умолчанию,
# float, list, str и т.п.). Начальные значения в ячейках таблицы равны 0 (целое число).

# С объектами класса TableValues должны выполняться следующие команды:
# table[row, col] = value# запись нового значения в ячейку с индексами row, col (индексы отсчитываются с нуля)
# value = table[row, col] # считывание значения из ячейки с индексами row, col

# for row in table:  # перебор по строкам
#     for value in row: # перебор по столбцам
#         print(value, end=' ')  # вывод значений ячеек в консоль
#     print()

# При попытке записать по индексам table[row, col] данные другого типа (не совпадающего с атрибутом type_data
# объекта класса TableValues), должно генерироваться исключение командой:
# raise TypeError('неверный тип присваиваемых данных')

# При работе с индексами row, col, необходимо проверять их корректность. Если индексы не целое число или они
# выходят за диапазон размера таблицы, то генерировать исключение командой:
# raise IndexError('неверный индекс')




class Cell:
    def __init__(self, data=None):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class TableValues:
    def __init__(self, rows, cols, type_dat=int):
        self.rows = rows
        self.cols = cols
        self.type_dat = type_dat
        self.__table = tuple(tuple(Cell(0) for _ in range(cols)) for _ in range(rows))

    def __check_indexes(self, row_idx, col_idx):
        valid_row = 0 <= row_idx < self.rows and type(row_idx) == int
        valid_col = 0 <= col_idx < self.cols and type(col_idx) == int
        if not (valid_row and valid_col):
            raise IndexError('неверный индекс')

    def __check_data(self, value):
        if type(value) != self.type_dat:
            raise TypeError('неверный тип присваиваемых данных')

    def __getitem__(self, item):
        row, col = item
        self.__check_indexes(row, col)
        return self.__table[row][col].data

    def __setitem__(self, key, value):
        row, col = key
        self.__check_indexes(row, col)
        self.__check_data(value)
        self.__table[row][col].data = value

    def __iter__(self):
        for row in self.__table:
            yield (cell.data for cell in row)

    def get_table(self):
        return self.__table